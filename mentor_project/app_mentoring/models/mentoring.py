from django.conf import settings
from django.db import models

from .role import Role


User = settings.AUTH_USER_MODEL


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

    role_mentoring = models.ForeignKey(
        Role,
        related_name="role_mentoring",
        blank=False,
        null=False,
        on_delete=models.CASCADE,
    )

    number_sesion = models.PositiveSmallIntegerField(default=1)

    description = models.CharField(max_length=250, blank=True, null=True)

    def __str__(self):
        return "{} - {} - date: {}".format(self.mentor, self.learner, self.date)
