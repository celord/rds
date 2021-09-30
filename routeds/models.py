from django.conf import settings
from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse


class Eventum(models.Model):
    eventum = models.IntegerField()

    def __str__(self):
        return str(self.eventum)


class Client(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class NumLine(models.Model):
    numline = models.IntegerField()
    client = models.ForeignKey(Client, on_delete=models.CASCADE, default=None)

    def __str__(self):
        return str(self.numline)

class Tec(models.Model):
    name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name} {self.last_name}"


class RouteDistinguiser(models.Model):
    rd = models.CharField(max_length=50, null=False, unique=True)
    tec = models.ForeignKey(Tec, on_delete=models.CASCADE, default=None)
    client = models.ForeignKey(Client, on_delete=models.CASCADE, default=None)
    eventum = models.ForeignKey(
        Eventum, on_delete=models.CASCADE, default=None)
    numline = models.ForeignKey(
        NumLine, on_delete=models.CASCADE, default=None)
    date = models.DateTimeField(auto_now_add=True)

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
