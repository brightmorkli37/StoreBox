from multiprocessing import context
from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required(login_url='accounts:login')
def dashboard(request):

    template_name = 'storage/dashboard.html'
    context = {}
    return render(request, template_name, context)

@login_required(login_url='accounts:login')
def upload_images(request):

    template_name = 'storage/images.html'
    context = {}
    return render(request, template_name, context)

@login_required(login_url='accounts:login')
def upload_audio(request):
    
    template_name = 'storage/audio_files.html'
    context = {}
    return render(request, template_name, context)

@login_required(login_url='accounts:login')
def upload_videos(request):
    
    template_name = 'storage/videos.html'
    context = {}
    return render(request, template_name, context)

def upload_files(request):
    
    template_name = 'storage/documents.html'
    context = {}
    return render(request, template_name, context)