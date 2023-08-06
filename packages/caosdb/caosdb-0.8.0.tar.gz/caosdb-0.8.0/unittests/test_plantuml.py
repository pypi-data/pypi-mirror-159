#!/usr/bin/env python3
# encoding: utf-8
#
# ** header v3.0
# This file is a part of the CaosDB Project.
#
# Copyright (C) 2022 Indiscale GmbH <info@indiscale.com>
# Copyright (C) 2022 Henrik tom Wörden <h.tomwoerden@indiscale.com>
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

"""
test plantuml utility
"""

import tempfile
import pytest
import caosdb as db
import shutil
from caosdb.utils.plantuml import to_graphics


@pytest.fixture
def setup_n_teardown(autouse=True):

    with tempfile.TemporaryDirectory() as td:
        global output
        output = td
        yield


@pytest.fixture
def entities():
    return [db.RecordType(name="TestRT1").add_property("testprop"),
            db.RecordType(name="TestRT2").add_property("testprop2"),
            db.Property("testprop")]


@pytest.mark.skipif(shutil.which('plantuml') is None, reason="No plantuml found")
def test_to_graphics1(entities, setup_n_teardown):
    to_graphics(entities, "data_model", output_dirname=output)


@pytest.mark.skipif(shutil.which('plantuml') is None, reason="No plantuml found")
def test_to_graphics2(entities, setup_n_teardown):
    to_graphics(entities, "data_model", output_dirname=output, formats=["tpng", "tsvg"],
                add_properties=False, add_legend=False, style="salexan")
