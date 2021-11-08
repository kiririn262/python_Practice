# -*- coding: utf-8 -*-
import enum
from kivy.app import App
from kivy.config import Config
from kivy.properties import StringProperty
from kivy.uix.widget import Widget

Config.set('graphics', 'width', '200')
Config.set('graphics', 'height', '300')


class MethodType(enum.IntEnum):
    No = 0
    Plus = 1
    Minus = 2
    Times = 3
    Divide = 4
    Equal = 5

class CalculateWidget(Widget):
    text = StringProperty()

    def __init__(self, **kwargs):
        super(CalculateWidget, self).__init__(**kwargs)
        self.text = '0'
        self.cal1 = None
        self.method_type = MethodType.No.value
        self.is_refresh = False

    def press_number(self, instance):
        self.change_display(instance.text)

    def change_display(self, number):
        if self.text == '0':
            self.text = number
        elif self.is_refresh:
            self.text = number
            self.is_refresh = False
        else:
            self.text += number

    def clear_all(self):
        self.text = '0'
        self.cal1 = None
        self.method_type = 0

    def calculate(self):
        if self.method_type == MethodType.Plus.value:
            return float(self.cal1) + float(self.text)
        
        elif self.method_type == MethodType.Minus.value:
            return float(self.cal1) - float(self.text)
        
        elif self.method_type == MethodType.Times.value:
            return float(self.cal1) * float(self.text)
        
        elif self.method_type == MethodType.Divide.value:
            return float(self.cal1) / float(self.text)

    def call_method(self, method_type):
        if not self.cal1 and method_type != MethodType.Equal.value:
            self.cal1 = float(self.text)
            self.method_type = method_type
            self.text = '0'
       
        elif self.cal1 and self.method_type and method_type == MethodType.Equal.value:
            value = self.calculate()
            self.text = str(value)
            self.cal1 = None
            self.method_type = MethodType.No.value
        
        elif self.cal1 and self.method_type and method_type != MethodType.Equal.value:
            value = self.calculate()
            self.text = str(value)
            self.cal1 = value
            self.method_type = method_type
            self.is_refresh = True


class CalculatorApp(App):
    def __init__(self, **kwargs):
        super(CalculatorApp, self).__init__(**kwargs)
        self.title = 'calculator'


if __name__ == '__main__':
    CalculatorApp().run()