from django.db.models.fields import SlugField
from django.shortcuts import render
from .models import question,lesson
# Create your views here.
context = {
    "elicanada":question.objects.filter(published= 'P')
}
#context2 = {
#    "lesson":question.objects.filter(lessonName=lesson.slug,published = 'P')
#}

def exam(request):
    return render(request,"questions/examSheet.html",context)

#def lesson(request):
#    return render(request,"questions/lesson.html",context2)