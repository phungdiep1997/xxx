11. API, Flask, Jinja2, DB, ORM, Sphinx
=======================================

Sphinx
------

Make doc from .rst files in this directory.

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


Jinja2
------

ORM
---

TDD
---

- unittest
- BDD
- http://flask.pocoo.org/docs/0.10/testing/
- https://docs.djangoproject.com/en/1.8/topics/testing/


Top packages
------------

- http://pythonwheels.com/
- https://github.com/hvnsweeting/pypitop
