from django import forms


class ContactForm(forms.Form):
  fullname= forms.CharField(widget= forms.TextInput(attrs={'class':'form-control'}))
  email= forms.EmailField()
  message = forms.CharField(widget= forms.Textarea())


  def clean_email(self):
    email= self.cleaned_data.get("email")
    if not 'gmail.com' in email:
      raise forms.ValidationError('email must be gmail')
    return email