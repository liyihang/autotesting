
# coding: utf-8

# In[5]:


import requests
import os
import random
url = "http://debug.2video.cn//captcha/default"
root = r"C://Users\Administrator.ZXW-20170702ZMN/automaticTesting/result/"
i = 1
while i<10000: 
    path = root +str(random.randint(1,9999))+'.png'
    try:
        if not os.path.exists(root):
            os.mkdir(root)
        if not os.path.exists(path):
            r = requests.get(url)
            r.raise_for_status()
            #使用with语句可以不用自己手动关闭已经打开的文件流
            with open(path,"wb") as f: #开始写文件，wb代表写二进制文件
                f.write(r.content)
            print("爬取完成")
            i=i+1
            print(i)
        
        else:
            print("文件已存在")
            
    except Exception as e:
        print("爬取失败:"+str(e))
    


