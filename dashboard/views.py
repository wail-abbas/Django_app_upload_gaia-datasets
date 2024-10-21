from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse


#@login_required(login_url="/login/")
def index(request):
    context = {'segment': 'index'}

    html_template = loader.get_template('index.html')
    return HttpResponse(html_template.render(context, request))
