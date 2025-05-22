from django.shortcuts import render, redirect
from django.views import generic
from .models import Article
from django.urls import reverse_lazy

class IndexView(generic.ListView):
    model = Article
    template_name = 'bbs/index.html'

class DetailView(generic.DetailView):
    model = Article
    template_name = 'bbs/detail.html'

class CreateView(generic.CreateView):
    model = Article
    template_name = 'bbs/create.html'
    fields = '__all__'

class UpdateView(generic.UpdateView):
    model = Article
    template_name = 'bbs/create.html'
    fields = '__all__'

class DeleteView(generic.DeleteView):
    model = Article
    template_name = 'bbs/delete.html'
    success_url = reverse_lazy('bbs:index')

def like(request, article_id):
    print(f"Article ID is: {article_id}")
    return redirect('bbs:index')  # リダイレクト
    
