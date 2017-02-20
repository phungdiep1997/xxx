Git commands
============

Install
-------

Ubuntu
~~~~~~

  sudo apt-get install -y git tig

Git clone
---------

> Clone a repository into a new directory

Command::

  git clone https://gitlab.com/pyfml/pyfml.git pyfml

Or use ssh::

  git clone git@gitlab.com:pyfml/pyfml.git pyfml

Change directory to cloned directory::

  cd pyfml

Git branch
----------

> git-checkout - Checkout a branch or paths to the working tree

Display current branch::

  git branch

Create new branch::

  git checkout -b branch_name

Change branch::

  git checkout branch_name

Change code, then add it to git::

  git add baitapX.py

Commit it::

  git commit -m 'add baitapX.py'

Push branch to remote::

  git push remote_name branch_name
  E.g: git push origin hvn

Delete branch::

  git branch -d branch_name

Git commands
------------

- git status
- git fetch
- git merge
- git pull
- git remote -v
- get help XXX
- git checkout branch
- git log
- ``git add .``
- ``git add -u``
- git revert
- git pull = git fetch + git merge
- let's merge!
- git log --graph

Merge request (MR)
------------------

- learn to create branch
- create MR
- review on MR
- pull request on Github (https://github.com/saltstack/salt/pulls)

Cheat sheet
-----------

https://training.github.com/kit/downloads/github-git-cheat-sheet.pdf
