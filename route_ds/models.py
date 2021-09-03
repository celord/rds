from django.conf import settings
from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse


class RouteDs(models.Model):
    rd = models.CharField(max_length=50, null=False, unique=True)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    tec = models.CharField(max_length=100, null=False)
    eventum = models.IntegerField(null=False)
    date = models.DateTimeField(auto_now_add=True)
    client = models.CharField(max_length=200)
    numline = models.IntegerField()

    LIBRE = 'Libre'
    OCUPADO = 'Ocupado'
    DUPLICADO = 'Duplicado'
    status_choices = [
        (LIBRE, 'Libre'),
        (OCUPADO, 'Ocupado'),
        (DUPLICADO, 'Duplicado'),
    ]
    status = models.CharField(
        max_length=10,
        choices=status_choices,
        default=LIBRE)

    def __str__(self):
        return self.rd

    def get_absolute_url(self):
        return reverse("routeds_detail", kwargs={"pk": self.pk})
