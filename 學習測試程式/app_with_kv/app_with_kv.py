# -*- coding: utf-8 -*-
"""
Created on Sun Sep 29 21:01:19 2019

@author: user1
"""

'''
Application built from a  .kv file
==================================

This shows how to implicitly use a .kv file for your application. You
should see a full screen button labelled "Hello from test.kv".

After Kivy instantiates a subclass of App, it implicitly searches for a .kv
file. The file test.kv is selected because the name of the subclass of App is
TestApp, which implies that kivy should try to load "test.kv". That file
contains a root Widget.
'''

import kivy
kivy.require('1.0.7')

from kivy.app import App


class TestApp(App):
    pass


if __name__ == '__main__':
    TestApp().run()

