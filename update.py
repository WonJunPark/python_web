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
else:
    pageId = 'welcome'
    description = 'hello web'

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
  <!-- method는 기본적으로 get방식 -->
  <!-- get방식은 query string을 이용함 -->
  <form action="process_create.py" method="post">
      <p><input type="text" name="title" placeholder="title"
      value="{form_default_title}"></p>
      <p><textarea rows="4" name="description" placeholder="description">
      {form_default_description}</textarea></p>
      <p><input type="submit"></p>
  </form>

</body>
</html>
'''.format(title=pageId, desc = description, listStr = listStr,
form_default_title = pageId,
form_default_description = description)
)
