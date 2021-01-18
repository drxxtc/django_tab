import django_tables2 as tables
from .models import Project

class ProjTab(tables.Table):
    class Meta:
        model= Project
        #template_name="django_tables2/bootstrap4.html"
        fields=("project_name", "status", "created_at", "author", "tema", "typep")
