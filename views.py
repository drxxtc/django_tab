from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core import serializers
from . import models
from .forms import ProjectForm

#добавление проекта в таблицу
def main(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        form.save()
       
        return redirect('main')
    return render(request, 'main.html', 
    {'Project.status': 'ready','projectform': ProjectForm,
     'projects': models.Project.objects.all()})
#обновление страницы
def getList(request):
	projects = models.Project.objects.all()
	return HttpResponse(serializers.serialize('json', projects),
                     content_type='application/json')
#просто возращение страницы...    
def proj(request):
    return render(request,'myproject.html', {'proj': models.Project.objects.all()})    
#метод tables2 
from django_tables2 import SingleTableView#, SingleTableMixin 
from .tables import   ProjTab

class ListView(SingleTableView):
    model= models.Project
    table_class=ProjTab
    template_name="table.html"
    
from .filters import PrF  
def project_list(request):
    f= PrF(request.GET, queryset=models.Product.objects.all())
    return render(request, 'main.html', {'filter':f})
'''from django_filters.views import FilterView
from .filters import ProjFilt

class FilterView(SingleTableMixin, FilterView):
    model = models.Project
    table_class = ProjTab
    template_name='table.html'
    filterset_class = ProjFilt
    
предмтавление-функции 
    def list(request):
    model = models.Project.objects.all()
    filterset_class = ProjFilt(request.GET, model)
    table = models.Project
    return render(request=request, template_name="myproject.html", context = {"model": model, "table":table, "filterset_class": filterset_class})
''' 
  
    
    
    
    
    
    
'''def project_list(request):
    filter= models.ProjectFilter(request.GET, queryset = models.Project.objects.all())
    return render(request, 'main.html', {'filter': filter})'''
#фильтрация
'''def filt(request):
    queryset.filter(created_at__date__range=(request.POST, request.POST))
    return 0
'''    
#class ProjectListView(generics.ListAPIView):
    #serializer_class=ProjectListSerializer
#    filter_backends=(DjangoFilterBackend,)

'''def statustime(request):s
    proj=Project()
    proj.status='ready'
    proj.save()
    return render(request, 'main.html', 
    {'Project.status': 'ready','projectform': ProjectForm,
     'projects': models.Project.objects.all()})
    
from datetime import  datetime, timedelta
a= datetime.now()+timedelta(seconds=3)
if a == Project.created_at:'''

'''def post(self, request):
    pr_fr=ProjectForm(request.POST)
    if pr_fr.is_valid():
        pr_fr.save()
    response = {"data": "goes here"}
    return HttpResponse(json.dumps(response), 
    content_type='application/json')'''
