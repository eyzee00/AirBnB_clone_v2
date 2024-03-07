#!/usr/bin/env bash
# sets up a webstatic


sudo apt update
sudo apt install -y nginx


sudo mkdir -p /data/web_static/shared/
sudo mkdir -p /data/web_static/releases/test/
echo "<html><head></head><body>Holberton School</body></html>" > /data/web_static/releases/test/index.html

ln -sf /data/web_static/releases/test/ /data/web_static/current

sudo chown -R ubuntu /data/
sudo chgrp -R ubuntu /data/

printf %s "server {
        listen  80 default_server;
        listen  [::]:80 default_server;
        root    /var/www/html;
        index   index.html;

	location /hbnb_static {
	alias /data/web_static/current;
	index index.html index.htm;
	}

        location /redirect_me {
        return 301 http://googl.com;
        }
        error_page 404 /404.html;
        location /404 {
        root /var/www/html;
        internal;
        }
}" > /etc/nginx/sites-available/default

sudo service nginx restart
