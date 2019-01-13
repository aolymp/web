#!/bin/bash

sudo rm -f /etc/nginx/sites-enabled/default
sudo ln -s /home/box/web/etc/nginx.conf  /etc/nginx/sites-enabled/test.conf
sudo /etc/init.d/nginx restart
sudo rm -f /etc/gunicorn.d/*
sudo ln -s /home/box/web/etc/gunicorn.conf /etc/gunicorn.d/gunicorn
sudo ln -s /home/box/web/etc/django.conf /etc/gunicorn.d/django
sudo /etc/init.d/gunicorn restart
sudo /etc/init.d/mysql start
echo "create database ..."
mysql -uroot -e 'CREATE DATABASE `ural` CHARACTER SET utf8;'
mysql -uroot -e 'CREATE USER "portal"@"%" IDENTIFIED BY "m5portal";'
mysql -uroot -e 'GRANT ALL PRIVILEGES ON ural.* TO "portal"@"%";'
mysql -uroot -e 'FLUSH PRIVILEGES;'
