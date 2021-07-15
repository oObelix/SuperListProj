from django.shortcuts import render, redirect
from lists.models import Item


def home_page(request):
    """домашняя страница"""
    # return HttpResponse('<html><title>To-Do lists</title></html>')

    # TODO: Показывать несколько элементов в таблице
    # TODO: Поддержка более чем одного списка!

    if request.method == 'POST':
        Item.objects.create(text=request.POST['item_text'])
        return redirect("/")

    items = Item.objects.all()
    return render(request, "home.html", {'items': items})
