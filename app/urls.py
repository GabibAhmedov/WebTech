from django.urls import path, include

from app import views

urlpatterns = [
    path('<int:i>',views.question, name="question")
]
