from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from TimeSheet.models import Profile


class NewUserForm(UserCreationForm):
	email = forms.EmailField(required=True)

	class Meta:
		model = User
		fields = ("username", "first_name", "email", "password1", "password2")

	def save(self, commit=True):
		user = super(NewUserForm, self).save(commit=False)
		user.email = self.cleaned_data['email']
		if commit:
			user.save()
		return user


class NewProfileForm(forms.ModelForm):
	class Meta:
		model = Profile
		exclude = ["user", "deleted_date", "deleted_by"]


# class SignUpForm(NewUserForm, NewProfileForm):
# 	def save(self, commit=True):
# 		user = super(SignUpForm, self).save(commit=False)
# 		user.firstname = self.cleaned_data['first_name']
# 		user.email = self.cleaned_data['email']
# 		if commit:
# 			user.save()
# 		return user