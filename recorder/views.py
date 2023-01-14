from django.shortcuts import render
from .models import Scene, Audio, AudioForm


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


class AudioViewSet(viewsets.ModelViewSet):
    queryset = Audio.objects.all()

    def create(self, request, *args, **kwargs) -> Response:

        dataset_form = AudioForm(request.POST, request.FILES)
        if dataset_form.is_valid():
            dataset = dataset_form.save()

            return Response("Done", status=status.HTTP_201_CREATED)
        else:
            return Response(dataset_form.error_messages, status=status.HTTP_400_BAD_REQUEST)
