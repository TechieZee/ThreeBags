from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from .models import OpportunityPost
from .forms import OpprotunityPostForm
from django.urls import reverse_lazy, reverse
from datetime import datetime
from profiles_app.models import Student
from django.core.mail import send_mail
from django.contrib.auth.decorators import login_required


# Create your views here.
def post_detail(request, post_id):
	post = get_object_or_404(OpportunityPost, pk=post_id)
	return render(request, 'posts_app/detail.html', {'post': post})



@login_required
def post_create(request):
	form = OpprotunityPostForm()

	if request.method == "POST":
		form = OpprotunityPostForm(request.POST)

		if form.is_valid():
			post = form.save(commit=True)

			return HttpResponseRedirect(reverse_lazy('posts_app:post_detail', args=(post.pk,)))

	return render(request, 'posts_app/create.html', {'form': form})
		




def posts_list(request):
	posts = OpportunityPost.objects.filter(publish_date__month__gte=datetime.now().month-3)

	return render(request, 'posts_app/list.html', {'posts': posts})





@login_required
def send_to_all(request, post_id):
	# create a view to select stream
	sent = False
	post = get_object_or_404(OpportunityPost, pk=post_id)
	
	to_emails = [student.email for student in Student.objects.all()]

	subject = "3bags.com - " + post.title
	message = post.body + "\n\n" + "Go to post: " + post.get_absolute_url()

	send_mail(subject, message, "no_reply@3bags.com", to_emails)
	sent = True

	return render(request, 'posts_app/sent_to_all.html', {'to_emails': to_emails, 'sent': sent, 'post_id': post_id})




	