from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404,HttpResponseRedirect
from django.core import serializers
from . import models
from .forms import ProjectForm
from django.urls import reverse

#добавление проекта в таблицу
def main(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        form.save()       
        return redirect('progmod:main')
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
        return render(request, 'pr_id.html', {'uploaded_file_url': uploaded_file_url})
    return render(request, 'pr_id.html')
#переход на страницу проекта
def detail(request, project_id):
    try:
         p=models.Project.objects.get(id=project_id)
    except:
        raise Http404('Проект не найден')
    comment_list= p.comment_set.order_by('-id')[:10]
    return render(request, 'pr_id.html',{'project':p, 'comment_list': comment_list })

from pathlib import Path
def typedownload(request, file):
    tip=Path(file).suffix[1:].lower()
    return render(request, 'pr_id.html', {'tip': tip })

#Оставить комментарий 
def leave_comment(request, project_id):
    try:
        p=models.Project.objects.get(id = project_id)
    except:
        raise Http404("Проект не найден")
    p.comment_set.create(author_name = request.POST['name'], comment_text=request.POST['text'])
    return HttpResponseRedirect(reverse('progmod:detail', args=(p.id, )) )

#Paginator in Project
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger    
def post_list(request):  
    object_list = models.Task.published.all()  
    paginator = Paginator(object_list, 1)  
    page = request.GET.get('page')  
    try:  
        posts = paginator.page(page)  
    except PageNotAnInteger:  
        # Если страница не является целым числом, поставим первую страницу  
        posts = paginator.page(1)  
    except EmptyPage:  
        # Если страница больше максимальной, доставить последнюю страницу результатов  
        posts = paginator.page(paginator.num_pages)  
    return render(request,  
	          'pr_id.html',  
		  {'page': page,  
		   'posts': posts})
#создание новой задачи
def create_task(request):
    pass
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


                
