#!/usr/bin/python
from django import forms

from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt

from images.models import Image
from django.template import Context, Template

from django.views.generic import ListView
from django.views.generic import DetailView


class ImageList(ListView):
    model = Image
    context_object_name = 'images'
    template_name = 'images.html'


class AddImageForm(forms.Form):
    file=forms.ImageField()
    title=forms.CharField(max_length=200)
    desc=forms.CharField(max_length=200)


@csrf_exempt
def AddImage(request):
    if request.method == 'POST':
        form = AddImageForm(request.POST, request.FILES)
        if form.is_valid():
            i=Image(title=form.cleaned_data['title'], desc=form.cleaned_data['desc'], file=form.cleaned_data['file'])
            i.save()
            return HttpResponseRedirect('/')
            else:
                form=AddImageForm()
    return render_to_response('form.html', {'form': form, })
