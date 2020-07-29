from django.urls import path
from .views import *

urlpatterns = [
    path('register',Student_Register),
    path('upgrade_student',Upgrade_Student),
    path('view_all_student_partial_info',View_All_Student_Partial_Info),
    path('view_student_detail_info/<str:pk>',View_Student_Detail_Info),
    path('get_students_class_section/<str:grade>/<str:section>',GetAllStudentByClassAndSection)
]
