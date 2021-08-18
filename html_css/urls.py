from django.urls import path
from . import views


app_name = 'html_css'

urlpatterns = [
    path('questions/', views.questions, name='questions'),
    path('questions/<int:question_id>/', views.question, name='question'),
    path('new_question/', views.new_question, name='new_question'),
    path('new_answer/<int:question_id>/', views.new_answer, name='new_answer')
]