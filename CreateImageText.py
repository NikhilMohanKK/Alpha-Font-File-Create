# -*- coding: utf-8 -*-
"""
Created on Fri Jan 11 06:11:43 2019

@author: KK NIKHIL MOHAN
"""

import os
import glob
from PIL import Image,ImageDraw, ImageFont

#Path variable indicates the location of the fonts in the windows OS
fontpath1="C:/Windows/Fonts/*.ttf"
fontpath2="C:/Windows/Fonts/*.otf"
#Path to store the image files in my system
path='D:/College Files/Vishal Project/Font Text Recog/Fonts/'

#This glob is used for taking all the names of the files available on the particular folder
files=glob.glob(fontpath1)+glob.glob(fontpath2)
for n in files:
    q=n.split("\\")
    r=q[1].split(".")
    flnm1=path+'/'+r[0]
    os.makedirs(flnm1)
    fnt = ImageFont.truetype(n, 35)
    #0-9
    for i in range(48,58):
        img = Image.new('RGB', (150, 100), color = 'white')
        img.save('pil_red.png')
        d = ImageDraw.Draw(img)
        #text image dimensions along with color and font and the text to be included
        d.text((60,20), "", font=fnt,fill=(0,0,0))
        d.text((60,20), chr(i), font=fnt,fill=(0,0,0))
        flnm=path+'/'+r[0]+'/'+chr(i)+'.png'
        img.save(flnm)
    #A-Z    
    for i in range(65,91):
        img = Image.new('RGB', (150, 100), color = 'white')
        img.save('pil_red.png')
        d = ImageDraw.Draw(img)
        d.text((60,20), "", font=fnt,fill=(0,0,0))
        d.text((60,20), chr(i), font=fnt,fill=(0,0,0))
        flnm=path+'/'+r[0]+'/U'+chr(i)+'.png'
        img.save(flnm)
    #a-z
    for i in range(97,123):
        img = Image.new('RGB', (150, 100), color = 'white')
        img.save('pil_red.png')
        d = ImageDraw.Draw(img)
        d.text((60,20), "", font=fnt,fill=(0,0,0))
        d.text((60,20), chr(i), font=fnt,fill=(0,0,0))
        flnm=path+'/'+r[0]+'/L'+chr(i)+'.png'
        img.save(flnm)