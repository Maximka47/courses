from django.contrib import admin
from django.urls import path
from students.views import MyView, ViewSubjects, ViewSubjectStudents

urlpatterns = [
    path('view1/', MyView.as_view()),
    path('view2/<pk>', MyView.as_view()),
    path('view2/', MyView.as_view()),
    path('courses/subject', ViewSubjects.as_view()),
    path('courses/subject/<id>', ViewSubjectStudents.as_view()),

]