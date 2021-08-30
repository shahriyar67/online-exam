from django.urls import path,include
from .views import exam,lesson


app_name = "questions"
urlpatterns = [
    path('exam/',exam),
]
