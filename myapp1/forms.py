# myapp3/forms.py
from django import forms
from .models import Contact

class CreateContactForm(forms.Form):
    name = forms.CharField(label='Name', max_length=100)
    address = forms.CharField(label='Address', max_length=200)
    profession = forms.CharField(label='Profession', max_length=100)
    tel_number = forms.CharField(label='Tel Number', max_length=20)
    email_address = forms.EmailField(label='Email Address')
class UpdateContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'address', 'profession', 'tel_number', 'email_address']