from django.db import models
from django.contrib.auth.hashers import make_password
# Create your models here.
from django.contrib.auth.models import AbstractUser

class Person(AbstractUser):
    db_table = 'Person'
    # this comes and wel 

    age = models.IntegerField()

    mobile = models.CharField(max_length=15,unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    gender = models.BooleanField(blank=True, null=True)
    birthdate = models.DateField(blank=True, null=True)

    # def save(self, *args, **kwargs):
    #     self.password = make_password(self.password)
    #
    #     super().save(*args, **kwargs)
    class Meta:
        db_table = 'Human'
        ordering = ['created_at']# this creates
        verbose_name = 'Human'
        verbose_name_plural = 'Humans'
        # unique_together = ('firstname', 'lastname'♦
class Student(Person):
     # person = models.OneToOneField(Person,models.CASCADE)
     iq = models.PositiveIntegerField(blank=True,null=True)
     class Meta:
         db_table = 'Student'
         ordering = ['created_at']  # this creates
         verbose_name = 'Student'
         verbose_name_plural = 'Students'

class PersonAddress(models.Model):
    person = models.ForeignKey(Person,models.CASCADE)
    city = models.CharField(max_length=100)
    address = models.TextField(max_length=100)
    class Meta:
        db_table = 'personaddress'