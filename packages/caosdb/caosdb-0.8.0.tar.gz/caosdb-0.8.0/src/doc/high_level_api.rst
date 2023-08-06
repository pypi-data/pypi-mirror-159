High Level API
==============

In addition to the old standard pylib API, new versions of pylib ship
with a high level API that facilitates usage of CaosDB entities within
data analysis scripts. In a nutshell that API exposes all properties of
CaosDB Records as standard python attributes making their access easier.

Or to speak it out directly in Python:

.. code:: python


   import caosdb as db
   # Old API:
   r = db.Record()
   r.add_parent("Experiment")
   r.add_property(name="alpha", value=5)
   r.get_property("alpha").value = 25 # setting properties (old api)
   print(r.get_property("alpha").value + 25) # getting properties (old api)

   from caosdb.high_level_api import convert_to_python_entity
   obj = convert_to_python_object(r) # create a high level entity
   obj.r = 25 # setting properties (new api)
   print(obj.r + 25) # getting properties (new api)

Quickstart
----------

The module, needed for the high level API is called:
``caosdb.high_level_api``

There are two functions converting entities between the two
representation (old API and new API):

-  ``convert_to_python_object``: Convert entities from **old** into
   **new** representation.
-  ``convert_to_entity``: Convert entities from **new** into **old**
   representation.

Furthermore there are a few utility functions which expose very
practical shorthands:

-  ``new_high_level_entity``: Retrieve a record type and create a new
   high level entity which contains properties of a certain importance
   level preset.
-  ``create_record``: Create a new high level entity using the name of a
   record type and a list of key value pairs as properties.
-  ``load_external_record``: Retrieve a record with a specific name and
   return it as high level entity.
-  ``create_entity_container``: Convert a high level entity into a
   standard entity including all sub entities.
-  ``query``: Do a CaosDB query and return the result as a container of
   high level objects.

So as a first example, you could retrieve any record from CaosDB and use
it using its high level representation:

.. code:: python

   from caosdb.high_level_api import query

   res = query("FIND Record Experiment")
   experiment = res[0]
   # Use a property:
   print(experiment.date)

   # Use sub properties:
   print(experiment.output[0].path)

The latter example demonstrates, that the function query is very
powerful. For its default parameter values it automatically resolves and
retrieves references recursively, so that sub properties, like the list
of output files "output", become immediately available.

**Note** that for the old API you were supposed to run the following
series of commands to achieve the same result:

.. code:: python

   import caosdb as db

   res = db.execute_query("FIND Record Experiment")
   output = res.get_property("output")
   output_file = db.File(id=output.value[0].id).retrieve()
   print(output_file.path)

Resolving subproperties makes use of the "resolve\ :sub:`reference`"
function provided by the high level entity class
(``CaosDBPythonEntity``), with the following parameters:

-  ``deep``: Whether to use recursive retrieval
-  ``references``: Whether to use the supplied db.Container to resolve
   references. This allows offline usage. Set it to None if you want to
   automatically retrieve entities from the current CaosDB connection.
-  ``visited``: Needed for recursion, set this to None.

Objects in the high level representation can be serialized to a simple
yaml form using the function ``serialize`` with the following
parameters:

-  ``without_metadata``: Set this to True if you don't want to see
   property metadata like "unit" or "importance".
-  ``visited``: Needed for recursion, set this to None.

This function creates a simple dictionary containing a representation of
the entity, which can be stored to disk and completely deserialized
using the function ``deserialize``.

Furthermore the "*str*" function is overloaded, so that you can use
print to directly inspect high level objects using the following
statement:

.. code:: python

   print(str(obj))

Concepts
--------

As described in the section Quickstart the two functions
``convert_to_python_object`` and ``convert_to_entity`` convert entities
beetween the high level and the standard representation.

The high level entities are represented using the following classes from
the module ``caosdb.high_level_api``:

-  ``CaosDBPythonEntity``: Base class of the following entity classes.
-  ``CaosDBPythonRecord``
-  ``CaosDBPythonRecordType``
-  ``CaosDBPythonProperty``
-  ``CaosDBPythonMultiProperty``: **WARNING** Not implemented yet.
-  ``CaosDBPythonFile``: Used for file entities and provides an
   additional ``download`` function for being able to directly retrieve
   files from CaosDB.

In addition, there are the following helper structures which are
realized as Python data classes:

-  ``CaosDBPropertyMetaData``: For storing meta data about properties.
-  ``CaosDBPythonUnresolved``: The base class of unresolved "things".
-  ``CaosDBPythonUnresolvedParent``: Parents of entities are stored as
   unresolved parents by default, storing an id or a name of a parent
   (or both).
-  ``CaosDBPythonUnresolvedReference``: An unresolved reference is a
   reference property with an id which has not (yet) been resolved to an
   Entity.

The function "resolve\ :sub:`references`" can be used to recursively
replace ``CaosDBPythonUnresolvedReferences`` into members of type
``CaosDBPythonRecords`` or ``CaosDBPythonFile``.

Each property stored in a CaosDB record corresponds to:

-  a member attribute of ``CaosDBPythonRecord`` **and**
-  an entry in a dict called "metadata" storing a CaosDBPropertyMetadata
   object with the following information about proeprties:

   -  ``unit``
   -  ``datatype``
   -  ``description``
   -  ``id``
   -  ``importance``
