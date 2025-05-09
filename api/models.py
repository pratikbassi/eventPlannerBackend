from django.db import models


# Create your models here.

class Track(models.Model):
    title = models.CharField(max_length=128)
    description = models.TextField(max_length=512)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.title

class Event(models.Model):
    title = models.CharField(max_length=128)
    description = models.TextField(max_length=512)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    track = models.ForeignKey(Track, null=True, on_delete=models.CASCADE, related_name='events')


    def __str__(self):
        return self.title

