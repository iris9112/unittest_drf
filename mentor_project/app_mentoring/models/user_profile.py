from django.conf import settings
from django.db import models

from .node import Node
from .role import Role


User = settings.AUTH_USER_MODEL


JUNIOR = 'Junior'
MIDDLE  = 'Middle'
SENIOR = 'Senior'

LEVEL_CHOICES = (
    (JUNIOR, JUNIOR),
    (MIDDLE, MIDDLE),
    (SENIOR, SENIOR),
)


class UserProfile(models.Model):

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        blank=False,
        related_name='user_profile'
    ) 

    node = models.ForeignKey(
        Node,
        related_name="nodes",
        blank=False,
        null=False,
        on_delete=models.CASCADE,
    )

    role = models.ForeignKey(
        Role,
        related_name="roles",
        blank=False,
        null=False,
        on_delete=models.CASCADE,
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
