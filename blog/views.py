from django.shortcuts import render
from django.contrib.staticfiles.templatetags.staticfiles import static
from django.contrib.staticfiles.storage import staticfiles_storage
from django.shortcuts import render
from django.template import Context, Template
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

def main(request):
    return render(request, 'blog/index.html')
# Create your views here.
