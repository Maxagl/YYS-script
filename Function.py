import cv2,time
import action
import CaptureInactiveWindow
import Featurematcah
import CtrInacWindow
import pyautogui
import keyboard
import os
import sys

# 阴阳师日常class
class Daily:
# 单人探索
    def __init__(self, HWND, BBOX, IMGS, L_BOARDER, U_BOARDER):
        self.HWND = HWND
        self.BBOX = BBOX
        self.IMGS = IMGS
        self.L_BOARDER = L_BOARDER
        self.U_BOARDER = U_BOARDER
    def solo(self):
        hwnd = self.HWND
        bbox = self.BBOX
        imgs = self.IMGS
        L_Boarder = self.L_BOARDER
        U_Boarder = self.U_BOARDER
        flag = 0
        flag2 = 0
        w = bbox[2] - bbox[0]
        h = bbox[3] - bbox[1]
        print (w,h)
        while True:  # 直到取消，或者出错
            self.__processInput()
            screen = CtrInacWindow.capture_inactive_window(hwnd)
            screen = cv2.cvtColor(screen, cv2.COLOR_BGR2GRAY)
            want = imgs['guding']
            pts = action.locate_matchTemplate(screen, want, 0)
            if not len(pts) == 0:
                want = imgs['exp']
                want2 = imgs['jian']
                want = want[0]
                pts = Featurematcah.surf(want, screen, 0.75)
                if (len(pts) != 0 or flag2 < 5) :
                    flag2 = flag2 + 1
                    if not len(pts) == 0:
                        print('***找到了经验怪***')
                        if (pts[0] - w / 8 > 0 and pts[0] + w / 8 < w):
                            target = action.cut(screen, [pts[0] - w / 8, 0], [pts[0] + w / 8, pts[1]])
                            if(target.shape[0] < want2[0].shape[0] or target.shape[1] < want2[0].shape[1]):
                                continue
                            pts2 = action.locate_matchTemplate(target, want2, 0)
                            if not len(pts2) == 0:
                                print('找到了剑')
                                posi_1 = []
                                posi_1.append(pts[0] - w / 8 + pts2[0] + bbox[0] - L_Boarder)
                                posi_1.append(pts2[1] + bbox[1] - U_Boarder)
                                xx = action.cheat(posi_1, 10, 10)
                                CtrInacWindow.click_inactive_window(hwnd, xx)
                                time.sleep(3)
                                flag2 = 0
                                continue
                            else:
                                continue
                        if (pts[0] - w / 8 < 0):
                            target = action.cut(screen, [0, 0], [pts[0] + w / 8, pts[1]])
                            pts2 = action.locate(target, want2, 0)
                            if not len(pts2) == 0:
                                print('找到了剑')
                                posi_1 = []
                                posi_1.append(pts[0] - w / 8 + pts2[0] + bbox[0] - L_Boarder)
                                posi_1.append(pts2[1] + bbox[1] -U_Boarder)
                                xx = action.cheat(posi_1, 10, 10)
                                # pyautogui.click(xx)
                                CtrInacWindow.click_inactive_window(hwnd, xx)
                                print('点击小怪')
                                flag2 = 0
                                time.sleep(1)
                                continue
                            else:
                                continue
                        if (pts[0] + w / 8 > w):
                            target = action.cut(screen, [0, 0], [w, pts[1]])
                            pts2 = action.locate_matchTemplate(target, want2, 0)
                            if not len(pts2) == 0:
                                print('找到了剑')
                                posi_1 = []
                                posi_1.append(pts[0] - w / 8 + pts2[0] + bbox[0] - L_Boarder)
                                posi_1.append(pts2[1] + bbox[1] - U_Boarder)
                                xx = action.cheat(posi_1, 10, 10)
                                # pyautogui.click(xx)
                                CtrInacWindow.click_inactive_window(hwnd, xx)
                                time.sleep(1)
                                flag2 = 0
                                continue
                            else:
                                continue
                    else:
                        continue
                else:
                    CtrInacWindow.drag_inactive_window(hwnd, bbox)
                    flag2 = 0
                    flag = 1 + flag
                    time.sleep(0.5)
                    if (flag <= 1):
                        continue
                    for i in ['tuichu', 'queren']:
                        print('退出')
                        posi_1 = []
                        want = imgs[i]
                        pts = action.locate_matchTemplate(screen, want, 0)
                        if not len(pts) == 0:
                            posi_1.append(pts[0] + bbox[0] - L_Boarder)
                            posi_1.append(pts[1] + bbox[1] - U_Boarder)
                            print(want[0].shape)
                            posi_1 = action.cheat(posi_1, 20, 20)
                            #pyautogui.click(posi_1)
                            CtrInacWindow.click_inactive_window(hwnd, posi_1)
                            time.sleep(0.1)
                        screen = CaptureInactiveWindow.capture_inactive_window(hwnd)
                        screen = cv2.cvtColor(screen, cv2.COLOR_BGR2GRAY)
                        continue
                    continue
            # 换狗粮
            want = imgs['man']
            screen = CtrInacWindow.capture_inactive_window(hwnd)
            screen = cv2.cvtColor(screen,cv2.COLOR_BGR2GRAY)
            target = action.cut(screen, [0, h * 9 / 20 + U_Boarder], [w, h])
            pts = action.locate_matchTemplate(target, want, 0)
            #print(pts)
            #cv2.imshow('target',target)
            #cv2.waitKey(0)
            if not len(pts) == 0:
                posi_1 = []
                posi_1.append(pts[0] + bbox[0] - 50)
                posi_1.append(pts[1] + bbox[1] + h * 9 // 20 + 50)
                man = action.cheat(posi_1, 10, 10)
                CtrInacWindow.click_inactive_window(hwnd, man)
                time.sleep(2)
                screen = CtrInacWindow.capture_inactive_window(hwnd)
                screen = cv2.cvtColor(screen, cv2.COLOR_BGR2GRAY)
                want = imgs['quanbu']
                pts = action.locate_matchTemplate(screen, want, 0)
                if not len(pts) == 0:
                    posi_1 = []
                    posi_1.append(pts[0] + bbox[0] - L_Boarder)
                    posi_1.append(pts[1] + bbox[1] - U_Boarder)
                    # quanbu = action.cheat(posi_1, 10, 10)
                    CtrInacWindow.click_inactive_window(hwnd, posi_1)
                    time.sleep(1)

                    screen = CtrInacWindow.capture_inactive_window(hwnd)
                    screen = cv2.cvtColor(screen, cv2.COLOR_BGR2GRAY)
                    want = imgs['N']
                    pts = action.locate(screen, want, 0)
                    if not len(pts) == 0:
                        posi_1 = []
                        posi_1.append(pts[0] + bbox[0] - L_Boarder)
                        posi_1.append(pts[1] + bbox[1] - U_Boarder)
                        N = action.cheat(posi_1, 10, 10)
                        CtrInacWindow.click_inactive_window(hwnd, N)
                        CtrInacWindow.drag_Ncard(hwnd, bbox)
                        # pyautogui.moveTo(w * 3 // 20 + bbox[0], h * 3 // 4 + bbox[1])
                        # time.sleep(0.5)
                        # pyautogui.dragTo(w * 3 // 20, h // 2, 0.5, button='left')
                        # time.sleep(0.5)
                        screen = CtrInacWindow.capture_inactive_window(hwnd)
                        screen = cv2.cvtColor(screen, cv2.COLOR_BGR2GRAY)
                        want = imgs['zhunbei']
                        pts = action.locate(screen, want, 0)
                        if not len(pts) == 0:
                            posi_1 = []
                            posi_1.append(pts[0] + bbox[0] - L_Boarder)
                            posi_1.append(pts[1] + bbox[1] - U_Boarder)
                            zhunbei = action.cheat(posi_1, 10, 10)
                            CtrInacWindow.click_inactive_window(hwnd, zhunbei)
            else:
                want = imgs['zhunbei']
                pts = action.locate_matchTemplate(screen, want, 0)
                if not len(pts) == 0:
                    posi_1 = []
                    posi_1.append(pts[0] + bbox[0])
                    posi_1.append(pts[1] + bbox[1])
                    zhunbei = action.cheat(posi_1, 10, 10)
                    CtrInacWindow.click_inactive_window(hwnd, zhunbei)
                    continue

            for i in ['shengli', 'jiangli']:
                want = imgs[i]
                target = screen
                pts = action.locate_matchTemplate(target, want, 0)
                if not len(pts) == 0:
                    posi_1 = []
                    posi_1.append(pts[0] + bbox[0] )#- L_Boarder
                    posi_1.append(pts[1] + bbox[1] )#- U_Boarder
                    xy = action.cheat(posi_1, 10, 10)
                    CtrInacWindow.click_inactive_window(hwnd, xy)
                    print('领取奖励:{}'.format(time.ctime()))
                    time.sleep(0.1)
                    flag2 = 0
                    break

            want = imgs['tansuo']
            target = screen
            pts = action.locate_matchTemplate(target, want, 0)
            if not len(pts) == 0:
                flag = 0
                print('重新进入地图')
                posi_1 = []
                posi_1.append(pts[0] + bbox[0] )#- L_Boarder
                posi_1.append(pts[1] + bbox[1] )#- U_Boarder
                print(posi_1)
                xy = action.cheat(posi_1, 10, 10)
                print(xy)
                CtrInacWindow.click_inactive_window(hwnd, posi_1)
                time.sleep(0.15)

            want = imgs['shaonv']
            pts = action.locate_matchTemplate(screen, want, 0)
            if not len(pts) == 0:
                flag = 0
                print('进入世界地图')
                posi_1 = []
                posi_1.append(pts[0] + bbox[0] - L_Boarder)
                posi_1.append(pts[1] + bbox[1] - U_Boarder)
                xy = action.cheat(posi_1, 15, 15)
                CtrInacWindow.click_inactive_window(hwnd, xy)
    def solo_jinbi(self):
        hwnd = self.HWND
        bbox = self.BBOX
        imgs = self.IMGS
        L_Boarder = self.L_BOARDER
        U_Boarder = self.U_BOARDER
        flag = 0
        flag2 = 0
        w = bbox[2] - bbox[0]
        h = bbox[3] - bbox[1]
        while True:  # 直到取消，或者出错
            self.__processInput()
            screen = CtrInacWindow.capture_inactive_window(hwnd)
            screen = cv2.cvtColor(screen, cv2.COLOR_BGR2GRAY)
            want = imgs['guding']
            pts = action.locate_matchTemplate(screen, want, 0)
            if not len(pts) == 0:
                want = imgs['jinbi']
                want2 = imgs['jian']
                want = want[0]
                pts = Featurematcah.surf(want, screen, 0.75)
                if (len(pts) != 0 or flag2 < 5) :
                    flag2 = flag2 + 1
                    if not len(pts) == 0:
                        print('***找到了金币怪***')
                        if (pts[0] - w / 8 > 0 and pts[0] + w / 8 < w):
                            target = action.cut(screen, [pts[0] - w / 8, 0], [pts[0] + w / 8, pts[1]])
                            if(target.shape[0] < want2[0].shape[0] or target.shape[1] < want2[0].shape[1]):
                                continue
                            pts2 = action.locate_matchTemplate(target, want2, 0)
                            if not len(pts2) == 0:
                                print('找到了剑')
                                posi_1 = []
                                posi_1.append(pts[0] - w / 8 + pts2[0] + bbox[0] - L_Boarder)
                                posi_1.append(pts2[1] + bbox[1] - U_Boarder)
                                xx = action.cheat(posi_1, 10, 10)
                                CtrInacWindow.click_inactive_window(hwnd, xx)
                                time.sleep(3)
                                flag2 = 0
                                continue
                            else:
                                continue
                        if (pts[0] - w / 8 < 0):
                            target = action.cut(screen, [0, 0], [pts[0] + w / 8, pts[1]])
                            pts2 = action.locate(target, want2, 0)
                            if not len(pts2) == 0:
                                print('找到了剑')
                                posi_1 = []
                                posi_1.append(pts[0] - w / 8 + pts2[0] + bbox[0] - L_Boarder)
                                posi_1.append(pts2[1] + bbox[1] -U_Boarder)
                                xx = action.cheat(posi_1, 10, 10)
                                # pyautogui.click(xx)
                                CtrInacWindow.click_inactive_window(hwnd, xx)
                                print('点击小怪')
                                flag2 = 0
                                time.sleep(1)
                                continue
                            else:
                                continue
                        if (pts[0] + w / 8 > w):
                            target = action.cut(screen, [0, 0], [w, pts[1]])
                            pts2 = action.locate_matchTemplate(target, want2, 0)
                            if not len(pts2) == 0:
                                print('找到了剑')
                                posi_1 = []
                                posi_1.append(pts[0] - w / 8 + pts2[0] + bbox[0] - L_Boarder)
                                posi_1.append(pts2[1] + bbox[1] - U_Boarder)
                                xx = action.cheat(posi_1, 10, 10)
                                # pyautogui.click(xx)
                                CtrInacWindow.click_inactive_window(hwnd, xx)
                                time.sleep(1)
                                flag2 = 0
                                continue
                            else:
                                continue
                    else:
                        continue
                else:
                    CtrInacWindow.drag_inactive_window(hwnd, bbox)
                    flag2 = 0
                    flag = 1 + flag
                    time.sleep(0.5)
                    if (flag <= 1):
                        continue
                    for i in ['tuichu', 'queren']:
                        print('退出')
                        posi_1 = []
                        want = imgs[i]
                        pts = action.locate_matchTemplate(screen, want, 0)
                        if not len(pts) == 0:
                            posi_1.append(pts[0] + bbox[0] - L_Boarder)
                            posi_1.append(pts[1] + bbox[1] - U_Boarder)
                            queding = action.cheat(posi_1, 20, 20)
                            # pyautogui.click(queding)
                            CtrInacWindow.click_inactive_window(hwnd, queding)
                            time.sleep(0.5)
                        screen = CaptureInactiveWindow.capture_inactive_window(hwnd)
                        screen = cv2.cvtColor(screen, cv2.COLOR_BGR2GRAY)
                        continue
                    continue
            # 换狗粮
            want = imgs['man']
            screen = CtrInacWindow.capture_inactive_window(hwnd)
            screen = cv2.cvtColor(screen,cv2.COLOR_BGR2GRAY)
            target = action.cut(screen, [0, h * 9 / 20 + U_Boarder], [w, h])
            pts = action.locate_matchTemplate(target, want, 0)
            #print(pts)
            #cv2.imshow('screen',screen)
            #cv2.imshow('target',target)
            #cv2.waitKey(0)
            if not len(pts) == 0:
                posi_1 = []
                posi_1.append(pts[0] + bbox[0])
                posi_1.append(pts[1] + bbox[1] + h * 9 // 20)
                man = action.cheat(posi_1, 10, 10)
                CtrInacWindow.click_inactive_window(hwnd, man)
                time.sleep(2)
                screen = CtrInacWindow.capture_inactive_window(hwnd)
                screen = cv2.cvtColor(screen, cv2.COLOR_BGR2GRAY)
                want = imgs['quanbu']
                pts = action.locate_matchTemplate(screen, want, 0)
                if not len(pts) == 0:
                    posi_1 = []
                    posi_1.append(pts[0] + bbox[0] - L_Boarder)
                    posi_1.append(pts[1] + bbox[1] - U_Boarder)
                    # quanbu = action.cheat(posi_1, 10, 10)
                    CtrInacWindow.click_inactive_window(hwnd, posi_1)
                    time.sleep(1)

                    screen = CtrInacWindow.capture_inactive_window(hwnd)
                    screen = cv2.cvtColor(screen, cv2.COLOR_BGR2GRAY)
                    want = imgs['N']
                    pts = action.locate(screen, want, 0)
                    if not len(pts) == 0:
                        posi_1 = []
                        posi_1.append(pts[0] + bbox[0] - L_Boarder)
                        posi_1.append(pts[1] + bbox[1] - U_Boarder)
                        N = action.cheat(posi_1, 10, 10)
                        CtrInacWindow.click_inactive_window(hwnd, N)
                        CtrInacWindow.drag_Ncard(hwnd, bbox)
                        # pyautogui.moveTo(w * 3 // 20 + bbox[0], h * 3 // 4 + bbox[1])
                        # time.sleep(0.5)
                        # pyautogui.dragTo(w * 3 // 20, h // 2, 0.5, button='left')
                        # time.sleep(0.5)
                        screen = CtrInacWindow.capture_inactive_window(hwnd)
                        screen = cv2.cvtColor(screen, cv2.COLOR_BGR2GRAY)
                        want = imgs['zhunbei']
                        pts = action.locate(screen, want, 0)
                        if not len(pts) == 0:
                            posi_1 = []
                            posi_1.append(pts[0] + bbox[0] - L_Boarder)
                            posi_1.append(pts[1] + bbox[1] - U_Boarder)
                            zhunbei = action.cheat(posi_1, 10, 10)
                            CtrInacWindow.click_inactive_window(hwnd, zhunbei)
            else:
                want = imgs['zhunbei']
                pts = action.locate_matchTemplate(screen, want, 0)
                if not len(pts) == 0:
                    posi_1 = []
                    posi_1.append(pts[0] + bbox[0])
                    posi_1.append(pts[1] + bbox[1])
                    zhunbei = action.cheat(posi_1, 10, 10)
                    CtrInacWindow.click_inactive_window(hwnd, zhunbei)
                    continue

            for i in ['shengli', 'jiangli']:
                want = imgs[i]
                target = screen
                pts = action.locate_matchTemplate(target, want, 0)
                if not len(pts) == 0:
                    posi_1 = []
                    posi_1.append(pts[0] + bbox[0] - L_Boarder)
                    posi_1.append(pts[1] + bbox[1] - U_Boarder)
                    xy = action.cheat(posi_1, 10, 10)
                    CtrInacWindow.click_inactive_window(hwnd, xy)
                    print('领取奖励')
                    time.sleep(0.1)
                    flag2 = 0
                    break

            want = imgs['tansuo']
            target = screen
            pts = action.locate_matchTemplate(target, want, 0)
            if not len(pts) == 0:
                flag = 0
                print('重新进入地图')
                posi_1 = []
                posi_1.append(pts[0] + bbox[0] - L_Boarder)
                posi_1.append(pts[1] + bbox[1] - U_Boarder)
                print(posi_1)
                xy = action.cheat(posi_1, 10, 10)
                print(xy)
                CtrInacWindow.click_inactive_window(hwnd, xy)
                time.sleep(0.4)

            want = imgs['shaonv']
            pts = action.locate_matchTemplate(screen, want, 0)
            if not len(pts) == 0:
                flag = 0
                print('进入世界地图')
                posi_1 = []
                posi_1.append(pts[0] + bbox[0] - L_Boarder)
                posi_1.append(pts[1] + bbox[1] - U_Boarder)
                xy = action.cheat(posi_1, 10, 10)
                CtrInacWindow.click_inactive_window(hwnd, xy)

    def huntu_driver(self):      
        hwnd = self.HWND
        bbox = self.BBOX
        imgs = self.IMGS
        L_Boarder = self.L_BOARDER
        U_Boarder = self.U_BOARDER
        w = bbox[2] - bbox[0]
        h = bbox[3] - bbox[1]
        while True:  # 直到取消，或者出错
            self.__processInput()
            screen = CtrInacWindow.capture_inactive_window(hwnd)
            screen = cv2.cvtColor(screen, cv2.COLOR_BGR2GRAY)
            want = imgs['yuhuntiaozhan']
            pts = action.locate_matchTemplate(screen, want, 0)
            if not len(pts) == 0:
                time.sleep(1)
                CtrInacWindow.click_inactive_window(hwnd, pts)

            screen = CtrInacWindow.capture_inactive_window(hwnd)
            screen = cv2.cvtColor(screen, cv2.COLOR_BGR2GRAY)
            want = imgs['zhunbei']
            pts = action.locate_matchTemplate(screen, want, 0)
            if not len(pts) == 0:
                print("检测到司机准备按钮")
                posi_1 = []
                posi_1.append(pts[0] + bbox[0])
                posi_1.append(pts[1] + bbox[1])
                zhunbei = action.cheat(posi_1, 10, 10)
                CtrInacWindow.click_inactive_window(hwnd, zhunbei)
                print("司机准备完毕")
                time.sleep(19)
                continue

            for i in ['dianjijixu', 'jiangli']:
                want = imgs[i]
                target = screen
                pts = action.locate_matchTemplate(target, want, 0)
                if not len(pts) == 0:
                    posi_1 = []
                    posi_1.append(pts[0] + bbox[0] - L_Boarder + 40)
                    posi_1.append(pts[1] + bbox[1] - U_Boarder)
                    xy = action.cheat(posi_1, 10, 10)
                    CtrInacWindow.click_inactive_window(hwnd, xy)
                    time.sleep(1)
                    break

            screen = CtrInacWindow.capture_inactive_window(hwnd)
            screen = cv2.cvtColor(screen, cv2.COLOR_BGR2GRAY)
            want = imgs['yaoqing']
            pts = action.locate_matchTemplate(screen, want, 0)
            if not len(pts) == 0:
                posi_1 = []
                posi_1.append(pts[0] + bbox[0])
                posi_1.append(pts[1] + bbox[1])
                zhunbei = action.cheat(posi_1, 10, 10)
                CtrInacWindow.click_inactive_window(hwnd, zhunbei)
                time.sleep(0.5)

            want = imgs['queding']
            pts = action.locate_matchTemplate(screen, want, 0)
            if not len(pts) == 0:
                posi_1 = []
                posi_1.append(pts[0] + bbox[0])
                posi_1.append(pts[1] + bbox[1])
                zhunbei = action.cheat(posi_1, 10, 10)
                CtrInacWindow.click_inactive_window(hwnd, zhunbei)
                time.sleep(0.1)
                continue
            time.sleep(2)

    def huntu_fighter(self):
        hwnd = self.HWND
        bbox = self.BBOX
        imgs = self.IMGS
        L_Boarder = self.L_BOARDER
        U_Boarder = self.U_BOARDER
        w = bbox[2] - bbox[0]
        h = bbox[3] - bbox[1]
        while True:  # 直到取消，或者出错
            self.__processInput()
            screen = CtrInacWindow.capture_inactive_window(hwnd)
            screen = cv2.cvtColor(screen, cv2.COLOR_BGR2GRAY)
            want = imgs['zhunbei']
            pts = action.locate_matchTemplate(screen, want, 0)
            if not len(pts) == 0:
                print("检测到打手准备按钮")
                posi_1 = []
                posi_1.append(pts[0] + bbox[0])
                posi_1.append(pts[1] + bbox[1])
                zhunbei = action.cheat(posi_1, 10, 10)
                CtrInacWindow.click_inactive_window(hwnd, zhunbei)
                print("打手准备完毕")
                time.sleep(19)
                continue

            for i in ['dianjijixu', 'jiangli']:
                want = imgs[i]
                target = screen
                pts = action.locate_matchTemplate(target, want, 0)
                if not len(pts) == 0:
                    posi_1 = []
                    posi_1.append(pts[0] + bbox[0] - L_Boarder + 50)
                    posi_1.append(pts[1] + bbox[1] - U_Boarder)
                    xy = action.cheat(posi_1, 5, 5)
                    CtrInacWindow.click_inactive_window(hwnd, xy)
                    time.sleep(1)
                    flag2 = 0
                    break

            screen = CtrInacWindow.capture_inactive_window(hwnd)
            screen = cv2.cvtColor(screen, cv2.COLOR_BGR2GRAY)
            want = imgs['mojie']
            pts = action.locate_matchTemplate(screen, want, 0)
            if not len(pts) == 0:
                posi_1 = []
                posi_1.append(pts[0] + bbox[0])
                posi_1.append(pts[1] + bbox[1])
                zhunbei = action.cheat(posi_1, 10, 10)
                CtrInacWindow.click_inactive_window(hwnd, zhunbei)
                time.sleep(0.2)

            screen = CtrInacWindow.capture_inactive_window(hwnd)
            screen = cv2.cvtColor(screen, cv2.COLOR_BGR2GRAY)
            want = imgs['queding']
            pts = action.locate_matchTemplate(screen, want, 0)
            if not len(pts) == 0:
                posi_1 = []
                posi_1.append(pts[0])
                posi_1.append(pts[1])
                zhunbei = action.cheat(posi_1, 10, 10)
                CtrInacWindow.click_inactive_window(hwnd, zhunbei)
                time.sleep(0.1)
            time.sleep(2)

    def jinbi_driver(self):
        hwnd = self.HWND
        bbox = self.BBOX
        imgs = self.IMGS
        L_Boarder = self.L_BOARDER
        U_Boarder = self.U_BOARDER
        flag = 0
        flag2 = 0
        w = bbox[2] - bbox[0]
        h = bbox[3] - bbox[1]
        print (w,h)
        while True:  # 直到取消，或者出错
            self.__processInput()
            screen = CtrInacWindow.capture_inactive_window(hwnd)
            screen = cv2.cvtColor(screen, cv2.COLOR_BGR2GRAY)
            want = imgs['kun28tiaozhan']
            pts = action.locate_matchTemplate(screen, want, 0)
            if not len(pts) == 0:
                CtrInacWindow.click_inactive_window(hwnd, pts)
                time.sleep(0.3)
            screen = CtrInacWindow.capture_inactive_window(hwnd)
            screen = cv2.cvtColor(screen, cv2.COLOR_BGR2GRAY)
            want = imgs['guding']
            pts = action.locate_matchTemplate(screen, want, 0)
            if not len(pts) == 0:
                want = imgs['jinbi']
                want2 = imgs['jian']
                want = want[0]
                pts = Featurematcah.surf(want, screen, 0.75)
                if (len(pts) != 0 or flag2 < 5) :
                    flag2 = flag2 + 1
                    print(flag2)
                    if not len(pts) == 0:
                        print('***找到了金币怪***')
                        if (pts[0] - w / 8 > 0 and pts[0] + w / 8 < w):
                            target = action.cut(screen, [pts[0] - w / 8, 0], [pts[0] + w / 8, pts[1]])
                            if(target.shape[0] < want2[0].shape[0] or target.shape[1] < want2[0].shape[1]):
                                continue
                            pts2 = action.locate_matchTemplate(target, want2, 0)
                            if not len(pts2) == 0:
                                print('找到了剑')
                                posi_1 = []
                                posi_1.append(pts[0] - w / 8 + pts2[0] + bbox[0] - L_Boarder)
                                posi_1.append(pts2[1] + bbox[1] - U_Boarder)
                                xx = action.cheat(posi_1, 10, 10)
                                CtrInacWindow.click_inactive_window(hwnd, xx)
                                time.sleep(3)
                                flag2 = 0
                                continue
                            else:
                                continue
                        if (pts[0] - w / 8 < 0):
                            target = action.cut(screen, [0, 0], [pts[0] + w / 8, pts[1]])
                            pts2 = action.locate(target, want2, 0)
                            if not len(pts2) == 0:
                                print('找到了剑')
                                posi_1 = []
                                posi_1.append(pts[0] - w / 8 + pts2[0] + bbox[0] - L_Boarder)
                                posi_1.append(pts2[1] + bbox[1] -U_Boarder)
                                xx = action.cheat(posi_1, 10, 10)
                                # pyautogui.click(xx)
                                CtrInacWindow.click_inactive_window(hwnd, xx)
                                print('点击小怪')
                                flag2 = 0
                                time.sleep(1)
                                continue
                            else:
                                continue
                        if (pts[0] + w / 8 > w):
                            target = action.cut(screen, [0, 0], [w, pts[1]])
                            pts2 = action.locate_matchTemplate(target, want2, 0)
                            if not len(pts2) == 0:
                                print('找到了剑')
                                posi_1 = []
                                posi_1.append(pts[0] - w / 8 + pts2[0] + bbox[0] - L_Boarder)
                                posi_1.append(pts2[1] + bbox[1] - U_Boarder)
                                xx = action.cheat(posi_1, 10, 10)
                                # pyautogui.click(xx)
                                CtrInacWindow.click_inactive_window(hwnd, xx)
                                time.sleep(1)
                                flag2 = 0
                                continue
                            else:
                                continue
                    else:
                        continue
                else:
                    CtrInacWindow.drag_inactive_window(hwnd, bbox)
                    flag2 = 0
                    flag = 1 + flag
                    time.sleep(0.5)
                    if (flag <= 1):
                        continue
                    for i in ['tuichu', 'queren']:
                        print('退出')
                        posi_1 = []
                        want = imgs[i]
                        pts = action.locate_matchTemplate(screen, want, 0)
                        if not len(pts) == 0:
                            posi_1.append(pts[0] + bbox[0] - L_Boarder)
                            posi_1.append(pts[1] + bbox[1] - U_Boarder)
                            print(want[0].shape)
                            posi_1 = action.cheat(posi_1, 20, 20)
                            #pyautogui.click(posi_1)
                            CtrInacWindow.click_inactive_window(hwnd, posi_1)
                            time.sleep(0.1)
                        screen = CaptureInactiveWindow.capture_inactive_window(hwnd)
                        screen = cv2.cvtColor(screen, cv2.COLOR_BGR2GRAY)
                        continue
                    continue

            want = imgs['zhunbei']
            screen = CtrInacWindow.capture_inactive_window(hwnd)
            screen = cv2.cvtColor(screen,cv2.COLOR_BGR2GRAY)
            pts = action.locate_matchTemplate(screen, want, 0) 
            if not len(pts) == 0:
                posi_1 = []
                posi_1.append(pts[0] + bbox[0])
                posi_1.append(pts[1] + bbox[1])
                zhunbei = action.cheat(posi_1, 10, 10)
                CtrInacWindow.click_inactive_window(hwnd, zhunbei)
                continue

            for i in ['shengli', 'jiangli']:
                screen = CtrInacWindow.capture_inactive_window(hwnd)
                screen = cv2.cvtColor(screen,cv2.COLOR_BGR2GRAY)
                want = imgs[i]
                target = screen
                pts = action.locate_matchTemplate(target, want, 0)
                if not len(pts) == 0:
                    posi_1 = []
                    posi_1.append(pts[0] + bbox[0] )#- L_Boarder
                    posi_1.append(pts[1] + bbox[1] )#- U_Boarder
                    xy = action.cheat(posi_1, 15, 15)
                    CtrInacWindow.click_inactive_window(hwnd, xy)
                    print('领取奖励')
                    time.sleep(0.1)
                    flag2 = 0
                    break
            screen = CtrInacWindow.capture_inactive_window(hwnd)
            screen = cv2.cvtColor(screen, cv2.COLOR_BGR2GRAY)
            want = imgs['queding']
            pts = action.locate(screen, want, 0)
            if not len(pts) == 0:
                posi_1 = []
                posi_1.append(pts[0] + bbox[0] )#- L_Boarder
                posi_1.append(pts[1] + bbox[1] )#- U_Boarder
                xy = action.cheat(posi_1, 10, 10)
                CtrInacWindow.click_inactive_window(hwnd, xy)
                print('发送邀请')
                time.sleep(2)

    def jinbi_fighter(self):
        
        hwnd = self.HWND
        bbox = self.BBOX
        imgs = self.IMGS
        L_Boarder = self.L_BOARDER
        U_Boarder = self.U_BOARDER
        flag = 0
        flag2 = 0
        w = bbox[2] - bbox[0]
        h = bbox[3] - bbox[1]
        while True:
            self.__processInput()
            screen = CtrInacWindow.capture_inactive_window(hwnd)
            screen = cv2.cvtColor(screen, cv2.COLOR_BGR2GRAY)
            want = imgs['biaoqing']
            want_1 = imgs['tuichu']
            pts = action.locate_matchTemplate(screen, want, 0)
            pts_1 = action.locate_matchTemplate(screen, want_1, 0)
            if not len(pts_1) == 0 and len(pts) == 0:
                posi_1 = []
                posi_1.append(pts_1[0] + bbox[0] )#- L_Boarder
                posi_1.append(pts_1[1] + bbox[1] )#- U_Boarder
                xy = action.cheat(posi_1, 10, 10)
                CtrInacWindow.click_inactive_window(hwnd, xy)
                time.sleep(0.3)

                screen = CtrInacWindow.capture_inactive_window(hwnd)
                screen = cv2.cvtColor(screen, cv2.COLOR_BGR2GRAY)
                want = imgs['queren']
                pts = action.locate_matchTemplate(screen, want, 0)
                if not len(pts) == 0:
                    posi_1 = []
                    posi_1.append(pts[0] + bbox[0])# - L_Boarder)
                    posi_1.append(pts[1] + bbox[1])# - U_Boarder)
                    xy = action.cheat(posi_1, 15, 15)
                    CtrInacWindow.click_inactive_window(hwnd, xy)

                print('打手退出困28')
                time.sleep(0.3)
            
            screen = CtrInacWindow.capture_inactive_window(hwnd)
            screen = cv2.cvtColor(screen, cv2.COLOR_BGR2GRAY)
            want = imgs['kun28yaoqing']
            pts = action.locate_matchTemplate(screen, want, 0)
            if not len(pts) == 0:
                posi_1 = []
                posi_1.append(pts[0] + bbox[0] )#- L_Boarder
                posi_1.append(pts[1] + bbox[1] )#- U_Boarder
                xy = action.cheat(posi_1, 10, 10)
                CtrInacWindow.click_inactive_window(hwnd, xy)
                print('打手接受邀请')
                time.sleep(1)
            
            # 换狗粮
            want = imgs['man']
            screen = CtrInacWindow.capture_inactive_window(hwnd)
            screen = cv2.cvtColor(screen,cv2.COLOR_BGR2GRAY)
            target = action.cut(screen, [0, h * 9 / 20 + U_Boarder], [w, h])
            pts = action.locate_matchTemplate(target, want, 0)
                #print(pts)
                #cv2.imshow('target',target)
                #cv2.waitKey(0)
            if not len(pts) == 0:
                posi_1 = []
                posi_1.append(pts[0] + bbox[0] - 50)
                posi_1.append(pts[1] + bbox[1] + h * 9 // 20 + 50)
                man = action.cheat(posi_1, 10, 10)
                CtrInacWindow.click_inactive_window(hwnd, man)
                time.sleep(2)
                screen = CtrInacWindow.capture_inactive_window(hwnd)
                screen = cv2.cvtColor(screen, cv2.COLOR_BGR2GRAY)
                want = imgs['quanbu']
                pts = action.locate_matchTemplate(screen, want, 0)
                if not len(pts) == 0:
                    posi_1 = []
                    posi_1.append(pts[0] + bbox[0] - L_Boarder)
                    posi_1.append(pts[1] + bbox[1] - U_Boarder)
                    # quanbu = action.cheat(posi_1, 10, 10)
                    CtrInacWindow.click_inactive_window(hwnd, posi_1)
                    time.sleep(1)

                    screen = CtrInacWindow.capture_inactive_window(hwnd)
                    screen = cv2.cvtColor(screen, cv2.COLOR_BGR2GRAY)
                    want = imgs['N']
                    pts = action.locate(screen, want, 0)
                    if not len(pts) == 0:
                        posi_1 = []
                        posi_1.append(pts[0] + bbox[0] - L_Boarder)
                        posi_1.append(pts[1] + bbox[1] - U_Boarder)
                        N = action.cheat(posi_1, 10, 10)
                        CtrInacWindow.click_inactive_window(hwnd, N)
                        CtrInacWindow.drag_Ncard(hwnd, bbox)
                        # pyautogui.moveTo(w * 3 // 20 + bbox[0], h * 3 // 4 + bbox[1])
                        # time.sleep(0.5)
                        # pyautogui.dragTo(w * 3 // 20, h // 2, 0.5, button='left')
                        # time.sleep(0.5)
                        screen = CtrInacWindow.capture_inactive_window(hwnd)
                        screen = cv2.cvtColor(screen, cv2.COLOR_BGR2GRAY)
                        want = imgs['zhunbei']
                        pts = action.locate(screen, want, 0)
                        if not len(pts) == 0:
                            posi_1 = []
                            posi_1.append(pts[0] + bbox[0] - L_Boarder)
                            posi_1.append(pts[1] + bbox[1] - U_Boarder)
                            zhunbei = action.cheat(posi_1, 10, 10)
                            CtrInacWindow.click_inactive_window(hwnd, zhunbei)
            else:
                screen = CtrInacWindow.capture_inactive_window(hwnd)
                screen = cv2.cvtColor(screen, cv2.COLOR_BGR2GRAY)
                want = imgs['zhunbei']
                pts = action.locate_matchTemplate(screen, want, 0)
                if not len(pts) == 0:
                    posi_1 = []
                    posi_1.append(pts[0] + bbox[0])
                    posi_1.append(pts[1] + bbox[1])
                    zhunbei = action.cheat(posi_1, 10, 10)
                    CtrInacWindow.click_inactive_window(hwnd, zhunbei)
                    continue
            
            for i in ['shengli', 'jiangli']:
                want = imgs[i]
                target = screen
                pts = action.locate_matchTemplate(target, want, 0)
                if not len(pts) == 0:
                    posi_1 = []
                    posi_1.append(pts[0] + bbox[0] )#- L_Boarder
                    posi_1.append(pts[1] + bbox[1] )#- U_Boarder
                    xy = action.cheat(posi_1, 10, 10)
                    CtrInacWindow.click_inactive_window(hwnd, xy)
                    print('领取奖励')
                    time.sleep(0.1)
                    flag2 = 0
                    break
    def huodong(self):
        hwnd = self.HWND
        bbox = self.BBOX
        imgs = self.IMGS
        L_Boarder = self.L_BOARDER
        U_Boarder = self.U_BOARDER
        w = bbox[2] - bbox[0]
        h = bbox[3] - bbox[1]
        while True:  # 直到取消，或者出错
            self.__processInput()
            screen = CtrInacWindow.capture_inactive_window(hwnd)
            screen = cv2.cvtColor(screen, cv2.COLOR_BGR2GRAY)
            want = imgs['huodong_tiaozhan']
            pts = action.locate_matchTemplate(screen, want, 0)
            if not len(pts) == 0:
                CtrInacWindow.click_inactive_window(hwnd, pts)


            for i in ['dianjijixu', 'jiangli']:
                want = imgs[i]
                target = screen
                pts = action.locate_matchTemplate(target, want, 0)
                if not len(pts) == 0:
                    posi_1 = []
                    posi_1.append(pts[0] + bbox[0] - L_Boarder + 40)
                    posi_1.append(pts[1] + bbox[1] - U_Boarder)
                    xy = action.cheat(posi_1, 10, 10)
                    CtrInacWindow.click_inactive_window(hwnd, xy)
                    time.sleep(0.5)
                    break
            time.sleep(0.5)
        
    def yuling(self):
        
        hwnd = self.HWND
        bbox = self.BBOX
        imgs = self.IMGS
        L_Boarder = self.L_BOARDER
        U_Boarder = self.U_BOARDER
        w = bbox[2] - bbox[0]
        h = bbox[3] - bbox[1]
        while True:  # 直到取消，或者出错
            self.__processInput()
            screen = CtrInacWindow.capture_inactive_window(hwnd)
            screen = cv2.cvtColor(screen, cv2.COLOR_BGR2GRAY)
            want = imgs['yuling_tiaozhan']
            pts = action.locate_matchTemplate(screen, want, 0)
            if not len(pts) == 0:
                CtrInacWindow.click_inactive_window(hwnd, pts)


            for i in ['dianjijixu', 'jiangli']:
                want = imgs[i]
                target = screen
                pts = action.locate_matchTemplate(target, want, 0)
                if not len(pts) == 0:
                    posi_1 = []
                    posi_1.append(pts[0] + bbox[0] - L_Boarder + 40)
                    posi_1.append(pts[1] + bbox[1] - U_Boarder)
                    xy = action.cheat(posi_1, 10, 10)
                    CtrInacWindow.click_inactive_window(hwnd, xy)
                    time.sleep(0.5)
                    break
            time.sleep(0.5)
    def juexing(self):
        hwnd = self.HWND
        bbox = self.BBOX
        imgs = self.IMGS
        L_Boarder = self.L_BOARDER
        U_Boarder = self.U_BOARDER
        w = bbox[2] - bbox[0]
        h = bbox[3] - bbox[1]
        while True:  # 直到取消，或者出错
            self.__processInput()
            screen = CtrInacWindow.capture_inactive_window(hwnd)
            screen = cv2.cvtColor(screen, cv2.COLOR_BGR2GRAY)
            want = imgs['juexing_tiaozhan']
            pts = action.locate_matchTemplate(screen, want, 0)
            # cv2.rectangle(screen,(pts[0]+10, pts[1] +10), pts, (0,255,0),3)
            # screen = cv2.cvtColor(screen, cv2.COLOR_BGR2GRAY)
            # cv2.imshow("123", screen)
            # cv2.waitKey()
            if not len(pts) == 0:
                CtrInacWindow.click_inactive_window(hwnd, pts)



            for i in ['dianjijixu', 'jiangli']:
                want = imgs[i]
                target = screen
                pts = action.locate_matchTemplate(target, want, 0)
                if not len(pts) == 0:
                    posi_1 = []
                    posi_1.append(pts[0] + bbox[0] - L_Boarder + 40)
                    posi_1.append(pts[1] + bbox[1] - U_Boarder)
                    xy = action.cheat(posi_1, 10, 10)
                    CtrInacWindow.click_inactive_window(hwnd, xy)
                    time.sleep(0.5)
                    break
            time.sleep(0.5)

    def __processInput(self):
        if keyboard.is_pressed('F1'):
            exit()
        elif keyboard.is_pressed('F2'):
            os.execl(sys.executable, os.path.abspath(__file__), *sys.argv) 


        




