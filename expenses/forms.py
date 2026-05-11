from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Expense

class RegisterForm(UserCreationForm):
    email= forms.EmailField()

    class Meta:
        model=User
        fields=['username','email','password1','password2']

class ExpenseForm(forms.ModelForm):
    date=forms.DateField(
        widget=forms.DateInput(attrs={
            'type':'date',
            'class':'form-control'
        })
    )
    class Meta:
        model=Expense
        fields= ['amount','category','date','description']
        widgets={
            'amount':forms.NumberInput(attrs={'class':'form-control'}),
            'category':forms.Select(attrs={'class':'form-select'}),
            'amount':forms.Textarea(attrs={'class':'form-control','rows':3}),
        }