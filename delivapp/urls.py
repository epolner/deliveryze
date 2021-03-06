from django.conf.urls import patterns, url

from delivapp import views
from deliveryze import settings

urlpatterns = patterns('',
  url(r'^$', views.homepage, name='homepage'),
  url(r'^signup$', views.signup, name='signup'),
  url(r'^login$', views.login, name='login'),
  url(r'^logout$', views.logout, name='logout'),
  url(r'^done$', views.done, name='done'),
  url(r'^placeorder$', views.placeorder, name='placeorder'),
  url(r'^processing$', views.processing, name='processing'),
)

from django.contrib.staticfiles.urls import staticfiles_urlpatterns
urlpatterns += patterns('', (
    r'^static/(?P<path>.*)$',
    'django.views.static.serve',
    {'document_root': settings.STATIC_ROOT}
))
