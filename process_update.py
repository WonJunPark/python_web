#!C:\Users\dnjsw\Anaconda3\python.exe

import cgi, os

#id값 받기
form = cgi.FieldStorage()
pageId = form["pageId"].value
title = form["title"].value
description = form["description"].value

#파일에 저장
opened_file = open('data/'+pageId,'w')
opened_file.write(description)
opened_file.close()

os.rename('data/'+pageId, 'data/'+title)

#redirection
print("Location: index.py?id="+title)
print()
