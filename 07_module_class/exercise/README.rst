Exercises
=========

Notice:

- All exercise must done in separate module, which must use check
``if __name__ == ...`` in the end of file.

- All of files must be executable.

7.1
---

Simulate a person go to market to build food. There are:

- Buyer (money, bag)
- Seller (money, goods)
- Goods (name, size, price)
- Bag of buyer. (size)

Seller has two apples(10k/each), three bottle of milks
(40k/bottle), 3 Kg of beef (100k/kg).

Let buyer buys each at least one.

Use class to represent that.

7.2
---

Simulate Pig game https://en.wikipedia.org/wiki/Pig_%28dice_game%29

- With 1 player, he will play 100 games, calculate winning rate.

- With 2 players, they will play 100 games, calculate winning rate of each.

7.3
---

Implement function that returns Nth Fibonacci number in recursive way.

7.4
---

Implement Tower of Hanoi https://en.wikipedia.org/wiki/Tower_of_Hanoi



7.5
---

Download file names.txt_ - một file text 46K chứa danh sách hơn 5000 username.
Hãy viết chương trình sắp xếp những username này theo thứ tự bảng chữ cái. Sau
đó, tính điểm cho mỗi username. Điểm số của mỗi chữ cái tương đương với thứ tự
của nó trong bảng chữ cái.

Điểm được tính như sau:
Ví dụ, sau khi danh sách các username được sắp xếp theo thứ tự bảng chữ cái,
"COLIN" sẽ xếp thứ 938 trong danh sách đó, vì vậy nó sẽ có giá trị:

  (3 + 15 + 12 + 9 + 14) * 938 = 49714

Tính tổng điểm số của tất cả các username trong file đã cho.

Link:  https://projecteuler.net/problem=22

name.txt_: https://projecteuler.net/project/resources/p022_names.txt

7.6
---

Viết chương trình thực hiện sự chuyển đổi sau:

  input: a
  output: a

  input: abbbccccdddd
  output: abb3cc4dd4

  input: xxyyyxyyx
  output: xx2yy3xyy2x

Giải thích: Những chữ cái không lặp lại thì oputut giữ nguyên chữ cái đó. Những
chữ cái liên tiếp sẽ in ra 2 lần + số lần lặp lại liên tiếp.