from django.contrib import admin
from . import models

admin.site.register(models.DataUser),
admin.site.register(models.ListEvent),
admin.site.register(models.ListLevelEvent),
admin.site.register(models.Event),
admin.site.register(models.PlaceEvent),
