from django.conf.urls import include, url
from . import views
from django.contrib import admin 
urlpatterns = [
    url(r'^$', views.post_list),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^post/(?P<pk>[0-9]+)/$', views.post_detail, name='post_detail'),

]
