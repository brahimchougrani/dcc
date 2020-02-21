from django.urls import path

from .views import CreateStudent,DeleteStudent,EditStudent,ListStudentRegistration
app_name = 'students'
urlpatterns = [
    path('',CreateStudent.as_view(),name='CreateStudent'),
    path('list/', ListStudentRegistration.as_view(), name='list_student'),
    path('update/<int:pk>/', EditStudent, name='Update'),
    path('delete/<int:pk>/', DeleteStudent, name='Delete'),
]
