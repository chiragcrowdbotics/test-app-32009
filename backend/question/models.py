from django.conf import settings
from django.db import models


class Option(models.Model):
    "Generated Model"
    option_name = models.CharField(
        max_length=256,
    )


# Create your models here.
