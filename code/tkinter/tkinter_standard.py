# -----------------------------
# tkinter 基礎
# https://youtu.be/F-QjKc4aEIw
# -----------------------------
import tkinter as tk

from pathlib import Path # デフォルトで開かれているディレクトリをカレントにする
from tkinter import filedialog # 書き込む先を選択するダイアログを出力
import openpyxl #excelファイルを扱う

# Tkinterのwidget
# フレームを作成

# フレームを継承したクラス
class Application(tk.Frame):
    # 基底クラス(Frame)のイニシャライザを呼ぶ
    def __init__(self, root=None): # rootを渡す
        # 処理
        super().__init__(root,width=380, height=280,
                         borderwidth=1, relief='groove') #横，縦の長さ，境界線の太さと種類
        self.pack() # 位置を設定して配置
        self.pack_propagate(0) # サイズ調整
        self.root = root
        self.create_widgets()

    # 機能実装（アプリケーションの部品，ウィジェット）
    def create_widgets(self):
        # 閉じるボタン
        quit_btn = tk.Button(self) # ボタンクラスを利用
        quit_btn['text'] = '閉じる' # ボタンに表示させる文字
        quit_btn['command'] = self.root.destroy # ボタンを押した時に実行される処理
        quit_btn.pack(side='bottom')

        # テキストボックス
        # 入力された値をクラスのインスタンス変数として持っておきたいのでselfをつける
        # 他のメソッドやクラスの外で利用されない場合はつけなくてよい
        self.text_box = tk.Entry(self) # エントリークラスを利用
        self.text_box['width'] = 10
        self.text_box.pack()

        # 実行ボタン
        submit_btn = tk.Button(self)
        submit_btn['text'] = '実行'
        # submit_btn['command'] = self.input_handler #作成した関数
        submit_btn['command'] = self.save_data #Excelファイルはpyファイルと同じ階層に置く
        submit_btn.pack()

        # 受けとった文字列を表示
        # メッセージ出力
        self.message = tk.Message(self)
        self.message.pack()

    # テキストに入力された値を読み取る
    def input_handler(self):
        text = self.text_box.get() # get()で取得できる
        self.message['text'] = f'{text}!!!' #取得した文字列を表示

    # excelに保存する
    def save_data(self):
        text = self.text_box.get()
        # ファイルを選択するためのダイアログ，引数に現在のパス
        file_path = filedialog.askopenfilename(initialdir=Path.cwd) # file_pathの戻り値は選択したexcelファイルのパス

        wb = openpyxl.load_workbook(file_path)
        ws = wb.worksheets[0] # 一枚目のシートを指定
        ws['B1'].value = text # セルにデータを設定
        wb.save(file_path)# bookの保存
        self.message['text'] = '保存完了'

# トップレベルのウィンドウの作成
root = tk.Tk() # ウィンドウを作成
root.title('app') # タイトルの指定
root.geometry('400x300') #サイズの指定
#root.mainloop() #アプリの起動
app = Application(root=root)
app.mainloop()

# ---------------------------------------------------------------------------------------

# Sample
# https://colab.research.google.com/drive/1_ifu9PP-2jSDEcac3xvdP9w19kW9ZtDw?usp=sharing#scrollTo=oXkq2x4iqTF2
# https://colab.research.google.com/drive/1ZLIC8IrkTm-qdG25qHgRxMKRA56OHx-X?usp=sharing
# https://colab.research.google.com/drive/18W3-SM4rnZSqinjNcdoMZ2Cu3nMnh49I?usp=sharing
# https://colab.research.google.com/drive/1B2HMhQ_mwC7E1BmIkqoGP9Lu5Fg3i5jY?usp=sharing

# tkinterのウィジェット
# Button
# Radiobutton
# Checkbutton
# Listbox
# Entry
# Message
# Text
# Spinbox