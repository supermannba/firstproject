#!/usr/bin env python 3.4

import os
import time
from ctypes import cdll

lib=cdll.LoadLibrary('./libfoo.so')

class Foo(object):
  def __init__(self):
    self.obj=lib.Foo_new()
    
  def bar(self):
    lib.Foo_bar(self.obj)
    
    
if __main__=="__main__":
  f=Foo()
  f.bar()
