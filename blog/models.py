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
    fetched_date = models.DateTimeField(default=timezone.now, null=True)
    published_date = models.DateTimeField(blank=True, null=True)
    area = models.CharField(max_length=200, null=True)
    jobstyle = models.CharField(max_length=200, null=True)
    deadline = models.CharField(max_length=200, null=True)
    salary = models.CharField(max_length=200, null=True)

    def str(self):
        return " ".join([company_name, job_description, str(published_date)])

class Job_Jobkorea(models.Model):
    company_name = models.CharField(max_length=200)
    company_etc = models.CharField(max_length=200, null=True)
    job_title = models.CharField(max_length=200)
    job_description = models.TextField()
    post_link = models.CharField(max_length=200)
    published_date = models.CharField(max_length=200, null=True)
    area = models.CharField(max_length=200, null=True)
    jobstyle = models.CharField(max_length=200, null=True)
    deadline = models.CharField(max_length=200, null=True)
    salary = models.CharField(max_length=200, null=True)
    education = models.CharField(max_length=200, null=True)
    experience = models.CharField(max_length=200, null=True)
    etc = models.CharField(max_length=200, null=True)

    def str(self):
        return " ".join([company_name, job_description, str(published_date)])