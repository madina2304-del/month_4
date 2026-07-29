from django.shortcuts import render
from django.http import HttpResponse

def MyFavouriteBook(request):
    if request.methot == 'GET':
        return HttpResponse('Моя любимая книга - Атомные привычки')

def AboutMySelf(request):
    if request.method == 'GET':
        return HttpResponse('Меня зовут Мадина. Я изучаю Backend.')

def MyDream(request):
    if request.methot == 'GET':
        return HttpResponse('Моя мечта - стать Backend-разработчиком и открыть свой бизнес.')
        



