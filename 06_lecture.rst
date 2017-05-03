6. File, JSON, Function, Exception
==================================

try/except basic
----------------

::

  d = {'lactroi': 10041243}
  try:
      views = d['lactroi']
  except KeyError as e:
      print(e)
  else:
      print("Đứng đầu bảng xếp hạng là Lạc trôi với %d views" % views)

with statement
--------------

- auto close resources.
- context manager protocol.
  https://docs.python.org/2/whatsnew/2.6.html?highlight=contextmanager#pep-343-the-with-statement

JSON
----

- often used for API
- Dump json::

  $ echo '{"message": "Validation Failed", "errors": [{"field": "title", "code": "missing_field", "resource": "Issue"}]}' | python -m json.tool
  {
      "errors": [
          {
              "code": "missing_field",
              "field": "title",
              "resource": "Issue"
          }
      ],
      "message": "Validation Failed"
  }


CSV
---

Pickle
------

User-defined function
---------------------

double = lambda x: x * 2
print(double(2))

sum2 = lambda x, y: x + y

Function
--------

- Built-in functions
- User-defined function::

    def func_name(arg1, args):  # function signature
        '''Docstring
        end of docstring'''

        body_of_function
        return something

- Function name, indent
- Return None, return value
- Keyword argument, position argument
- Default argument, position, default value types
- Local variable scope
- Return best practice (one type only)
- When to write a function (need to repeat more than twice)
- Mandatory arguments, optional arguments
- Positional arguments, keyword arguments
- Function aliasing: https://github.com/saltstack/salt/blob/develop/salt/states/virtualenv_mod.py#L274
- Side effect
- Function in function
- Meaning of function which has name starts with ``_``
- ``*args, **kwargs, print(*args)``  # after dict only
- Recursive function

::
    def calculate_average_age(first_age, second_age):
        total_of_all_ages = first_age + second_age
        return total_of_all_ages / 2
