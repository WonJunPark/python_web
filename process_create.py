#!C:\Users\dnjsw\Anaconda3\python.exe

import cgi

#id값 받기
form = cgi.FieldStorage()
title = form["title"].value
description = form["description"].value

#파일에 저장
opened_file = open('data/'+title,'w')
opened_file.write(description)
opened_file.close()

#redirection
print("Location: index.py?id="+title)
print()
