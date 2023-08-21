from django import forms
from .models import MediaFile
from multiupload.fields import MultiFileField

class MediaUploadForm(forms.ModelForm):
    class Meta:
        model = MediaFile
        fields = ['file', 'media_type']

    file = MultiFileField(min_num=1, max_num=10)