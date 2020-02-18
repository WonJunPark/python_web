#!C:\Users\dnjsw\Anaconda3\python.exe
print("content-type:text/html; charset=UTF-8\n")

import cgi, os, view, html_sanitizer

sanitizer = html_sanitizer.Sanitizer()

form = cgi.FieldStorage()
if 'id' in form:
    title = pageId = form["id"].value
    description = open('data/' + pageId ,'r').read()
    title = sanitizer.sanitize(title)
    description = sanitizer.sanitize(description)
    updata_link = '<a href="update.py?id={}">update</a>'.format(pageId)
    delete_action = '''
        <form action = "process_delete.py" method = "post">
            <input type = "hidden" name = "pageId" value = "{}">
            <input type = "submit" value = "delete">
        </form>
    '''.format(pageId)
else:
    pageId = 'welcome'
    description = 'hello web'
    updata_link = ''
    delete_action = ''

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
  {delete_action}

  <h2>{title}</h2>
  <p>{desc}</p>
</body>
</html>
'''.format(title=pageId,
            desc = title,
            listStr = view.getList(),
            update_link=updata_link,
            delete_action=delete_action)
)
