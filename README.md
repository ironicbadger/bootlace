# bootlace
A simple Python app to send a push notification via the Pushover API.

Sign up for an account with Pushover, generate a user and app token. Fill these into the app.

For example I use this app when my server boots to ping me a notification (on Linux ofc). To do this, modify your crontab using `crontab -e` and add the following line `@reboot python /path/to/bootlace.py`. 
