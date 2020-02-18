import os, html_sanitizer

def getList():
    sanitizer = html_sanitizer.Sanitizer()
    #data dir에 있는 값들을 가져옴
    files = os.listdir('data')
    listStr = ''
    for item in files:
        item = sanitizer.sanitize(item)
        listStr += '<li><a href="index.py?id={name}">{name}</a></li>'.format(name=item)
    return listStr
