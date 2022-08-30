# Developed by Surfa
from django import forms
from operator import mod
from pyexpat import model
from django import forms
from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render,redirect
from django.core.exceptions import ValidationError
from django.forms import ModelForm
from native.models import Contact



# class ImageForm(forms.ModelForm):
#     """Form for the image model"""
#     class Meta:
#         model = Galary
#         fields = ('title', 'image2')



class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'
    
    # def send_name(self):
    #     # send email using the self.cleaned_data dictionary
    #     name = self.cleaned_data['name'].lower()
    #     r = Contact.objects.filter(name=name)
    #     if r.count():
    #         raise  ValidationError("Username already exists")
    #     return name
    
    # def send_email(self):
    #     email = self.cleaned_data['email'].lower()
    #     r = Contact.objects.filter(email=email)
    #     if r.count():
    #         raise  ValidationError("Email already exists")
    #     return email
    
    # def send_website(self):
    #     website = self.cleaned_data['website'].lower()
    #     r = Contact.objects.filter(website=website)
    #     if r.count():
    #         raise  ValidationError("Email already exists")
    #     return website
    




# class UserCreatForm(UserCreationForm):
    
#     class Meta:
#         fields = ('name', 'email', 'website','comment')
#         model = get_user_model()
        
#         def __init__(self,*args,**kwargs):
#             super().__init__(*args,**kwargs)
#             self.fields['name'].lebel= 'First Name'
#             self.fields['email'].lebel = 'Email Address'
#             self.fields['website'].lebel = 'website'
#             self.fields['comment'].lebel = 'comment' 

# class Contact(forms.Form):
#     name = models.CharField(max_length=200, unique=True)
#     email = models.EmailField(max_length=200, unique=True)
#     website =  models.CharField(max_length=200, unique=True)
#     message = models.TextField(max_length=2000, unique=False)