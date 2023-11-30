from django.urls import path
from .views import home, success, contact_list, update_contact, delete_contact
urlpatterns = [
	path('success/', success, name='success'),
	path('', home, name='home'),
    path('contact_list/', contact_list, name='contact_list'),
    path('update_contact/<int:contact_id>/', update_contact, name='update_contact'),
    path('delete_contact/<int:contact_id>/', delete_contact, name='delete_contact')
    
]
