"""Bootlace - A simple Python app to send notifications via Pushover

Usage:
  bootlace -m MESSAGE -t TOKEN -u USER [options]
  bootlace --help

Options:
  -h, --help                        Show this help message and exit
  -m MESSAGE, --message=MESSAGE     The message to be conveyed
  -d DEVICE, --device=DEVICE        Override device name
  -T TITLE, --title=TITLE           Override message title [default: Bootlace]
  -t TOKEN, --token=TOKEN           Pushover application token
  -u USER, --user=USER              Pushover user token
  -p PRIORITY, --priority=PRIORITY  A value of -2, -1, 0 (default), 1, or 2. Only priority 1 or less is currently supported.
  --html                            Set to '1' to enable HTML prasing of message
  --timestamp                       Replace timestamp of message receipt with time message was sent
"""

import docopt
import requests
import socket
import time

url = 'https://api.pushover.net/1/messages.json'
keys = ['token', 'user', 'device', 'message', 'title', 'html', 'priority', 'timestamp']

args = docopt.docopt(__doc__)

if args['--html']:  #If HTML flag set, set value to '1' to enable HTML parsing of MESSAGE
    args['--html'] = 1

if args['--timestamp']: #If TIMESTAMP flag set, set value to current Unix time of host
    args['--timestamp'] = int(time.time())

if not args['--device']:  #If no device name provided, use Hostname
    args['--device'] = socket.gethostname()

constructed_message = {key: args['--'+key] for key in keys}

result = requests.post(url, constructed_message)
print(result)