# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from .models import Post


def home_page(request):
    posts = Post.objects.all()
    post_list = list()
    for count, post in enumerate(posts):
        post_list.append("No.{0} {1}<br>".format(count, post))

    return HttpResponse(post_list)