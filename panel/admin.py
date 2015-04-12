from django.contrib import admin

# Register your models here.
from .models import Satici, Alici


class SaticiAdmin(admin.ModelAdmin):
    class meta:
        model = Satici


admin.site.register(Satici, SaticiAdmin)