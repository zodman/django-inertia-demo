from django.shortcuts import render
from inertia.views import render_inertia

def index(request):
    return render_inertia(request, "Index")
