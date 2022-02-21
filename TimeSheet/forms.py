from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from TimeSheet.models import Profile, WorkDay


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
		exclude = ['user', 'deleted_date', 'deleted_by']


Hospital1 = 'h1'
Hospital2 = 'h2'
Hospital3 = 'h3'
Hospital4 = 'h4'
Hospital5 = 'h5'
location_choices = (
	(Hospital1, 'Hospital One'),
	(Hospital2, 'Hospital Two'),
	(Hospital3, 'Hospital Three'),
	(Hospital4, 'Hospital Four'),
	(Hospital5, 'Hospital Five'),
)

FBP_billing = 'FBP'
AMCO_billing = 'AMCO'
billing_choices = (
	(FBP_billing, 'FBP Billing'),
	(AMCO_billing, 'AMCO Billing'),
)


class NewWorkDayForm(forms.ModelForm):
	class Meta:
		model = WorkDay
		workdate = forms.DateTimeField(input_formats=['%m/%d/%y'])
		time_in = forms.TimeField(input_formats=['%H:%M'])
		time_out = forms.TimeField(input_formats=['%H:%M'])
		widgets = {
			'location': forms.Select(choices=location_choices, attrs={'class': 'form-control'}),
			'billing': forms.Select(choices=billing_choices, attrs={'class': 'form-control'}),
		}
		fields = ('workdate', 'location', 'billing', 'time_in', 'time_out')
		exclude = ['sector', 'batch_ID', 'company_code']
