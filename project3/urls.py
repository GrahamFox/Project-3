"""project3 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from music import views
from accounts import views as accounts_views
from blog.views import post_list

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^logout/', accounts_views.logout, name='logout'),
    url(r'^register/', accounts_views.register, name='register'),
    url(r'^login/', accounts_views.login, name='login'),
    url(r'^profile/', accounts_views.profile, name='profile'),
    url(r'^music/', include('music.urls')),
    url(r'blog/', include('blog.urls')),
    url(r'^$', post_list, name='index'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
