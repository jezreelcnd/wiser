#User for Web
from django.conf.urls import url
from . import views
#use for REST
#from rest_framework import routers
from .api import LeadViewSet

#use for Web
urlpatterns = [
  url(r'^$', views.index, name='index'), #<---r'^$' is for root / will look for a method in views.py file call index
  url(r'^details/(?P<id>\d+)/$', views.details, name='details'),
  url(r'^idealweight/',views.IdealWeight),
  url(r'^asociateUser/',views.AsociateUser)
]

#use for REST
#router = routers.DefaultRouter()
#router.register('api/leads', LeadViewSet, 'leads')

#urlpatterns = router.urls