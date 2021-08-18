from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Questions(models.Model):
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'questions'

    def __str__(self):
        return self.text


class Answer(models.Model):
    question = models.ForeignKey(Questions, on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)


    class Meta:
        verbose_name_plural = 'answers'

    def __str__(self):
        return f"{self.text[:50]}..."

