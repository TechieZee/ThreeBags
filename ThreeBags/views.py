from django.shortcuts import render, HttpResponseRedirect
from profiles_app.forms import StudentForm
from django.urls import reverse_lazy


def home_student_form(request):
	form = StudentForm()

	if request.method == 'POST':
		form = StudentForm(request.POST)
		if form.is_valid():
			form.save(commit=True)
			success = True

			return HttpResponseRedirect(reverse_lazy('posts_app:posts_list'))


	return render(request, 'home.html', {'form': form})
