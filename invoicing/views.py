from django.shortcuts import render, reverse


from .models import Employee, Invoice
from .forms import InvoiceEntryForm, EmployeeEntryForm


def home(request):
  return render(request, 'invoicing/home.html', {})



def add_invoice(request):
  form= InvoiceEntryForm()

  if request.method == 'POST':
    form= InvoiceEntryForm(request.POST)    
    if form.is_valid():
      print('success!')
      print(form.cleaned_data['invoice_num'])
  return render(request, 'invoicing/add_invoice.html', {'form': form})  



def show_employees(request):
  employees= Employee.objects.all()
  return render(request, 'invoicing/employee.html', {'employees': employees})


def show_employee(request, employee_id):
  employee= Employee.objects.get(pk= employee_id)
  return render(request, 'invoicing/employee.html', {'emp': employee})


def add_employee(request):
  #form= InvoiceEntryForm()
  
  form= EmployeeEntryForm()
  
  if request.method== 'POST':
    form= EmployeeEntryForm(request.POST)    
    if form.is_valid():
      #cd= form.cleaned_data
      print('xx')
      form.save(commit= True)
      #return reverse('invoicing:show_employee', employee_id= pk)
      return reverse('invoicing:show_employees')
  return render(request, 'invoicing/add_employee.html', {'form': form})
