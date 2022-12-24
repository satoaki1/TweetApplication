from django.views.generic import TemplateView, CreateView, ListView, DetailView, DeleteView
from django.urls import reverse_lazy
from tweet.forms import TweetForm
from tweet.models import Tweet


class IndexView(TemplateView):
    template_name = 'index.html'


class TweetCreateView(CreateView):
    template_name = 'tweet_create.html'
    form_class = TweetForm
    success_url = reverse_lazy('tweet:tweet_create_complete')


class TweetCreateCompleteView(TemplateView):
    template_name = 'tweet_create_complete.html'


class TweetListView(ListView):
    template_name = 'tweet_list.html'
    model = Tweet


class TweetDetailView(DetailView):
    template_name = 'tweet_detail.html'
    model = Tweet


class TweetDeleteView(DeleteView):
    template_name = 'tweet_delete.html'
    model = Tweet
    success_url = reverse_lazy('tweet:tweet_list')