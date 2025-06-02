from django.contrib import admin
from .models import Patient, MedicalRecord, Appointment

@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = ('name', 'age', 'gender', 'contact')
    search_fields = ('name', 'contact')
    list_filter = ('gender',)

@admin.register(MedicalRecord)
class MedicalRecordAdmin(admin.ModelAdmin):
    list_display = ('patient', 'date', 'doctor', 'diagnosis')
    list_filter = ('date', 'doctor')
    search_fields = ('patient__name', 'doctor', 'diagnosis')

@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ('patient', 'date', 'doctor', 'reason')
    list_filter = ('date', 'doctor')
    search_fields = ('patient__name', 'doctor', 'reason')
