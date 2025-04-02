from django.urls import path
from . import views

urlpatterns = [
    path('', views.exam_list, name='exam_list'),
    path('exam/<int:exam_id>/', views.exam_detail, name='exam_detail'),
    path('exam/create/', views.exam_create, name='exam_create'),
    path('exam/<int:exam_id>/question/add/', views.question_create, name='question_create'),
    path('exam/<int:exam_id>/update/', views.exam_update, name='exam_update'),
    path('exam/<int:exam_id>/delete/', views.exam_delete, name='exam_delete'),
    path('exam/<int:exam_id>/solve/', views.exam_solve, name='exam_solve'),
]

