from django import forms


from .models import Invoice, Employee


class InvoiceEntryForm(forms.Form):
  invoice_num= forms.CharField()
  invoice_amount= forms.DecimalField()

  '''
  class Meta:
    model= Invoice
  '''

'''
class EmployeeEntryForm(forms.Form):
  first_name= forms.CharField()
  last_name = forms.CharField()
  email     = forms.EmailField()
'''


class EmployeeEntryForm(forms.ModelForm):
  class Meta():
    model= Employee
    fields= '__all__'




  
  