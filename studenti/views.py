from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .models import Student
from .forms import StudentForm

# Create your views here.
# we can create a default view: - there are 2 types of views in python
# 1. function based views
# 2. class based views
# in this tutorial we will use function based views


def index(request):
    return render(request, 'studenti/index.html', {
        'studenti': Student.objects.all()
    })


def vezi_student(request, id):
    return HttpResponseRedirect(reverse('index'))


def adauga(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            new_numar_matricol = form.cleaned_data['numar_matricol']
            new_prenume = form.cleaned_data['prenume']
            new_nume = form.cleaned_data['nume']
            new_email = form.cleaned_data['email']
            new_specializarea = form.cleaned_data['specializarea']
            new_media = form.cleaned_data['media']

            new_student = Student(
                numar_matricol=new_numar_matricol,
                prenume=new_prenume,
                nume=new_nume,
                email=new_email,
                specializarea=new_specializarea,
                media=new_media
            )
            new_student.save()
            return render(request, 'studenti/adauga.html', {
                'form': StudentForm(),
                'success': True
            })
    else:
        form = StudentForm()
    return render(request, 'studenti/adauga.html', {
        'form': StudentForm()
    })


def editeaza(request, id):
    if request.method == 'POST':
        student = Student.objects.get(pk=id)
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return render(request, 'studenti/editeaza.html', {
                'form': form,
                'success': True
            })
    else:
        student = Student.objects.get(pk=id)
        form = StudentForm(instance=student)
    return render(request, 'studenti/editeaza.html', {
        'form': form
    })


def sterge(request, id):
    if request.method == 'POST':
        student = Student.objects.get(pk=id)
        student.delete()
    return HttpResponseRedirect(reverse('index'))
