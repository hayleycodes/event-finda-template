from django.db import models
from django.forms import ModelForm


class Event(models.Model):
    title = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    start_time = models.DateTimeField('start time and date')
    end_time = models.DateTimeField('end time and date')
    categories = models.ManyToManyField('Category', related_name='events', blank=True)

    def __str__(self):
        return self.title


class Category(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title


class EventForm(ModelForm):
    class Meta:
        model = Event
        fields = ['title', 'location', 'start_time', 'end_time']