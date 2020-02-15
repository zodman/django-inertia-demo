from django.contrib import messages
from inertia.share import share


class DemoMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.

    def __call__(self, request):
        
        if request.user.is_authenticated: 
            share(request, 'auth', {
                    'user':{
                        'account':{
                            'id':request.user.id,
                            'name':request.user.username,
                        },
                        'id': request.user.id,
                        'firt_name': request.user.first_name,
                        'last_name': request.user.last_name,
                        'email': request.user.email,
                    }
                })
        else:
            share(request, 'auth', {
                    'user':{
                        'account':{
                            'id':"request.user.id",
                            'name':"request.user.username",
                        },
                        'id': "request.user.id",
                        'firt_name': "request.user.first_name",
                        'last_name': "request.user.last_name",
                        'email': "request.user.email",
                    }
                })
        
        share(request, "flash", {'success':request.session.get("success",False),
                                 'error':request.session.get("error", False)})
        share(request, 'errors', request.session.get("errors",[]) )
        response = self.get_response(request)
        return response
