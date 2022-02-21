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


Hospital1 = 'First Hospital'
Hospital2 = 'Second Hospital'
Hospital3 = 'Third Hospital'
Hospital4 = 'Fourth Hospital'
Hospital5 = 'Fifth Hospital'
location_choices = (
	(Hospital1, 'Hospital One'),
	(Hospital2, 'Hospital Two'),
	(Hospital3, 'Hospital Three'),
	(Hospital4, 'Hospital Four'),
	(Hospital5, 'Hospital Five'),
)


class NewWorkDayForm(forms.ModelForm):
	class Meta:
		model = WorkDay
		workdate = forms.DateTimeField(input_formats = ['%m/%d/%y'])
		#location = forms.ChoiceField(choices = location_choices)
		time_in = forms.DateTimeField(input_formats = ['%H:%M:%S'])
		time_out = forms.DateTimeField(input_formats = ['%H:%M:%S'])
		widgets = {
			'location': forms.Select(choices=location_choices, attrs={'class': 'form-control'}),
			'billing': forms.Select(choices=WorkDay.billing_choices, attrs={'class': 'form-control'}),
		}
		#billing_choice = forms.ChoiceField(choices = WorkDay.billing_choices)
		fields = ('workdate', 'location', 'time_in', 'time_out', 'billing')
		exclude = ['sector', 'billing', 'batch_ID', 'company_code']
