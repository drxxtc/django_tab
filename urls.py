# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-
from django.urls import path
#from django.contrib.auth import views as views_auth
from .views import main, getList, ListView, project_list, proj, detail, leave_comment#, FilterView list, project_list
from django.conf import settings
from django.conf.urls.static import static
app_name="progmod"
urlpatterns = [
  path('main', main, name='main'),
  path('list', getList, name='getList'),
  path('table', ListView.as_view()),
  path('pr_list', project_list),
  path('proj', proj),
  path('<int:project_id>/', detail, name='detail'),
  path('<int:project_id>/leave_comment/', leave_comment, name='leave_comment')
  
    
  
  #path('json/datesfilter', datesfilter)
  #path('filter', FilterView.as_view()),
 # path('myproject', proj, name='myproject')
  #path('list', list, name='list')
  #path('project_list', project_list, name='project_list')
  #path('/filt', getList, name='filt')

]

if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
