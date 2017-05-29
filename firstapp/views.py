# -*- coding: utf-8 -*-
from django.shortcuts import render, HttpResponse, redirect
from firstapp.models import Person, Article, Comment
from django.template import Context, Template
from firstapp.form import CommentForms
# Create your views here.

def first_site(request):
    person = Person(name='tianjigor', position= 'coding')
    html_string = '''<html>
                        <head>
                            <meta charset="utf-8">
                            <link rel="stylesheet"
                            href="https://cdnjs.cloudflare.com/ajax/libs/semantic-ui/2.2.6/semantic.css"
                            media="screen" title="no title">
                            <title>firstapp</title>
                        </head>
                        <body>
                            <h1 class="ui center aligned icon header">
                            <i class="hand spock icon"></i>
                                Hello, {{ person.name }}
                            </h1>
                        </body>
                    </html>'''
    t = Template(html_string)
    c = Context({'person':person})
    web_page =  t.render(c)

    return HttpResponse(web_page)


def index(request):
    queruset = request.GET.get('tag')
    if queruset:
        article = Article.objects.filter(tag=queruset)
    else:
        article = Article.objects.all()
    context = {}
    context['article_list'] = article
    return render(request, 'first_web_2.html', context)


def article_detail(request, page_num):
    if request.method == 'GET':
        form = CommentForms
        print 'request get'
    if request.method == 'POST':
        print 'request POST'
        form = CommentForms(request.POST)
        # is_valid表单对象的首要任务就是验证数据。对于绑定的表单实例，可以调用is_valid()方法来执行验证并返回一个表示数据是否合法的布尔值。
        if form.is_valid():
            print 'form pass'
            # cleaned_data表单类中的每个字段不仅负责验证数据，还负责“清洁”它们 —— 将它们转换为正确的格式。这是个非常好用的功能，因为它允许字段以多种方式输入数据，并总能得到一致的输出。
            name = form.cleaned_data['name']
            comment = form.cleaned_data['comment']
            c = Comment(name=name, comment=comment)
            c.save()
            return redirect(to='article_detail')
    print 'make sure here'
    context = {}
    comment_list = Comment.objects.all()
    article = Article.objects.get(id=page_num)
    context['article'] = article
    context['comment_list'] = comment_list
    context['form'] = form
    print dir(form)
    return render(request, 'article_detail.html', context)
