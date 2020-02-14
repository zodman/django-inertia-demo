from django.shortcuts import render
from inertia.views import render_inertia, InertiaMixin
from inertia.share import share
from .models import Contact, Organization
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage
from django.urls import reverse
from .utils import _get_objs, share_flash
from django.forms import model_to_dict
from .serializers import ContactSchema, OrganizationSchema

def organizations(request):
    objects = Organization.objects.all()
    search =  request.GET.get("search", "")
    if search:
        objects = objects.filter(name__icontains=search)
    args = ("id","name", 'region','city','phone')
    objs, links = _get_objs(request, objects, args,"demo:organizations")
    props = {
        'filters': {
                'search':search,
                'trashed':"",
                   },
        'organizations':{
            'links':links,
            'data':objs
        }
    }
    return render_inertia(request, "Organization", props)


def contacts(request):
    objects = Contact.objects.all()
    search =  request.GET.get("search", "")
    if search:
        objects = objects.filter(first_name__icontains=search)
    args = ("id","organization__name", "first_name", "last_name",'city','phone')
    objs, links = _get_objs(request, objects, args, "demo:contacts")
    props = {
        'links':links,
        'contact_list': objs,
        'filters': {
                'search':search,
                'trashed':"",
                   }
    }
    return render_inertia(request, "Contacts", props)



def contact_edit(request, id):
    contact = Contact.objects.get(id=id)
    c = ContactSchema()
    org_schema = OrganizationSchema(many=True, only=("id","name"))
    orgs = Organization.objects.all()
    props = {
        'contact': c.dump(contact),
        'organizations': org_schema.dump(orgs), 
    }
    return render_inertia(request, "Contacts.Edit", props)



def index(request):
    # share_flash(request, errors=["yeah",])
    return render_inertia(request, "Index")
