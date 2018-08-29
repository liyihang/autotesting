
# coding: utf-8

# In[3]:


from PIL import Image
import pytesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Subtitle Edit\Tesseract\tesseract.exe'
# 导入图片
im = Image.open('./result/911.png')
# 灰度处理
image = im.convert('L')
# 二值化处理
threshold = 150
table = []
for i in range(256):
    if i < threshold:
        table.append(0)
    else:
        table.append(1)
out = image.point(table, '1')
img= pytesseract.image_to_string(out)
print(img)


# In[5]:


from PIL import Image
import pytesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Subtitle Edit\Tesseract\tesseract.exe'
# 导入图片
im = Image.open('3.png')
code= pytesseract.image_to_string(im)
print(code)

