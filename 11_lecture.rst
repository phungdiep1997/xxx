11. API, Flask
==============

What is API?
------------

- Application programming interface.
- Endpoints
- Slug
- URL
- URI

Flask
-----

Components
~~~~~~~~~~

- Routing
- Templating

Exercise: write an endpoint that return list of running process
(ps xau) in JSON format::

  [
    {
      'PID': NUMBER,
      'CPU': PERCENT_CPU,
      'MEM': PERCENT_MEM,
      'CMD': COMMAND,
    },
    {...}
  ]

StackOverFlow
-------------

http://stackoverflow.com/questions/tagged/python

Terms
-----

Top packages
------------

- http://pythonwheels.com/
- https://github.com/hvnsweeting/pypitop
