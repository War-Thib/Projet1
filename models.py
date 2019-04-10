'''
Created on Dec 21, 2018

@author: groupe62
'''
from django.db import models

class User(models.Model):
    firstname = models.CharField(max_length=30)
    lastname = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    phone = models.CharField(max_length=30)
    password = models.CharField(max_length=128)
    GENDER_CHOICES = (
        ('M','Male'),
        ('F','Female'),
        ('X','X'),
        )
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    friends = models.ManyToManyField('self')
    conjoint = models.OneToOneField('self', null=True, blank=True)

    def __str__(self):
        return self.firstname + ' ' + self.lastname


class WallMessage(models.Model):
    author = models.ForeignKey('User')
    content = models.TextField()
    publication_date = models.DateField()    
