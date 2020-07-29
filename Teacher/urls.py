from django.urls import path
from .views import *
urlpatterns = [
    path('register',Teacher_Register),
    path('view_all_teacher_partial_info',View_All_Teacher_Partial_Info),
    path('view_teacher_detail_info/<str:pk>',View_Teacher_Detail_Info),
    path('get_teachers_list',Get_Teachers_List)
]
