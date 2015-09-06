from django.db import models
from django_extensions.db.models import TimeStampedModel
from django.contrib.auth.models import User

# Create your models here.


class Category(TimeStampedModel):
    name = models.CharField(max_length=50, unique=True)
    description = models.TextField()

    def __str__(self):
        return self.name
    

class Challenge(TimeStampedModel):
    name = models.CharField(max_length=50, unique=True)
    description = models.TextField()
    link = models.URLField(blank=True)
    difficulty = models.SmallIntegerField(
        default=1,
        choices=[(1, 'easy'), (2, 'medium'), (3, 'hard'), (4, 'very hard')]
    )
    active = models.BooleanField(default=True)

    categories = models.ManyToManyField(Category)

    def __str__(self):
        return self.name


class Flag(TimeStampedModel):
    flag = models.CharField(max_length=100, unique=True)
    credits = models.PositiveIntegerField()
    stage = models.PositiveIntegerField()
    stage_description = models.TextField()
    stage_link = models.URLField(blank=True)

    challenge = models.ForeignKey(Challenge)
    user = models.ManyToManyField(User, through='Solve')

    class Meta:
        unique_together = (('stage', 'challenge'),)

    def __str__(self):
        return self.flag


class Hint(TimeStampedModel):
    order = models.PositiveIntegerField()
    description = models.TextField()
    price = models.PositiveIntegerField()

    flag = models.ForeignKey(Flag)
    user = models.ManyToManyField(User, through='BuyHint')

    class Meta:
        unique_together = (('order', 'flag'),)

    def __str__(self):
        return self.flag.flag + ' - ' + str(self.order)


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
        return ': '.join([str(self.hint.order), self.user.username])

