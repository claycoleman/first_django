"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings  
from django.conf.urls.static import static



urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    # url(pattern, view)
    url(r'^home/$', 'main.views.state_list', name="state_list"),

    url(r'^state_detail/(?P<pk>\d+)/$', 'main.views.state_detail', name='state_detail'),
    url(r'^city_list/$', 'main.views.city_search', name='city_search'),
    url(r'^city_detail/(?P<pk>\d+)/$', 'main.views.city_detail', name='city_detail'),
    url(r'^city_create/$', 'main.views.city_create', name='city_create'),
    url(r'^city_create/(?P<pk>\d+)/$', 'main.views.city_create', name='city_create'),
    url(r'^capital_detail/(?P<pk>\d+)/$', 'main.views.capital_detail', name='capital_detail'),
    url(r'^capital_list/$', 'main.views.capital_list', name="capital_list"),
    url(r'^logout/$', 'main.views.logout_user', name='logout'),
    url(r'^city_delete/(?P<pk>\d+)/$', 'main.views.city_delete', name ='city_delete'),
    url(r'^state_delete/(?P<pk>\d+)/$', 'main.views.state_delete', name='state_delete'),
    url(r'^contact_view/$', 'main.views.contact_view', name='contact_view'),
    url(r'^city_edit/(?P<pk>\d+)/$', 'main.views.city_edit', name='city_edit'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
