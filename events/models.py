from django.db import models

class Event(models.Model):
    title = models.CharField(max_length=200)
    date = models.DateTimeField()
    location = models.CharField(max_length=200)
    description = models.TextField()
    organizer = models.CharField(max_length=100)

    def __str__(self):
        return self.title
