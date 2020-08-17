# setting up an apache2 server instead a django provided server
https://www.youtube.com/watch?v=Sa_kQheCnds&list=PL-osiE80TeTtoQCKZ03TU5fNfx2UY6U4p&index=13

# setting up apache and WSGI
sudo apt-get install apache2
sudo apt-get install libapache2-mod-wsgi-py3

# configuring apache Server
# inside the sites-available directory are apache configuration files located
cd /etc/apache2/sites-available/
# copying the 000-default.conf file to django_project.conf to the same location
sudo cp 000-default.conf django_project.conf
# aditing the configuration file
sudo nano django_project.conf

####################################
#### configuring APACHE server #####
####################################
# this should go to
Alias /static /home/grigorij/django_project/static # map apache requests to our static apps folder

<Directory /home/grigorij/django_project/static> # adding permissions
    Require all granted
</Directory>

Alias /media /home/grigorij/django_project/media # map apache requests to our media apps folder

<Directory /home/grigorij/django_project/media>
    Require all granted
</Directory>

<Directory /home/grigorij/django_project/django_project> # granting access for apache to access the wsgi.py file
    <Files wsgi.py> # this is how our app will talk to our web server
        Require all granted
    </Files>
</Directory>

WSGIScriptAlias / /home/grigorij/django_project/django_project/wsgi.py # go to the base of our project and find the wsgi.py file that is located in home/grigorij/django_project/django_project
# django_app is just a random name for the daemon process
# python-path is the locatio of the projec Directory, no spaces between the = sign
# python-home is the location of the virtual environment
WSGIDaemonProcess django_app python-path=/home/grigorij/django_project python-home=/home/grigorij/django_project/venv>
# the process group shoulb be equaly named as the Daemonprocess
WSGIProcessGroup django_app
####################################
#### configuring APACHE server #####
####################################

# enabling the changes and apache
sudo a2ensite django_project # a2 = apache, en = enable, site = site
# before activation of of our site we should deactivate the default site
sudo a2dissite 000-default.conf

# to change the database configurations we need to grant apache access to the sqlite3 direction and so the access to the database itself
# we want to change sqlite3 to postgres and to do so apache needs to be able to read and write to this location
# apache (:www-data) will be the group owner of the file/database
sudo chown :www-data django_project/db.sqlite3
# after changing/assigning the group owner we change the permissions
sudo chmod 664 django_project/db.sqlite3
# on top we will change the owner of the django_project to apache aka :www-data
# drwxr-xr-x 8 grigorij www-data 4096 May  5 19:47 django_project > grigorij is the owner but the group is www-data aka apache
sudo chown :www-data django_project/
sudo chmod 775 django_project # !!!!!! This was the problem !!!!!!

# to give apache permissions to upload and change the media folder
sudo chown -R :www-data django_project/media
sudo chmod -R 775 django_project/media

# we will create a config file for storing all global variables
sudo touch /etc/config.json

{
        "SECRET_KEY": "vbyzuw@*qriuk6prdjdqt((jm9x1!#+z%4i#gg2^udzcth!qe)",
        "EMAIL_USER": "chaosambulance@googlemail.com",
        "EMAIL_PASS": "rimn xjkl vfbl rcyj"
}


# first we grab the secret key from our settings.py file
# adding the secret key, email and google generated password to that file
# inside the setting file on the lidone server we will substitute the key, email and password information
# we will use the json file that we load from the config.file
# the json file is loaded as a dictionary and the keys can be accessed as ususal
import json

with open('/etc/config.json') as config_file:
    config = json.load(config_file)

SECRET_KEY = config['SECRET_KEY']
EMAIL_HOST_USER = config.get('EMAIL_USER')
EMAIL_HOST_PASSWORD = config.get('EMAIL_PASS')

# before going live we have to disallow the 8000 port
sudo ufw delete allow 8000
# and allowing http traffic
sudo ufw allow http/tcp
# restart apache service
# use it always after implementing some changes
sudo service apache2 restart
