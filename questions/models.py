from django.db import models
from django.contrib.auth import get_user_model
# Create your models here.


class QuestionsData(models.Model):
    type = models.CharField(max_length=100)
    questions = models.TextField()
    correct = models.CharField(max_length=200)
    wrong1 = models.CharField(max_length=200)
    wrong2 = models.CharField(max_length=200)
    wrong3 = models.CharField(max_length=200)

    def __str__(self):
        return self.questions

   
   