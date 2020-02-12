from django.shortcuts import render
from inertia.views import render_inertia, InertiaMixin
from inertia.share import share
from .models import Contact
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage
from django.urls import reverse


def share_flash(request, success=False, error=False, errors = []):
    share(request, "flash",{'success':success,'error':error})
    if errors:
        share(request, "errors",errors)


def _get_objs(request, objects, fields):
    p = Paginator(objects, 10)
    page_number = request.GET.get('page')
    links = []
    try:
        page_obj = p.get_page(page_number)
        objs = list(page_obj.object_list.values(*fields))
    except EmptyPage:
        objs = []
    
    
    if page_obj.has_previous():
        prev_page_num = page_obj.previous_page_number()
        links.append({'url': "{}?page={}".format(reverse("demo:contacts"), prev_page_num),
                        'label': 'Prev'})
    if page_obj.has_next():
        next_page_num = page_obj.next_page_number()
        links.append({'url': "{}?page={}".format(reverse("demo:contacts"), next_page_num),
                      'label': 'Next'})
    return objs, links

def contacts(request):

    objects = Contact.objects.all()
    args = ("id","organization__name", "first_name", "last_name",'city','phone')
    objs, links = _get_objs(request, objects, args)

    props = {
        'links':links,
        'contact_list': objs
            
    }
    return render_inertia(request, "Contacts", props)

def index(request):
    # share_flash(request, errors=["yeah",])
    return render_inertia(request, "Index")
