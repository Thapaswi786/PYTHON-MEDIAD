from django.urls import path
from . import views

urlpatterns = [
    path('', views.patient_list, name='patient_list'),
    path('patient/new/', views.patient_create, name='patient_create'),
    path('patient/<int:pk>/', views.patient_detail, name='patient_detail'),
    path('patient/<int:pk>/update/', views.patient_update, name='patient_update'),
    path('patient/<int:pk>/delete/', views.patient_delete, name='patient_delete'),
    
    path('patient/<int:patient_pk>/record/new/', views.medical_record_create, name='medical_record_create'),
    path('record/<int:pk>/update/', views.medical_record_update, name='medical_record_update'),
    path('record/<int:pk>/delete/', views.medical_record_delete, name='medical_record_delete'),
    
    path('patient/<int:patient_pk>/appointment/new/', views.appointment_create, name='appointment_create'),
    path('appointment/<int:pk>/update/', views.appointment_update, name='appointment_update'),
    path('appointment/<int:pk>/delete/', views.appointment_delete, name='appointment_delete'),
    
    path('patient/<int:patient_pk>/lab-test/new/', views.lab_test_create, name='lab_test_create'),
    path('lab-test/<int:pk>/update/', views.lab_test_update, name='lab_test_update'),
    path('lab-test/<int:pk>/delete/', views.lab_test_delete, name='lab_test_delete'),
] 