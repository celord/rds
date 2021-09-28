from django.contrib import admin

from .models import RouteDs,Tec,Client,Eventum,NumLine
mymodels = [RouteDs,Tec,Client,Eventum,NumLine]
admin.site.register(mymodels)

# Register your models here.
