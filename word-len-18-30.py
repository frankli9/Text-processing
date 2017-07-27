#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re


file_object=open('E:\\Chinese\\20170727缪姐项目\\抗战烽火之护国系统.txt','rt',encoding='utf-8')#gb2312/gb18030，
lines_seen = set()
a=re.findall('[\u4e00-\u9fa5]{18,30}',file_object.read())
for line in a:
    if line not in lines_seen:
        text_1 = open('E:\\Chinese\\20170727缪姐项目\\限制字数\\小说-1-limit18-30.txt', 'a',encoding='utf-8')
        text_1.write(line+'\n')
        lines_seen.add(line)
        # print(line)
    else:
        text_1 = open('E:\\Chinese\\20170727缪姐项目\\限制字数\\chongfu.txt', 'a', encoding='utf-8')
        text_1.write(line + '\n')
        print(line)
file_object.close()
#从文件中找出符合18到30个联系字的句子，并写入新文档，重复的句子写入另外一个文档

# myfile=open("1.txt")
# full=myfile.read()
# import re
# tgt=re.compile("kundi la( \w){1,7}")
# pop=[]
# m=tgt.search(full)
# while m:
#         pop.append(m.group(0)+"\n")
#         full=full.replace(m.group(0), "")
#         m=tgt.search(full)
# newfile=open("1_new.txt", "w")
# for full in pop:
#         newfile.write(full)