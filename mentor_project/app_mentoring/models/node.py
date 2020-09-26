from django.db import models


class Node(models.Model):

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
