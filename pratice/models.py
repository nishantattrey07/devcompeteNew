from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField

# Create your models here.

class Question(models.Model):
    question_name = models.CharField(max_length=200)
    question_text = RichTextField()
    pub_date = models.DateTimeField('date publish')
    score = models.IntegerField(default=0)
    difficulty = models.CharField(max_length=200, choices=[('easy', 'easy'), ('medium', 'medium'), ('hard', 'hard')], default='easy')

    def __str__(self):
        return self.question_name



class TestCase(models.Model):
    test_input = models.TextField()
    test_output = models.TextField()
    test_score = models.IntegerField(default=1)
    hidden = models.BooleanField(default=False)
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name="test_cases", blank=True, null=True)

    def __str__(self):
        return self.test_input

class Submission(models.Model):
    submission_text = models.TextField()
    submission_score = models.IntegerField(default=0)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    pub_date = models.DateTimeField('date published')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="submissions")

