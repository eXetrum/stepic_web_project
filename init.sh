sudo ln -sf /home/box/web/etc/nginx.conf /etc/nginx/sites-enabled/test.conf
sudo rm -rf /etc/nginx/sites-enabled/default
sudo /etc/init.d/nginx restart
sudo ln -sf /home/box/web/etc/gunicorn.conf   /etc/gunicorn.d/wsgi.example
sudo service gunicorn restart
sudo /etc/init.d/gunicorn restart
﻿sudo /etc/init.d/mysql start﻿