from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField()
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title + " \n" + self.description
    

class Contact(models.Model):
    name_sur = models.CharField('Chi invia', max_length=200)
    object_msg = models.CharField('Oggetto del messaggio', max_length=255)
    body = models.TextField('Messaggio', default="")
    create_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name_sur + "\n" + self.object_msg + "\n" + self.create_at