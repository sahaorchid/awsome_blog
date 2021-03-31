from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm,UsernameField
from django import forms
from .models import post

#for signup customize form
class signupForm(UserCreationForm):
    password1 = forms.CharField(label='Password',widget=forms.PasswordInput(attrs={'class':'form-control','id':'exampleInputEmail1'}))
    password2 = forms.CharField(label='Confirm Password(again)',widget=forms.PasswordInput(attrs={'class':'form-control','id':'exampleInputEmail1'}))
    class Meta:
        model=User
        fields=['username','email','first_name','last_name',]
        widgets={'username':forms.TextInput(attrs={'class':'form-control','id':'exampleInputEmail1'}),
                 'email':forms.EmailInput(attrs={'class':'form-control'}),
                 'first_name':forms.TextInput(attrs={'class':'form-control'}),
                 'last_name':forms.TextInput(attrs={'class':'form-control'})}


#for login customize form
class loginForm(AuthenticationForm):
    username = UsernameField(widget=forms.TextInput(attrs={'autofocus':True,'class':'form-control','id':'exampleInputEmail1'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'autofocus':'current-password','class':'form-control','id':'exampleInputEmail1'}))


#addpost form
class addpostform(forms.ModelForm):
    class Meta:
        model=post
        fields=['titel','desc']
        labels={'titel':'Title','desc':'Description'}
        widgets={
            'desc': forms.Textarea(attrs={'class': 'form-control', 'id': 'exampleInputEmail1'}),
            'titel': forms.TextInput(attrs={'class': 'form-control', 'id': 'exampleInputEmail1'}),
        }


