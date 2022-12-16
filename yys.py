import time
import pyautogui
import action
import win32gui
import win32api
import win32con
from Function import Daily
import threading
import cv2
import CtrInacWindow
from time import sleep
# 读取文件 精度控制   显示名字
toplist, winlist = [], []
imgs = action.load_imgs()
pyautogui.PAUSE = 0.1
start_time = time.time()
print('此脚本受益于 Github YYS-master。但好像这个项目不见了\n')
print('脚本仅用作学习和个人娱乐。联系邮箱:zhaobangliuagl@gmail.com\n')
print('程序启动,现在时间', time.ctime())
def enum_cb(hwnd, results):
    winlist.append((hwnd, win32gui.GetWindowText(hwnd)))

def callback(hwnd, hwnds):
    if win32gui.IsWindowVisible(hwnd) and win32gui.IsWindowEnabled(hwnd):
        hwnds[win32gui.GetWindowText(hwnd)] = hwnd
    return True

def choose_menu(raw, agent):
    agent = int(agent)
    if raw.isdigit():
        index = int(raw)
    else:
        index = raw
    if  index == 1:
        if agent == 1:
            daily1.solo()
        elif agent == 2:
            daily2.solo()
        elif agent == 3:
            daily3.solo()
    elif index == 2:
        if agent == 1:
            daily1.solo_jinbi()
        elif agent == 2:
            daily2.solo_jinbi()
        elif agent == 3:
            daily3.solo_jinbi()
    elif index == 3:
        daily1.huntu_driver()
    elif index == 4:
        daily1.huntu_fighter()
    elif index == 5:
        t2 = threading.Thread(target=daily2.huntu_driver, args=())
        t1 = threading.Thread(target=daily1.huntu_fighter, args=())
        
        t2.start()
        t1.start()
        
        t2.join()
        t1.join()
        
    elif index == 6:
        t1 = threading.Thread(target=daily1.jinbi_fighter, args=())
        t2 = threading.Thread(target=daily2.jinbi_driver, args=())
        t1.start()
        t2.start()

        t1.join()
        t2.join()
    elif index == 7:
        t1 = threading.Thread(target=daily1.huntu_fighter, args=())
        t2 = threading.Thread(target=daily2.huntu_fighter, args=())
        t3 = threading.Thread(target=daily3.huntu_driver, args=())
        t1.start()
        t2.start()
        t3.start()

        t1.join()
        t2.join()
        t3.join()
    elif index == 8:
        if agent == 1:
            daily1.yuling()
        elif agent == 2:
            daily2.yuling()
        elif agent == 3:
            daily3.yuling()     
    elif index == 9:
        if agent == 1:
            daily1.juexing()
        elif agent == 2:
            daily2.juexing()
        elif agent == 3:
            daily3.juexing()  

    elif index == 0:
        print('''
注意事项:
    1：确保管理员运行此脚本。右键此脚本，选择以管理员运行
    2：确保电脑的缩放为百分百。win11可以右键显示设置里面查看
    3：确保游戏窗口分辨率为游戏打开时的分辨率
脚本内容:
    1:单刷探索,需要先进入探索页面(有小怪的那)同时保证狗粮队长在队伍的最左侧
    2:觉醒,御灵需要锁定整容,同时从组队界面开始
    3:单开的魂土需要保证初始进入了组队界面
    4:双开需要使用sandbox,链接:https://sandboxie-plus.com/downloads/ 。同时确保sanbox为司机,本体为打手,同样从组队界面开始
    5:活动暂时没更新
                ''')
        choose_menu(input("选择功能模式:"))
    elif index == "F1":
        exit()
    elif index == "F2":
        os.execl(sys.executable, os.path.abspath(__file__), *sys.argv) 
   

        

if __name__ == '__main__':
    win32gui.EnumWindows(enum_cb, toplist)

    yys_1 = [(hwnd1, title) for hwnd1, title in winlist if '阴阳师-网易游戏' in title] #[#] 阴阳师-网易游戏 [#]
    #yys_1 = yys_1[0]
    #hwnd1 = yys_1[0]
    # 多开
    #yys_2 = [(hwnd2, title) for hwnd2, title in winlist if '阴阳师-网易游戏' in title]
    #yys_3 = [(hwnd3, title) for hwnd3, title in winlist if '[#] 阴阳师-网易游戏 [#]' in title]
    if not yys_1 == []:
        sandbox = yys_1[0]
        hwnd1 = sandbox[0]
        bbox1 = win32gui.GetClientRect(hwnd1)
        bbox1_1 = win32gui.GetWindowRect(hwnd1)
        W1 = bbox1_1[2] - bbox1_1[0]
        H1 = bbox1_1[3] - bbox1_1[1]
        L_Boarder1 = (W1 - bbox1[2]) // 2
        U_Boarder1 = H1 - bbox1[3] - L_Boarder1
        daily1 = Daily(hwnd1, bbox1, imgs, L_Boarder1, U_Boarder1)
    if len(yys_1) >=2:
        client = yys_1[1]
        hwnd2 = client[0]
        bbox2 = win32gui.GetClientRect(hwnd2)
        bbox2_1 = win32gui.GetWindowRect(hwnd2)
        W2 = bbox2_1[2] - bbox2_1[0]
        H2 = bbox2_1[3] - bbox2_1[1]
        L_Boarder2 = (W2 - bbox2[2]) // 2
        U_Boarder2 = H2 - bbox2[3] - L_Boarder2
        daily2 = Daily(hwnd2, bbox2, imgs, L_Boarder2, U_Boarder2)
    
    if len(yys_1) >= 3:
        second = yys_1[2]
        hwnd3 = second[0]
        bbox3 = win32gui.GetClientRect(hwnd3)
        bbox3_1 = win32gui.GetWindowRect(hwnd3)
        W3 = bbox3_1[2] - bbox3_1[0]
        H3 = bbox3_1[3] - bbox3_1[1]
        L_Boarder3 = (W3 - bbox3[2]) // 2
        U_Boarder3 = H3 - bbox3[3] - L_Boarder3
        daily3 = Daily(hwnd3, bbox3, imgs, L_Boarder3, U_Boarder3)


    
    action.alarm(1)
    print('''\n菜单: 脚本运行中可按F1可直接退出脚本,或按F2可重启脚本
    0 说明
    1 单刷探索经验怪
    2 单刷探索金币怪
    3 魂土司机
    4 魂土打手
    5 双开魂土
    6 双开困28
    7 三开魂土
    8 御灵
    9 觉醒
    ''')
    raw = input("\n选择功能模式:")
    # An application cannot force a window to the foreground while the user is working with another window.
    # win32gui.SetForegroundWindow(hwnd1)
    print('''\n
    1 桌面版
    2 沙盒
    3 mumu

    ''')
    agent = input("\n选择功能模式:")
    choose_menu(raw, agent)
    








