from django.shortcuts import render
from app.forms import *
from django.views.generic import FormView
from django.http import HttpResponse
# Create your views here.

class studentform(FormView):
    template_name='studentform.html'
    form_class=StudentForm
    def form_valid(self, form):
        data=form.cleaned_data
        return HttpResponse(str(data))
class emp_froms(FormView):
    template_name='emp_from.html'
    form_class=Emp_details

    def form_valid(self, form):
        form.save()
        return HttpResponse('data submited successfully')