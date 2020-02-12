
from django.urls import path
from demo.views import index , contacts,organizations

app_name="demo"

urlpatterns = [
    
    path('users/', index, name='users'),
    path('users/logout', index, name='logout'),
    path('users/edit/<int:id>', index, name='users.edit'),
    path('contacts/edit/<int:id>', index, name='contacts.edit'),
    path('contacts/create/', index, name='contacts.create'),
    path('contacts', contacts, name='contacts'),
    path('reports', index, name='reports'),
    path('organizations/edit/<int:id>', organizations, name='organizations.edit'),
    path('organizations/create/', organizations, name='organizations.create'),
    path('organizations', organizations, name='organizations'),
    path('dashboard', index, name='dashboard'),
    path('', index, name='index'),
] 
