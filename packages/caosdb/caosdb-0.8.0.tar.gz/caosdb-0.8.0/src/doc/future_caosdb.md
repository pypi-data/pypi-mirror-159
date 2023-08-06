# The future of the CaosDB Python Client

The current Python client has done us great services but its structure and the 
way it is used sometimes feels outdated and clumsy. In this document we sketch
how it might look different in future and invite everyone to comment or
contribute to this development.

At several locations in this document there will be links to discussion issues.
If you want to discuss something new, you can create a new issue
[here](https://gitlab.com/caosdb/caosdb-pylib/-/issues/new).

## Overview
Let's get a general impression before discussing single aspects.

``` python
import caosdb as db
experiments = db.query("FIND Experiment")
# print name and date for each `Experiment`
for exp in experiments:
   print(exp.name, exp.date)

# suppose `Experiments` reference `Projects` which have a `Funding` Property
one_exp = experiments[0]
print(one_exp.Project.Funding)

new_one = db.create_record("Experiment")
new_one.date = "2022-01-01"
new_one.name = "Needle Measurement"
new_one.insert()
```
Related discussions:
- [recursive retrieve in query](https://gitlab.com/caosdb/caosdb-pylib/-/issues/57)
- [create_record function](https://gitlab.com/caosdb/caosdb-pylib/-/issues/58)
- [data model utility](https://gitlab.com/caosdb/caosdb-pylib/-/issues/59)

## Quickstart
Note that you can try out one possible implementation using the 
`caosdb.high_level_api` module. It is experimental and might be removed in 
future!

A `resolve_references` function allows to retrieve the referenced entities of 
an entity, container or a query result set (which is a container).
It has the following parameters which can also be supplied to the `query` 
function:

-   `deep`: Whether to use recursive retrieval
-   `depth`: Maximum recursion depth
-   `references`: Whether to use the supplied db.Container to resolve
    references. This allows offline usage. Set it to None if you want to
    automatically retrieve entities from the current CaosDB connection.

In order to allow a quick look at the object structures an easily readable 
serialization is provided by the `to_dict` function. It has the following 
argument:
-   `without_metadata`: Set this to True if you don\'t want to see
    property metadata like \"unit\" or \"importance\".

This function creates a simple dictionary containing a representation of
the entity, which can be stored to disk and completely deserialized
using the function `from_dict`.

Furthermore, the `__str__` function uses this to display objects in yaml 
format by default statement

## Design Decisions

### Dot Notation
Analogue, to what Pandas does. Provide bracket notation 
`rec.properties["test"]` for Properties with names that are in conflict with 
default attributes or contain spaces (or other forbidden characters).

Entities can be initialized with a set of Propertynames. Those Propertynames will be used as 
attributes such that tab completion is possible in interactive use. The value however will be a special
value (e.g. UnsetPropertyValue) and accessing it results in an Exception. Thus, tab completion can be used 
but no Properties are inserted unexpectedly with NULL values. 

- Raise Exception if attribute does not exist but is accessed?

[Discussion](https://gitlab.com/caosdb/caosdb-pylib/-/issues/60)

We aim for a distinction between "concrete" Properties of Records/RecordTypes and "abstract" Properties as part of the definition of a data model. Concrete properties are always "contained" in a record or record type while abstract properties stand for themselves.

Draft:
```
class ConcreteProperty:
  def __init__(self, v, u):
    self.value = v
    self.unit = u
    
class Entity:
  def __init__(self):
    pass
    
  def __setattr__(self, name, val):
    if name not in dir(self):
        # setattr(self, name, ConcreteProperty(val, None))
        self.properties[name] = ConcreteProperty(val, None)
    else:
        # getattribute(self, name).value = val
        self.properties[name].value = val
```

The old "get_property" functions serves the same purpose as the new "[]" notation.

Instead of `get_property` / `add_property` etc. functions belonging to class Entity, we should refactor the list of properties (of an entity) to be a special kind of list, e.g. PropertyList.
This list should enherit from a standard list, have all the known functions like "append", "extend", "__in__" and allow for all property-related functionality as part of its member functions (instead of access via Entity directly).
Same story for the parents.

**GET RID OF MULTI PROPERTIES!!!**

#### how to deal with "property metadata"

Current suggestion: stored in a special field "property_metadata" belonging to the object.
`property_metadata` is a dict:
- importance
- unit
- description
- ...

### Serialization
What information needs to be contained in (meta)data? How compatible is it with 
GRPC json serialization?


### Recursive Retrieval



I can resolve later and end up with the same result:
`recs =db.query("FIND Experiment", depth=2)`  equals `recs = db.query("FIND Experiment"); recs = resolve_references(recs, depth=2)`

[Discussion](https://gitlab.com/caosdb/caosdb-pylib/-/issues/57)


#### Alternative

`FIND Experiment` with `depth=2` will retrieve all referenced entities from any experiment found. A typical use case could also be:

```python
recs = db.query("FIND Experiment")
recs[0].resolve_references(depth=2)
```

#### Idea

Recursive retrievel as functionality of the server.

retrieve and query commands should support the `depth` argument.

### In-Place operations
Default behavior is to return new objects instead of modifying them in-place.
This can be changed with the argument `inplace=True`.
Especially the following functions operate by default NOT in-place:
- update
- insert
- retrieve
- resolve_references
[Discussion](https://gitlab.com/caosdb/caosdb-pylib/-/issues/61)

## Extended Example
``` python
import caosdb as db

dm = db.get_data_model()

new_one = db.create_record(dm.Experiment)
new_one.date = "2022-01-01"
new_one.name = "Needle Measurement"
new_one.dataset = db.create_record(dm.Dataset)
new_one.dataset.voltage = (5, "V")
new_one.dataset.pulses = [5, 5.3]
inserted = new_one.insert()
print("The new record has the ID:", inserted.id)
```

### Factory method
While creating an Entity will not talk to a CaosDB server and can thus be done offline, the factory method
`create_record` allows to 
1. Retrieve the parent and set attributes according to inheritance
2. Use a container to resolve the parent and set attributes

In general, more complex "magic" will be placed in the factory and only the straight forward version 
in the constructor.

### References and sub entities

Several possibilities exist for references:

- value is the id of a referenced entity
- value is a "sub object"
- value is a reference to another (entity-)list element (similar to second variant, but with "sub object" always contained in container/entity-list)

To be discussed: Which should be the obligatory/preferred variant?
