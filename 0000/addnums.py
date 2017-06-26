# -*- coding: utf-8 -*-
"""
Created on Mon Jun 26 23:51:06 2017

@author: vendy
"""

# 导入PIL中的图像、画图和字体模块
from PIL import Image, ImageDraw, ImageFont

# 定义函数,num默认为1
def add_num(imgfilepath,num=1):
    '''
    (str) -> ('saved_img.jpg')
    Return the imgfile with some digits
    '''
    
    # 加载图像，定义字体和字体大小

    img = Image.open(imgfilepath)

    fontsize = img.size[1]/2

    font = ImageFont.truetype("msyh.ttf",fontsize)

    # 作图
    
    draw = ImageDraw.Draw(img)
    
    draw.text((fontsize*2,0),str(num),font=font,fill='red')

    # 显示效果
    img.show()

    # 保存

    img.save('saved_img.jpg')

if __name__ == "__main__":
    imgfilepath = '0.jpg'
    num = '6'
    add_num(imgfilepath,num)