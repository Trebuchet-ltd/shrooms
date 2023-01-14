from django.urls import path

from . import views

app_name = "Homapage"

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('edit/<str:title>', views.edit, name='edit'),
    # path('details/', views.details, name='details')
]
