
file_object=open('E:\\Chinese\\普通话\\set_word.txt','rt',encoding='utf-8')#gb2312/gb18030，
lines_seen = set()
for line in file_object:
    if len(line) >= 7 and len(line) <= 35 and line not in lines_seen:
        text_1 = open('E:\\Chinese\\普通话\\整理\\字数限制7-35\\set_word-limit-7-35.txt', 'a',encoding='utf-8')
        text_1.write(line)
        lines_seen.add(line)
        print(line)
file_object.close()
