"""Bootlace - A simple Python app to send notifications via Pushover

Usage:
  bootlace -m MESSAGE -t TOKEN -u USER [options]
  bootlace --help

Options:
  -h, --help                       Show this help message and exit
  -m MESSAGE, --message=MESSAGE    The message to be conveyed
  -d DEVICE, --device=DEVICE       Override device name
  -T TITLE, --title=TITLE          Override message title [default: Bootlace]
  -t TOKEN, --token=TOKEN          Pushover application token
  -u USER, --user=USER             Pushover user token
"""

import docopt
import requests
import socket

url = 'https://api.pushover.net/1/messages.json'
keys = ['token', 'user', 'device', 'message', 'title']

args = docopt.docopt(__doc__)

if not args['--device']:
    args['--device'] = socket.gethostname()

constructed_message = {key: args['--'+key] for key in keys}

result = requests.post(url, constructed_message)
print(result)