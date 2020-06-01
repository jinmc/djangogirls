import django_filters
from .models import Job_Jobkorea

class JobkoreaFilter(django_filters.FilterSet):
    class Meta:
        model = Job_Jobkorea
        # published = CharFilter(field_name='job_description', method=filter_not_empty)
        # fields = ['job_description', 'area']
        fields = {
            'company_name': ['contains'],
            'job_title': ['contains'],
            'job_description': ['contains'],
            'area': ['contains'],
            'experience': ['contains'],
            'education': ['contains'],
        }