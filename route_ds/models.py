from django.conf import settings
from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse


class RouteDs(models.Model):
    rd = models.CharField(max_length=50, null=False, unique=True)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
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

class Tec(models.Model):
    tec = models.ForeignKey(RouteDs,on_delete=models.CASCADE)
    name = models.CharField(max_length=100, null=False)
    last_name = models.CharField(max_length=100, null=False)

    def __str__(self):
        return self.name
    

class Client(models.Model):
    client = models.ForeignKey(RouteDs,on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name

class Eventum(models.Model):
    eventum = models.ForeignKey(RouteDs,on_delete=models.CASCADE)
    numeventum = models.IntegerField()

    def __str__(self):
        return self.numeventum

class NumLine(models.Model):
    numline = models.ForeignKey(RouteDs,on_delete=models.CASCADE)
    line = models.IntegerField()

    def __str__(self):
        return self.line