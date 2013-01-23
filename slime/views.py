#coding=utf8
from django.http import Http404
from django.shortcuts import render_to_response
from .models import Update

def slime(request):
    return render_to_response('slime.html')

def update(request):
    list = Update.objects.all().order_by('-date')
    updates = []
    for l in list:
        update = {}
        update['date'] = l.date
        update['content'] = l.content
        updates.append(update)
    return render_to_response('update.html',{'updates':updates})