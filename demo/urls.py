
from django.urls import path
from demo.views import index , contacts,organizations
from demo.views import contact_edit, organization_edit
from demo.views import contact_create, organization_create
from demo.views import login_view as login
from demo.views import logout_view as logout

app_name="demo"

urlpatterns = [

    path('login', login, name='login'),
    path('users/logout', logout, name='logout'),

    path('reports', index, name='reports'),
    path('users/', index, name='users'),
    path('users/edit/<int:id>', index, name='users.edit'),


    path('contacts/edit/<int:id>', contact_edit, name='contacts.edit'),
    path('contacts/create/', contact_create, name='contacts.create'),
    path('contacts', contacts, name='contacts'),
    path('organizations/edit/<int:id>', organization_edit, name='organizations.edit'),
    path('organizations/create/', organization_create, name='organizations.create'),
    path('organizations/store/', organization_create, name='organizations.store'),
    path('organizations', organizations, name='organizations'),
    path('dashboard', index, name='dashboard'),
    path('', index, name='index'),
]
