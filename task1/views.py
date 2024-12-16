# Добавить вью news, которая будет возвращать отрендеренный 'news.html' и контекст, содержащий поле news - объект
# страницы, полученный с помощью Paginator из модуля django.core.paginator, как в примере из видео-урока.

from django.shortcuts import render
from django.urls import reverse
from django.views.generic import TemplateView
from django.http import HttpResponse
from django.core.paginator import Paginator
from .forms import UserRegister
from .models import Buyer, Game


class Task3Main(TemplateView):
    template_name = 'glavnaya.html'


class Task3Tovar(TemplateView):
    template_name = 'tovar.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['items'] = Game.objects.all()
        return context


class Task3Korzina(TemplateView):
    template_name = 'korzina.html'


def sign_up_by_django(request):
    info = {'form': UserRegister(), 'method': 'django'}
    if request.method == 'POST':
        form = UserRegister(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            password_repeat = form.cleaned_data['repeat_password']
            age = form.cleaned_data['age']

            if password != password_repeat:
                info['error'] = 'Пароли не совпадают'
            elif age < 18:
                info['error'] = 'Вы должны быть старше 18'
            elif Buyer.objects.filter(name=username).exists():
                info['error'] = 'Пользователь уже существует'
            else:
                Buyer.objects.create(name=username, balance=0.00, age=age)
                return HttpResponse(
                    f'Приветствуем, {username}!<br>'
                    f'<a href="{reverse("glavnaya")}">На главную</a>'
                )
        info['form'] = form
    return render(request, 'reg_page.html', info)


class News(TemplateView):
    template_name = 'news.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        news_list = Game.objects.all()
        paginator = Paginator(news_list, 5)
        page_number = self.request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        context['news'] = page_obj
        return context
