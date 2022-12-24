from django.urls import path
from . import views

app_name = 'tweet'
urlpatterns = [
    path('index/', views.IndexView.as_view(), name='index'),
    path('tweet/create/', views.TweetCreateView.as_view(), name='tweet_create'),
    path('tweet/create/complete/', views.TweetCreateCompleteView.as_view(), name='tweet_create_complete'),
    path('tweet/list/', views.TweetListView.as_view(), name='tweet_list'),
    path('tweet/detail/<uuid:pk>/', views.TweetDetailView.as_view(), name='tweet_detail'),
    path('tweet/delete/<uuid:pk>/', views.TweetDeleteView.as_view(), name='tweet_delete'),
]