# -*- coding: utf-8 -*-
"""
Created on Mon Sep 30 12:15:28 2019

@author: user1
"""

from kivy.app import App
#kivy.require("1.8.0")
from kivy.uix.floatlayout import FloatLayout

class SimpleKivy4(App):
    def build(self):
        return FloatLayout()

if __name__ == "__main__":
    SimpleKivy4().run()