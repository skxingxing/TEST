#!/usr/bin/python
# -*- coding: utf-8 -*-


import chardet

demo_str = "demo string".encode('utf-8')
print(demo_str)
print(chardet.detect(demo_str))
#print(chardet.detect(demo_str))

demo_str = "demo string".encode("gbk")
print(demo_str)
print(chardet.detect(demo_str))
demo_str = demo_str.decode("gbk").encode('utf-8')
print(demo_str)
print(chardet.detect(demo_str))