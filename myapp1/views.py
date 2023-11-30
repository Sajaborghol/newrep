# myapp3/views.py
from .forms import UpdateContactForm
from .forms import CreateContactForm
from .models import Contact
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect

def home(request):
    if request.method == 'POST':
        form = CreateContactForm(request.POST)
        if form.is_valid():
            formdata = form.cleaned_data
            name = formdata['name']
            address = formdata['address']
            profession = formdata['profession']
            tel_number = formdata['tel_number']
            email_address = formdata['email_address']
            Contact.objects.create(name=name, address=address, profession=profession, tel_number=tel_number, email_address=email_address)
            return HttpResponseRedirect('/success')
    else:
        form = CreateContactForm()
    return render(request, 'myapp1/create_contact.html', {'form': form})

def success(request):
    return render(request, 'myapp1/success.html')



def contact_list(request):
    contacts = Contact.objects.all()  # Retrieve all contacts from the database
    return render(request, 'myapp1/contact_list.html', {'contacts': contacts})


def update_contact(request, contact_id):
    contact = get_object_or_404(Contact, pk=contact_id)
    if request.method == 'POST':
        form = UpdateContactForm(request.POST, instance=contact)
        if form.is_valid():
            form.save()
            return redirect('contact_list')  # Redirect to a success page
    else:
        form = UpdateContactForm(instance=contact)
    return render(request, 'myapp1/update_contact.html', {'form': form, 'contact': contact})

def delete_contact(request, contact_id):
    contact = get_object_or_404(Contact, pk=contact_id)
    
    if request.method == 'POST':
        contact.delete()
        return redirect('contact_list')
    
    return render(request, 'myapp1/delete_contact.html', {'contact': contact})