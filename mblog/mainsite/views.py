# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from .models import Post

from django.template.loader import get_template
from datetime import datetime


def home_page(request):
    template = get_template('index.html')

    posts = Post.objects.all()
    now = datetime.now()

    html = template.render(locals())

    return HttpResponse(html)