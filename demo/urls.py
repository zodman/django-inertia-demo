
from django.urls import path
from demo.views import index 

app_name="demo"

urlpatterns = [
    
    path('users/', index, name='users'),
    path('users/logout', index, name='logout'),
    path('users/edit/<int:id>', index, name='users.edit'),
    path('reports', index, name='reports'),
    path('organizations', index, name='organizations'),
    path('dashboard', index, name='dashboard'),
    path('contacts', index, name='contacts'),
    path('', index, name='index'),
] 
