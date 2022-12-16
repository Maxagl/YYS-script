import win32ui
import win32gui
import win32con
import win32api
from time import sleep
import numpy as np
import cv2

def drag_inactive_window(hwnd,bbox):
    # user32 = ctypes.WinDLL('user32.dll')
    # user32.SwitchToThisWindow(hwnd, True)
    w = bbox[2] - bbox[0]
    h = bbox[3] - bbox[1]
    move_x = np.linspace(w-50, 20, num=40, endpoint=True)[0:]
    # move_y = np.linspace(int((bbox[3]-bbox[1])/2, int((bbox[3]-bbox[1])/2), num=10, endpoint=True)[0:]

    win32api.PostMessage(hwnd, win32con.WM_LBUTTONDOWN, 0, win32api. MAKELONG(w,int((bbox[3]-bbox[1])/6))) #int((bbox[3]-bbox[1])/6)
    # win32api.PostMessage(hwnd, win32con.WM_MOUSEMOVE, 0, win32api. MAKELONG(0,int((bbox[3]-bbox[1])/2)))
    sleep(0.1)
    for i in range(40):
        x = int(round(move_x[i]))
        y = int(round(int((bbox[3]-bbox[1])/6)))
        win32gui.SendMessage(
            hwnd, win32con.WM_MOUSEMOVE, 0, win32api.MAKELONG(x, y))
        sleep(0.01)
    win32api.PostMessage(hwnd, win32con.WM_LBUTTONUP, 0,win32api.MAKELONG(10,int((bbox[3]-bbox[1])/6)))

    # print(temp1)
    sleep(1)
def drag_Ncard(hwnd,bbox):
    w = bbox[2] - bbox[0]
    h = bbox[3] - bbox[1]
    # move_x = np.linspace(w*3//20, w*3//20, num=20, endpoint=True)[0:]
    move_y = np.linspace(h*3//4, h//2, num=20, endpoint=True)[0:]
    win32api.SendMessage(hwnd, win32con.WM_LBUTTONUP, 0, win32api. MAKELONG(w*4//20,h*3//4))
    sleep(0.2)
    win32api.SendMessage(hwnd, win32con.WM_LBUTTONDOWN, 0, win32api. MAKELONG(w*4//20 + 2,h*3//4 + 2))
    # win32api.PostMessage(hwnd, win32con.WM_MOUSEMOVE, 0, win32api. MAKELONG(10,int((bbox[3]-bbox[1])/2)))
    sleep(1)
    for i in range(20):
        x = int(round(w*4//20))
        y = int(round(move_y[i]))
        win32gui.SendMessage(
            hwnd, win32con.WM_MOUSEMOVE, 0, win32api.MAKELONG(x, y))
        sleep(0.01)
    win32api.PostMessage(hwnd, win32con.WM_LBUTTONUP, 0,win32api.MAKELONG(w*3//20,h//2))

def click_inactive_window(hwnd,pos):
    win32gui.SendMessage(
        hwnd, win32con.WM_MOUSEMOVE, 0, win32api.MAKELONG(int(pos[0]), int(pos[1])))
    sleep(0.1)
    win32gui.SendMessage(
        hwnd, win32con.WM_LBUTTONDOWN, 0, win32api.MAKELONG(int(pos[0]), int(pos[1])))
    sleep(0.1)
    win32gui.SendMessage(
        hwnd, win32con.WM_LBUTTONUP, 0, win32api.MAKELONG(int(pos[0]), int(pos[1])))
    sleep(0.1)
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
    try:
        saveBitMap.CreateCompatibleBitmap(mfcDC, w, h)
    except:
        print('出现Bitmap错误')
        return capture_inactive_window(hwnd)

    saveDC.SelectObject(saveBitMap)
    saveDC.BitBlt((0, 0), (w, h), mfcDC, (0,0), win32con.SRCCOPY)

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