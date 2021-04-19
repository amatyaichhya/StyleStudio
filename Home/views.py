from django.shortcuts import render
from .models import Category, Trending, Style, New, Top, Recommend


def index(request):
    category = Category.objects.all()[0:5]
    category1 = Category.objects.all()[5:10]
    trends = Trending.objects.all()[0:5]
    style = Style.objects.all()[0:5]
    new = New.objects.all()[0:5]
    new1 = New.objects.all()[5:10]
    return render(request, 'Home/index.html', {'category': category,
                                               'next_category': category1,
                                               'trend': trends, 'style': style,
                                               'F_row': new, 'L_row': new1})


def listing(request):
    tops = Top.objects.all()
    return render(request, 'Home/listing.html', {'tops': tops})


def detail(request):
    recommend = Recommend.objects.all()[0:5]
    recommend1 = Recommend.objects.all()[5:10]
    return render(request, 'Home/detail.html', {'recommend': recommend, 'recommend1': recommend1})
