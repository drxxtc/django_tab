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
    return render(request,'pr_id.html')  
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
def datesfilter(request):
    startdate=request.Get.get('from')
    enddate=request.Get.get('to')
    dates_Project=models.Project.objects.filter(data_lt=startdate).filter(data_gt=enddate)
    #context = {'dates_Project': dates_Project}
    return HttpResponse(serializers.serialize('json', dates_Project),
                     content_type='application/json')
    
#from django.conf import settings
from django.core.files.storage import FileSystemStorage
def simple_upload(request):
    if request.method=='POST' and request.files['myfile']:
        myfile=request.FILES['myfile']
        fs=FileSystemStorage()
        filename=fs.save(myfile.name, myfile)
        uploaded_file_url=fs.url(filename)
        return render(request, 'main.html', {'uploaded_file_url': uploaded_file_url
                                             })
    return render(request, 'main.html')
        
'''Оставить комментарий def leave_comment(request, project_id):
    try:
        p=models.Project.objects.get(id=project_id)
    except:
        raise Http404("Проект не найден")
    p.project
'''
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
  
    
