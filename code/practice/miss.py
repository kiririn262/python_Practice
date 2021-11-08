# 1 if x == True:
    x = True
    if x == True:
        print('xが真の時')

    if x:
        print('xが真の時')

    # True/False
    # if 0: if 1:
    # if '': #空文字 if'abc'
    # if []: #空のリスト if [11, 22]:

# 2 f文字列を使っていない
    x = 200
    text = 'これは' + str(x) + '円です'
    text = 'これは{}円です'.format(x)

    # python3.6以降で使える
    text = f'これは{x}円です'

    # name + '様'などはよい
    # 「数値を文字列に埋め込む」「文字列の間に変数を埋め込む」「複数の変数を埋め込む」などはf文字列を使うべき

# 3 自作インクリメント変数
    x_list = [10, 30, 50]
    y_list = [20, 90, 40]

    i = 0 #初期化
    for x in x_list:
        y = y_list[i] #要素取り出す
        print(x + y)
        i += 1

    #zip関数を使う
    for x, y in zip(x_list, y_list):
        print(x + y)

    i = 0
    for x in x_list:
        print(f'{i}番目のデータ： {x}')
        i += 1

    for x,i in enumerate(x_list):
        print(f'{i}番目のデータ： {x}')

# 4 リスト一括処理をforで
    numbers = [10, 21, 86]
    #頭に「No.」をつけて新しいリストを作成

    new_list = []
    for n in numbers:
        new_list.append(f'No.{n}')

    # map関数，filter関数などの高階関数，リスト内包表記を使う
    new_list = [f'No. {n}' for n in numbers]

# 5 import *

    #全部をインポート
    from xxx import *

    from xxx import *
    from yyy import *
    from zzz import *

    con = connect_db()
    # どこからインポートされたかわからない
    # 何が実行されているのかわからない，バグが発生しやすい

# 6 例外を握りつぶしている
    try:
        with open('aaa.txt') as f:
            s = f.read()
    except FileNotFoundError:
        #エラー時の処理が書かれていない
        pass

    try:
        with open('aaa.txt') as f:
            s = f.read()
    except FileNotFoundError:
        #ログの出力
        logger.error('aaa.txtが存在しません')
        #例外の送出
        raise FileNotFoundError('aaa.txtが存在しません')