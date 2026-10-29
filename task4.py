import json

inData = '{"one": ["http", "[yandex.ru](http://yandex.ru/)"], "two": ["https", "[google.com](http://google.com/)"]}'

outData = json.loads(inData)