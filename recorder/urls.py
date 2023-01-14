from django.urls import path

from . import views

app_name = "Homapage"

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('edit/<str:title>', views.edit, name='edit'),
    path('audio/', views.AudioViewSet.as_view({'post': 'create'}), name='audio'),
    # path('details/', views.details, name='details')
]
