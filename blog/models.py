from django.db import models
from django.utils import timezone
from django.conf import settings

class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

class Job_Heykorean(models.Model):
    company_name = models.CharField(max_length=200)
    job_description = models.TextField()
    post_link = models.CharField(max_length=200)
    fetched_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    area = models.CharField(max_length=200)
    jobstyle = models.CharField(max_length=200)
    deadline = models.CharField(max_length=200)
    salary = models.CharField(max_length=200)

    def str(self):
        return " ".join([company_name, job_description, str(published_date)])