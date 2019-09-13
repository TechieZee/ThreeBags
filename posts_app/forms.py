from django import forms
from .models import OpportunityPost

class OpprotunityPostForm(forms.ModelForm):
	class Meta:
		model = OpportunityPost
		fields = ('title', 'body')

