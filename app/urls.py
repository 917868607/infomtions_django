# -*- coding: utf-8 -*-


from django.conf.urls import url
from .views import index,del_info,update_info,about_me

urlpatterns = [
    url(r'^about_me',about_me, name='about'),
    url(r'^update',update_info, name='update'),
    url(r'^del_info',del_info, name='del_info'),
    url(r'^$',index,name='index'),
]