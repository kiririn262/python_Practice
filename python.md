# Pythonのチートシート

## 基本

### 変数

``` python
# 入力を整数として代入
n = int(input())

# 入力を半角スペース区切りで代入
s,t,r = input().split() # 1 2 3 ⇒ s = '1',t = '2',r = '3'

# 変数に型指定して一気に代入（map関数）
n,m,k = map(int,input().split())

# インクリメント
# x++は使えない
n += 1
```

### リスト

```python
a = [1, 2, 4]
a = list(1,2,4)
a = ["Hello", 1, "world", 2, "!"]

# スライス
# indexで[開始位置 : 終了位置]
b = a[1:3] # ⇒[2, 4]
c = a[2:-1] # ⇒[4]
d = a[1:] # ⇒[2, 4]
e = a[:1] # ⇒[1]

# リストの最後の要素を取り出す
list_a = a[-1:]
# 最初の要素を除いたリスト
list_b = a[1:]

# 要素の追加
a = [1,2,4]
a.append(7) # ⇒[1,2,4,7]
a = a + [7]

# 要素の挿入
a = [1,2,4]
a.insert(2,7) # ⇒[1,2,7,4]

# 要素の削除
a = [1,2,4,7]
del a[2] # ⇒[1,2,7]
a.remove(7) # ⇒[1,2,4] リスト内に存在しない値の場合エラー,複数存在する場合は最初の要素のみ削除

# 値を取得し，要素の削除
a = [1,2,4]
b = a.pop(0) # a = [2,4], b = 1
# a.pop()は末尾

リストの結合
a = [1, 2, 4]
b = [5, 7]
a.extend(b) # [1,2,4,5,7]
# a = a + b
a.append(b) # [1,2,4,[5,7]]

# リスト内包表記
a = [i**2 for i in range(10)] # ⇒[0,1,4,9,16,25,36,49,64,81]

# リスト初期化
a.clear()

# リスト内の検索 戻り値はTrue/False
a = [1,2,4]
if 4 in a:
    print(4)
if 7 not in a:
    print(none 7)

# リストの要素のインデックス
a = [1,2,4]
b = a.index(4) # ⇒2

# リストの長さ
a = [1,2,4]
b = a.count() # ⇒3
length = len(a)

# 文字列型の変数を作成
a = ["1","2","3","4","Hello","World"] # 全ての要素が文字列型でないとエラー
str1 = ''.join(a) # ⇒1234HelloWorld
str2 = ' '.join(a) # ⇒1 2 3 4 Hello World

一文字ずつ格納
list("日月火水木金土") # ⇒ "日,月,火,水,木,金,土"

# 標準入力からリストに格納
p = []
p = list(map(float,input().split()))
```

f構文を使ったprint文

``` python
print(f'Best in {s[0]} {s[1]}')

a = 123
b = 'abc'
print('{} and {}'.format(a, b))
print('{first} and {second}'.format(first=a, second=b))
print(f'{a} and {b}')
print(F'{a} and {b}')
print(f"{a} and {b}")
print(f'''{a} and {b}''')
print(f"""{a} and {b}""")
```

bool型

``` python
print(bool(1)) # ⇒True
print(bool(0)) # ⇒False
print(bool("文字列があります")) # ⇒True
print(bool("")) # ⇒False

def baisu(num):
    if num % 3 == 0:
        return True
if baisu(15):
    print('3の倍数です')
```



### 標準エラー出力
``` python
import sys
print("error", file=sys.stderr)

# 関数化
import sys
def error(*args, end="\n"):
    print(*args, end=end, file=sys.stderr)
```

## List

### 配列の要素指定

``` py
A = [5, 1, -8, 3]

A_0 = A[0] # 5
A_end = A[-1] # 3
```

### 分岐

switch文はない
if文などで実装する

or

```py
(age <= 10) or (80 <= age)
```

```py
x or y
x and y
not x

x = 20
if not x < 20:
    return True
```

### 標準入力

``` py
A = []
A = list(map(int, input().split()))
```

### ソート

``` python
# リストの要素並び替え
a = [1,2,4]
a.sort() # 昇順
a.sort(reverse=True) # 降順
a.reverse() # 逆順

A = [6,4,10,-3]

# 昇順
A_sort = sorted(A) # [-3,4,6,10]

# 降順
A_sort = sorted(A, reverse=True) # [10,6,4,-3]
```

注意点
Pythonでは数値や文字列は代入した瞬間に別物になるのですが、リストは代入しても「参照」のコピーが作られるだけで、完全に別物にはならない

```python
a = [1,2,4]
b = a # リストの代入は参照のコピー
b[0] = 10 # ⇒a = b = [10, 2, 4]
```

```python
prices = {
    'mackerel': 200,
    'salmon': 300,
    'yellowtail': 300,
    'shrimp': 300,
    'conger': 400,
    'tuna': 400,
    'eel': 500,
    'salmon_roe': 500,
}
# print(prices)

prices['salmon'] # => 300

prices['sea_urchin'] = 600
# prices => 追加される

list(prices.keys()) # 名前の一覧表示

for k, v in prices.items():
    # print('{0}: {1}'.format(k, v))
    print(f'{k}: {v}')

# 参考

- [競プロでのデバッグを標準エラー出力で行っているという話](https://qiita.com/amaguri0408/items/61d65c3bea3a5815d704)
- [Pythonの可変長引数（*args, **kwargs）の使い方 | note.nkmk.me](https://note.nkmk.me/python-args-kwargs-usage/)
- [Pythonのbool型について現役エンジニアが解説【初心者向け】](https://techacademy.jp/magazine/35075)
リスト
- [Pythonのリスト（list）の基本的な操作方法やメソッドの一覧をまるっと解説！](https://camp.trainocate.co.jp/magazine/python-list/)
- [【Python入門】listの使い方とメソッドまとめ](https://www.sejuku.net/blog/23633)
- [Python配列の基礎はこれで完璧！初心者必見のメソッドを多数紹介](https://udemy.benesse.co.jp/development/python-work/python-list.html)
- [文字列を１文字ずつのリストにする](https://qiita.com/cress_cc/items/5600be0416a0be72ecfb)
- [Pythonのf文字列（フォーマット済み文字列リテラル）の使い方](https://note.nkmk.me/python-f-strings/)
- [論理演算子の使い方](https://www.javadrive.jp/python/if/index6.html)