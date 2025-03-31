from http.client import HTTPResponse

from django.http import Http404
from django.shortcuts import render
from main.models import Car, Sale, Client


def cars_list_view(request, model=None):
    # получите список авто
    search_query = request.GET.get('q', '')

    if search_query:
        car_list = Car.objects.filter(model__icontains=search_query)
    else:
        car_list = Car.objects.all()

    template_name = 'main/list.html'
    context = {
        'cars': car_list
    }
    return render(request, template_name, context)  # передайте необходимый контекст


def car_details_view(request, car_id):
    # получите авто, если же его нет, выбросьте ошибку 404
    try:
        car = Car.objects.get(id=car_id)
        template_name = 'main/details.html'
        context = {
            'car': car
        }
        return render(request, template_name, context)  # передайте необходимый контекст
    except:
        raise Http404('Автомобиль не найден')


def sales_by_car(request, car_id):
    try:
        sales = Sale.objects.filter(car=car_id)
        # получите авто и его продажи
        template_name = 'main/sales.html'
        context = {
            'sales': sales
        }
        print(sales)
        return render(request, template_name, context)  # передайте необходимый контекст
    except Car.DoesNotExist:
        raise Http404('Автомобиль не найден')