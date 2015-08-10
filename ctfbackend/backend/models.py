from django.db import models
from django_extensions.db.models import TimeStampedModel
from django.contrib.auth.models import User

# Create your models here.


class Category(TimeStampedModel):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name
    

class Challenge(TimeStampedModel):
    name = models.CharField(max_length=50, unique=True)
    description = models.TextField()
    link = models.URLField(blank=True)
    status = models.BooleanField(default=False)

    categories = models.ManyToManyField(Category)

    def __str__(self):
        return self.name


class Flag(TimeStampedModel):
    flag = models.CharField(max_length=100, unique=True)
    credits = models.PositiveIntegerField()

    challenge = models.ForeignKey(Challenge)
    user = models.ManyToManyField(User, through='Solve')

    def __str__(self):
        return self.flag


class Hint(TimeStampedModel):
    name = models.CharField(max_length=50)
    description = models.TextField()
    price = models.PositiveIntegerField()

    challenge = models.ForeignKey(Challenge)
    user = models.ManyToManyField(User, through='BuyHint')

    def __str__(self):
        return self.name


class Solve(TimeStampedModel):
    solution = models.TextField()

    flag = models.ForeignKey(Flag)
    user = models.ForeignKey(User)

    def __str__(self):
        return ': '.join([self.flag.flag, self.flag.challenge.name])


class BuyHint(TimeStampedModel):
    hint = models.ForeignKey(Hint)
    user = models.ForeignKey(User)

    def __str__(self):
        return ': '.join([self.hint.name, self.user.username])
