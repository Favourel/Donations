from django.shortcuts import render
from django.views.generic import TemplateView


# Create your views here.


def home_view(request):
    return render(request, "main/index.html")


def about_view(request):
    return render(request, "main/ABOUT.html")


def services_view(request):
    template = ""
    if request.path == "/services/for-individuals/":
        template = "main/services_for_individuals.html"
    elif request.path == "/services/for-churches-institutions/":
        template = "main/services_for_churches_institutions.html"
    elif request.path == "/services/for-professional-advisory/":
        template = "main/services_for_professional_advisory.html"
    return render(request, template)


def ministries_view(request):
    template = ""
    if request.path == "/ministries/grants/":
        template = "main/ministries_grants.html"
    elif request.path == "/ministries/seminary-scholarships/":
        template = "main/ministries_seminary_scholarships.html"

    elif request.path == "/ministries/for-professional-advisory/":
        template = "main/ministries_professional_advisory.html"
    return render(request, template)


def financial_info_view(request):
    template = ""
    if request.path == "/financial-info/terms-to-know/":
        template = "main/financial_info_terms_to_know.html"
    elif request.path == "/financial-info/investment-philosophy/":
        template = "main/financial_info_investment_philosophy.html"

    elif request.path == "/financial-info/wespath-institutional-investments/":
        template = "main/financial_info_wespath_institutional_investments.html"
    return render(request, template)


def news_events_view(request):
    template = ""
    if request.path == "/news-events/foundation-news/":
        template = "main/news_events_foundation_news.html"
    elif request.path == "/news-events/legacies-newsletter/":
        template = "main/news_events_legacies_newsletter.html"

    elif request.path == "/news-events/market-financial-news/":
        template = "main/financial_info_wespath_institutional_investments.html"

    elif request.path == "/news-events/events/":
        template = "main/news_events_events.html"

    return render(request, template)


def give_a_gift_view(request):
    template = ""
    if request.path == "/give-a-gift/donate-now/":
        template = "main/give_a_gift_donate_now.html"
    elif request.path == "/give-a-gift/ways-to-give/":
        template = "main/give_a_gift_ways_to_give.html"

    return render(request, template)