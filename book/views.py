from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from . import models

def MyFavouriteBook(request):
    if request.methot == 'GET':
        return request('Моя любимая книга - Атомные привычки')

def AboutMySelf(request):
    if request.method == 'GET':
        return request('Меня зовут Мадина. Я изучаю Backend.')

def MyDream(request):
    if request.methot == 'GET':
        return request('Моя мечта - стать Backend-разработчиком и открыть свой бизнес.')
        
def book_list_view(request):
    if request.method == 'GET':
        book_lst = models.Book.objects.all().order_by("-id")
        return render(request, "book_list.html", {"book_lst": book_lst})

def book_detail_view(request, id):
    if request.method == 'GET':
        book_id = get_object_or_404(models.Book, id=id)
        return render(request, ("book_detail.html", {"book_id": book_id}))


