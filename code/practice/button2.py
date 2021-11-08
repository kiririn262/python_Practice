# coding:utf-8

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button

from kivy.lang.builder import Builder

Builder.load_string('''
<MainScreen>:
    Button:
        text: "hello"
    Button:
        text: "everyone"
    BoxLayout:
        orientation: "vertical"
        Button:
            text: "how"
        Button:
            text: "are"
        Button:
            text: "you"
    Button:
        text: "today?"

<SubScreen>:
    orientation: "vertical"
    Button:
        text: "how"
    Button:
        text: "are"
    Button:
        text: "you"
    Button:
        text: "today?"
''')

class MainScreen(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

class SubScreen(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

class MainApp(App):
    def build(self):
        hoge = True
        # hoge = False

        if hoge:
            return MainScreen()
        else:
            return SubScreen()

if __name__=="__main__":
    MainApp().run()