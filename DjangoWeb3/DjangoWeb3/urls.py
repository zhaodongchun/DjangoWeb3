"""
Definition of urls for DjangoWeb3.
"""

from django.conf.urls import include, url
from django.contrib import admin
from  learning_logs  import views

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = [
    # Examples:
    # url(r'^$', DjangoWeb3.views.home, name='home'),
    # url(r'^DjangoWeb3/', include('DjangoWeb3.DjangoWeb3.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
     url(r'^admin/', include(admin.site.urls)),
    # url(r'^index/$', views.index, name='index'),
     url(r'', include('learning_logs.urls',namespace='learning_logs')),


]
