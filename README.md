# bootlace
A simple Python app to send a push notification via the Pushover API.

Sign up for an account with Pushover, generate a user and app token. Specify these at run time like this:

    python bootlace.py -m "Message content" -t "Application token" -u "Pushover user token" -d "Override device name" -T "Override notification title"

For example I use this app when my server boots to ping me a notification (on Linux ofc). To do this, modify your crontab using `crontab -e` and add the following line `@reboot python /path/to/bootlace.py`. 
