from multiprocessing import context
from django.shortcuts import render


def dashboard(request):

    template_name = 'storage/base.html'
    context = {}
    return render(request, template_name, context)
