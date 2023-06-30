from django.db import models

# Create your models here.
class Page(models.Model):
    title = models.CharField(max_length=20)
    content = models.TextField()

class Comment(models.Model):
    content = models.TextField()
    TYPE_SELECT = (
        ('0', 'A'), 
        ('1', 'B'),
        )
    choice = models.CharField(max_length=10, choices=TYPE_SELECT, default='')
    page = models.ForeignKey(Page, on_delete=models.CASCADE, default='')

