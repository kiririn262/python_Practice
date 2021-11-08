# -----------------------------
# tkinter ウィジェット10選
# https://youtu.be/5xbVQyWm1XM
#
# Button
# Radiobutton
# Checkbutton
# Listbox
# Entry
# Message
# Text
# Spinbox
# -----------------------------
import tkinter as tk

class Application(tk.Frame):
    def __init__(self, root=None): # rootを渡す
        super().__init__(root,width=960, height=600,
                         borderwidth=1, relief='groove') #横，縦の長さ，境界線の太さと種類
        self.root = root
        self.pack() # 位置を設定して配置
        self.pack_propagate(0) # サイズ調整
        self.create_widgets()

    # 機能実装（アプリケーションの部品，ウィジェット）
    def create_widgets(self):
        # ボタン
        button = tk.Button(self, text='実行', command=self.submit)
        button.pack()

        # テキストボックス(一行)
        self.text_box = tk.Entry(self, width=30)
        # テキストボックス(複数行)
        self.text = tk.Text(self, width=20, height=10) #(横文字数x縦文字数)
        self.text.pack()

        # メッセージ(文章を表示させる)
        message = tk.Message(self, text='レジギガガガガゴゴゴゴゴゴゴゴ', width=200) # 幅指定(ピクセル)
        message.pack()

        # ラベル(ラベルや見出し)
        label = tk.Label(self, text='ラベル1')
        label.pack()

        # チェックボタン
        # チェックされているかを判定するオブジェクト
        self.is_student = tk.BooleanVar()
        chk_btn = tk.Checkbutton(self, text='学生', variable=self.is_student)
        chk_btn.pack()

        #ラジオボタン
        self.selected_radio = tk.StringVar()
        radio_1 = tk.Radiobutton(self, text='A型', value='A',variable=self.selected_radio)
        radio_2 = tk.Radiobutton(self, text='B型', value='B',variable=self.selected_radio)
        radio_3 = tk.Radiobutton(self, text='O型', value='O',variable=self.selected_radio)
        radio_4 = tk.Radiobutton(self, text='AB型', value='AB',variable=self.selected_radio)
        radio_1.pack()
        radio_2.pack()
        radio_3.pack()
        radio_4.pack()

        # リストボックス
        self.items = ['京都府','大阪府','奈良県','兵庫県','和歌山','滋賀県'] # リストを作成
        list_items = tk.StringVar(value=self.items) #選択肢用のオブジェクト，リストを参照
        self.list_box = tk.Listbox(self, listvariable=list_items)
        self.list_box.pack()

        # スピンボックス
        items = ['A型','B型','O型','AB型']
        self.sp = tk.Spinbox(self, state='readonly',values=items) # readonlyでないと選択肢が変更できてしまう
        self.sp.pack()

        # メニュー
        menu = tk.Menu(self.root) # rootはTk()オブジェクト
        menu1 = tk.Menu(menu, tearoff=False) # 一つの項目を作成，メニューをアプリから切り離す設定をオフ
        menu1.add_command(label='画面設定', command=self.screen_setting)
        menu1.add_command(label='音量設定', command=self.volume_setting)
        menu.add_cascade(label='設定', menu=menu1) #メニューの中にメニュー配置
        self.root.config(menu=menu) #画面にメニューを配置

    def volume_setting(self):
        print('音量設定が押されました')

    def screen_setting(self):
        print('画面設定が押されました')

    def submit(self):
        print('ボタンが押されました')
        #一行読み取る
        text = self.text_box.get()
        print(f'入力された値：{text}')

        # 複数行
        t = self.text.get(1.0, tk.END + '-1c') #1.0:始めから，tk.END：終わりまで（改行コード含む），-1C：改行を除く
        print(t)

        # チェックボタンの判定を出力
        print(self.is_student.get()) # True/False

        # ラジオボタンの選択
        print(self.selected_radio.get())

        # リストボックスの出力
        selected_index = self.list_box.curselection()[0] # 一つ目の値をセレクトされた値として持つ，戻り値はタプル，選択したアイテムが何番目なのか(リストの要素)を表す値
        print(self.items[selected_index])

        # スピンボックスの出力
        print(self.sp.get())

root = tk.Tk() # ウィンドウを作成
root.title('app') # タイトルの指定
root.geometry('1080x720') #サイズの指定
app = Application(root=root)
app.mainloop()