# coding:utf-8

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button

class MainScreen(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        btn = Button(text="hello")
        self.add_widget(btn)

        btn2 = Button(text="everyone")
        self.add_widget(btn2)

        # MainScreenに追加する、BoxLayoutというWidgetを用意
        bl = BoxLayout()
        bl.orientation = "vertical"

        # blに追加する３つのボタンを用意
        btn3 = Button(text="how")
        btn4 = Button(text="are")
        btn5 = Button(text="you")

        # blにボタンを追加
        bl.add_widget(btn3)
        bl.add_widget(btn4)
        bl.add_widget(btn5)

        # MainScreenにblを追加
        self.add_widget(bl)

        btn6 = Button(text="today?")
        self.add_widget(btn6)

class MainApp(App):
    def on_start(self):
        print("App Start!!")

    def build(self):
        MS = MainScreen()
        return MS

    def on_stop(self):
        print("App End!!")

if __name__=="__main__":
    MainApp().run()