import requests
 
url = "https://api.pushover.net/1/messages.json"
 
data = {
        'token':'',
        'user':'',
        'device':'epsilon',
        'title':'Bootlace',
        'message':'Epsilon has booted!'
}
 
r = requests.post(url, data)
 
print r
