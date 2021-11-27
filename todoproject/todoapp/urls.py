from django.urls import path

from . import views

urlpatterns = [

    path('',views.home,name='home'),
    # giving the id which is the type of int to the url path
    path('delete/<int:taskid>/',views.delete,name='delete'),
    # giving the url for update
    path('update/<int:id>/',views.update,name='update'),
]
