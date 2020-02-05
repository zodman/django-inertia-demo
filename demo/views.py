from django.shortcuts import render
from inertia.views import render_inertia, InertiaListView
from inertia.share import share
from .models import Contact

class ContactView(InertiaListView):
    model = Contact
    component_name ="Contacts"

contacts = ContactView.as_view()

def index(request):
    share("auth",{
        'user': {
            'account':{
                'name':"account name"
            },
            'id':"123123",
            'first_name':'andres',
            'last_name':'vargas',
        }
    })
    return render_inertia(request, "Index")
