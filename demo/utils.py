from inertia.share import share
from django.core.paginator import Paginator, EmptyPage
from django.urls import reverse



def share_flash(request, success=False, error=False, errors = []):
    share(request, "flash",{'success':success,'error':error})
    if errors:
        share(request, "errors",errors)


def _get_objs(request, objects, fields, url_name):
    p = Paginator(objects, 5)
    page_number = request.GET.get('page', 1)
    links = []
    try:
        page_obj = p.get_page(page_number)
        objs = list(page_obj.object_list.values(*fields))
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


