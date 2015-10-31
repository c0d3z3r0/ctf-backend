from django.db import models
from django_extensions.db.models import TimeStampedModel
from django.contrib.auth.models import User
from registration.signals import user_registered
from django.core.validators import ValidationError
from django.db.models import Max

# Create your models here.


class Category(TimeStampedModel):
    name = models.CharField(max_length=50, unique=True)
    description = models.TextField()

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name


class Challenge(TimeStampedModel):
    name = models.CharField(max_length=50, unique=True)
    active = models.BooleanField(default=True)
    description = models.TextField(blank=True)
    difficulty = models.SmallIntegerField(
        default=1,
        choices=[(1, 'easy'), (2, 'medium'), (3, 'hard'), (4, 'very hard')]
    )
    categories = models.ManyToManyField(Category)

    def __str__(self):
        return self.name


class Flag(TimeStampedModel):
    flag = models.CharField(max_length=100, unique=True)
    credits = models.PositiveIntegerField()
    active = models.BooleanField(default=True)
    stage = models.PositiveIntegerField(blank=True)
    stage_title = models.CharField(max_length=50, unique=False, blank=True)
    stage_description = models.TextField(blank=True)

    challenge = models.ForeignKey(Challenge)
    user = models.ManyToManyField(User, through='Solve')

    class Meta:
        unique_together = (('stage', 'challenge'),)

    def save(self, **kwargs):
        if not self.stage:
            max = self.challenge.flag_set.aggregate(Max("stage"))['stage__max']
            self.stage = max + 1 if max else 1
        super(Flag, self).save(**kwargs)

    def __str__(self):
        return self.flag


class File(TimeStampedModel):
    file = models.FileField()

    challenge = models.ForeignKey(Challenge, null=True, blank=True)
    stage = models.ForeignKey(Flag, null=True, blank=True)

    def clean(self):
        if not self.challenge and not self.stage:
            raise ValidationError('Either challenge or stage must be defined.')

    def __str__(self):
        return self.file.name


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

    class Meta:
        unique_together = (('hint', 'user'),)
        verbose_name_plural = "Bought Hints"

    def __str__(self):
        return ': '.join([str(self.hint.order), self.user.username])


class Faculty(models.Model):
    name = models.CharField(max_length=100, unique=True)
    short_name = models.CharField(max_length=15, unique=True)

    class Meta:
        verbose_name_plural = "Faculties"

    def __str__(self):
        return self.name


class Course(models.Model):
    short_name = models.CharField(max_length=15, unique=True)
    long_name = models.CharField(max_length=100, unique=True)
    faculty = models.ForeignKey(Faculty)

    class Meta:
        unique_together = [('short_name', 'long_name', 'faculty')]

    def __str__(self):
        return '/'.join([self.faculty.short_name, self.short_name])


class Profile(TimeStampedModel):
    user = models.OneToOneField(User, unique=True)

    course = models.ForeignKey(Course)
    semester = models.PositiveSmallIntegerField()

    class Meta:
        verbose_name_plural = "Profile"

    def __str__(self):
        return ''.join(
            (self.user.username, '|',
             self.course.faculty.name, '/',
             self.course.short_name, ':',
             str(self.semester)
             ))
