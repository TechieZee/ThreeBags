from django.db import models
from django.urls import reverse
# Create your models here.


class OpportunityPost(models.Model):
	title = models.CharField(max_length=50)
	# slug = models.SlugField(max_length=50, unique_for_date='publish_date')
	body = models.TextField()
	publish_date = models.DateTimeField(auto_now_add=True)

	class Meta:
		ordering = ('-publish_date',)


	def __str__(self):
		return self.title


	def get_absolute_url(self):
		return reverse('posts_app:post_detail',
			args=[self.pk])