# В этом домашнем задании Вам предстоит добавить Ваши модели Game и Buyer, созданные в предыдущих заданиях, в админку.
# Добавьте в файл admin.py Вашего приложения следующие классы:
# GameAdmin - админ-класс модели Game, в него добавьте:
# Фильтрацию по полям size и cost.
# Отображение полей title, cost и size при отображении всех полей списком.
# Поиск по полю title.
# Ограничение кол-ва записей до 20.
# GameAdmin - админ-класс модели Game, в него добавьте:
# Фильтрацию по полям balance и age.
# Отображение полей name, balance и age при отображении всех полей списком.
# Поиск по полю name.
# Ограничение кол-ва записей до 30.
# Доступным только для чтения поле balance.
# *Не забудьте наследовать ваши админ-классы от ModelAdmin и добавить к ним декоратор @admin.register.

from django.contrib import admin

from .models import Game, Buyer


@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    list_display = ('title', 'cost', 'size')

    list_filter = ('size', 'cost')

    search_fields = ('title',)

    list_per_page = 20


@admin.register(Buyer)
class BuyerAdmin(admin.ModelAdmin):
    list_display = ('name', 'balance', 'age')

    list_filter = ('balance', 'age')

    search_fields = ('name',)

    list_per_page = 30

    readonly_fields = ('balance',)
