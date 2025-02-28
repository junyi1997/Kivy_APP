# -*- coding: utf-8 -*-
"""
Created on Mon Sep 30 20:15:15 2019

@author: user1
"""

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.graphics import Line

class DrawInput(Widget):
    
    def on_touch_down(self, touch):
        print(touch)
        with self.canvas:
            touch.ud["line"] = Line(points=(touch.x, touch.y))
        
    def on_touch_move(self, touch):
        print(touch)
        touch.ud["line"].points += (touch.x, touch.y)
		
    def on_touch_up(self, touch):
        print("RELEASED!",touch)


class SimpleKivy4(App):
    
    def build(self):
        return DrawInput()

if __name__ == "__main__":
    SimpleKivy4().run()