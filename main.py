from win32api import *
from win32gui import *
import win32con
import sys, os
import struct
import time

# Class
class WindowsBalloonTip:
    def __init__(self):
        message_map = { win32con.WM_DESTROY: self.OnDestroy,}

        # Register the window class.
        wc = WNDCLASS()
        self.hinst = wc.hInstance = GetModuleHandle(None)
        wc.lpszClassName = 'PythonTaskbar'
        wc.lpfnWndProc = message_map # could also specify a wndproc.
        self.classAtom = RegisterClass(wc)

                    

    def OnDestroy(self, hwnd, msg, wparam, lparam):
        nid = (self.hwnd, 0)
        Shell_NotifyIcon(NIM_DELETE, nid)
        PostQuitMessage(0)

    def balloon_tip(self,title, msg):
        style = win32con.WS_OVERLAPPED | win32con.WS_SYSMENU
        hwnd = CreateWindow(self.classAtom, "Taskbar",style, 0, 0, win32con.CW_USEDEFAULT, win32con.CW_USEDEFAULT, 0, 0, self.hinst, None)
        UpdateWindow(hwnd)

        hicon = LoadIcon(0, win32con.IDI_APPLICATION)

        flags =NIF_ICON | NIF_MESSAGE | NIF_TIP
        nid = (hwnd, 0, flags, win32con.WM_USER+20, hicon, 'Tooltip')
        Shell_NotifyIcon(NIM_ADD, nid)
        Shell_NotifyIcon(NIM_MODIFY, (hwnd, 0, NIF_INFO, win32con.WM_USER+20, hicon, 'Balloon Tooltip', msg, 200, title,NIIF_INFO))
        
        time.sleep(1)   

    
# Main
if __name__ == '__main__':
    # Example
    w=WindowsBalloonTip()
    w.balloon_tip('Example one', 'Python is awsm')
    w.balloon_tip('Example two', 'Once you start coding in Python you will hate other languages')
   