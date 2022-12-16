import win32gui
import win32ui
from ctypes import windll
from PIL import Image
import win32con
import numpy as np
import cv2

def capture_inactive_window(hwnd):

    # hwnd = win32gui.FindWindow(None, 'WeChat')

    # Change the line below depending on whether you want the whole window
    # or just the client area.
    left, top, right, bot = win32gui.GetWindowRect(hwnd)
    w = right-left
    h = bot-top

    hwndDC = win32gui.GetWindowDC(hwnd)
    mfcDC  = win32ui.CreateDCFromHandle(hwndDC)
    saveDC = mfcDC.CreateCompatibleDC()

    saveBitMap = win32ui.CreateBitmap(w,h)
    saveBitMap.CreateCompatibleBitmap(mfcDC, w, h)

    saveDC.SelectObject(saveBitMap)
    saveDC.BitBlt((0, 0), (w, h), mfcDC, (0,0), win32con.SRCCOPY)


    # Change the line below depending on whether you want the whole window
    # or just the client area.
    #result = windll.user32.PrintWindow(hwnd, saveDC.GetSafeHdc(), 1)
    # result = windll.user32.PrintWindow(hwnd, saveDC.GetSafeHdc(), 0)

    # print (result)
    signedIntsArray = saveBitMap.GetBitmapBits(True)
    img = np.fromstring(signedIntsArray, dtype='uint8')
    img.shape = (h, w, 4)
    cv2.cvtColor(img, cv2.COLOR_BGRA2BGR)

    # bmpinfo = saveBitMap.GetInfo()
    # bmpstr = saveBitMap.GetBitmapBits(True)
    #
    # im = Image.frombuffer(
    #     'RGB',
    #     (bmpinfo['bmWidth'],bmpinfo['bmHeight']),
    #     bmpstr, 'raw', 'BGRX',0,1)

    win32gui.DeleteObject(saveBitMap.GetHandle())
    saveDC.DeleteDC()
    mfcDC.DeleteDC()
    win32gui.ReleaseDC(hwnd, hwndDC)
    img = cv2.cvtColor(img,cv2.COLOR_BGRA2BGR)
    return img