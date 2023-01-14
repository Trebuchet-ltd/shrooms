from django.db import models
from django import forms


# Create your models here.
class Scene(models.Model):
    name = models.CharField(max_length=100)
    speech = models.TextField(max_length=10000,null=True,blank=True)
    background = models.FileField(upload_to='static/images')
    scene_prompts = models.TextField(max_length=10000)
    audio = models.ForeignKey('Audio', on_delete=models.CASCADE, null=True, blank=True)


class Audio(models.Model):
    audio = models.FileField(upload_to='audio')


class AudioForm(forms.Form):
    class Meta:
        model = Audio
