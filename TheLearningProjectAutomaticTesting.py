
# coding: utf-8

# In[3]:


# 导包
from selenium import webdriver
import time
drive = webdriver.Chrome()
url = 'http://debug.2video.cn'
drive.get(url)
# 注册模块测试
try:
    element =  drive.find_element_by_xpath("//td[@width='570']//a[@href='/signup']")
except Exception as e:
    print('Can not find any element',format(e) )
element.click()
time.sleep(2)
# 1.表单填充
username = drive.find_element_by_xpath("//html//tr[1]/td[2]/input[1]")
username.send_keys('hello')
password = drive.find_element_by_xpath("//input[@type='password']")
password.send_keys('123456')
email = drive.find_element_by_xpath("//input[@type='email']")
email.send_keys('lidoudoou@gmail.com')
captche = drive.find_element_by_xpath("//html//tr[4]/td[2]/input[1]")

