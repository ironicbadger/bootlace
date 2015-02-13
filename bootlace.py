# Bootlace - A simple Python app to send notifications via Pushover
#
# Author - Alex Kretzschmar

from optparse import OptionParser
import socket
import requests
import sys

url = 'https://api.pushover.net/1/messages.json'
token = None
user = None
device = socket.gethostname()
message = None
title = 'Bootlace'

parser = OptionParser()
parser.add_option("-m", "--message", dest="message",
                help="The message to be conveyed")
parser.add_option("-d", "--device", dest="device",
                  help="(Optional) Override device name")
parser.add_option("-T", "--title", dest="title",
                  help="(Optional) Override message title")
parser.add_option("-t", "--token", dest="token",
                  help="Pushover application token")
parser.add_option("-u", "--user", dest="user",
                  help="Pushover user token")

option, content = parser.parse_args()

if option.message:
    message = option.message
if option.device:
    device = option.device
if option.title:
    title = option.title
if option.token:
    token = option.token
if option.user:
    user = option.user

fields = (token, user, device, message, title)

for f in fields:
    if not f:
        print('Required field not supplied.')
        sys.exit(2)

# Construct message using specified data

constructed_message = {
        'token':token,
        'user':user,
        'device':device,
        'title':title,
        'message':message
}

# Send message using constructed message
print constructed_message
result = requests.post(url, constructed_message)
print result