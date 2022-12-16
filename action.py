
import cv2,time,os, random
from winsound import Beep
import Featurematcah

 #在背景查找目标图片，并返回查找到的结果坐标列表，target是背景，want是要找目标
def locate(target,want, show=0, msg=0):
    want,treshold,c_name=want[0],want[1],want[2]
    pts = Featurematcah.surf(want, target, 0.61)
    return pts

def locate_matchTemplate(target,want, show=0, msg=0):
    want,treshold,c_name=want[0],want[1],want[2]
    result=cv2.matchTemplate(target,want,cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
    if(max_val > 0.7):
        return max_loc
    return []




#按【文件内容，匹配精度，名称】格式批量聚聚要查找的目标图片，精度统一为0.85，名称为文件名
#补充 这里是把所有图片一起读取了。全部放在内存里面。放在目标这个字典里面
def load_imgs():
    mubiao = {} #字典
    path = os.getcwd() + '/jpg' #返回当前目录路径
    file_list = os.listdir(path) #用于返回指定的文件夹包含的文件或文件夹的名字的列表。

    for file in file_list:
        name = file.split('.')[0]
        file_path = path + '/' + file
        b = cv2.imread(file_path)
        b = cv2.cvtColor(b, cv2.COLOR_BGR2GRAY)
        a = [b, 0.85, name] #值
        mubiao[name] = a #把值赋给键，这里这个作者写得让人有点误解。name既是键也是值的一部分.也就是前面的a里面也有name

    return mubiao

#蜂鸣报警器，参数n为鸣叫资料
def alarm(n):
    frequency = 1500
    last = 500

    for n in range(n):   
        Beep(frequency,last)
        time.sleep(0.05)

#裁剪图片以缩小匹配范围，screen为原图内容，upleft、downright是目标区域的左上角、右下角坐标
def cut(screen,upleft,downright): 

    a,b=upleft
    a = int(a)
    b = int(b)
    c,d=downright
    c = int(c)
    d = int(d)
    screen=screen[b:d,a:c]
    # cv2.imshow('1',screen)
    # cv2.waitKey()

    return screen

#随机偏移坐标，防止游戏的外挂检测。p是原坐标，w、n是目标图像宽高，返回目标范围内的一个随机坐标
def cheat(p, w, h):
    a,b = p
    #w, h = int(w/3), int(h/3)
    c,d = random.randint(w - 10, w),random.randint( h - 10, h)
    e,f = a + c, b + d
    y = [e, f]
    return(y)