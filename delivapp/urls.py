from django.conf.urls import patterns, url

from delivapp import views

urlpatterns = patterns('',
  url(r'^$', views.homepage, name='homepage'),
  url(r'^signup$', views.signup, name='signup'),
  url(r'^login$', views.login, name='login'),
  url(r'^done$', views.done, name='done'),
  url(r'^placeorder$', views.placeorder, name='placeorder'),
  url(r'^processing$', views.processing, name='processing'),
)
