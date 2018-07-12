# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from .models import Post

from django.template.loader import get_template
from datetime import datetime

from django.shortcuts import redirect


def homepage(request):
    template = get_template('index.html')
    posts = Post.objects.all()
    # post_list = list()
    now = datetime.now()

    # for count, post in enumerate(posts):
    #     # post_list.append("No.{0} {1} {2}".format(count, post, "<br>"))
    #     post_list.append("No.{0} {1} {2}".format(count, post, "<hr>"))
    #     post_list.append("<small>.{0} {1}</small><br><br>".format(count, post.body, "<br>"))

    html = template.render(locals())

    # return HttpResponse(post_list)
    return HttpResponse(html)


def show_post(request, slug):
    template = get_template('post.html')
    try:
        post = Post.objects.get(slug=slug)
        print '-------Post:   ', post
        if post:
            html = template.render(locals())
            return HttpResponse(html)
    except:
        return redirect('/')
