from django.db import models
from django.contrib.auth.models import AbstractUser
from app_mentoring.models.node import Node


LEARNER = 'learner'
MENTOR = 'mentor'

USER_TYPE_CHOICES = (
    (LEARNER, LEARNER),
    (MENTOR, MENTOR),
)

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
