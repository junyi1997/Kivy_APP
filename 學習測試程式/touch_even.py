# -*- coding: utf-8 -*-
"""
Created on Mon Sep 30 15:49:44 2019

@author: user1
"""

from kivy.app import App
from kivy.uix.widget import Widget

class TouchInput(Widget):

    def on_touch_down(self, touch):
        print(touch)
    def on_touch_move(self, touch):
        print(touch)
    def on_touch_up(self, touch):
        print("RELEASED!",touch)

class SimpleKivy4(App):

    def build(self):
        return TouchInput()

if __name__ == "__main__":
    SimpleKivy4().run()