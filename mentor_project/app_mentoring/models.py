from django.db import models
from django.contrib.auth.models import AbstractUser

LEARNER = 'learner'
MENTOR = 'mentor'

USER_TYPE_CHOICES = (
    (LEARNER, LEARNER),
    (MENTOR, MENTOR),
)

JUNIOR = 'Junior'
MIDDLE  = 'Middle'
SENIOR = 'Senior'

LEVEL_CHOICES = (
    (JUNIOR, JUNIOR),
    (MIDDLE, MIDDLE),
    (SENIOR, SENIOR),
)


class PioNode(models.Model):

    name = models.CharField(max_length=25)
    foundation_date = models.DateTimeField(
        auto_now_add=True,
        null=True, blank=True,
    )
    city = models.CharField(
        max_length=25,
        blank=False,
        null=False,
        default='Cali',
    )

    def __str__(self):
        return self.name


class User(AbstractUser):

    user_type = models.CharField(
        max_length=20,
        choices=USER_TYPE_CHOICES,
        default=LEARNER,
    )

    def __str__(self):
        return "{}: {}".format(self.user_type, self.username)

    @property
    def is_learner(self):
        return self.user_type == LEARNER

    @property
    def is_mentor(self):
        return self.user_type == MENTOR


class UserProfile(models.Model):

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        blank=False,
        related_name='user_profile'
    ) 
    pionode = models.ForeignKey(
        PioNode,
        related_name="nodes",
        blank=False,
        null=False,
        on_delete=models.CASCADE,
    )
    role = models.CharField(
        max_length=30,
        blank=True,
        null=True
    )
    avatar = models.ImageField(
        blank=True,
        null=True,
        upload_to='img',
    )
    level = models.CharField(
        max_length=30,
        blank=True,
        null=True,
        choices=LEVEL_CHOICES,
    )
    years = models.PositiveSmallIntegerField(default=1)
    description = models.CharField(max_length=250, blank=True, null=True)

    def __str__(self):
        return "Profile: {}".format(self.user.username)


class Mentoring(models.Model):

    learner = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        blank=False,
        related_name='learner'
    )
    mentor = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        blank=False,
        related_name='mentor'
    ) 
    date = models.DateField(blank=True, null=True)

    role_mentoring = models.CharField(
        max_length=30,
        blank=True,
        null=True
    )
    number_sesion = models.PositiveSmallIntegerField(default=1)
    description = models.CharField(max_length=250, blank=True, null=True)

    def __str__(self):
        return "{} - {} - date: {}".format(self.mentor, self.learner, self.date)
