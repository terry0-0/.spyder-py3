# -*- coding: utf-8 -*-
"""
Spyderエディタ

これは一時的なスクリプトファイルです
"""

import time
import base64
import os
from selenium import webdriver

print ('import OK')

#driver = webdriver.Chrome()
driver = webdriver.Chrome(executable_path='C:\\Programing\\chromedriver_win32\\chromedriver.exe')
driver.get('http://hero.d.163.com/?page=0')
time.sleep(2)

cmd = input()

#話数
for wasu in range(1, 6):
    print("話数：" + str(wasu))
    
    #canvasList = driver.find_elements_by_css_selector("canvas")
    canvasList = driver.find_elements_by_css_selector(".page-image")

    print("ページ数：" + str(len(canvasList)))
    #page number
    page_number = 0
    for canvas in canvasList:
        page_number += 1

        try:
            #canvas = canvasList[0]
            #print(canvas.get_attribute("width"))
            # get the canvas as a PNG base64 string
            canvas_base64 = driver.execute_script("return arguments[0].toDataURL('image/png').substring(21);", canvas)

            # decode
            canvas_png = base64.b64decode(canvas_base64)

            # save to a file
            os.makedirs(str(wasu).zfill(3), exist_ok=True)
            file_name = str(wasu).zfill(3) + "\\" + str(page_number).zfill(3) + ".jpg"
            print(file_name)
            with open(file_name, 'wb') as f:
                f.write(canvas_png)
        except:
            print("Error!")
        finally:
            try:
                driver.find_elements_by_css_selector(".js-slide-forward")[0].click()
            except:
                print("slide error!")
            
    #time.sleep(2)   
    next_link = driver.find_elements_by_css_selector(".next-link")
    print(next_link)
    next_link[0].click()
#driver.quit()