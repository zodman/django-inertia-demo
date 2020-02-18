from inertia.share import share
from django.core.paginator import Paginator, EmptyPage
from django.urls import reverse
from django.db import models

def _filter(request, objects, filter_param):
    trashed = request.GET.get("trashed","")
    if trashed == "with":
        objects = objects.filter(models.Q(deleted=True)|models.Q(deleted=False))
    elif trashed == "only":
        objects = objects.filter(deleted=True)
    search =  request.GET.get("search", "")
    if search =="undefined":
        search = ""
    if search != "":
        d = {filter_param: search}
        objects = objects.filter(**d)
    return objects


def _get_objs(request, objects, fields, url_name):
    p = Paginator(objects, 20)
    page_number = request.GET.get('page', 1)
    links = []
    try:
        page_obj = p.get_page(page_number)
        objs = page_obj.object_list
    except EmptyPage:
        objs = []
        page_obj = None

    if page_obj:
        if page_obj.has_previous():
            prev_page_num = page_obj.previous_page_number()
            links.append({'url': "{}?page={}".format(reverse(url_name), prev_page_num),
                            'label': 'Prev'})
        for i in p.page_range:
            active=False
            if int(page_number) == i:
                active =True
            
            links.append({'url': "{}?page={}".format(reverse(url_name), i),
                          'active':active,
                                'label': i})

        if page_obj.has_next():
            next_page_num = page_obj.next_page_number()
            links.append({'url': "{}?page={}".format(reverse(url_name), next_page_num),
                          'label': 'Next'})
    return objs, links


