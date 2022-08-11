import cv2
import time
import numpy as np
from mss import mss
import pyautogui
from python_imagesearch.imagesearch import imagesearch_loop, imagesearch
from paddleocr import PaddleOCR, draw_ocr

def most_frequent(List):

    counter = 0
    num = ''
     
    for i in List:
        curr_frequency = List.count(i)
        if(curr_frequency> counter and curr_frequency > 4):
            counter = curr_frequency
            num = i
 
    return num
    
pyautogui.FAILSAFE = False
TIMELAPSE = 1

Step1_Img = './img/step_1.png'
Step2_Img = './img/step_2.png'

ocr = PaddleOCR(use_angle_cls=True, lang="en") 

bounding_box = {'top': 205, 'left': 830, 'width': 260, 'height': 60}

sct = mss()

count = 0

time_list = []

code = []

counter = 5

while True:
    sct_img = sct.grab(bounding_box)
    cv2.imshow('screen', np.array(sct_img))

    pyautogui.position()

    filename = './img/detection.png'
    cv2.imwrite(filename, np.array(sct_img))

    result = ocr.ocr(filename, cls=True)
    
    try:
        possible_code = [line[1][0] for line in result][0]
        if possible_code != '' and len(possible_code) == 12:
            corrected_code = possible_code.replace("0","D").replace("O",'Q')
            print("Possible Code: " + corrected_code)
            code.append(corrected_code)
            try:
                if str(most_frequent(code)) == '':
                    continue
                else:
                    print("Most Frequent: " + most_frequent(code))
                step1 = imagesearch(Step1_Img, 0.8)
                if counter == 0:
                    break

                if not step1[0] == -1:
                    print("claming cdk...")
                    pyautogui.click(step1[0], step1[1])
                    pyautogui.write(str(most_frequent(code)))
                    time.sleep(0.5)
                    step2 = imagesearch(Step2_Img, 0.8)
                    if not step2[0] == -1:
                        pyautogui.click(step2[0], step2[1])
                        counter -= 1
            except Exception:
                pass
    except Exception:
            pass


    if (cv2.waitKey(1) & 0xFF) == ord('q'):
        cv2.destroyAllWindows()
        break
