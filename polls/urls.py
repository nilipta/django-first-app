from django.urls import path

from . import views

urlpatterns = [
    path('', views.mainF, name='mainF'),
    path('index', views.index, name='index'),
    path('<int:question_id>/details', views.details, name='details'),
    path('<int:question_id>/result', views.result, name='result'),
    path('<int:question_id>/vote', views.vote, name='vote'),
]