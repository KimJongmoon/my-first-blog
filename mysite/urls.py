from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth import views as auth_views
from blog.views import post_list
from django.conf import settings
from django.conf.urls.static import static

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
    url(r'^post/(?P<pk>[0-9]+)/$', post_list, name = 'post_list'),
]
urlpatterns += static('upload_files', document_root=settings.MEDIA_ROOT)
