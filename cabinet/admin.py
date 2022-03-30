from django.contrib import admin
from . import models

# Данные пользователей
admin.site.register(models.Group),
admin.site.register(models.DataUser),

# Данные о мероприятиях
admin.site.register(models.ListEvent),
admin.site.register(models.ListLevelEvent),
admin.site.register(models.PlaceEvent),
admin.site.register(models.Event),
