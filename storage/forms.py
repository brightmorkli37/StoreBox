from django.forms import ModelForm
from .models import *

class ImageForm(ModelForm):
    
    class Meta:
        model = Image
        fields = ("image",)


class AudioForm(ModelForm):
    
    class Meta:
        model = Audio
        fields = ("audio",)


class VideoForm(ModelForm):
        
        class Meta:
            model = Video
            fields = ("video",)


class DocumentForm(ModelForm):
    
    class Meta:
        model = Document
        fields = ("file",)


