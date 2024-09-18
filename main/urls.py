from . import views as main_views
from django.urls import path

urlpatterns = [
    path('', main_views.home_view, name='home'),
    path('about/', main_views.about_view, name='about'),

    path('services/for-individuals/', main_views.services_view, name='services_individuals'),
    path('services/for-churches-institutions/', main_views.services_view, name='services_churches_institutions'),
    path('services/for-professional-advisory/', main_views.services_view, name='services_professional_advisory'),

    path('ministries/grants/', main_views.ministries_view, name='ministries_grants'),
    path('ministries/seminary-scholarships/', main_views.ministries_view, name='ministries_seminary_scholarships'),
    path('ministries/clergy-leadership-training/', main_views.ministries_view,
         name='ministries_clergy_leadership_training'),

    path('financial-info/terms-to-know/', main_views.financial_info_view, name='financial_info_terms_to_know'),
    path('financial-info/investment-philosophy/', main_views.financial_info_view,
         name='financial_info_investment_philosophy'),
    path('financial-info/wespath-institutional-investments/', main_views.financial_info_view,
         name='financial_info_wespath_institutional_investments'),

    path('news-events/foundation-news/', main_views.news_events_view, name='news_events_foundation_news'),
    path('news-events/legacies-newsletter/', main_views.news_events_view, name='news_events_legacies_newsletter'),
    path('news-events/market-financial-news/', main_views.news_events_view, name='news_events_market_financial_news'),
    path('news-events/events/', main_views.news_events_view, name='news_events_events'),

    path('give-a-gift/donate-now/', main_views.give_a_gift_view, name='give_a_gift_donate_now'),
    path('give-a-gift/ways-to-give/', main_views.give_a_gift_view, name='give_a_gift_ways_to_give'),
]
