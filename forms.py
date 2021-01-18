from django import forms
from .models import Project, Share
import time, threading
from django.utils.translation import ugettext_lazy as _

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
    


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields=('project_name', 'status', 'created_at')
        widgets={'status': forms.HiddenInput(), 'created_at': forms.HiddenInput()}
    def updateStatus(self, timeSec, project):
        time.sleep(timeSec)
        project.status="ready"
        project.save()
    def save(self, commit=True):
        project = super(ProjectForm, self).save(commit=False)
        print("self", super(ProjectForm,self))
        print("self, self")
        if commit:
            project.save()
        threading.Thread(target=self.updateStatus, args = (3, project,)).start()
        return project
class ShareForm(forms.ModelForm):
    class Meta:
        model = Share
        fields=['author', 'teammate']
        labels= {
                "author": _("Author     "),
                "teammate": _("Teammate    ")
                }

class DateForm(forms.Form):
    date = forms.DateTimeField(
            input_formats=['%d/%m/%Y %H:%M'],
            widget=forms.DateTimeInput(attrs={
            'class':'form-control datetimepicker-input',
            'data-target':'#datetimepicker1'
            })
            )
        
    
