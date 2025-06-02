from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.urls import reverse
from django.db.models import Q
from django.core.paginator import Paginator
from .models import Patient, MedicalRecord, Appointment, LabTest
from .forms import PatientForm, MedicalRecordForm, AppointmentForm, LabTestForm

def patient_list(request):
    patients = Patient.objects.all()
    
    # Search functionality
    search_query = request.GET.get('search', '')
    if search_query:
        patients = patients.filter(
            Q(name__icontains=search_query) |
            Q(contact__icontains=search_query) |
            Q(address__icontains=search_query)
        )
    
    # Filter by gender
    gender = request.GET.get('gender', '')
    if gender:
        patients = patients.filter(gender=gender)
    
    # Filter by blood group
    blood_group = request.GET.get('blood_group', '')
    if blood_group:
        patients = patients.filter(blood_group=blood_group)
    
    # Sorting
    sort_by = request.GET.get('sort', 'name')
    sort_direction = request.GET.get('direction', 'asc')
    
    if sort_direction == 'desc':
        sort_by = f'-{sort_by}'
    
    patients = patients.order_by(sort_by)
    
    # Pagination
    paginator = Paginator(patients, 10)  # Show 10 patients per page
    page_number = request.GET.get('page', 1)
    page_obj = paginator.get_page(page_number)
    
    # Get current sort parameters for template
    current_sort = {
        'field': sort_by.lstrip('-'),
        'direction': 'desc' if sort_by.startswith('-') else 'asc'
    }
    
    return render(request, 'patients/patient_list.html', {
        'page_obj': page_obj,
        'search_query': search_query,
        'selected_gender': gender,
        'selected_blood_group': blood_group,
        'current_sort': current_sort,
        'total_patients': patients.count()
    })

def patient_detail(request, pk):
    patient = get_object_or_404(Patient, pk=pk)
    medical_records = patient.medical_records.all().order_by('-date')
    appointments = patient.appointments.all().order_by('date')
    lab_tests = patient.lab_tests.all().order_by('-test_date')
    return render(request, 'patients/patient_detail.html', {
        'patient': patient,
        'medical_records': medical_records,
        'appointments': appointments,
        'lab_tests': lab_tests
    })

def patient_create(request):
    if request.method == 'POST':
        form = PatientForm(request.POST)
        if form.is_valid():
            patient = form.save()
            messages.success(request, 'Patient created successfully!')
            return redirect('patient_detail', pk=patient.pk)
    else:
        form = PatientForm()
    return render(request, 'patients/patient_form.html', {'form': form, 'title': 'Add New Patient'})

def patient_update(request, pk):
    patient = get_object_or_404(Patient, pk=pk)
    if request.method == 'POST':
        form = PatientForm(request.POST, instance=patient)
        if form.is_valid():
            form.save()
            messages.success(request, 'Patient updated successfully!')
            return redirect('patient_detail', pk=patient.pk)
    else:
        form = PatientForm(instance=patient)
    return render(request, 'patients/patient_form.html', {
        'form': form,
        'title': 'Update Patient',
        'patient': patient
    })

def patient_delete(request, pk):
    patient = get_object_or_404(Patient, pk=pk)
    if request.method == 'POST':
        patient.delete()
        messages.success(request, 'Patient deleted successfully!')
        return redirect('patient_list')
    return render(request, 'patients/patient_confirm_delete.html', {'patient': patient})

def medical_record_create(request, patient_pk):
    patient = get_object_or_404(Patient, pk=patient_pk)
    if request.method == 'POST':
        form = MedicalRecordForm(request.POST)
        if form.is_valid():
            medical_record = form.save(commit=False)
            medical_record.patient = patient
            medical_record.save()
            messages.success(request, 'Medical record added successfully!')
            return redirect('patient_detail', pk=patient.pk)
    else:
        form = MedicalRecordForm()
    return render(request, 'patients/medical_record_form.html', {
        'form': form,
        'patient': patient,
        'title': 'Add Medical Record'
    })

def medical_record_update(request, pk):
    medical_record = get_object_or_404(MedicalRecord, pk=pk)
    if request.method == 'POST':
        form = MedicalRecordForm(request.POST, instance=medical_record)
        if form.is_valid():
            form.save()
            messages.success(request, 'Medical record updated successfully!')
            return redirect('patient_detail', pk=medical_record.patient.pk)
    else:
        form = MedicalRecordForm(instance=medical_record)
    return render(request, 'patients/medical_record_form.html', {
        'form': form,
        'patient': medical_record.patient,
        'title': 'Update Medical Record'
    })

def medical_record_delete(request, pk):
    medical_record = get_object_or_404(MedicalRecord, pk=pk)
    patient_pk = medical_record.patient.pk
    if request.method == 'POST':
        medical_record.delete()
        messages.success(request, 'Medical record deleted successfully!')
        return redirect('patient_detail', pk=patient_pk)
    return render(request, 'patients/medical_record_confirm_delete.html', {'medical_record': medical_record})

def appointment_create(request, patient_pk):
    patient = get_object_or_404(Patient, pk=patient_pk)
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            appointment = form.save(commit=False)
            appointment.patient = patient
            appointment.save()
            messages.success(request, 'Appointment scheduled successfully!')
            return redirect('patient_detail', pk=patient.pk)
    else:
        form = AppointmentForm()
    return render(request, 'patients/appointment_form.html', {
        'form': form,
        'patient': patient,
        'title': 'Schedule Appointment'
    })

def appointment_update(request, pk):
    appointment = get_object_or_404(Appointment, pk=pk)
    if request.method == 'POST':
        form = AppointmentForm(request.POST, instance=appointment)
        if form.is_valid():
            form.save()
            messages.success(request, 'Appointment updated successfully!')
            return redirect('patient_detail', pk=appointment.patient.pk)
    else:
        form = AppointmentForm(instance=appointment)
    return render(request, 'patients/appointment_form.html', {
        'form': form,
        'patient': appointment.patient,
        'title': 'Update Appointment'
    })

def appointment_delete(request, pk):
    appointment = get_object_or_404(Appointment, pk=pk)
    patient_pk = appointment.patient.pk
    if request.method == 'POST':
        appointment.delete()
        messages.success(request, 'Appointment deleted successfully!')
        return redirect('patient_detail', pk=patient_pk)
    return render(request, 'patients/appointment_confirm_delete.html', {'appointment': appointment})

def lab_test_create(request, patient_pk):
    patient = get_object_or_404(Patient, pk=patient_pk)
    if request.method == 'POST':
        form = LabTestForm(request.POST)
        if form.is_valid():
            lab_test = form.save(commit=False)
            lab_test.patient = patient
            lab_test.save()
            messages.success(request, 'Lab test added successfully!')
            return redirect('patient_detail', pk=patient.pk)
    else:
        form = LabTestForm()
    return render(request, 'patients/lab_test_form.html', {
        'form': form,
        'patient': patient,
        'title': 'Add Lab Test'
    })

def lab_test_update(request, pk):
    lab_test = get_object_or_404(LabTest, pk=pk)
    if request.method == 'POST':
        form = LabTestForm(request.POST, instance=lab_test)
        if form.is_valid():
            form.save()
            messages.success(request, 'Lab test updated successfully!')
            return redirect('patient_detail', pk=lab_test.patient.pk)
    else:
        form = LabTestForm(instance=lab_test)
    return render(request, 'patients/lab_test_form.html', {
        'form': form,
        'patient': lab_test.patient,
        'title': 'Update Lab Test'
    })

def lab_test_delete(request, pk):
    lab_test = get_object_or_404(LabTest, pk=pk)
    patient_pk = lab_test.patient.pk
    if request.method == 'POST':
        lab_test.delete()
        messages.success(request, 'Lab test deleted successfully!')
        return redirect('patient_detail', pk=patient_pk)
    return render(request, 'patients/lab_test_confirm_delete.html', {'lab_test': lab_test})
