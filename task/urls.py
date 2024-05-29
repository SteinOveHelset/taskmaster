from django.urls import path

from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('<int:task_id>/delete_task/', views.delete_task, name='delete_task'),
    path('<int:task_id>/mark_as_done/', views.mark_as_done, name='mark_as_done'),
]