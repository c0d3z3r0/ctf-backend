from django.db import models
from django_extensions.db.models import TimeStampedModel
# Create your models here.


class Category(TimeStampedModel):
    name = models.CharField(max_length=50)


class Challenge(TimeStampedModel):
    name = models.CharField(max_length=50)
    description = models.TextField()
    link = models.URLField(blank=True)

    categories = models.ManyToManyField(Category)

    def __str__(self):
        return self.name


class Flag(TimeStampedModel):
    flag = models.CharField(max_length=100)
    credits = models.PositiveIntegerField()

    challenge = models.ForeignKey(Challenge)

    def __str__(self):
        return self.flag


class Hint(TimeStampedModel):
    name = models.CharField(max_length=50)
    description = models.TextField()
    price = models.PositiveIntegerField()

    challenge = models.ForeignKey(Challenge)

    def __str__(self):
        return self.name


class User(TimeStampedModel):
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    email = models.EmailField()
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=100)

    admin = models.BooleanField(default=0)
    confirmed = models.BooleanField(default=0)

    def __str__(self):
        return self.username + ' / ' +\
            ' '.join([self.firstname, self.lastname])
