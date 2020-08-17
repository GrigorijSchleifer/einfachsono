NewUser...
abc123.,-...

admin username:
grigorijschleifer
password:
h...p

##########################
######## virtenv #########
##########################
# creates a virtual environment inside a predefined directory
virtenv name_project
# activates the environment
source name_project/bin/activate




#######################################
############ PROJECT CREATION #########
#######################################

-- start virtual environment (from the folder that contains the files of the virtenv) --
source django_env/bin/activate

-- create a project --
django-admin startproject namevvv

-- create
django-admin startapp name

-- start server --
python manage.py runserver

-- collects all static files into the main application
-- every time one would add some static files this command needs to be executed
python manage.py collect static


#######################################
############ MIGRATIONS ###############
#######################################

-- update the database and add auth_user to the database so that we can create a superuser
-- no changes detected will be displayed if no changes were made to the database
-- will just make the migrations but will not apply those migrations
python manage.py makemigrations

-- applies the migrations to the database
python migrate.py migrate

-- shows sql code that is run on the database
python manage.py sqlmigrate appname migrations_file_filenumber


#############################################
############ CREATE SUPERUSER ###############
#############################################

-- update the database and add auth_user to the database so that we can create a superuser
-- no changes detected will be displayed if no changes were made to the database
-- will just make the migrations but will not apply those migrations
python manage.py makemigrations

-- applies the migrations to the database
python migrate.py migrate

-- creates superuser after the migrations are completed
python manage.py createsuperuser

    >> grigorijschleifer
    >> grigorij.schleifer@outlook.com
    >> Hw ps

---- Keyboard ----

##################################
############ SHELL ###############
##################################

python manage.py shell

from blog.models import Post -- imports the Post table/model
from django.contrib.auth.models import User -- imports the User table/model

-- list all Users in the User table
User.objects.all()
User.objects.first()
User.objects.last()

-- filtering Users
User.objects.filter(username='grigorijschleifer')
User.objects.filter(username='grigorijschleifer').first() -- will return only the user instead of a QuerySet

User.objects.get(id=1) -- will get the the user with that id

Post.objects.all() - if no posts are generated yet, it should return an empty QuerySet
user = User.objects.filter(username='grigorijschleifer').first()
user = User.objects.get(id=1) -- same as above

-- will get all posts that the user has created
user.post_set.all()



####################
post_1 = Post(title='Blog 1', content='First Post comment', author=user) -- date will be autogenerated for us
post_1.save()

post_2=Post(title='Blog 2', content='Second Post content', author_id=user.id)
post_2.save()

post = Post.objects.all().first()
post.title
post.content
post.date_posted
post.author
post.author.email

-- to crearte a post directly, no saving needed
user.post_set.create(title='Post 3', content='Third Post Content')

################## access the profile of a user
from django.contrib.auth.models import User
user = User.objects.filter(username='grigorijschleifer').first()
user.profile # returns the entire Profile
user.profile.image # gets the image
user.profile.image.width/height/size
user.profile.image.url # direct location of the image to use it in the <img> "src" tag


######################################
############ PAGINATOR ###############
######################################

import json

from blog.models import Post
with open('posts.json') as f:
    posts_json = json.load(f)

for post in posts_json:
    post = Post(title=post['title'], content = post['content'], author_id = post['user_id'])
    post.save()

from django.core.paginator import Paginator
posts = ['1', '2', '3', '4', '5']
p = Paginator(posts, 2) # displaying only two posts per page
p.num_pages # will return 3 pages because posts counts 5 posts and one will be left on the third page

# will loop and print all pages
for page in p.page_range:
...     print(page)

# assigning pages to variables
p1 = p.page(1) # <Page 1 of 3>
p1.number # will return the number of that page and not the thing above
p1.object_list # returns a list of objects on that page
p1.has_previous() # method to check if there is a previous page
p1.has_next()
p1.has_next_number()

>>> from django.core.paginator import Paginator
>>> posts = ['1', '2', '3', '4', ]
>>>
>>> posts = ['1', '2', '3', '4', '5']
>>> posts
['1', '2', '3', '4', '5']
>>> p = Paginator(posts, 2)
>>> p.num_pages
3
>>> for page in p.page_range:
...     print(page)
...
1
2
3
>>> p1 = p.page(1)
>>> p1
<Page 1 of 3>
>>> p1.number
1
>>> p1.object_list
['1', '2']
>>> p1.has_previous()
False
>>> p1.has_next()
True
>>> p1.next_page_number()
2
