from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from blogging.models import Post

class BlogListView(ListView):
    """Only lists blogs with published dates, ordered by reversed published date"""
    queryset = Post.objects.exclude(published_date__isnull=True).order_by("-published_date")
    template_name = 'blogging/list.html'

class BlogDetailView(DetailView):
    """Only renders blogs that have a published date"""
    queryset = Post.objects.exclude(published_date__isnull=True)
    template_name = 'blogging/detail.html'
