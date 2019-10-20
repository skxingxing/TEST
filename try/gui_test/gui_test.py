import easygui as g
import os

if g.ccbox("okokpok","hudong"):
    pass
filePath=g.fileopenbox('.txt')
#此处根据实际情况,进行字符编码设计
with open(filePath) as f:
    title=os.path.basename(filePath)
    msg='文件%s的内容如下：'%title
    txt=f.read()
    g.textbox(title,msg,txt)
