#########################
######## Linode #########
#########################
# for development we have been using a server provided by django


# starting 0.0.0.0:8000



Server Name: django-server
PW: HwPw for the Linode server

!!! Nod advised to log in as root !!!
ssh root@172.104.157.56

# log in as [user]
ssh [name]@172.104.157.56

# Linode server, used for login from the web to "grigorij"
user: grigorij == [name]
pw: v..e-{gb}
passfrase: MacBook pw

# exit the ssh connection: control a+d

# exit
exit
# should be run after first time logging to the linode server to update the apt-get binaries
apt-get update && apt-get upgrade

# set hostname of the machine
hostnamectl set-hostname [name] (hostnamectl set-hostname django-server)
# showing the hostname
hostname
# set the hostname in the hosts file by adding the ip adress provided by lonodes server
nano /etc/hosts (172.104.157.56  django-server)
# adding a limited user without root priviliges
adduser [name]
# assigning some root privileges to the user
# will add [user] to the sudo group and make running sudo commands by that user possible
adduser [name] sudo
# set up SSH key based authentification to log in without a password
# setting up ssh keys and firewalls

# create a .shh folder in the home directory
# -p flag > creating the whole directory tree
mkdir -p ~/.ssh

>>>> LOCAL MACHINE <<<<
ssh-keygen -b 4096

Your identification has been saved in /Users/grigorijschleifer/.ssh/id_rsa.
Your public key has been saved in /Users/grigorijschleifer/.ssh/id_rsa.pub.
# the public key will be stored on the server

# The key fingerprint is:
SHA256:OONqqMbmxduGyOp9RSRfMxCP2uZYiF0NcInjAFY/D2Y grigorijschleifer@Grigorijs-MBP.fritz.box


# Generating public/private rsa key pair.
passfrase: MacBook pw

# put the public key to the server
# public key from ~/.ssh/id_rsa.pub >>> linodes location at ~/.ssh/authorized_keys (new folder)
# no need to specify file extensions on linux
# !!!!!!!! the key inside id_rsa.pub should be the same as in authorized keys to log in !!!!!
scp ~/.ssh/id_rsa.pub grigorij@172.104.157.56:~/.ssh/authorized_keys


#### IN THE SERVER ####
# changing permissions for the user for the directory .ssh
# user, group and everyone else > 7 read/write and execute, 6 is just read and wri
sudo chmod 700 ~/.ssh/
# changing permissions for the file and assign the the rights for read/write
sudo chmod 600 ~/.ssh/*

####### Not allowing root logins and password authentifications ########
sudo nano /etc/ssh/sshd_config

PermitRootLogin yes >>> PermitRootLogin no
PasswordAuthentication yes >> PasswordAuthentication no

# After the modifications were made we need to restart the ssh service
sudo systemctl restart sshd

# setting up a firewall
# ufw == uncomplicated firewall
sudo apt-get install ufw
sudo ufw default allow outgoing
sudo ufw default deny incoming

# denieng all incoming trafic can cause server shutdown
# to prevent this we will allow ssh trafic
sudo ufw allow ssh
# for testing we will allow port 8000 for HTTP inqueries
# if testing is comleted we will allow HTTP over port 80
sudo ufw allow 8000
# enabling the rules
# only after allowing ssh, otherwise it will disrupt existing ssh connections
sudo ufw enable

# show status
udo ufw status

To                         Action      From
--                         ------      ----
22/tcp                     ALLOW       Anywhere << SSH
8000                       ALLOW       Anywhere
22/tcp (v6)                ALLOW       Anywhere (v6)
8000 (v6)                  ALLOW       Anywhere (v6)

##############################################
######## Pushin the project to Linode ########
##############################################
# if we used virtenv than we need to create a requirements.txt file with all dependencies
# we activate the environment for the django project
source ~/Desktop/Django/Environments/django_env/bin/activate

# creating a requirements.txt file
# this will create a requirements.txt file in the pwd location you are at
pip freeze > requirements.txt
# copy the project to linode we go to Desctop or where the
# -r flag is used for copying a directory
# :~/ will copy the content to the home directory of the user
scp -r django_project [grigorij]@172.104.157.56:~/


#### preparation #####
sudo apt-get install python3-pip # to use pip we will need to type pip3
sudo apt-get install python3-venv
# create virtual environment inside the django project folder on our server
python3 -m venv django_project/venv
# installing packages from requirements.txt
# -r flag used to install the txt file
pip istall -r requirements.txt

# inside the settings.py file of our project add server ip und location of our static files
# ALLOWED_HOSTS = [...]
# STATIC_ROOT = os.path.join(BASE_DIR, 'static')
python manage.py collectstatic # this will create a static folder inside the project

# after activating the venv from inside the django django_project
# and connecting to Linode via ssh
source django_project/bin/activate
# we can run a dev server under 0.0.0.0:8000
python manage.py runserver 0.0.0.0:8000
# the site can then be reached under the adress 172.104.157.56:8000
