from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^myquiz/', include('myquiz.urls')),
    url(r'^admin/', admin.site.urls),
]
