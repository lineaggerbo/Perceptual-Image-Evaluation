from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<scene_id>[0-9]+)/$', views.scene, name='scene'),
    url(r'^end/$', views.end, name='end'),
] 