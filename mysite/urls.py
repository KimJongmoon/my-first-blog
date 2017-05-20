from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.conf import settings

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'', include('blog.urls')),
    url(
        r'^accounts/login/',
        auth_views.login,
        name = 'login',
        kwargs={
            'template_name': 'login.html'
        }
    ),
    url(
        r'^accounts/logout/',
        auth_views.logout,
        name = 'logout',
        kwargs={
            'next_page': settings.LOGIN_URL,
        }
    ),
]
