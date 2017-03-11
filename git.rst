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

Our workflow
------------

- Clone repo
- Checkout ``master`` branch; run ``git pull`` to get latest version.
- Create new branch start with your name (change HN1702 to your class code)::

    git checkout -b HN1702_MYNAME_master

- Push to server::

    git push origin HN1702_MYNAME_master # origin is remote name (default), HN1702_MYNAME_master is branch name

  .. note::

    You can only push to BRANCHX when you checked out branch BRANCHX

- Now you have your base branch. Every time you do homework, checkout
  ``HN1702_MYNAME_master`` an create new branch. E.g: HN1702_MYNAME_ex3
  And commit, push, create MR against ``HN1702_MYNAME_master``

Dùng script nopbai.py
~~~~~~~~~~~~~~~~~~~~~

.. note::

    Chú ý, bài tập phải là file có đuôi .py, đặt trong thư mục exercises

Nếu gặp khó khăn khi dùng Git, chạy script nopbai.py với tên branch
cần tạo để nộp bài. Ví dụ::

  [hvn:~/me/pyfml] $ python nopbai.py hcm1702_hvnex4
  Đang lấy thông tin mới từ GitLab
  Your branch is up-to-date with 'origin/master'.
  HEAD is now at b36db6b Add prefix to branch name
  [hcm1702_hvnex4 0d74273] hcm1702_hvnex4 add exs
   1 file changed, 0 insertions(+), 0 deletions(-)
    create mode 100644 exercises/ex45.py
    Nộp bài thành công
    Vào https://gitlab.com/pyfml/pyfml/merge_requests để tạo Merge Request.

Cheat sheet
-----------

https://training.github.com/kit/downloads/github-git-cheat-sheet.pdf
