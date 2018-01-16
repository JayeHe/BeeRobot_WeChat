from django.shortcuts import render, redirect
from .models import Item


def home(request):
    if request.method == 'POST':
        Item.objects.create(text=request.POST['item_text'])
        return redirect('/chat/')
    items = Item.objects.all()
    count = request.COOKIES.get('count')
    if count:
        count = int(count)+1
    else:
        count = 1
    res = render(request, 'home.html', {'items': items, 'counter': count})
    res.set_cookie('count', count)
    return res
