from django import forms
from .models import Service,Brand,Demand
from django.db import models


class ServiceForm(forms.ModelForm):
    
    class Meta:
        model = Service
        fields = ("name","company_name","phone","mail","brand","submodel","content")
        widgets = {
            'company_name': forms.TextInput(attrs={'placeholder': 'Bireysel ise boş bırakın.'}),
            'content': forms.Textarea(attrs={'placeholder': 'Lütfen cihazınızdaki arıza ile ilgili detaylı bilgi yazın.'}),
            
        }

class ServiceUForm(forms.ModelForm):
    
    class Meta:
        model = Service
        fields = ("agent","name","company_name","phone","mail","brand","submodel","content")
        widgets = {
            'company_name': forms.TextInput(attrs={'readonly': 'readonly'}),
            'name': forms.TextInput(attrs={'readonly': 'readonly'}),
            'phone' : forms.TextInput(attrs={'readonly': 'readonly'}),
            'mail' : forms.TextInput(attrs={'readonly': 'readonly'}),
            'brand' : forms.TextInput(attrs={'readonly': 'readonly'}),
            'submodel' : forms.TextInput(attrs={'readonly': 'readonly'}),
            'content': forms.Textarea(attrs={'readonly': 'readonly'}),
        }



class DemandForm(forms.ModelForm):
    class Meta:
        model = Demand
        fields = ("name","company_name","phone","mail","product","quantity","content")
        widgets = {
            'company_name': forms.TextInput(attrs={'placeholder': 'Bireysel ise boş bırakın.'}),
        }
        
        
class DemandUForm(forms.ModelForm):
    class Meta:
        model = Demand
        fields = ("agent","name","company_name","phone","mail","product","quantity","content")
        widgets = {
            'company_name': forms.TextInput(attrs={'readonly': 'readonly'}),
            'name': forms.TextInput(attrs={'readonly': 'readonly'}),
            'phone' : forms.TextInput(attrs={'readonly': 'readonly'}),
            'mail' : forms.TextInput(attrs={'readonly': 'readonly'}),
            'product' : forms.TextInput(attrs={'readonly': 'readonly'}),
            'quantity' : forms.TextInput(attrs={'readonly': 'readonly'}),
            'content': forms.Textarea(attrs={'readonly': 'readonly'}),
        }
