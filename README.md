# bootlace
A simple Python app to send a push notification via the Pushover API.

Sign up for an account with Pushover, generate a user and app token. Specify these at run time like this:

    python bootlace.py -m "Message content" -t "Application token" -u "Pushover user token" -d "Override device name" -T "Override notification title"

## Usage

### Preperation
You will need a Pushover account, user token, and app token. 

1. Log in to your Pushover account and click `Create an Application/API Token`.

    ![CreateToken](https://i.imgur.com/8prNVpW.png)

2. Fill out the application information. All fields except "Name" are optional.
    
    ![NewApp](https://i.imgur.com/L7o0PUa.png)
    
3. Copy your new API Token
    
    ![APIToken](https://i.imgur.com/vssC4E6.png)
    
4. Copy your User Key

    ![UserKey](https://i.imgur.com/sN0JqTF.png)

### Installation
To use bootlace you'll need Python installed as well as the contents of `requirements.yaml`. Use the following commands to download Bootlace and install the required dependancies:
```
git clone https://github.com/IronicBadger/bootlace.git
cd bootlace
pip install -r requirements.txt
```
### Arguments
```
  -h, --help                        Show this help message and exit
  -m MESSAGE, --message=MESSAGE     The message to be conveyed
  -d DEVICE, --device=DEVICE        Override device name
  -T TITLE, --title=TITLE           Override message title [default: Bootlace]
  -t TOKEN, --token=TOKEN           Pushover application token
  -u USER, --user=USER              Pushover user token
  -p PRIORITY, --priority=PRIORITY  A value of -2, -1, 0 (default), 1, or 2
          # Only priority 1 or less is currently supported
  --html                            Set to '1' to enable HTML prasing of message
  --timestamp                       Replace timestamp of message receipt with time message was sent
  --url=URL                         Supplementary URL to include with message
          # URL MUST be complete and valid to open on receipient device
  --urltitle=URLTITLE               Title to override URL display in message
  --sound=SOUND                     Sound name to override default sound
          # See https://pushover.net/api#sounds for valid sound options
```

### Examples
-**Alert on server boot.** To do this, modify your crontab using `crontab -e` and add the following line

`@reboot python /path/to/bootlace.py -m "Server Booted" -t "Application token" -u "Pushover user token"`
