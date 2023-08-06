# This file is a part of the CaosDB Project.
#
# Copyright (C) 2018 Research Group Biomedical Physics,
# Max-Planck-Institute for Dynamics and Self-Organization Göttingen
# Copyright (C) 2022 Alexander Schlemmer <alexander.schlemmer@ds.mpg.de>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program. If not, see <https://www.gnu.org/licenses/>.
#
# ** end header
#
# Test high level api module
# A. Schlemmer, 02/2022


import caosdb as db
from caosdb.high_level_api import (convert_to_entity, convert_to_python_object,
                                   new_high_level_entity)
from caosdb.high_level_api import (CaosDBPythonUnresolvedParent,
                                   CaosDBPythonUnresolvedReference,
                                   CaosDBPythonRecord, CaosDBPythonFile,
                                   high_level_type_for_standard_type,
                                   standard_type_for_high_level_type,
                                   high_level_type_for_role,
                                   CaosDBPythonEntity)
from caosdb.apiutils import compare_entities

from caosdb.common.datatype import (is_list_datatype,
                                    get_list_datatype,
                                    is_reference)

import pytest
from lxml import etree
import os
import tempfile
import pickle

import sys
import traceback
import pdb


@pytest.fixture
def testrecord():
    parser = etree.XMLParser(remove_comments=True)
    testrecord = db.Record._from_xml(
        db.Record(),
        etree.parse(os.path.join(os.path.dirname(__file__), "test_record.xml"),
                    parser).getroot())
    return testrecord


def test_convert_object(testrecord):
    r2 = convert_to_python_object(testrecord)
    assert r2.species == "Rabbit"


def test_pickle_object(testrecord):
    r2 = convert_to_python_object(testrecord)
    with tempfile.TemporaryFile() as f:
        pickle.dump(r2, f)
        f.seek(0)
        rn2 = pickle.load(f)
    assert r2.date == rn2.date


def test_convert_record():
    """
    Test the high level python API.
    """
    r = db.Record()
    r.add_parent("bla")
    r.add_property(name="a", value=42)
    r.add_property(name="b", value="test")

    obj = convert_to_python_object(r)
    assert obj.a == 42
    assert obj.b == "test"

    # There is no such property
    with pytest.raises(AttributeError):
        assert obj.c == 18

    assert obj.has_parent("bla") is True
    assert obj.has_parent(CaosDBPythonUnresolvedParent(name="bla")) is True

    # Check the has_parent function:
    assert obj.has_parent("test") is False
    assert obj.has_parent(CaosDBPythonUnresolvedParent(name="test")) is False

    # duplicate parent
    with pytest.raises(RuntimeError):
        obj.add_parent("bla")

    # add parent with just an id:
    obj.add_parent(CaosDBPythonUnresolvedParent(id=225))
    assert obj.has_parent(225) is True
    assert obj.has_parent(CaosDBPythonUnresolvedParent(id=225)) is True
    assert obj.has_parent(226) is False
    assert obj.has_parent(CaosDBPythonUnresolvedParent(id=228)) is False

    # same with just a name:
    obj.add_parent(CaosDBPythonUnresolvedParent(name="another"))
    assert obj.has_parent("another") is True


def test_convert_with_references():
    r_ref = db.Record()
    r_ref.add_property(name="a", value=42)

    r = db.Record()
    r.add_property(name="ref", value=r_ref)

    # try:
    obj = convert_to_python_object(r)
    # except:
    #     extype, value, tb = sys.exc_info()
    #     traceback.print_exc()
    #     pdb.post_mortem(tb)
    assert obj.ref.a == 42

    # With datatype:
    r_ref = db.Record()
    r_ref.add_parent("bla")
    r_ref.add_property(name="a", value=42)

    r = db.Record()
    r.add_property(name="ref", value=r_ref)

    obj = convert_to_python_object(r)
    assert obj.ref.a == 42
    # Parent does not automatically lead to a datatype:
    assert obj.get_property_metadata("ref").datatype is None
    assert obj.ref.has_parent("bla") is True

    # Add datatype explicitely:
    r_ref = db.Record()
    r_ref.add_parent("bla")
    r_ref.add_property(name="a", value=42)

    r = db.Record()
    r.add_property(name="ref", value=r_ref, datatype="bla")

    obj = convert_to_python_object(r)
    assert obj.ref.a == 42
    # Parent does not automatically lead to a datatype:
    assert obj.get_property_metadata("ref").datatype is "bla"
    assert obj.ref.has_parent("bla") is True

    # Unresolved Reference:
    r = db.Record()
    r.add_property(name="ref", value=27, datatype="bla")

    obj = convert_to_python_object(r)
    # Parent does not automatically lead to a datatype:
    assert obj.get_property_metadata("ref").datatype is "bla"
    assert isinstance(obj.ref, CaosDBPythonUnresolvedReference)
    assert obj.ref.id == 27


def test_resolve_references():
    r = db.Record()
    r.add_property(name="ref", value=27, datatype="bla")
    r.add_property(name="ref_false", value=27)  # this should be interpreted as integer property
    obj = convert_to_python_object(r)

    ref = db.Record(id=27)
    ref.add_property(name="a", value=57)

    unused_ref1 = db.Record(id=28)
    unused_ref2 = db.Record(id=29)
    unused_ref3 = db.Record(name="bla")

    references = db.Container().extend([
        unused_ref1, ref, unused_ref2, unused_ref3])

    # Nothing is going to be resolved:
    obj.resolve_references(False, db.Container())
    assert isinstance(obj.ref, CaosDBPythonUnresolvedReference)
    assert obj.ref.id == 27
    assert obj.ref_false == 27

    # deep == True does not help:
    obj.resolve_references(True, db.Container())
    assert isinstance(obj.ref, CaosDBPythonUnresolvedReference)
    assert obj.ref.id == 27

    # But adding the reference container will do:
    obj.resolve_references(False, references)
    assert not isinstance(obj.ref, CaosDBPythonUnresolvedReference)
    assert isinstance(obj.ref, CaosDBPythonRecord)
    assert obj.ref.id == 27
    assert obj.ref.a == 57
    # Datatypes will not automatically be set:
    assert obj.ref.get_property_metadata("a").datatype is None

    # Test deep resolve:
    ref2 = db.Record(id=225)
    ref2.add_property(name="c", value="test")
    ref.add_property(name="ref", value=225, datatype="bla")

    obj = convert_to_python_object(r)
    assert isinstance(obj.ref, CaosDBPythonUnresolvedReference)
    obj.resolve_references(False, references)
    assert not isinstance(obj.ref, CaosDBPythonUnresolvedReference)
    assert isinstance(obj.ref.ref, CaosDBPythonUnresolvedReference)
    assert obj.ref.ref.id == 225

    # Will not help, because ref2 is missing in container:
    obj.resolve_references(True, references)
    assert not isinstance(obj.ref, CaosDBPythonUnresolvedReference)
    assert isinstance(obj.ref.ref, CaosDBPythonUnresolvedReference)
    assert obj.ref.ref.id == 225

    references.append(ref2)
    obj.resolve_references(False, references)
    assert not isinstance(obj.ref, CaosDBPythonUnresolvedReference)
    assert isinstance(obj.ref.ref, CaosDBPythonUnresolvedReference)
    assert obj.ref.ref.id == 225

    obj.resolve_references(True, references)
    assert not isinstance(obj.ref, CaosDBPythonUnresolvedReference)
    assert not isinstance(obj.ref.ref, CaosDBPythonUnresolvedReference)
    assert obj.ref.ref.c == "test"

    # Test circular dependencies:
    ref2.add_property(name="ref", value=27, datatype="bla")
    obj = convert_to_python_object(r)
    obj.resolve_references(True, references)
    assert obj.ref.ref.ref == obj.ref


def equal_entities(r1, r2):
    res = compare_entities(r1, r2)
    if len(res) != 2:
        return False
    for i in range(2):
        if len(res[i]["parents"]) != 0 or len(res[i]["properties"]) != 0:
            return False
    return True


def test_conversion_to_entity():
    r = db.Record()
    r.add_parent("bla")
    r.add_property(name="a", value=42)
    r.add_property(name="b", value="test")
    obj = convert_to_python_object(r)
    rconv = convert_to_entity(obj)
    assert equal_entities(r, rconv)

    # With a reference:
    r_ref = db.Record()
    r_ref.add_parent("bla")
    r_ref.add_property(name="a", value=42)

    r = db.Record()
    r.add_property(name="ref", value=r_ref)
    obj = convert_to_python_object(r)
    rconv = convert_to_entity(obj)
    assert (rconv.get_property("ref").value.get_property("a").value
            == r.get_property("ref").value.get_property("a").value)
    # TODO: add more tests here


def test_base_properties():
    r = db.Record(id=5, name="test", description="ok")
    r.add_property(name="v", value=15, datatype=db.INTEGER, unit="kpx",
                   importance="RECOMMENDED", description="description")
    obj = convert_to_python_object(r)
    assert obj.name == "test"
    assert obj.id == 5
    assert obj.description == "ok"
    metadata = obj.get_property_metadata("v")
    assert metadata.id is None
    assert metadata.datatype == db.INTEGER
    assert metadata.unit == "kpx"
    assert metadata.importance == "RECOMMENDED"
    assert metadata.description == "description"

    rconv = convert_to_entity(obj)
    assert rconv.name == "test"
    assert rconv.id == 5
    assert rconv.description == "ok"
    prop = rconv.get_property("v")
    assert prop.value == 15
    assert prop.datatype == db.INTEGER
    assert prop.unit == "kpx"
    assert prop.description == "description"
    assert rconv.get_importance("v") == "RECOMMENDED"


def test_empty():
    r = db.Record()
    obj = convert_to_python_object(r)
    assert isinstance(obj, CaosDBPythonRecord)
    assert len(obj.get_properties()) == 0
    assert len(obj.get_parents()) == 0

    rconv = convert_to_entity(obj)
    assert len(rconv.properties) == 0


def test_wrong_entity_for_file():
    r = db.Record()
    r.path = "test.dat"
    r.file = "/local/path/test.dat"
    assert r.path == "test.dat"
    assert r.file == "/local/path/test.dat"
    with pytest.raises(RuntimeError):
        obj = convert_to_python_object(r)


def test_serialization():
    r = db.Record(id=5, name="test", description="ok")
    r.add_property(name="v", value=15, datatype=db.INTEGER, unit="kpx",
                   importance="RECOMMENDED")

    obj = convert_to_python_object(r)
    text = str(obj)
    teststrs = ["description: ok", "id: 5", "datatype: INTEGER",
                "importance: RECOMMENDED", "unit: kpx", "name: test", "v: 15"]
    for teststr in teststrs:
        assert teststr in text

    r = db.Record(description="ok")
    r.add_property(name="v", value=15, datatype=db.INTEGER, unit="kpx",
                   importance="RECOMMENDED")
    obj = convert_to_python_object(r)
    text = str(obj)
    assert "name" not in text
    assert "id" not in text


def test_files():
    # empty file:
    r = db.File()
    obj = convert_to_python_object(r)
    print(type(obj))
    assert isinstance(obj, CaosDBPythonFile)
    assert len(obj.get_properties()) == 0
    assert len(obj.get_parents()) == 0

    rconv = convert_to_entity(obj)
    assert len(rconv.properties) == 0

    r.path = "test.dat"
    r.file = "/local/path/test.dat"
    obj = convert_to_python_object(r)
    assert r.path == "test.dat"
    assert r.file == "/local/path/test.dat"
    assert isinstance(obj, CaosDBPythonFile)

    assert obj.path == "test.dat"
    assert obj.file == "/local/path/test.dat"

    assert "path: test.dat" in str(obj)
    assert "file: /local/path/test.dat" in str(obj)

    # record with file property:
    rec = db.Record()
    rec.add_property(name="testfile", value=r)
    assert rec.get_property("testfile").value.file == "/local/path/test.dat"
    assert rec.get_property("testfile").value.path == "test.dat"

    obj = convert_to_python_object(rec)
    assert obj.testfile.file == "/local/path/test.dat"
    assert obj.testfile.path == "test.dat"

    rconv = convert_to_entity(obj)
    assert rconv.get_property("testfile").value.file == "/local/path/test.dat"
    assert rconv.get_property("testfile").value.path == "test.dat"

    # record with file property as reference:
    rec = db.Record()
    rec.add_property(name="testfile", value=2, datatype=db.FILE)
    obj = convert_to_python_object(rec)
    assert type(obj.testfile) == CaosDBPythonUnresolvedReference
    assert obj.testfile.id == 2
    assert obj.get_property_metadata("testfile").datatype == db.FILE

    # without resolving references:
    rconv = convert_to_entity(obj)
    p = rconv.get_property("testfile")
    assert p.value == 2
    assert p.datatype == db.FILE

    # with previously resolved reference (should not work here, because id is missing):
    obj.resolve_references(True, db.Container().extend(r))
    rconv = convert_to_entity(obj)
    p = rconv.get_property("testfile")
    assert p.value == 2
    assert p.datatype == db.FILE

    # this time it must work:
    r.id = 2
    obj.resolve_references(True, db.Container().extend(r))
    rconv = convert_to_entity(obj)
    p = rconv.get_property("testfile")
    assert type(p.value) == db.File
    assert p.datatype == db.FILE
    assert p.value.file == "/local/path/test.dat"
    assert p.value.path == "test.dat"


@pytest.mark.xfail
def test_record_generator():
    rt = db.RecordType(name="Simulation")
    rt.add_property(name="a", datatype=db.INTEGER)
    rt.add_property(name="b", datatype=db.DOUBLE)
    rt.add_property(name="inputfile", datatype=db.FILE)

    simrt = db.RecordType(name="SimOutput")
    rt.add_property(name="outputfile", datatype="SimOutput")

    obj = new_high_level_entity(
        rt, "SUGGESTED", "", True)
    print(obj)
    assert False


def test_list_types():
    r = db.Record()
    r.add_property(name="a", value=[1, 2, 4])

    assert get_list_datatype(r.get_property("a").datatype) is None

    obj = convert_to_python_object(r)
    assert type(obj.a) == list
    assert len(obj.a) == 3
    assert 4 in obj.a
    assert obj.get_property_metadata("a").datatype is None

    conv = convert_to_entity(obj)
    prop = r.get_property("a")
    assert prop.value == [1, 2, 4]
    assert prop.datatype is None

    r.get_property("a").datatype = db.LIST(db.INTEGER)
    assert r.get_property("a").datatype == "LIST<INTEGER>"
    obj = convert_to_python_object(r)
    assert type(obj.a) == list
    assert len(obj.a) == 3
    assert 4 in obj.a
    assert obj.get_property_metadata("a").datatype == "LIST<INTEGER>"

    conv = convert_to_entity(obj)
    prop = r.get_property("a")
    assert prop.value == [1, 2, 4]
    assert obj.get_property_metadata("a").datatype == "LIST<INTEGER>"

    # List of referenced objects:
    r = db.Record()
    r.add_property(name="a", value=[1, 2, 4], datatype="LIST<TestReference>")
    obj = convert_to_python_object(r)
    assert type(obj.a) == list
    assert len(obj.a) == 3
    assert obj.get_property_metadata("a").datatype == "LIST<TestReference>"
    for i in range(3):
        assert type(obj.a[i]) == CaosDBPythonUnresolvedReference
    assert obj.a == [CaosDBPythonUnresolvedReference(id=i) for i in [1, 2, 4]]

    # Try resolving:

    # Should not work:
    obj.resolve_references(False, db.Container())
    assert type(obj.a) == list
    assert len(obj.a) == 3
    assert obj.get_property_metadata("a").datatype == "LIST<TestReference>"
    for i in range(3):
        assert type(obj.a[i]) == CaosDBPythonUnresolvedReference
    assert obj.a == [CaosDBPythonUnresolvedReference(id=i) for i in [1, 2, 4]]

    references = db.Container()
    for i in [1, 2, 4]:
        ref = db.Record(id=i)
        ref.add_property(name="val", value=str(i) + " bla")
        references.append(ref)

    obj.resolve_references(False, references)
    assert type(obj.a) == list
    assert len(obj.a) == 3
    assert obj.get_property_metadata("a").datatype == "LIST<TestReference>"
    for i in range(3):
        assert type(obj.a[i]) == CaosDBPythonRecord

    assert obj.a[0].val == "1 bla"

    # Conversion with embedded records:
    r2 = db.Record()
    r2.add_property(name="a", value=4)
    r3 = db.Record()
    r3.add_property(name="b", value=8)

    r = db.Record()
    r.add_property(name="a", value=[r2, r3])

    obj = convert_to_python_object(r)
    assert type(obj.a) == list
    assert len(obj.a) == 2
    assert obj.a[0].a == 4
    assert obj.a[1].b == 8

    # Serialization
    text = str(obj)
    text2 = str(convert_to_python_object(r2)).split("\n")
    print(text)
    # cut away first two characters in text
    text = [line[4:] for line in text.split("\n")]
    for line in text2:
        assert line in text


# Test utility functions:
def test_type_conversion():
    assert high_level_type_for_standard_type(db.Record()) == CaosDBPythonRecord
    assert high_level_type_for_standard_type(db.Entity()) == CaosDBPythonEntity
    assert standard_type_for_high_level_type(CaosDBPythonRecord()) == db.Record
    assert standard_type_for_high_level_type(CaosDBPythonEntity()) == db.Entity
    assert standard_type_for_high_level_type(CaosDBPythonFile(), True) == "File"
    assert standard_type_for_high_level_type(CaosDBPythonRecord(), True) == "Record"
    assert high_level_type_for_role("Record") == CaosDBPythonRecord
    assert high_level_type_for_role("Entity") == CaosDBPythonEntity
    assert high_level_type_for_role("File") == CaosDBPythonFile
    with pytest.raises(RuntimeError, match="Unknown role."):
        high_level_type_for_role("jkaldjfkaldsjf")

    with pytest.raises(RuntimeError, match="Incompatible type."):
        standard_type_for_high_level_type(42, True)

    with pytest.raises(ValueError):
        high_level_type_for_standard_type("ajsdkfjasfkj")

    with pytest.raises(RuntimeError, match="Incompatible type."):
        class IncompatibleType(db.Entity):
            pass
        high_level_type_for_standard_type(IncompatibleType())


def test_deserialization():
    r = db.Record(id=17, name="test")
    r.add_parent("bla")
    r.add_property(name="a", value=42)
    r.add_property(name="b", value="test")

    obj = convert_to_python_object(r)

    serial = obj.serialize()
    obj_des = CaosDBPythonEntity.deserialize(serial)

    assert obj_des.name == "test"
    assert obj_des.id == 17
    assert obj_des.has_parent(CaosDBPythonUnresolvedParent(name="bla"))
    print(obj)
    print(obj_des)

    # This test is very strict, and might fail if order in dictionary is not preserved:
    assert obj.serialize() == obj_des.serialize()

    f = db.File()
    f.file = "bla.test"
    f.path = "/test/n/bla.test"

    obj = convert_to_python_object(f)

    serial = obj.serialize()
    obj_des = CaosDBPythonEntity.deserialize(serial)
    assert obj_des.file == "bla.test"
    assert obj_des.path == "/test/n/bla.test"

    r = db.Record(id=17, name="test")
    r.add_parent("bla")
    r.add_property(name="a", value=42)
    r.add_property(name="b", value="test")

    ref = db.Record(id=28)
    ref.add_parent("bla1")
    ref.add_parent("bla2")
    ref.add_property(name="c", value=5,
                     unit="s", description="description missing")
    r.add_property(name="ref", value=ref)

    obj = convert_to_python_object(r)

    serial = obj.serialize()
    obj_des = CaosDBPythonEntity.deserialize(serial)
    assert obj.serialize() == obj_des.serialize()


@pytest.fixture
def get_record_container():
    record_xml = """
<Entities>
  <Record id="109">
    <Version id="da669fce50554b2835c3826cf717d6a4532f02de" head="true">
      <Predecessor id="68534369c5fd05e5bb1d37801a3dbc1532a8e094"/>
    </Version>
    <Parent id="103" name="Experiment" description="General type for all experiments in our lab"/>
    <Property id="104" name="alpha" description="A fictitious measurement" datatype="DOUBLE" unit="km" importance="FIX" flag="inheritance:FIX">16.0</Property>
    <Property id="107" name="date" datatype="DATETIME" importance="FIX" flag="inheritance:FIX">2022-03-16</Property>
    <Property id="108" name="identifier" datatype="TEXT" importance="FIX" flag="inheritance:FIX">Demonstration</Property>
    <Property id="111" name="sources" description="The elements of this lists are scientific activities that this scientific activity is based on." datatype="LIST&lt;ScientificActivity&gt;" importance="FIX" flag="inheritance:FIX">
      <Value>109</Value>
    </Property>
  </Record>
</Entities>"""

    c = db.Container.from_xml(record_xml)
    return c


def test_recursion(get_record_container):
    r = convert_to_python_object(get_record_container[0])
    r.resolve_references(r, get_record_container)
    assert r.id == 109
    assert r.sources[0].id == 109
    assert r.sources[0].sources[0].id == 109
    assert "&id001" in str(r)
    assert "*id001" in str(r)

    d = r.serialize(True)
    assert r.sources[0] == r.sources[0].sources[0]


@pytest.mark.xfail
def test_recursion_advanced(get_record_container):
    # TODO:
    # This currently fails, because resolve is done in a second step
    # and therefore a new python object is created for the reference.
    r = convert_to_python_object(get_record_container[0])
    r.resolve_references(r, get_record_container)
    d = r.serialize(True)
    assert r == r.sources[0]
