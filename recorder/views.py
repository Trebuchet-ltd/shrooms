from django.shortcuts import render
from .models import Scene


# Create your views here.

def homepage(request):
    if request.method == 'POST':
        print(request.POST)
        title = request.POST.get('title')
        if title:
            scene = Scene(name=title)
            scene.save()

    scenes = Scene.objects.all()
    print(scenes)
    context = {
        "scenes": scenes
    }
    return render(request, 'base.html', context)


def edit(request, title):
    scenes = Scene.objects.get(name=title)
    context = {
        "scene" : scenes
    }
    return render(request, 'edit.html', context)
