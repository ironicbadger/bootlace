# bootlace
A simple Python app to send a push notification via the Pushover API.

Sign up for an account with Pushover, generate a user and app token. Specify these at run time like this:

    python bootlace.py -m "Message content" -t "Application token" -u "Pushover user token" -d "Override device name" -T "Override notification title"

## Usage

### Preperation
You will need a Pushover account, user token, and app token. 

1. Log in to your Pushover account and click `Create an Application/API Token`.

    ![CreateToken](https://i.imgur.com/8prNVpW.png)

2. Fill out the application information. All field except "Name" are optional.
    
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
    
### Examples
-**Alert on server boot.** To do this, modify your crontab using `crontab -e` and add the following line

`@reboot python /path/to/bootlace.py -m "Server Booted" -t "Application token" -u "Pushover user token"`
