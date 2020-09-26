from django.db import models


BACKEND = 'Backend'
FRONTEND = 'Frontend'
DEVOPS = 'Devops'
QA = 'QA'
DESIGNER = 'Designer'
DATA_SCIENTIST = 'Data Scientist'
FULL_STACK = 'Full stack'

ROLE_CHOICES = (
    (BACKEND, BACKEND),
    (FRONTEND, FRONTEND),
    (DEVOPS, DEVOPS),
    (QA, QA),
    (DESIGNER, DESIGNER),
    (DATA_SCIENTIST, DATA_SCIENTIST),
    (FULL_STACK, FULL_STACK),
)


class Role(models.Model):

    name = models.CharField(max_length=80, choices=ROLE_CHOICES,)

    description = models.CharField(max_length=250, blank=True)

    def __str__(self):
        return self.name
