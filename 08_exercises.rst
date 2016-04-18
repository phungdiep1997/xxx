Lecture 08
==========

Python script = python module + if __name__ == '__main__' + set header + chmod

8.1
---

Write a python script that simulate ``cat`` command::

    pass 1 argument : path of file (mycat.py /etc/passwd)
    print that file's content

Use ``sys.argv``

8.2
---

Write a python script prints names of all functions and classes in a module (and
count how many functions, how many classes)::

    func_class.py func_class.py

8.3
---

Write a python script which analysis a python packages (a directory).
Print out:

- Number of modules
- Number of classes
- Number of functions
- Top 10 most used variables

Use: ``os.walk``

8.4
---

Write a python script simulates
`head <http://manpages.ubuntu.com/manpages/trusty/en/man1/head.1.html>`_
and `tail <http://manpages.ubuntu.com/manpages/trusty/en/man1/tail.1.html>`_
commands.

Usage::

  head_tail.py -h file_path

  Print 10 first lines of file_path

  head_tail.py -t file_path

  Print 10 last lines of file_path

Use ``sys.argv``
