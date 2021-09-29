from django.contrib import admin

from .models import RouteDistinguiser, Tec, Client, Eventum, NumLine


@admin.register(RouteDistinguiser)
class RouteDistinguiserAdmin(admin.ModelAdmin):
    list_display = ('rd','tec','client','eventum','numline','date')


@admin.register(Tec)
class TecAdmin(admin.ModelAdmin):
    pass


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    pass


@admin.register(Eventum)
class EventumAdmin(admin.ModelAdmin):
    pass


@admin.register(NumLine)
class NumLineAdmin(admin.ModelAdmin):
    pass
