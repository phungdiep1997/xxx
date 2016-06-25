String
------

- Create string
- Single quote, double quote
- Triple quote
- Multi lines
- Escaping ``\n \t \\ \' \"``
- Automatically concat
- Indexing
- Slicing
- Reverse
- len()
- ASCII, Unicode, bits and byte.
- Immutable

Variable
--------

Name
----

Binding
~~~~~~~

Object
~~~~~~

name --binding--> object

![](/Resource/var_binding.jpg)


- use id() to get "identify" of an object.
- two names bind to same object with have id(x) == id(y)
- #TODO add objgraph for above example here.

Deleting name
-------------

Before:

```
~Namespace~~~~\
|name          \ --binding--> object
|---------------
```

After

```
~Namespace~~~~\
|              \         object
|---------------
```

And Garbage collector will collect object, remove it from memory.

Deletion of a name removes the binding of that name from the local or global
namespace, depending on whether the name occurs in a global statement in the
same code block. If the name is unbound, a NameError exception will be raised.

Hashing
-------

- hash function
- hash()

Builtin functions
-----------------

https://docs.python.org/3/library/functions.html

- all
- any
- chr
- dir
- globals()
- locals
- input
- min
- max
- ord
