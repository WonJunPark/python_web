#!C:\Users\dnjsw\Anaconda3\python.exe
print("content-type:text/html; charset=UTF-8\n")

import cgi, os

#data dir에 있는 값들을 가져옴
files = os.listdir('data')
listStr = ''
for item in files:
    listStr += '<li><a href="index.py?id={name}">{name}</a></li>'.format(name=item)

form = cgi.FieldStorage()
if 'id' in form:
    pageId = form["id"].value
    description = open('data/' + pageId ,'r').read()
    updata_link = '<a href="update.py?id={}">update</a>'.format(pageId)
else:
    pageId = 'welcome'
    description = 'hello web'
    updata_link = ''

print(
'''
<!doctype html>
<html>
<head>
  <title>WEB1 - html</title>
  <meta charset="utf-8">
</head>
<body>
  <h1><a href="index.py">WEB</a></h1>
  <ol>
    {listStr}
  </ol>
  <a href="create.py">create</a>
  {update_link}

  <h2>{title}</h2>
  <p>{desc}</p>
</body>
</html>
'''.format(title=pageId, desc = description, listStr = listStr, update_link=updata_link)
)
