from django.db import models

# Create your models here.
class Person(models.Model):
    db_table = 'Person'
    firstname = models.CharField(max_length=30)
    lastname = models.CharField(max_length=30)
    age = models.IntegerField()
    email = models.EmailField(unique=True)
    username = models.CharField(unique=True,max_length=30)
    mobile = models.CharField(max_length=9,unique=True)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    sex = models.BooleanField(blank=True, null=True)

    class Meta:
        db_table = 'Human'
        ordering = ['created_at']
        verbose_name = 'Human'
        verbose_name_plural = 'Humans'
        # unique_together = ('firstname', 'lastname')