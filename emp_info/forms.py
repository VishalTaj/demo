from django import forms
from django.contrib.auth.models import User

class RegForm(forms.ModelForm):
	username =forms.CharField(widget=forms.TextInput(attrs=
					{
					   'placeholder':'Enter username',
					}))
	email = forms.EmailField(widget=forms.TextInput(attrs=
					{
					   'placeholder':'Enter Email',
					}))
	password = forms.CharField(widget=forms.PasswordInput(attrs=
					{
					   'placeholder':'Enter Password',
					}))
	password2 = forms.CharField(widget=forms.PasswordInput(attrs=
					{
					   'placeholder':'Confirm Password',
					}))
	first_name = forms.CharField(widget=forms.TextInput(attrs=
					{
					   'placeholder':'Enter first_name',
					}))
	last_name = forms.CharField(widget=forms.TextInput(attrs=
					{
					   'placeholder':'Enter last_name',
					}))

	def clean_password2(self):
	   password = self.cleaned_data['password'] # cleaned_data dictionary has the
		                                     # the valid fields
	   password2 = self.cleaned_data['password2']
	   if password != password2:
	     raise forms.ValidationError("Passwords do not match.")
	   return password2
	class Meta:
		model = User
		fields = ['username','email','first_name','last_name','password']
"""
class LoginForm(forms.ModelForm):
	username =forms.CharField(widget=forms.TextInput(attrs=
					{
					   'placeholder':'Enter username',
					}))
	password=forms.CharField(widget=forms.PasswordInput(attrs=
					{
					   'placeholder':'Your Password',
                    }))

"""
class LoginForm(forms.ModelForm):
	username =forms.CharField(widget=forms.TextInput(attrs=
					{
					   'placeholder':'Enter username',
					}))
	password = forms.CharField(widget=forms.PasswordInput(attrs=
					{
					   'placeholder':'Enter Password',
					}))
	class Meta:
		model = User
		fields = ['username','password']

class EditForm(forms.ModelForm):
	email=forms.EmailField()
	class Meta:
		model = User
		fields = ['email']

class ChangeForm(forms.ModelForm):
	
	password = forms.CharField(widget=forms.PasswordInput(attrs=
					{
					   'placeholder':'Enter New Password',
					}))
	password2 = forms.CharField(widget=forms.PasswordInput(attrs=
					{
					   'placeholder':'Confirm Password',
					}))
	def clean_password2(self):
	   password = self.cleaned_data['password'] # cleaned_data dictionary has the
		                                     # the valid fields
	   password2 = self.cleaned_data['password2']
	   if password != password2:
	     raise forms.ValidationError("Passwords do not match.")
	   return password2
	class Meta:
		model = User
		fields = ['password']
	


		






