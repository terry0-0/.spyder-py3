# -*- coding: utf-8 -*-
"""
Spyderエディタ

これは一時的なスクリプトファイルです
"""

import time
import datetime
import smtplib, ssl
from selenium import webdriver
#from selenium.webdriver.support.ui import Text
from selenium.webdriver.support.ui import Select
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
#from email.mime.base import MIMEBase


def sendMail():
    port = 465  # For SSL
    # Create a secure SSL context
    context = ssl.create_default_context()
    
    with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
        server.login("terryooxx@gmail.com", 'Gamer08@')
        # TODO: Send email here
        # Add the From: and To: headers at the start!
        fromaddr = 'terryooxx@gmail.com'
        toaddr = 'terry0_0@hotmail.com'
        msg = ("From: %s\r\nTo: %s\r\n\r\nSubject:Chinese Gov Space!!!\r\n"
               % (fromaddr, ", ".join(toaddr)))
        
        server.set_debuglevel(1)
        server.sendmail(fromaddr, toaddr, msg)
        server.quit()

def send_mail(to_address, subject, body):
    smtp_user = "terryooxx@gmail.com"
    smtp_password = "ypbspynsrpbkinfk"
    server = "smtp.gmail.com"
    port = 587

    msg = MIMEMultipart("alternative")
    msg["Subject"] = subject
    msg["From"] = smtp_user
    msg["To"] = to_address
    msg.attach(MIMEText(body, "html"))
    s = smtplib.SMTP(server, port)
    #s.connect(server, port)
    s.ehlo()
    s.starttls()
    #s.ehlo()
    s.login(smtp_user, smtp_password)
    s.sendmail(smtp_user, to_address, msg.as_string())
    s.quit()

print ('import OK')
#send_mail("terry0_0@hotmail.com", "Chinese Gov Page Space!!!", "https://ppt.mfa.gov.cn/appo/page/reservation.html")
#driver = webdriver.Chrome()
#driver = webdriver.Chrome(executable_path='C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe')
#send_mail("dolphinyuan_8875@yahoo.co.jp", "Chinese Gov Page Space!!!", "https://ppt.mfa.gov.cn/appo/page/reservation.html")

driver = webdriver.Chrome(executable_path='C:\\Programing\\chromedriver_win32\\chromedriver.exe')

found = 0
for t in range(100000):
    print("=====================================================")
    dt_now = datetime.datetime.now()
    print(dt_now)
    print(t)

    #Open URL
    driver.get('https://ppt.mfa.gov.cn/appo/page/reservation.html')
    time.sleep(2)
    
    
    #click "继续未完成的申请预约"
    if (len(driver.find_elements_by_css_selector("#continueReservation")) > 0):
        driver.find_elements_by_css_selector("#continueReservation")[0].click()
        time.sleep(1)
    
    #############################
    if (len(driver.find_elements_by_css_selector("#showQueryHuifuMessage")) > 0):
                               
        #档 案 号
        dangAnHao = driver.find_elements_by_css_selector("#showQueryHuifuMessage")[0].find_elements_by_css_selector("#recordNumberHuifu")[0]
        dangAnHao.send_keys("202012250146934")
        #dangAnHao.send_keys("202012260251250")
        #验证问题
        yanZhengWenTi = Select(driver.find_elements_by_css_selector("#showQueryHuifuMessage")[0].find_elements_by_css_selector("#questionIDHuifu")[0])
        yanZhengWenTi.select_by_value("B17AD00AC5CB4C649FAABB0F8F13CAF8")
        #答     案
        daAn = driver.find_elements_by_css_selector("#showQueryHuifuMessage")[0].find_elements_by_css_selector("#answerHuifu")[0]
        daAn.send_keys("bentian")
        
        #submit
        tiJiao = driver.find_elements_by_css_selector("#showQueryHuifuMessage")[0].find_element_by_xpath("..").find_elements_by_css_selector("button")[1]
        tiJiao.click()
        time.sleep(1)
        
        #############################
        driver.find_elements_by_css_selector("#myButton")[0].click()
        time.sleep(1)
        
    ############################
    if (len(driver.find_elements_by_css_selector("#noMeetingTips")) > 0):
        queRen = driver.find_elements_by_css_selector("#noMeetingTips")[0].find_element_by_xpath("..").find_elements_by_css_selector("button")[1]
        queRen.click()


    for t2 in range(2):
        """
        if t % 2 == 0:
            driver.find_elements_by_css_selector(".ui-icon-circle-triangle-e")[0].click()
        else:
            driver.find_elements_by_css_selector(".ui-icon-circle-triangle-w")[0].click()
        """
        if (len(driver.find_elements_by_css_selector(".fc-header-title")) > 0):
            print(driver.find_elements_by_css_selector(".fc-header-title")[0].text)
        for span in driver.find_elements_by_css_selector('.fc-event-title'):
            print(span.text)
            space = span.text.split('/')
            if space[0] != space[1]:
                print("Chinese Gov Page Space!!!")
                send_mail("terry0_0@hotmail.com", "Chinese Gov Page Space!!!", "https://ppt.mfa.gov.cn/appo/page/reservation.html")
                send_mail("dolphinyuan_8875@yahoo.co.jp", "Chinese Gov Page Space!!!", "https://ppt.mfa.gov.cn/appo/page/reservation.html")
                span.click()
                found = 1
                break
        driver.find_elements_by_css_selector(".ui-icon-circle-triangle-e")[0].click()
        time.sleep(1)
    if (found == 1):
        break
