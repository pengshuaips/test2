#!/usr/bin/python
# -*- coding: UTF-8 -*-

try:
    fh = open("C:/Intel/ExtremeGraphics/CUI/Resource/testfile.txt", "w")
    fh.write("这是一个测试文件，用于测试异常!!")
except IOError:
    print "Error: 没有找到文件或读取文件失败"
else:
    print "内容写入文件成功"
    fh.close()
