from django.db import models
from django.utils import timezone
import django_filters
from django.core.files.storage import FileSystemStorage
from django.conf import settings
import os

class Project(models.Model): #Мои проекты
    project_name = models.CharField(max_length=60)
    status = models.CharField(max_length=60,default='in progress')
    created_at = models.DateTimeField(default= timezone.now)
    author= models.CharField(max_length=250, default='Author')
    tema= models.CharField(max_length=250, default='Theme')
    typep= models.CharField(max_length=50, default='Type')
    file=models.FileField(storage=FileSystemStorage(location=settings.MEDIA_ROOT), upload_to='logos', default='settings.MEDIA_ROOT/logos')
    description=models.CharField(max_length=250, default='Description')
    def publish(self):
        self.published_date = timezone.now()
        self.save()
    def extension(self):
        project_name, typep= os.path.splitext(self.file.project_name)
    def css_class(self):
        project_name, typep= os.path.splitext(self.file.project_name)
        if typep=='xlsx':
            return 'xlsx'
        if typep=='csv':
            return 'csv'
        return 'other'
    def __str__(self):
        return self.project_name
    def state(self):
        self.save()
    class Meta:
        verbose_name_plural = 'Проекты'
        verbose_name ='Проект' 
        ordering = ['-created_at']
class Share(models.Model):
    author=models.OneToOneField(Project ,on_delete=models.CASCADE, null=True)
    teammate=models.CharField(max_length=50)
    def __str__(self):
        return self.author

class ProjectFilter(django_filters.FilterSet):
    class Meta:
        model = Project
        fields=['created_at','tema', 'typep']
        
class Project_str(models.Model):
    project=models.ForeignKey(Project, on_delete= models.CASCADE)
    #size=models.FileField(allow_empty_file= False)

class Comment(models.Model):
    project=models.ForeignKey(Project, on_delete= models.CASCADE)
    author_name=models.CharField('имя автора', max_length=100)
    comment_text=models.TextField('текст комментария')
    def __str__(self):
        return self.project_name
    class Meta:
        verbose_name='Комментарий к проекту'
        verbose_name_plural='Комментарии к проекту'
        
class Task(models.Model):
    project=models.ForeignKey(Project, on_delete= models.CASCADE)
    name_task=models.CharField('Название задачи', max_length=25)
    def __str__(self):
        return self.name_task
    
        
