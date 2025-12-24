from django.shortcuts import render

from .models import Person


# Create your views here.
def createPerson(request):
    # create a person

    # Person.objects.create(firstname='Sahand', lastname='Hajiabadi', age=25, email='sahand.hajiabadi@gmail.com',
    #                       username='sahand', mobile='09123456789', description='This is a sample person')
    # create person other way
    person = Person(firstname='Sahand', lastname='Hajiabai', age=25, email='sahand.ha@gmail.com',
                          username='Sahand', mobile='09123456779', description='This is a sample person')
    person.save()