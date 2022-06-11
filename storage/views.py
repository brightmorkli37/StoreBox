from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from accounts.models import Payment
from storage.forms import *
from .models import *

@login_required(login_url='accounts:login')
def dashboard(request):

    template_name = 'storage/dashboard.html'
    context = {}
    return render(request, template_name, context)

@login_required(login_url='accounts:login')
def upload_images(request):
    payment = Payment.objects.all()

    my_images = Image.objects.filter(user=request.user)

    form = ImageForm()
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.instance.user = request.user
            form.save()
            return redirect('storage:my_images')
        else:
            form = ImageForm()

    template_name = 'storage/images.html'
    context = {'payment': payment, 'form': form, 'my_images': my_images}
    return render(request, template_name, context)

@login_required(login_url='accounts:login')
def upload_audio(request):
    payment = Payment.objects.all()

    my_audios = Audio.objects.filter(user=request.user)

    form = AudioForm()
    if request.method == 'POST':
        form = AudioForm(request.POST, request.FILES)
        if form.is_valid():
            form.instance.user = request.user
            form.save()
            return redirect('storage:my_audios')
        else:
            form = AudioForm()
    
    template_name = 'storage/audio_files.html'
    context = {'my_audios': my_audios, 'form': form, 'payment': payment}
    return render(request, template_name, context)

@login_required(login_url='accounts:login')
def upload_videos(request):
    payment = Payment.objects.all()

    my_videos = Video.objects.filter(user=request.user)

    form = VideoForm()
    if request.method == 'POST':
        form = VideoForm(request.POST, request.FILES)
        if form.is_valid():
            form.instance.user = request.user
            form.save()
            return redirect('storage:my_videos')
        else:
            form = VideoForm()
    
    template_name = 'storage/videos.html'
    context = {'my_videos': my_videos, 'form': form, 'payment': payment}
    return render(request, template_name, context)

def upload_files(request):
    payment = Payment.objects.all()

    my_files = Document.objects.filter(user=request.user)

    form = DocumentForm()
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.instance.user = request.user
            form.save()
            return redirect('storage:my_files')
        else:
            form = DocumentForm()
    
    template_name = 'storage/documents.html'
    context = {'my_files': my_files, 'form': form, 'payment': payment}
    return render(request, template_name, context)



# DELETE ITEMS SECTION

@login_required(login_url='login')
def delete_image(request, pk):
    image = Image.objects.get(pk=pk)
    image.delete()
    return redirect('storage:my_images')

@login_required(login_url='login')
def delete_video(request, pk):
    video = Video.objects.get(pk=pk)
    video.delete()
    return redirect('storage:my_videos')

@login_required(login_url='login')
def get_image(request, pk):
    image = Image.objects.get(pk=pk)
    return redirect('storage:my_images')
    # return render(request, 'storage/get_image.html', {'image': image})
