# -*- coding: utf-8 -*-
"""
Created on Mon Sep 30 20:28:58 2019

@author: user1
"""

from kivy.app import App
#kivy.require("1.8.0")
from kivy.lang import Builder

presentation = Builder.load_file("main.kv")
#presentation = Builder.load_string("""
#<Button>:
#    font_size: 40
#	color: 0,1,0,1
#	size_hint: 0.3, 0.2 
#
#<FloatLayout>:
#    Button:
#	    text: "Kivy"
#		pos_hint: {"x": 0, 'top':1}
#	
#	Button:
#	    text: "Tutorials"
#		pos_hint: {"right": 1, 'top':1}
#
#                                    """)
class MainApp(App):
    
    def build(self):
        return presentation
		

if __name__ == "__main__":

    MainApp().run()