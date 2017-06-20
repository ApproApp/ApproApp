"""
Definition of urls for ApproApp.
"""

from django.conf.urls import url, include


from ApproApp.Core import views

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = [
    # Examples:
    url(r'^$', views.home, name='home'),
    # url(r'^ApproApp/', include('ApproApp.ApproApp.urls')),
    # url(r'^mongonaut/', include('mongonaut.urls')),
    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', admin.site.urls),
]


