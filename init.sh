#!/bin/bash

sudo rm -f /etc/nginx/sites-enabled/default
sudo ln -s /home/box/web/etc/nginx.conf  /etc/nginx/sites-enabled/test.conf
sudo /etc/init.d/nginx restart
sudo rm -f /etc/gunicorn.d/*
sudo ln -s /home/box/web/etc/gunicorn.conf /etc/gunicorn.d/gunicorn
sudo ln -s /home/box/web/etc/django.conf /etc/gunicorn.d/django

sudo /etc/init.d/gunicorn restart
#sudo /etc/init.d/mysql start
