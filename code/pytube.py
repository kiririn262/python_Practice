# -*- coding: utf-8 -*-

import sys, os
import pytube
from pytube import YouTube
import tkinter
from tkinter import *

#エラーメッセージ
__ERROR_MESSAGE__ = None

#Youtubeの動画をダウンロードする
def get_youtube(y_url,download_location,audio_only_flg):
    #一旦エラーメッセージをクリア
    __ERROR_MESSAGE__ = None

    #URLの入力に関する例外処理
    if type(y_url) != str or y_url == "":
        __ERROR_MESSAGE__ = "URLには文字列を入れてください"

    #「http://」が省略されて入れば付け加える
    if not (y_url.startswith("http://") or y_url.startswith("https://")):
        y_url = "http://" + y_url

    #ダウンロード先フォルダが省略されて入れば、カレントディレクトリに設定
    if download_location == "" or download_location is None:
        download_location = "./"

    #エラーメッセージが出ていなければ動画を取得する
    if __ERROR_MESSAGE__ is None:
        youtube = YouTube(y_url)
        #動画をダウンロードするとき
        if audio_only_flg == False:
            youtube.streams.filter(subtype='mp4').first().download(download_location)
        #音声をダウンロードするとき
        else:
            youtube.streams.filter(only_audio=True,subtype='mp4').first().download(download_location)

#画面の表示
def main():
    root = Tk()
    #タイトル
    root.title('Youtube Downloader')
    root.minsize(600, 400)

    #urlボックスのラベル
    label1 = Label(text="YoutubeのURL")
    label1.pack(pady=10)

    #urlボックス
    y_url_box = Entry(width=50)
    y_url_box.pack()

    #ロケーションボックスのラベル
    label2 = Label(text="ダウンロード先のフォルダ（省略可）")
    label2.pack(pady=10)

    #ロケーションボックス
    download_location_box = Entry(width=50)
    download_location_box.pack()

    #オーディオボタン
    chk_state = BooleanVar()
    chk_state.set(False) 
    chk = Checkbutton(text='音声のみ', var=chk_state)
    chk.pack(pady=10)

    #ダウンロードボタン
    InputButton = Button(text="ダウンロード",command = lambda : get_youtube(y_url_box.get(),download_location_box.get(),chk_state.get()))
    InputButton.pack(pady=20)

    #エラーメッセージ表示欄
    label2 = Label(text=__ERROR_MESSAGE__)
    label2.pack(pady=30)

    root.mainloop()

if __name__ == "__main__":
    main()