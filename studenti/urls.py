from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:id>', views.vezi_student, name='vezi_student'),
    path('adauga/', views.adauga, name='adauga'),
    path('editeaza/<int:id>/', views.editeaza, name='editeaza'),
    path('sterge/<int:id>/', views.sterge, name='sterge'),
]
