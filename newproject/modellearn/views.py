from django.utils import timezone

from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect

from .models import Person

def show_register(request):
    if request.method == 'POST':
        print(request.POST.get('confirm-password'),request.POST.get('password'))
        if request.POST.get('confirm-password') == request.POST.get('password'):
            createPerson(request, request.POST.get('firstname'), request.POST.get('lastname'), request.POST.get('age'),
                         request.POST.get('email'), request.POST.get('username'), request.POST.get('mobile'),
                         request.POST.get('password'))
            return HttpResponse('your account is created')
        else:
            return HttpResponse('passwords do not match')
    else:
        print('not post')
    return render(request, 'register.html')
# Create your views here.
def createPerson(request,firstname,lastname,age,email,username,mobile,password):
    # create a person
    # if request.method == 'POST':
        try:
            Person.objects.create(firstname=firstname, lastname=lastname, age=age, email=email,
                                  username=username, mobile=mobile, password=password)
            return HttpResponse('Person created')
        except Exception as e:
            print(f'cant create person:{e}')
            return HttpResponse(f'Person not created:{e}')
    # return HttpResponse('Method not allowed')
    # create person other way
    # person = Person(firstname='Sahand', lastname='Hajiabai', age=25, email='sahand.ha@gmail.com',
    #                       username='Sahand', mobile='09123456779', description='This is a sample person')
    # person.save()

def read_person(request):
    persons = Person.objects.exclude(username__endswith='aaaq').order_by('-age')
    return render(request, 'read_person.html', {'persons': persons})

def delete_person(request,id):
    person = get_object_or_404(Person,id=id)
    person.delete()
    return redirect('read')

def update_person(request,id):
    person = get_object_or_404(Person,id=id)
    person.age = 300
    person.birthday = timezone.now()
    person.save()
    return redirect('read')






















