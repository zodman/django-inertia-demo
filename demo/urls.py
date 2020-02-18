
from django.urls import path
from demo.views import index , contacts,organizations
from demo.views import contact_edit, organization_edit
from demo.views import contact_create

app_name="demo"

urlpatterns = [

    path('reports', index, name='reports'),
    path('users/', index, name='users'),
    path('users/logout', index, name='logout'),
    path('users/edit/<int:id>', index, name='users.edit'),
    path('contacts/edit/<int:id>', contact_edit, name='contacts.edit'),
    path('contacts/create/', contact_create, name='contacts.create'),
    path('contacts', contacts, name='contacts'),
    path('organizations/edit/<int:id>', organization_edit, name='organizations.edit'),
    path('organizations/create/', organizations, name='organizations.create'),
    path('organizations', organizations, name='organizations'),
    path('dashboard', index, name='dashboard'),
    path('', index, name='index'),
]
