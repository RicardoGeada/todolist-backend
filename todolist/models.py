import datetime
from django.db import models
from django.conf import settings

# Create your models here.
class TodoModel(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    created_at = models.DateField(default=datetime.date.today)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    is_done = models.BooleanField(default=False)
    
    def __str__(self):
        return f'({self.id}) {self.title}'