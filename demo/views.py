from django.shortcuts import render
from inertia.views import render_inertia, InertiaListView
from inertia.share import share
from .models import Contact
from django.contrib import messages

def share_flash(request, success=False, error=False, errors = []):
    share(request, "flash",{'success':success,'error':error})
    if errors:
        share(request, "errors",errors)


class ContactView(InertiaListView):
    model = Contact
    component_name ="Contacts"
    paginate_by = 20

    def get_serialized_object(self):
        return list(self.object_list.values("first_name",'last_name','organization__name','city','phone'))

    
contacts = ContactView.as_view()

def index(request):
    share_flash(request, errors=["yeah",])
    return render_inertia(request, "Index")
