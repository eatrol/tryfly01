

# https://script.google.com/macros/s/AKfycbzMV9ibMX0QfRcYZiwZpPWmfcIRC5KxTOrjYehg0w/dev?type=select&order_no=1

import requests as req
import urllib.request as request
import json

src = "http://127.0.0.1:8000/jsontoeic/"

with request.urlopen(src) as response:
    data = json.load(response) # use json module to read json format data


data = json.loads(data)
for member in data:
    name  = member["fields"]["name"]
    url = member["fields"]["sound"]
    file = req.get(url, allow_redirects=True)   
    open(name+".mp3", 'wb').write(file.content)
    print(name)
    




# url = 'https://s.yimg.com/bg/dict/dreye/live/m/abounding.mp3'
# file = req.get(url, allow_redirects=True)
# open('abounding.mp3', 'wb').write(file.content)