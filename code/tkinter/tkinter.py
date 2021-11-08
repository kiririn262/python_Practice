#!/envs/python38
# -*- coding: utf8 -*-
import sys
import tkinter
# import tkMessageBox

root = tkinter.Tk()
root.title(u"Software Title")
root.geometry("400x300")

#
# ボタンが押されるとここが呼び出される
#
def DeleteEntryValue(event):
  #エントリーの中身を削除
  EditBox.delete(0, tkinter.END)


#ラベル
Static1 = tkinter.Label(text=u'test', foreground='#ff0000', background='#ffaacc')
Static1.pack()
# Static1.place(x=150, y=228)

#エントリー
EditBox = tkinter.Entry(width=50)
EditBox.insert(tkinter.END,"入力してください")
EditBox.pack()

#ここで，valueにEntryの中身が入る
value = EditBox.get()

#ボタン
Button = tkinter.Button(text=u'ボタン', width=30)
Button.bind("<Button-1>",DeleteEntryValue) 
#左クリック（<Button-1>）されると，DeleteEntryValue関数を呼び出すようにバインド
# Button.pack()
Button.place(x=105, y=60)

#
# チェックボックスのチェック状況を取得する
#
def check(event):
  global Val1
  global Val2
  global Val3

  text = ""

  if Val1.get() == True:
    text += "項目1はチェックされています\n"
  else:
    text += "項目1はチェックされていません\n"

  if Val2.get() == True:
    text += "項目2はチェックされています\n"
  else:
    text += "項目2はチェックされていません\n"

  if Val3.get() == True:
    text += "項目3はチェックされています\n"
  else:
    text += "項目3はチェックされていません\n"

#   tkMessageBox.showinfo('info',text)

#
# チェックボックスの各項目の初期値
#
Val1 = tkinter.BooleanVar()
Val2 = tkinter.BooleanVar()
Val3 = tkinter.BooleanVar()

Val1.set(False)
Val2.set(True)
Val3.set(False)


#チェックボタン
CheckBox1 = tkinter.Checkbutton(text=u"項目1", variable=Val1)
CheckBox1.pack()

CheckBox2 = tkinter.Checkbutton(text=u"項目2", variable=Val2)
CheckBox2.pack()

CheckBox3 = tkinter.Checkbutton(text=u"項目3", variable=Val3)
CheckBox3.pack()

button1 = tkinter.Button(root, text=u'チェックの取得',width=30)
button1.bind("<Button-1>",check)
button1.pack()

root.mainloop()