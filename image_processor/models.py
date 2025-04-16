import uuid

from django.db import models
from django.utils import timezone

# Create your models here.
class PeopleCounter(models.Model):
    original_file = models.ImageField(upload_to=f'uploads/original/{uuid.uuid4()}.jpg')
    yolo_processed_file = models.ImageField(upload_to=f'uploads/yolo/{uuid.uuid4()}.jpg',
                                            null=True,
                                            blank=True)
    hog_processed_file = models.ImageField(upload_to=f'uploads/hog/{uuid.uuid4()}.jpg',
                                           null=True,
                                           blank=True)

    yolo_counter = models.IntegerField(null=True, blank=True)
    hog_counter = models.IntegerField(null=True, blank=True)

    processed_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'People Counter {self.pk}'