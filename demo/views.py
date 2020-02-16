from django.shortcuts import render, redirect
from inertia.views import render_inertia, InertiaMixin
from inertia.share import share, share_flash
from .models import Contact, Organization
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage
from django.urls import reverse
from .utils import _get_objs, _filter
from django.forms import model_to_dict
from .serializers import ContactSchema, OrganizationSchema
import json
from marshmallow import  INCLUDE, ValidationError


def organization_edit(request, id):
    organization = Organization.objects.get(id=id)
    schema = OrganizationSchema()
    props = {
        'organization': schema.dump(organization)
    }
    return render_inertia(request, "Organizations.Edit", props)


def organizations(request):
    org_sche = OrganizationSchema(many=True)
    objects = Organization.objects.all()
    _filter(request, objects, "name__icontains")
    args = ("id","name", 'region','city','phone')
    objs, links = _get_objs(request, objects, args,"demo:organizations")
    trashed = request.GET.get("trashed","")
    search =  request.GET.get("search", "")
    props = {
        'filters': {
                'search':search,
                'trashed':trashed,
                   },
        'organizations':{
            'links':links,
            'data': org_sche.dump(objs)
        }
    }
    return render_inertia(request, "Organizations", props)


def contacts(request):
    objects = Contact.objects.all()
    objects = _filter(request, objects, "first_name__icontains")
    trashed = request.GET.get("trashed","")
    search =  request.GET.get("search", "")
    args = ("id","organization__name", "first_name", "last_name",'city','phone')
    objs, links = _get_objs(request, objects, args, "demo:contacts")
    contact_schema = ContactSchema(many=True)
    props = {
        'links':links,
        'contact_list': contact_schema.dump(objs),
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
