from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth import views as auth_views

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'', include('blog.urls')),
    url(
        r'^login/', auth_views.login, {'template_name': 'blog/login.html'},
        name = 'login',
    ),
    url(
        r'^logout/', auth_views.logout, name = 'logout',
    ),
]
