import easygui as g
import os
msg='浏览文件并打开'
title='测试'
default='D:\*'
fileType='全部文件'
filePath=g.fileopenbox(msg,title,default,fileType)
#此处根据实际情况,进行字符编码设计
with open(filePath,encoding='utf-8', errors='ignore') as f:
    title=os.path.basename(filePath)
    msg='文件%s的内容如下：'%title
    txt=f.read()
    g.textbox(title,msg,txt)

