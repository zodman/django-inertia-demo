from django.shortcuts import render, redirect
from inertia.views import render_inertia, InertiaMixin
from inertia.share import share, share_flash
from .models import Contact, Organization
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage
from django.urls import reverse
from .utils import _get_objs
from django.forms import model_to_dict
from .serializers import ContactSchema, OrganizationSchema
import json
from marshmallow import  INCLUDE, ValidationError

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
    trashed = request.GET.get("trashed","")
    if trashed == "with":
        objects = objects.filter(deleted=True)
    search =  request.GET.get("search", "")
    if search != "" and search !="undefined":
        objects = objects.filter(first_name__icontains=search)
    args = ("id","organization__name", "first_name", "last_name",'city','phone')
    objs, links = _get_objs(request, objects, args, "demo:contacts")
    props = {
        'links':links,
        'contact_list': objs,
        'filters': {
            'search':search,
            'trashed':trashed,
       }
    }
    return render_inertia(request, "Contacts", props)


def contact_edit(request, id):
    contact = Contact.objects.get(id=id)
    c = ContactSchema()
    org_schema = OrganizationSchema(many=True, only=("id","name"))
    orgs = Organization.objects.all()

    if request.method == "POST":
        data= json.loads(request.body)
        try:
            data_serialized = c.load(data, unknown=INCLUDE)
        except ValidationError  as err:
            share_flash(request, error="Exists errors on form")
            share_flash(request, errors= err.messages)
        else:
            Contact.objects.filter(id=id).update(**data)
            share_flash(request, success="Updated contact")
            return redirect(reverse("demo:contacts"))
    if request.method == "DELETE":
        contact.deleted = True
        contact.save()
        share_flash(request, success="Contact Deleted")
        return redirect(reverse("demo:contacts"))



    props = {
        'contact': c.dump(contact),
        'organizations': org_schema.dump(orgs)
    }
    return render_inertia(request, "Contacts.Edit", props)



def index(request):
    # share_flash(request, errors=["yeah",])
    return render_inertia(request, "Index")
