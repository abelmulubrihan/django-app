from django.urls import path
from . import views

app_name = 'OnlineCourse'

urlpatterns = [
    path('course/<int:course_id>/', views.course_details, name='course_details'),
    path('submit/<int:question_id>/', views.submit, name='submit'),
    path('exam_result/<int:course_id>/', views.show_exam_result, name='show_exam_result'),
]
