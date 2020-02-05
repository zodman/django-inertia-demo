from django.shortcuts import render
from inertia.views import render_inertia
from inertia.share import share

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
