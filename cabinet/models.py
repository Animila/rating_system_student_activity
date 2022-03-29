from django.db import models
from django.contrib import admin

# База пользователей
class DataUser(models.Model):
    id = models.BigAutoField(primary_key=True)
    names = models.CharField(max_length=150)
    date_birthday = models.DateField()
    email = models.EmailField(max_length=255)
    number_mobile = models.CharField(max_length=150)
    count_event = models.IntegerField()
    group = models.CharField(max_length=15)
    image = models.ImageField(upload_to='user/images/')

    def __str__(self):
        return self.names


# Уровень соревнований
class ListLevelEvent(models.Model):
    level_event = models.CharField(max_length=255)

    def __str__(self):
        return self.level_event


# Список соревнований
class ListEvent(models.Model):
    title_event = models.CharField(max_length=255)

    def __str__(self):
        return self.title_event


# список мест
class PlaceEvent(models.Model):
    number_place = models.IntegerField()

    def __str__(self):
        return str(self.number_place)


# список соревнований пользователя
class Event(models.Model):
    id = models.BigAutoField(primary_key=True)
    member_event = models.ForeignKey(DataUser, on_delete=models.CASCADE)
    title_event = models.ForeignKey(ListEvent, on_delete=models.CASCADE)
    level_event = models.ForeignKey(ListLevelEvent, on_delete=models.CASCADE)
    place = models.ForeignKey(PlaceEvent, on_delete=models.CASCADE)
    document_event = models.ImageField(upload_to='user/document/')
