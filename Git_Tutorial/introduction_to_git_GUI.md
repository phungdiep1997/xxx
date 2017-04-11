## Hướng dẫn cơ bản về git trên Window

- Trong hướng dẫn lần này, mình sẽ hướng dẫn các bạn cách cài đặt và sử dụng Git trên Window. Bao gồm hướng dẫn trên giao diện đồ họa GUI và Terminal.

- Đầu tiên, truy cập https://git-scm.com/downloads tải về bản git dành cho Window.

- Sau khi tải về sẽ có 1 file .exe, bạn tiến hành cài đặt như bình thường.

  ![Imgur](http://i.imgur.com/xWYy3t7.png)

  ​

- Xong khi cài đặt xong, bạn click chuột phải trên màn hình. Để ý sẽ thấy có 2 phần tùy chọn `Git Gui Here` và `Git Bash Here`

  ![Imgur](http://i.imgur.com/vA8D0ET.png)

- Bạn chọn git GUI, 1 cửa sổ thông báo sẽ hiện ra

  ![Imgur](http://i.imgur.com/BoX2oF4.png)

  ​

- Click mục `Help --> Set up SSH_KEY`, tiếp tục chọn `Generate Key`, xuất hiện 1 đoạn public key như hình bên dưới, sau đó copy

![Imgur](http://i.imgur.com/OdlO72v.png)

- Truy cập vào Gitlab, phần `Settings --> SSH Keys` và paste đoạn key vừa copy vào đó

![Imgur](http://i.imgur.com/9Q4AF9H.png)

- Sau đó bạn trup cập theo đường dẫn: https://gitlab.com/pyfml/pyfml để tiến hành clone hay kéo thư mục trên gitlab của lớp về máy. Để ý sẽ có 2 tuỳ chọn

![Imgur](http://i.imgur.com/R57XgaJ.png)

- Bạn có thể chọn 1 trong 2, nếu dùng HTTPS thì mỗi lần liên kết tới gitlab đều sẽ phải cung cập username và password. Ở đây, mình sẽ dùng HTTPs và tiến hành clone về máy (bạn chuột phải trên thư mục làm việc bạn muốn clone project về máy và chọn `Git Bash Here` )

![Imgur](http://i.imgur.com/aTwjMPu.png)

- Sau khi clone về máy, bạn có thể thao tác thực hành với git như trong hướng dẫn cơ bản về git của mình. Ví dụ ở đây mình tạo mới 1 thư mục trên máy và thực hiện 1 số thao tác cơ bản

  ![Imgur](http://i.imgur.com/tdsGDEd.png)

  ​

và kiểm tra, tạo và chuyển nhánh trên giao diện dòng lệnh

![Imgur](http://i.imgur.com/LFtFvFh.png)



__Phụ lục__: hướng dẫn cơ bản về git cho người mới bắt đầu -  https://gist.github.com/huyhoang17/d16139101db1cc7a53a2c646a16997b2