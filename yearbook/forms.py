from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from .models import *

class UserLoginForm(forms.ModelForm):
    class Meta:
        model = YearbookUser
        fields = ['user']

class UserRegistrationForm(UserCreationForm):
    first_name = forms.CharField()
    last_name = forms.CharField()
    email = forms.EmailField()

    def clean_email(self):
        if User.objects.filter(email=self.cleaned_data['email']).exists():
            raise forms.ValidationError("the given email is already registered")
        return self.cleaned_data['email']

    class Meta:
        model = User
        fields = ['first_name', 'last_name','username', 'email', 'password1', 'password2']

class YearbookUserRegistrationForm(forms.ModelForm):
    class Meta:
        model = YearbookUser
        fields = ['bio']

class SignatureForm(forms.ModelForm):
    class Meta:
        model = Signature
        fields = ['signature']

class YearbookUserUpdateForm(forms.ModelForm):
    class Meta:
        model = YearbookUser
        fields= ['bio', 'avatar']

class IYPUpdateForm(forms.ModelForm):
    class Meta:
        model = InstitutionYearProfile
        fields = ['yearbook_quote', 'yearbook_picture']

class InstitutionCreationForm(forms.ModelForm):
    class Meta:
        model = Institution
        fields  = ['institution_name', 'institution_city', 'institution_state', 'institution_year_founded']

class InstitutionYearProfileCreationForm(forms.Form):
    institution = forms.ModelChoiceField(Institution.objects.all())
    start_year = forms.IntegerField()
    end_year = forms.IntegerField()
    is_educator = forms.BooleanField(label='Check if you were a teacher', required= False)
 


   
