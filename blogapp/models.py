from django.db import models
from django.contrib.auth.models import User #user-authentication
from django.utils import timezone
# Create your models here.
class Post(models.Model):
	STATUS_CHOICES=(('draft', 'Draft'), ('published', 'Published'));
	title=models.CharField(max_length=264)
	slug=models.SlugField(max_length=264,unique_for_date='publish')
	author=models.ForeignKey(User,related_name='blog_posts',on_delete=models.CASCADE)
	body=models.TextField()
	publish=models.DateTimeField(default=timezone.now)
	created=models.DateTimeField(auto_now_add=True) #datetime of create() action
	updated=models.DateTimeField(auto_now=True)  #datetime of save() actionpip
	status=models.CharField(max_length=10,choices=STATUS_CHOICES,default='draft')
	class Meta:
		ordering=('-publish',)
		def __str__(self):			#for admin-page-display
			return self.title



