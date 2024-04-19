import kivy
from kivy.app import App
# from kivy.core import text
from kivy.uix.boxlayout import BoxLayout
import random

kivy.require('2.3.0')

class MySys(BoxLayout):
  def __init__(self):
    super(MySys, self).__init__()
  def Generate_number(self):
    self.random_label.text = str(random.randint(0, 1000))

class MyApp(App):
  def build(self):
    return MySys()
myApp = MyApp()
myApp.run()