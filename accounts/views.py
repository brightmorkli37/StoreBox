from multiprocessing import context
from re import template
from django.shortcuts import render


def index(request):

    template_name = 'accounts/index.html'
    context = {}
    return render(request, template_name, context)