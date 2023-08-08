from django.urls import path
from .import views

urlpatterns = [
    path('',views.index,name='index'),
    path('event-shikkha/',views.events,name='events'),
    path('events-2-shikkha/',views.events_2,name='events_2'),
    path('events/details-shikkha/',views.events_details,name='events_details'),
    path('course-shikkha/',views.course,name='course'),
    path('course/details-shikkha/',views.course_details,name='course_details'),
    path('news-shikkha/',views.news,name='news'),
    path('news/details-shikkha/',views.news_details,name='news_details'),
    path('shop-shikkha/',views.shop,name='shop'),
    path('contact-shikkha/',views.contact,name='contact'),
    path('user-login/',views.login_user,name="login"),
    path('user-signup/',views.register_user,name="signup"),
    path('logout',views.logout,name='logout'),

   
]