from multiprocessing import context
from re import template
from django.shortcuts import render


def dashboard(request):

    template_name = 'storage/dashboard.html'
    context = {}
    return render(request, template_name, context)


def upload_images(request):

    template_name = 'storage/images.html'
    context = {}
    return render(request, template_name, context)