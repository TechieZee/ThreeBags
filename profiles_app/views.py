from django.shortcuts import render, HttpResponseRedirect
from .forms import UserRegistrationForm, StreamForm, CollegeForm
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from .models import Stream, College
# Create your views here.

def register(request):
	user_form = UserRegistrationForm()

	if request.method == 'POST':
		user_form = UserRegistrationForm(data=request.POST)

		if user_form.is_valid():
			new_user = user_form.save(commit=False)
			new_user.set_password(user_form.cleaned_data['password'])
			new_user.save()

			return render(request, 'registration/register_done.html', {'new_user': new_user})


	return render(request, 'registration/register.html', {'user_form': user_form})



@login_required
def new_stream(request, success=False):
	form = StreamForm()
	
	if request.method == 'POST':
		form = StreamForm(request.POST)
		if form.is_valid():
			cd = form.cleaned_data
			strm, s = Stream.objects.get_or_create(name=cd['name'])
			strm.save()
			success = True
			# return HttpResponseRedirect(reverse_lazy('profiles_app:new_stream'))
			return render(request, 'registration/new_stream.html', {'form':StreamForm, 'success': success})

	return render(request, 'registration/new_stream.html', {'form':form, 'success': success})





@login_required
def new_college(request):
	form = CollegeForm()
	success = False
	if request.method == 'POST':
		form = CollegeForm(request.POST)

		if form.is_valid():
			form.save(commit=True)
			success = True

			return render(request, 'registration/new_college.html', {'form': CollegeForm, 'success': success})


	return render(request, 'registration/new_college.html', {'form': form, 'success': success})




@login_required
def managers_home(request):
	return render(request, 'profiles_app/managers_home.html')