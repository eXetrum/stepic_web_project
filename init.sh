#!/bin/sh

WORK_DIR="/home/box"
PROJ_DIR="$WORK_DIR/web"
NGINX_DIR="/etc/nginx"
GUNICORN_DIR="/etc/gunicorn.d"

# nginx
sudo ln -sf $PROJ_DIR/etc/nginx.conf $NGINX_DIR/sites-enabled/nginx.conf
sudo rm -rf $NGINX_DIR/sites-enabled/default
sudo /etc/init.d/nginx restart

# gunicorn
sudo rm -f $GUNICORN_DIR/*
sudo ln -sf $PROJ_DIR/etc/hello.conf $GUNICORN_DIR/hello.conf
sudo ln -sf $PROJ_DIR/etc/ask.conf $GUNICORN_DIR/ask.conf
sudo service gunicorn restart
sudo /etc/init.d/gunicorn restart


# MySQL
﻿sudo /etc/init.d/mysql start