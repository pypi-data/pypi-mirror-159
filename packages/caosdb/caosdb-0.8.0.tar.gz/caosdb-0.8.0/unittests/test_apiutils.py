# -*- encoding: utf-8 -*-
#
# This file is a part of the CaosDB Project.
#
# Copyright (C) 2018 Research Group Biomedical Physics,
# Max-Planck-Institute for Dynamics and Self-Organization Göttingen
# Copyright (C) 2020 Timm Fitschen <t.fitschen@indiscale.com>
# Copyright (C) 2020-2022 IndiScale GmbH <info@indiscale.com>
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
# Test apiutils
# A. Schlemmer, 02/2018


import pytest
import caosdb as db
import caosdb.apiutils
from caosdb.apiutils import (apply_to_ids, compare_entities, create_id_query,
                             resolve_reference, merge_entities)

from caosdb.common.models import SPECIAL_ATTRIBUTES


def test_apply_to_ids():
    parent = db.RecordType(id=3456)
    rec = db.Record(id=23)
    p = db.Property(id=23345, datatype=db.INTEGER)
    rec.add_parent(parent)
    rec.add_property(p)

    def invert(id_):
        return id_ * -1
    apply_to_ids([rec], invert)

    assert invert(3456) == -3456
    assert rec.parents[0].id == -3456
    assert rec.properties[0].id == -23345
    assert rec.id == -23


def test_id_query():
    ids = [1, 2, 3, 4, 5]
    assert create_id_query(ids) == 'FIND ENTITY WITH ID=1 OR ID=2 OR ID=3 OR '\
        'ID=4 OR ID=5'


def test_resolve_reference():
    original_retrieve_entity_with_id = caosdb.apiutils.retrieve_entity_with_id
    caosdb.apiutils.retrieve_entity_with_id = lambda eid: db.Record(id=eid)

    prop = db.Property(id=1, datatype=db.REFERENCE, value=100)
    prop.is_valid = lambda: True
    items = [200, 300, 400]
    prop_list = db.Property(datatype=db.LIST(db.REFERENCE),
                            value=items)
    prop_list2 = db.Property(datatype=db.LIST(db.REFERENCE),
                             value=[db.Record(id=500)])
    resolve_reference(prop)
    resolve_reference(prop_list)
    resolve_reference(prop_list2)
    assert prop.value.id == 100
    assert isinstance(prop.value, db.Entity)

    prop_list_ids = []

    for i in prop_list.value:
        prop_list_ids.append(i.id)
        assert isinstance(i, db.Entity)
    assert prop_list_ids == items

    for i in prop_list2.value:
        assert i.id == 500
        assert isinstance(i, db.Entity)

    no_reference = db.Property(id=5000, datatype=db.INTEGER, value=2)
    resolve_reference(no_reference)
    assert no_reference.value == 2
    assert no_reference.datatype is db.INTEGER

    # restore retrive_entity_with_id
    caosdb.apiutils.retrieve_entity_with_id = original_retrieve_entity_with_id


def test_compare_entities():
    r1 = db.Record()
    r2 = db.Record()
    r1.add_parent("bla")
    r2.add_parent("bla")
    r1.add_parent("lopp")
    r1.add_property("test", value=2)
    r2.add_property("test", value=2)
    r1.add_property("tests", value=3)
    r2.add_property("tests", value=45)
    r1.add_property("tester", value=3)
    r2.add_property("tester", )
    r1.add_property("tests_234234", value=45)
    r2.add_property("tests_TT", value=45)

    diff_r1, diff_r2 = compare_entities(r1, r2)

    assert len(diff_r1["parents"]) == 1
    assert len(diff_r2["parents"]) == 0
    assert len(diff_r1["properties"]) == 3
    assert len(diff_r2["properties"]) == 3

    assert "test" not in diff_r1["properties"]
    assert "test" not in diff_r2["properties"]

    assert "tests" in diff_r1["properties"]
    assert "tests" in diff_r2["properties"]

    assert "tester" in diff_r1["properties"]
    assert "tester" in diff_r2["properties"]

    assert "tests_234234" in diff_r1["properties"]
    assert "tests_TT" in diff_r2["properties"]


def test_compare_entities_units():
    r1 = db.Record()
    r2 = db.Record()
    r1.add_parent("bla")
    r2.add_parent("bla")
    r1.add_parent("lopp")
    r1.add_property("test", value=2, unit="cm")
    r2.add_property("test", value=2, unit="m")
    r1.add_property("tests", value=3, unit="cm")
    r2.add_property("tests", value=45, unit="cm")
    r1.add_property("tester", value=3)
    r2.add_property("tester", )
    r1.add_property("tests_234234", value=45, unit="cm")
    r2.add_property("tests_TT", value=45, unit="cm")

    diff_r1, diff_r2 = compare_entities(r1, r2)

    assert len(diff_r1["parents"]) == 1
    assert len(diff_r2["parents"]) == 0
    assert len(diff_r1["properties"]) == 4
    assert len(diff_r2["properties"]) == 4

    assert "tests" in diff_r1["properties"]
    assert "tests" in diff_r2["properties"]

    assert "tester" in diff_r1["properties"]
    assert "tester" in diff_r2["properties"]

    assert "tests_234234" in diff_r1["properties"]
    assert "tests_TT" in diff_r2["properties"]

    assert diff_r1["properties"]["test"]["unit"] == "cm"
    assert diff_r2["properties"]["test"]["unit"] == "m"


def test_compare_special_properties():
    # Test for all known special properties:
    SPECIAL_PROPERTIES = ("description", "name",
                          "checksum", "size", "path", "id")
    INTS = ("size", "id")
    HIDDEN = ("checksum", "size")

    for key in SPECIAL_PROPERTIES:
        set_key = key
        if key in HIDDEN:
            set_key = "_" + key
        r1 = db.Record()
        r2 = db.Record()
        if key not in INTS:
            setattr(r1, set_key, "bla 1")
            setattr(r2, set_key, "bla 1")
        else:
            setattr(r1, set_key, 1)
            setattr(r2, set_key, 1)

        diff_r1, diff_r2 = compare_entities(r1, r2)
        assert key not in diff_r1
        assert key not in diff_r2
        assert len(diff_r1["parents"]) == 0
        assert len(diff_r2["parents"]) == 0
        assert len(diff_r1["properties"]) == 0
        assert len(diff_r2["properties"]) == 0

        if key not in INTS:
            setattr(r2, set_key, "bla test")
        else:
            setattr(r2, set_key, 2)

        diff_r1, diff_r2 = compare_entities(r1, r2)
        assert key in diff_r1
        assert key in diff_r2
        if key not in INTS:
            assert diff_r1[key] == "bla 1"
            assert diff_r2[key] == "bla test"
        else:
            assert diff_r1[key] == 1
            assert diff_r2[key] == 2
        assert len(diff_r1["properties"]) == 0
        assert len(diff_r2["properties"]) == 0


@pytest.mark.xfail
def test_compare_properties():
    p1 = db.Property()
    p2 = db.Property()

    diff_r1, diff_r2 = compare_entities(p1, p2)
    assert len(diff_r1["parents"]) == 0
    assert len(diff_r2["parents"]) == 0
    assert len(diff_r1["properties"]) == 0
    assert len(diff_r2["properties"]) == 0

    p1.importance = "SUGGESTED"
    diff_r1, diff_r2 = compare_entities(p1, p2)
    assert len(diff_r1["parents"]) == 0
    assert len(diff_r2["parents"]) == 0
    assert len(diff_r1["properties"]) == 0
    assert len(diff_r2["properties"]) == 0
    assert "importance" in diff_r1
    assert diff_r1["importance"] == "SUGGESTED"

    # TODO: I'm not sure why it is not like this:
    # assert diff_r2["importance"] is None
    # ... but:
    assert "importance" not in diff_r2

    p2.importance = "SUGGESTED"
    p1.value = 42
    p2.value = 4

    diff_r1, diff_r2 = compare_entities(p1, p2)
    assert len(diff_r1["parents"]) == 0
    assert len(diff_r2["parents"]) == 0
    assert len(diff_r1["properties"]) == 0
    assert len(diff_r2["properties"]) == 0

    # Comparing values currently does not seem to be implemented:
    assert "value" in diff_r1
    assert diff_r1["value"] == 42
    assert "value" in diff_r2
    assert diff_r2["value"] == 4


def test_copy_entities():
    r = db.Record(name="A")
    r.add_parent(name="B")
    r.add_property(name="C", value=4, importance="OBLIGATORY")
    r.add_property(name="D", value=[3, 4, 7], importance="OBLIGATORY")
    r.description = "A fancy test record"

    c = r.copy()

    assert c is not r
    assert c.name == "A"
    assert c.role == r.role
    assert c.parents[0].name == "B"
    # parent and property objects are not shared among copy and original:
    assert c.parents[0] is not r.parents[0]

    for i in [0, 1]:
        assert c.properties[i] is not r.properties[i]
        for special in SPECIAL_ATTRIBUTES:
            assert getattr(c.properties[i], special) == getattr(r.properties[i], special)
        assert c.get_importance(c.properties[i]) == r.get_importance(r.properties[i])


def test_merge_entities():
    r = db.Record(name="A")
    r.add_parent(name="B")
    r.add_property(name="C", value=4, importance="OBLIGATORY")
    r.add_property(name="D", value=[3, 4, 7], importance="OBLIGATORY")
    r.description = "A fancy test record"

    r2 = db.Record()
    r2.add_property(name="F", value="text")
    merge_entities(r2, r)
    assert r2.get_parents()[0].name == "B"
    assert r2.get_property("C").name == "C"
    assert r2.get_property("C").value == 4
    assert r2.get_property("D").name == "D"
    assert r2.get_property("D").value == [3, 4, 7]

    assert r2.get_property("F").name == "F"
    assert r2.get_property("F").value == "text"


def test_merge_bug_109():
    rt = db.RecordType(name="TestBug")
    p = db.Property(name="test_bug_property", datatype=db.LIST(db.INTEGER))

    r_b = db.Record(name="TestRecord")
    r_b.add_parent(rt)
    r_b.add_property(p, value=[18, 19])

    r_a = db.Record(name="TestRecord")
    r_a.add_parent(rt)

    merge_entities(r_a, r_b)

    assert r_b.get_property("test_bug_property").value == [18, 19]
    assert r_a.get_property("test_bug_property").value == [18, 19]

    assert "<Value>18</Value>\n    <Value>19</Value>" in str(r_b)
    assert "<Value>18</Value>\n    <Value>19</Value>\n    <Value>18</Value>\n    <Value>19</Value>" not in str(r_b)

    assert "<Value>18</Value>\n    <Value>19</Value>" in str(r_a)
    assert "<Value>18</Value>\n    <Value>19</Value>\n    <Value>18</Value>\n    <Value>19</Value>" not in str(r_a)


@pytest.mark.xfail
def test_bug_109():
    rt = db.RecordType(name="TestBug")
    p = db.Property(name="test_bug_property", datatype=db.LIST(db.INTEGER))

    r_b = db.Record(name="TestRecord")
    r_b.add_parent(rt)
    r_b.add_property(p, value=[18, 19])

    r_a = db.Record(name="TestRecord")
    r_a.add_parent(rt)
    r_a.add_property(r_b.get_property("test_bug_property"))

    assert r_b.get_property("test_bug_property").value == [18, 19]
    assert r_a.get_property("test_bug_property").value == [18, 19]

    assert "<Value>18</Value>\n    <Value>19</Value>" in str(r_b)
    assert "<Value>18</Value>\n    <Value>19</Value>\n    <Value>18</Value>\n    <Value>19</Value>" not in str(r_b)

    assert "<Value>18</Value>\n    <Value>19</Value>" in str(r_a)
    assert "<Value>18</Value>\n    <Value>19</Value>\n    <Value>18</Value>\n    <Value>19</Value>" not in str(r_a)
