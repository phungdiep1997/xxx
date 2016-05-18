Exercise
========

10.1
----

Write a script to list all Github repositories of an user.

For example, user ``hvnsweeting``, use:
https://api.github.com/users/hvnsweeting/repos

Form::

  githubrepos.py username

Libs:

- argparse
- logging
- requests

10.2
----

Viết một script kiểm tra xem các số argument đầu vào có trúng lô không
(2 số cuối trùng với một giải nào đó). Nếu không có argument nào thì print
ra tất cả các giải từ đặc biệt -> giải 7.

Lấy kết quả từ ``ketqua.net``.

Form::

  ketqua.py [NUMBER1] [NUMBER2]

Libs:

- beautifulsoup4
- requests
- logging

Tips:

- ``nargs`` https://docs.python.org/2/library/argparse.html

10.3
----

Sử dụng ``requests`` viết một script lấy toàn bộ thông tin các Page của
các quán cafe, trà ở trung tâm Hà Nội bằng **Facebook Graph API**.  

Các từ khóa: ``"coffee", "tea", "cafe", "caphe"``.  

Tọa độ: ``21.027875, 105.853654`` với bán kính là ``2km``.  

Trả về kết quả bao gồm ``name, id, location, website`` của mỗi Page.  

- Sử dụng module quét tọa độ trong file ``./Resource/coorcal.py``  

- Hướng dẫn dùng Facebook API:  

https://developers.facebook.com/docs/graph-api/using-graph-api#search  

- Sử dụng Grapth API Explorer để thử:  

https://developers.facebook.com/tools-and-support/  

- Sử dụng App ID và App Secret sau để lấy token:  

``App ID: 1537101179929447``  

``App Secret: 4da789d9de5f279a58051e629a4c6ef3``  

- Hướng dẫn tạo Token: 

https://developers.facebook.com/docs/facebook-login/access-tokens/#apptokens  

**Chú ý**:  

- Để ý đến phần paging của mỗi response trả về. Hãy bấm vào đó để xem chuyện gì
sẽ xảy ra.  

- Kết quả trả về xuất ra một file ``hanoi_coffee.txt``.  

- Hãy sử dụng option ``indent`` cho function ``json.dump()``  

**Nếu cảm thấy khó, hãy tạo issue hoặc hỏi trực tiếp trên Skype, Slack.**

