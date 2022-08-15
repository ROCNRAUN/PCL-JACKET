import cv2
import time
import numpy as np
from mss import mss
import pyautogui
from python_imagesearch.imagesearch import imagesearch_loop, imagesearch
from paddleocr import PaddleOCR, draw_ocr
import collections, statistics
import traceback
import logging
from collections import Counter
import pyperclip
import subprocess
import requests
import re
import base64
import urllib.parse
import hashlib
import time
import cv2


def live(e):
    i, b = e.split('?')
    r = i.split('/')
    s = re.sub(r'.(flv|m3u8)', '', r[-1])
    c = b.split('&', 3)
    c = [i for i in c if i != '']
    n = {i.split('=')[0]: i.split('=')[1] for i in c}
    fm = urllib.parse.unquote(n['fm'])
    u = base64.b64decode(fm).decode('utf-8')
    p = u.split('_')[0]
    f = str(int(time.time() * 1e7))
    l = n['wsTime']
    t = '0'
    h = '_'.join([p, t, s, f, l])
    m = hashlib.md5(h.encode('utf-8')).hexdigest()
    y = c[-1]
    url = "{}?wsSecret={}&wsTime={}&u={}&seqid={}&{}".format(i, m, l, t, f, y)
    return url

def get_real_url(quality):
    try:
        if quality == 1:
            ratio = 10000
        elif quality == 2:
            ratio = 4000
        else:
            ratio = 4000
        room_url = 'https://m.huya.com/660004'
        header = {
            'Content-Type': 'application/x-www-form-urlencoded',
            'User-Agent': 'Mozilla/5.0 (Linux; Android 5.0; SM-G900P Build/LRX21T) AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/75.0.3770.100 Mobile Safari/537.36 '
        }
        response = requests.get(url=room_url, headers=header).text
        liveLineUrl = re.findall(r'"liveLineUrl":"([\s\S]*?)",', response)[0]
        liveline = base64.b64decode(liveLineUrl).decode('utf-8')
        if liveline:
            if 'replay' in liveline:
                return '直播录像：' + liveline
            else:
                liveline = live(liveline)
                real_url = ("https:" + liveline).replace("hls", "flv").replace("m3u8", "flv")
                real_url = real_url.replace("tars_mobile","huya_webh5")
                if 'ratio' not in real_url:
                    real_url = real_url + '&ratio=' + str(ratio)

        else:
            real_url = '未开播或直播间不存在'
    except:
        real_url = '未开播或直播间不存在'
    return real_url

def redeem(code):

    redeemImg_1 = './img/step_1.png'
    redeemImg_2 = './img/step_2.png'

    # Step 1
    pos = imagesearch(redeemImg_1, 0.7)
    x = pos[0] + 30
    y = pos[1] + 10
    if not pos[0] == -1:
        pyautogui.click(x, y)
    
    # Step 2
    pyautogui.write(code)

    # Step 3
    pos1 = imagesearch(redeemImg_2, 0.8)
    x1 = pos1[0]
    y1 = pos1[1]

    if not pos1[0] == -1:
        pyautogui.click(x1, y1)

def most_frequent(List,level):

    counter = 0
    num = ''
     
    for i in List:
        curr_frequency = List.count(i)
        if(curr_frequency> counter and curr_frequency > level):
            counter = curr_frequency
            num = i
 
    return num
    
pyautogui.FAILSAFE = False

Step1_Img = './img/step_1.png'
Step2_Img = './img/step_2.png'

ocr = PaddleOCR(use_angle_cls=True, lang="en") 

bounding_box = {'top': 205, 'left': 830, 'width': 260, 'height': 60}

listCodes = []

detect_start = 0

internet_speed = int(input("蓝光10M 请输入 1 \n蓝光4M 请输入 2 \n在虎牙网页端确认后并选择流畅播放的画质: "))

level = int(input("请输入识别等级 (从1到50, 数字越小识别准确率越低但同时速度也越快, 数字越大则反之, 建议值: 5): "))

STREAM_URL = get_real_url(internet_speed)

command = ['./ffmpeg/bin/ffmpeg.exe',
           '-i', STREAM_URL,
           '-f', 'image2pipe',
           '-pix_fmt', 'bgr24',
           '-loglevel','quiet',
           '-vcodec', 'rawvideo', '-an', '-']

width = 1920
height = 1080

p1 = subprocess.Popen(command, stdout=subprocess.PIPE)

while True:
    try:
        raw_frame = p1.stdout.read(width*height*3)

        if len(raw_frame) != (width*height*3):
            print('Error reading frame!!!') 

        frame = np.fromstring(raw_frame, np.uint8)
    
        frame = frame.reshape((height, width, 3))

        frame = frame[205:265, 830:1090]

        cv2.imshow('Press Q to quit', frame)
        detect_img = './img/detection.bmp'

        cv2.imwrite(detect_img,np.array(frame))

        result = ocr.ocr(detect_img, cls=True)

        code = [line[1][0] for line in result][0]
        score = [line[1][1] for line in result][0]

        if code != '' and len(code) == 12 and score != '0' and code.isalnum():

            if detect_start == 0:
                detect_start = time.time()
                

            listCodes.append(code)
                
            try:
                CDKey = most_frequent(listCodes,level)
                if str(CDKey) == '':
                    continue
                else:
                    print(CDKey)
                    duration_detect = str(time.time()-detect_start)
                    print("Detection Duration: " + duration_detect)

                    redeem_start = time.time()
                    redeem(CDKey)
                    duration_redeem = str(time.time()-redeem_start)
                    print("Redeem Process: " + duration_redeem)
                    break
            except Exception:
                pass
        
        p1.stdin.close()
        p1.wait()
    except Exception as e:
        #logging.error(traceback.format_exc())
        pass


    if (cv2.waitKey(1) & 0xFF) == ord('q'):
        cv2.destroyAllWindows()
        break
