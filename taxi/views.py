from django.db.models import Q
from django.shortcuts import render, get_object_or_404
from .models import Car, Driver, Order

def home(request):
    cars = Car.objects.all().order_by('-created_at')
    drivers = Driver.objects.select_related('car').all()
    orders = Order.objects.select_related('driver', 'driver__car').all().order_by('-order_date', '-order_time')

    context = {
        'cars': cars[:4],
        'drivers': drivers[:3],
        'orders': orders[:5],
        'cars_count': cars.count(),
        'drivers_count': drivers.count(),
        'orders_count': orders.count(),
    }
    return render(request, 'taxi/home.html', context)


def car_list(request):
    cars = Car.objects.all().order_by('brand')
    return render(request, 'taxi/car_list.html', {'cars': cars})


def driver_list(request):
    drivers = Driver.objects.select_related('car').all().order_by('last_name', 'first_name')
    return render(request, 'taxi/driver_list.html', {'drivers': drivers})


def order_list(request):
    query = request.GET.get('q', '')
    orders = Order.objects.select_related('driver', 'driver__car').all().order_by('-order_date', '-order_time')

    if query:
        orders = orders.filter(
            Q(pickup_address__icontains=query) |
            Q(destination_address__icontains=query)
        )

    return render(request, 'taxi/order_list.html', {
        'orders': orders,
        'query': query,
    })


def car_detail(request, pk):
    car = get_object_or_404(Car, pk=pk)
    drivers = car.drivers.all()
    return render(request, 'taxi/car_detail.html', {
        'car': car,
        'drivers': drivers,
    })


def driver_detail(request, pk):
    driver = get_object_or_404(Driver.objects.select_related('car'), pk=pk)
    orders = driver.orders.all().order_by('-order_date', '-order_time')
    return render(request, 'taxi/driver_detail.html', {
        'driver': driver,
        'orders': orders,
    })


def order_detail(request, pk):
    order = get_object_or_404(Order.objects.select_related('driver', 'driver__car'), pk=pk)
    return render(request, 'taxi/order_detail.html', {
        'order': order,
    })