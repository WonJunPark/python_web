#!C:\Users\dnjsw\Anaconda3\python.exe

import cgi, os

#id값 받기
form = cgi.FieldStorage()
pageId = form["pageId"].value

#파일 삭제
os.remove('data/'+pageId)

#redirection
print("Location: index.py")
print()
