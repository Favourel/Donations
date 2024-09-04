from django.shortcuts import render
from django.views.generic import TemplateView


# Create your views here.


def home_view(request):
    return render(request, "main/index.html")


def about_view(request):
    return render(request, "main/ABOUT.html")


def services_view(request):
    return render(request, "main/SERVICES.html")


def financial_info_view(request):
    return render(request, "main/FINANCIAL-INFO.html")


def ministries_view(request):
    return render(request, "main/MINISTRIES.html")


def news_events_view(request):
    return render(request, "main/news_events.html")


def give_a_gift_view(request):
    return render(request, "main/give_a_gift.html")
