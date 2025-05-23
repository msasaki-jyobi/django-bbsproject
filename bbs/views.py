from django.shortcuts import render
from django.views import generic
from .models import Article
from django.urls import reverse_lazy
from .forms import SearchForm

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

def search(request):
    articles = None
    searchform = SearchForm(request.GET)

    if searchform.is_valid():
        query = searchform.cleaned_data['words'] # フォームに入ってるデータを代入
        articles = Article.objects.filter(content__icontains=query)
        print(f"articles:{articles}")
        return render(request, 'bbs/result.html', {'articles':articles, 'searchform':searchform})
