# -*- coding: utf-8 -*-
"""
Created on Sun Sep 29 14:42:54 2019

@author: user1
"""

from kivy.app import App
from kivy.uix.scatter import Scatter
from kivy.uix.label import Label
 
class TutorialApp(App):
    def build(self):
        s = Scatter()
        l = Label(text='iPaoMi', font_size=150)
        s.add_widget(l)
        return s
 
if __name__ == "__main__":
    TutorialApp().run()