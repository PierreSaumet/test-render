from django.db import models

from users.models import User


# Create your models here.
class Blogs(models.Model):
    CATEGORY_CHOICE = {
        "S-F": "Science-Fiction",
        "ROM": "Roman",
        "FAN": "Fantasy"
    }
    title = models.CharField(max_length=100, unique=True)
    description = models.TextField()
    category = models.CharField(max_length=3, choices=CATEGORY_CHOICE)
    create_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.title}: category: {self.category}, created at: {self.create_at}"
