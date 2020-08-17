from django.contrib import admin
from django.contrib.auth import views as auth_views # views for logins and logouts
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
# impor of all views from the users app
from users import views as user_views

# 'boss' urls.py reference/maps the blog/urls.py and that points to view methods like home()
urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', user_views.register, name='register'),
    path('profile/', user_views.profile, name='profile'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    # form for the user to fill out
    path('password-reset/', auth_views.PasswordResetView.as_view(template_name='users/password_reset.html'),
        name='password_reset'),
    # url for when the reset is done succesfully
    path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='users/password_reset_done.html'),
        name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='users/password_reset_confirm.html'),
        name='password_reset_confirm'),
    path('password-reset-complete/', auth_views.PasswordResetCompleteView.as_view(template_name='users/password_reset_complete.html'),
        name='password_reset_complete'),
    # reference/mapping to our blog.urls file when a user enters localhost/blog/ site
    # one reference/mapping will suffice to handle all urls from the blog app
    # first will be just an empty string '' that is the base of the blog app
    path('', include('blog.urls')),
]

# will allow the media to work with the browser
# the static media files location will be added if only in debug mode
# adding media url and media root to the urlpatterns
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
