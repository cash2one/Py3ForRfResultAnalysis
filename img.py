#-*- coding:utf-8 -*-
__auth = '吕梓清'

import os, io, sys, re, time, json, random
from PIL import Image,ImageEnhance,ImageFile,ImageDraw,ImageFont
from time import ctime


class img(object):
    def __init__(self,file,num,Roadking):
        self.lj = file
        self.num = num
        self.Roadking = Roadking
        print(self.lj,self.num,self.Roadking)

    def img(self):
        tt = 'Auth:xiaoyaojjian'.encode('utf-8').decode("latin1")
        im = Image.open(self.lj)
        text = time.ctime()
        width, height = im.size
        textImaggeW = int(width * 1.5)
        textImaggeH = int(height * 1.5)
        txt = Image.new('RGB', im.size, (0, 0, 0, 0))
        FONT = "C:\\Windows\\Fonts\\COOPBL.TTF"
        size = 2

        n_font = ImageFont.truetype(FONT, size)  # 得到字体
        n_width, n_height = n_font.getsize(text)
        text_box = min(txt.size[0], txt.size[1])

        while (n_width + n_height < text_box):
            size += 2
            n_font = ImageFont.truetype(FONT, size=size)
            n_width, n_height = n_font.getsize(text)
            print(n_width, n_height)

        text_width = (txt.size[0] - n_width)/2
        text_height = (txt.size[1] - n_height)/2
        # watermark = watermark.resize((text_width,text_height), Image.ANTIALIAS)
        draw = ImageDraw.Draw(txt, 'RGBA')  # 在水印层加画笔
        draw.text((text_width, text_height),
                  tt, font= n_font, fill=('#21ACDA'))
        watermark = txt.rotate(23, Image.BICUBIC)

        alpha = watermark.split()[2]

        alpha = ImageEnhance.Brightness(alpha).enhance(0.50)
        watermark.putalpha(alpha)

        # txt = Image.new('RGBA', im.size, (0, 0, 0, 0))
        # fnt = ImageFont.truetype("COOPBL.TTF",19)


        d = ImageDraw.Draw(txt)

        # Font = ImageFont.truetype(k)
        text = time.ctime()

        d.text([400, 400], tt, fill=(255, 255, 255, 255))
        # print [(textImaggeW-400)/2,(textImaggeH-textH)/2]

        # out = Image.alpha_composite(im, txt)
        #
        # out.show()

        # a = 'C:\\Users\\Administrator\\Desktop\\'+str(time.time())+'.jpg'
        a = self.Roadking + u'测试图片' + str(self.num) + '.jpg'
        # im.save(a)
        Image.composite(watermark, im, watermark).save(a)
        return a, a