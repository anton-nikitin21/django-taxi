from django.contrib import admin
from django.utils.html import format_html
from .models import Car, Driver, Order


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ('brand', 'car_class', 'license_plate', 'color', 'year', 'image_preview')
    search_fields = ('brand', 'license_plate', 'color')
    list_filter = ('car_class', 'year')
    ordering = ('brand',)

    def image_preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="80" height="50" style="object-fit: cover; border-radius: 6px;" />', obj.image.url)
        return 'Нет фото'

    image_preview.short_description = 'Фото'


@admin.register(Driver)
class DriverAdmin(admin.ModelAdmin):
    list_display = (
        'last_name',
        'first_name',
        'patronymic',
        'birth_date',
        'inn',
        'car'
    )
    search_fields = (
        'last_name',
        'first_name',
        'patronymic',
        'inn',
        'passport_series',
        'passport_number'
    )
    list_filter = ('birth_date', 'car')
    ordering = ('last_name', 'first_name')


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = (
        'order_date',
        'order_time',
        'pickup_address',
        'destination_address',
        'passengers_count',
        'route_length',
        'driver'
    )
    search_fields = ('pickup_address', 'destination_address', 'driver__last_name')
    list_filter = ('order_date', 'passengers_count', 'driver')
    ordering = ('-order_date', '-order_time')