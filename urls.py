from django.urls import path
from django.contrib import admin

from feeds import views as newsfeed
urlpatterns =[
    path("home/",newsfeed.home,name="home"),
    path("bbc/",newsfeed.bbc,name='bbc'),
    path("washing/",newsfeed.washington,name="washington-post"),
    path("reuters/",newsfeed.reuters,name="reuters"),
    path("aljazeera/",newsfeed.aljazeera,name='aljazeera'),
    path("cnn/",newsfeed.cnn,name="cnn"),
    path("dw/",newsfeed.dw,name="dw"),
    path("espn",newsfeed.espn,name="espn"),
    path("great-goals/",newsfeed.greatgoals,name="great-goals"),
    path("sky-sports/",newsfeed.skysports,name="sky-sports"),
    path("soccernews/",newsfeed.soccernews,name="soccernews")
    
]