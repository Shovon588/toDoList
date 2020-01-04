from django.shortcuts import render
from list.models import Item
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages
from datetime import datetime

# Create your views here.


def index(request):
    items = Item.objects.all().order_by('-done', 'time')[::-1]
    context = {'data': items}

    if request.method == 'POST':
        try:
            item = request.POST.get('item')
            Item.objects.create(item=item, time=datetime.now())
        except:
            pass

        try:
            if request.POST.get('yes'):
                item = 'YES'

            print(item)
        except:
            pass

        return HttpResponseRedirect(reverse('list:index'))

    return render(request, 'index.html', context=context)


def update(request, pk):
    data = Item.objects.get(id=pk)
    if request.method == 'POST':
        item = request.POST.get('item')
        data.item = item
        data.save()
        messages.success(request, 'Updated Successfully!')
        return HttpResponseRedirect(reverse('list:index'))

    context = {'data': data}
    return render(request, 'update.html', context=context)


def delete(request, pk):
    item = Item.objects.get(id=pk)
    context = {'item': item}
    if request.method == 'POST':
            if request.POST.get('yes'):
                item.delete()
            messages.success(request, 'Item Successfully Deleted!')
            return HttpResponseRedirect(reverse('list:index'))

    return render(request, 'delete.html', context=context)


def mark(request, pk):
    item = Item.objects.get(id=pk)
    context = {'item': item}

    if request.method == 'POST':
        if request.POST.get('yes'):
            item.done=True
            item.save()
        else:
            item.done = False
            item.save()

        messages.success(request, 'Marker Updated!')
        return HttpResponseRedirect(reverse('list:index'))

    return render(request, 'mark.html', context=context)