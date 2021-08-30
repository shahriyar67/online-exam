from django.db import models
from django.db.models.fields import CharField, FloatField, IntegerField, SlugField
from django.utils import timezone
# Create your models here.

class lesson(models.Model):
    slug = SlugField(max_length=15,unique=True)
    lessonName = models.CharField(max_length=15,default="null")
    def __str__(self):
        return self.lessonName
    
class question(lesson):
    STATUS_CHOICES = (
        (0.25,"D = 0.25"),
        (0.5,"C = 0.5"),
        (0.75,"B = 0.75"),
        (1.00,'A = 1.00'),
    )
    question_text= models.CharField(max_length=200)
    true_answer = models.CharField(max_length=100)
    studentPoints = models.FloatField(max_length=3,choices=STATUS_CHOICES)
    desineDate = models.DateTimeField(default= timezone.now)
    published = models.CharField(max_length=1,choices=(('P','published'),('N','Not published')),default='P')
    
    
    def __str__(self):
        return self.question_text
    
class student(models.Model):
    name = models.CharField(max_length=10)
    family = models.CharField(max_length=10)
    
    def __str__(self):
        return self.name+self.family
    
