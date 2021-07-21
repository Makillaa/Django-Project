from django.shortcuts import render, redirect
from django.views.generic import DetailView, UpdateView, DeleteView

from .models import Articles
from .forms import ArticlesForm


def news_home(request):
    news = Articles.objects.order_by('-date')
    return render(request, 'news/news_home.html', {'news': news})

class NewsDetailView(DetailView):
    model = Articles  # сама модель
    template_name = 'news/detail_view.html'  # шаблон
    context_object_name = 'article'  # ключевое название для передачи в шаблон


class NewsUpdateView(UpdateView):
    model = Articles  # сама модель
    template_name = 'news/create.html'  # шаблон

    form_class = ArticlesForm  # указываем какой класс будет использоваться для отображения формы(в самом классе
    # прописаны стили уже)


class NewsDeleteView(DeleteView):
    model = Articles  # сама модель
    success_url = '/news/'  # сюда перекидывает после удаления
    template_name = 'news/news-delete.html'  # шаблон


def create(request):
    error = ''
    if request.method == 'POST':
        form = ArticlesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/news')
        else:
            error = 'Форма была неверной'

    form = ArticlesForm()

    data = {
        'form': form,
        'error': error
    }
    return render(request, 'news/create.html', data)  # вторым параметром записываем какой шаблон возвращаем
