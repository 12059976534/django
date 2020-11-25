from django.urls import path

from . import views
from .logreg import logreg

urlpatterns =[
    path('', views.index, name='index'),
    path('login/',logreg.login, name='login'),
    path('logout/',logreg.logout, name='logout'),
    path('admin/',views.admin, name='admin'),
    path('tambah/',views.tambah, name='tambah'),
    path('update/', views.update, name='update'),
    path('info/', views.info, name='info'),
]