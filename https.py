apachectl configtest # will result in syntax error detection
sudo apachectl configtest # no syntax errors

# don't forget to allow https traffic
sudo ufw allow https
# and then restart the apache server
sudo service apache2 restart

sudo apt-get update
sudo apt-get install software-properties-common
sudo add-apt-repository universe
sudo add-apt-reposity ppa:certbot/certbot
sudo add-apt-repository ppa:certbot/certbot
sudo apt-get update
sudo apt-get install python-certbot-apache

# change servername to my domain and comment stuff
sudo nano /etc/apache2/sites-available/django_project.conf

# grigorij.schleifer@ukbonn.de
sudo certbot --apache

Saving debug log to /var/log/letsencrypt/letsencrypt.log
Plugins selected: Authenticator apache, Installer apache

Which names would you like to activate HTTPS for?
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
1: www.einfachsono.de
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
Select the appropriate numbers separated by commas and/or spaces, or leave input
blank to select all options shown (Enter 'c' to cancel):

# /etc/apache2/sites-available/django_project-le-ssl.conf file created
# almost the same as the django_project.conf file but different port on 443 instead of 80

Obtaining a new certificate
Performing the following challenges:
http-01 challenge for www.einfachsono.de
Enabled Apache rewrite module
Waiting for verification...
Cleaning up challenges
Created an SSL vhost at /etc/apache2/sites-available/django_project-le-ssl.conf
Enabled Apache socache_shmcb module
Enabled Apache ssl module
Deploying Certificate to VirtualHost /etc/apache2/sites-available/django_project-le-ssl.conf
Enabling available site: /etc/apache2/sites-available/django_project-le-ssl.conf

Please choose whether or not to redirect HTTP traffic to HTTPS, removing HTTP access.
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
1: No redirect - Make no further changes to the webserver configuration.
2: Redirect - Make all requests redirect to secure HTTPS access. Choose this for
new sites, or if you're confident your site works on HTTPS. You can undo this
change by editing your web server's configuration.
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
Select the appropriate number [1-2] then [enter] (press 'c' to cancel): 2

IMPORTANT NOTES:
 - Congratulations! Your certificate and chain have been saved at:
   /etc/letsencrypt/live/www.einfachsono.de/fullchain.pem
   Your key file has been saved at:
   /etc/letsencrypt/live/www.einfachsono.de/privkey.pem
   Your cert will expire on 2020-09-25. To obtain a new or tweaked
   version of this certificate in the future, simply run certbot again
   with the "certonly" option. To non-interactively renew *all* of
   your certificates, run "certbot renew"

# deleted the alisase and WSGI settings inside the /etc/apache2/sites-available/django_project.conf file
# uncommented the WSGI settings in /etc/apache2/sites-available/django_project-le-ssl.conf


# Renewing certificates every 90 days
# dry run
sudo certbot renew --dry-run

# chrontab automatic setup
sudo chrontab -e
# choosing an editor and adding
# run the command at 3:40 on 1 once a month no matter what day
40 3 1 * * sudo certbot renew --quiet
