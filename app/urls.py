
from django.contrib import admin
from django.urls import path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from demo.views import index 
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index)
] + staticfiles_urlpatterns()
