from django.contrib import admin
from django.urls import path
from tracker import views

app_name = 'tracker'

urlpatterns = [
    # path('students/', views.student_list, name='student_list'),
    path('admin/', admin.site.urls),
    path('students/create/', views.create_student, name='create_student'),
    path('students/<int:pk>/edit/', views.edit_student, name='edit_student'),
    path('students/<int:pk>/delete/', views.delete_student, name='delete_student'),
    path('students/', views.student_list, name='student_list'),
    path('subjects/', views.subject_list, name='subject_list'),
    path('subjects/create/', views.create_subject, name='create_subject'),
    path('subjects/<int:pk>/edit/', views.edit_subject, name='edit_subject'),
    path('subjects/<int:pk>/delete/', views.delete_subject, name='delete_subject'),
    path('grades/', views.grade_list, name='grade_list'),
    path('grades/create/', views.create_grade, name='create_grade'),
    path('grades/<int:pk>/delete/', views.delete_grade, name='delete_grade'),
    path('grades/<int:pk>/edit/', views.edit_grade, name='edit_grade'),

    path('report/', views.report, name='report'),

    path('students/', views.student_list, name='student_list'),


    path('', views.home, name='home'),


    # Маршруты для представлений предметов и оценок аналогичным образом
]