from django.shortcuts import render
from profiles_app.forms import StudentForm



def home_student_form(request):
	form = StudentForm()
	success = False

	if request.method == 'POST':
		form = StudentForm(request.POST)
		if form.is_valid():
			form.save(commit=True)
			success = True


	return render(request, 'home.html', {'form': form, 'success': success})
