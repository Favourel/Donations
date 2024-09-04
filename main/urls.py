from . import views as main_views
from django.urls import path

urlpatterns = [
    path('', main_views.home_view, name='home'),
    path('about/', main_views.about_view, name='about'),
    path('services/', main_views.services_view, name='services'),
    path('financial-info/', main_views.financial_info_view, name='financial_info'),
    path('ministries/', main_views.ministries_view, name='ministries'),
    path('news-events/', main_views.news_events_view, name='news_events'),
    path('give-a-gift/', main_views.give_a_gift_view, name='give_a_gift'),
]
