from django import forms
from .models import Student, College, Stream
from django.contrib.auth.models import User

class StudentForm(forms.ModelForm):
	class Meta:
		model = Student
		fields = '__all__'




class UserRegistrationForm(forms.ModelForm):
	password = forms.CharField(label='Password', widget=forms.PasswordInput)

	password2 = forms.CharField(label='Repeat Password', widget=forms.PasswordInput)

	class Meta:
		model = User
		fields = ('username', 'first_name', 'last_name', 'email')


	def clean_password2(self):
		cd = self.cleaned_data

		if cd['password'] != cd['password2']:
			raise forms.ValidationError("Passwords don't match!")

		return cd['password2']



class CollegeForm(forms.ModelForm):
	class Meta:
		model = College
		fields = '__all__'


	def save(self, *args, **kwargs):
		try:
			coll = College.objects.get(name=self.cleaned_data['name'], city=self.cleaned_data['city']) or None
			if coll:
				return coll
		except:
			return super(CollegeForm, self).save(*args, **kwargs)

		



class StreamForm(forms.ModelForm):
	class Meta:
		model = Stream
		fields = '__all__'

