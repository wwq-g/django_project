from django.urls import path
from . import views

urlpatterns = [
    path("home/", views.home, name='home'),
    path("about/", views.about, name='about'),
    path("compile/<ls_id>", views.comp, name='compile'),
    path("del/<ls_id>",views.delet,name='delet'),
    path("cross/<ls_id>",views.cross,name='cross'),
]
