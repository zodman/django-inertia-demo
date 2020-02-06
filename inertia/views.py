import json
from django.core.exceptions import ImproperlyConfigured
from django.views.generic import View
from django.views.generic.list import BaseListView
from django.views.generic.detail import BaseDetailView
from django.shortcuts import render
from django.http import JsonResponse
from django.middleware import csrf
from .share import share
from .version import asset_version

from django.views.generic import View
from django.conf import settings
from django.core import serializers
from django.forms.models import model_to_dict



def _build_context(component_name, props, version, url):
    context = {
        "page": {
            "version": version,
            'url': url,
            "component": component_name,
            "props": props
        },
    }

    return context


def render_inertia(request, component_name, props=None, template_name=None):
    """
    Renders either an HttpRespone or JsonResponse of a component for 
    the use in an InertiaJS frontend integration.
    """
    inertia_template = None

    
    inertia_template = getattr(settings, "INERTIA_TEMPLATE", "base.html")

    if template_name is not None:
        inertia_template = template_name

    if inertia_template is None:
        raise ImproperlyConfigured(
            "No Inertia template found. Either set INERTIA_TEMPLATE"
            "in settings.py or pass template parameter."
        )

    if props is None:
        props = {}
    shared = {}
    for k, v in request.session.get("share",{}).items():
        shared[k]=v

    
    props.update(shared)

    del request.session["share"]
    

    # subsequent renders
    if ('x-inertia' in request.headers and
        'x-inertia-version' in request.headers and
        request.headers['x-inertia-version'] == str(asset_version.get_version())):
        response = JsonResponse({
            "component": component_name,
            "props": props,
            "version": asset_version.get_version(),
            "url": request.path
        })

        response['X-Inertia'] = True
        response['Vary'] = 'Accept'
        return response
    context = _build_context(component_name, props,
                             asset_version.get_version(), url=request.path)

    return render(request, inertia_template, context)


class InertiaMixin():
    component_name = ""
    props = None
    template_name = None
    
    def render_to_response(self, context):         
        serialized_object = self.get_serialized_object()
        object_name = self.get_object_name()
    
        if self.props is None:
            self.props = {object_name: serialized_object}
        else:
            self.props[object_name] = serialized_object

        return render_inertia(self.request, self.component_name, self.props, self.template_name)


class InertiaDetailView(InertiaMixin, BaseDetailView):
    """
    Similiar to Djangos DetailView, but with Inertia templates.
    """
    def get_serialized_object(self):
        return model_to_dict(self.object)
        

    def get_object_name(self):
        object_name = self.get_context_object_name(self.object)
        return obj_name


class InertiaListView(InertiaMixin, BaseListView):
    """
    Similiar to Djangos ListView, but with Inertia templates.
    """
    def get_serialized_object(self):    
        obj = list(self.object_list.values())
        return obj

    def get_object_name(self): 
        object_name = self.get_context_object_name(self.object_list)
        return object_name