from django.urls import path
from .views import *


urlpatterns = [
    path('assign_teacher_to_class',Assign_Teacher_To_Class),
    path('get_assigned_teacher_to_class/<str:grade>/<str:section>',Get_Assigned_Teacher_List),
    path('get_subject_class/<str:grade>/<str:section>/<str:teacher>',Get_Subjects_By_Section_Class),
    path('get_student_list_class/<str:grade>/<str:section>',GetStudentsListByClass),

    path('add_section_class',Save_Section_For_Classes),
    path('get_section_class/<str:grade>',Get_Section_For_Classes),


    path('add_subject',Add_Subject),
    path('get_subject_list',Get_Subject_List),
    path('get_subject_of_class',Get_Subject_Of_Class),
    path('add_section',Add_Section),
    path('get_section_list',Get_Section_List),

    path('get_result_of_class_by_subject',Get_Result_Of_Class_By_Subject),
    path('get_result_of_class',Get_Result_Of_Class),
    path('get_result_of_student',Get_Student_Result),
    path('post_result',Post_Result),
    path('download/result',Result_Pdf)
]
