from django import forms
from django.contrib.auth.models import User
from . import models


class CustomerUserForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['first_name','last_name','username','password']
        widgets = {
        'password': forms.PasswordInput()
        }
        
class CustomerForm(forms.ModelForm):
    class Meta:
        model=models.Customer
        fields=['address','mobile','profile_pic']

class ProductForm(forms.ModelForm):
    class Meta:
        model=models.Product
        fields=['name','price','description','product_image']

#address of shipment
class AddressForm(forms.Form):
    Name = forms.CharField(max_length=50)
    Email = forms.EmailField()
    Mobile= forms.CharField(max_length=10)
    Building = forms.CharField(max_length=500)
    Area = forms.CharField(max_length=500)
    Landmark = forms.CharField(max_length=500)
    City = forms.CharField(max_length=500)
    Pincode = forms.CharField(max_length=6)

class FeedbackForm(forms.ModelForm):
    class Meta:
        model=models.Feedback
        fields=['name', 'email','feedback']
        # widgets = {
        #     'name': forms.TextInput(attrs={'placeholder': 'Your Name'}),
        #     'email': forms.EmailField(attrs={'placeholder': 'Enter your Email'}),
        #     'feedback': forms.Textarea(attrs={'placeholder': 'Your Message'}),
        # }

#for updating status of order
class OrderForm(forms.ModelForm):
    class Meta:
        model=models.Orders
        fields=['status']

#for contact us page
class ContactusForm(forms.Form):
    Name = forms.CharField(max_length=30)
    Email = forms.EmailField()
    Message = forms.CharField(max_length=500,widget=forms.Textarea(attrs={'rows': 3, 'cols': 30}))
