import django_filters
from .models import Project

class ProjFilt(django_filters.FilterSet):
    project_name= django_filters.CharFilter(lookup_expr='icontains')
    
    class Meta: 
        model= Project
        fields = {'project_name'}
    
class PrF(django_filters.FilterSet):
    name=django_filters.CharFilter(lookup_expr='iexact')
    
    class Meta:
        model=Project
        fields=['created_at']
