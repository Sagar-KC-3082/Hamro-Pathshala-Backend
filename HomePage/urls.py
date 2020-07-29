from django.urls import path
from .views import *


urlpatterns = [
    path('post_banner_image',Post_Banner_Image),
    #path('save_banner',Save_homepage_banner),
    path('update_banner_image',Update_Banner_Image),

    path('post_principal_section',Post_Principal_Section),
    path('update_principal_section',Update_Principal_Section),

    path('post_notice',Post_Notice),
    path('update_notice/<str:pk>',Update_Notice),
    path('view_notice',View_Notice),

    path('save_notice',Post_Notice),

    path('post_marquee',Post_Marquee),
    path('update_marquee/<str:pk>',Update_Marquee),
    path('view_marquee',View_Marquee),

    path('post_other',Post_Other),
    path('update_other/<str:pk>',Update_Other),
    path('view_other',View_Other),

    path('post_about_school',Post_About_School),
    path('view_about_school',View_About_School),
    path('update_about_school/<str:pk>',Update_About_School),

    path("view_homepage1",View_Homepage1),
    path("view_homepage2",View_Homepage2),
    path("view_homepage3",View_Homepage3),
]
