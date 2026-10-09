from django.db import models


class Car(models.Model):
    CLASS_CHOICES = [
        ('business', 'Бизнес'),
        ('economy', 'Эконом'),
        ('shit', 'Дно'),
    
    ]
    created_at = models.DateTimeField(auto_now_add=True)
    brand = models.CharField(max_length=100, verbose_name='Марка')
    car_class = models.CharField(
        max_length=20,
        choices=CLASS_CHOICES,
        verbose_name='Класс'
    )
    license_plate = models.CharField(max_length=20, unique=True, verbose_name='Госномер')
    color = models.CharField(max_length=50, verbose_name='Цвет')
    year = models.PositiveIntegerField(verbose_name='Год выпуска')
    image = models.ImageField(
        upload_to='cars/',
        blank=True,
        null=True,
        verbose_name='Фотография автомобиля'
    )
    
    def __str__(self):
        return f"{self.brand} ({self.license_plate})"

    class Meta:
        verbose_name = 'Автомобиль'
        verbose_name_plural = 'Автомобили'


class Driver(models.Model):
    last_name = models.CharField(max_length=100, verbose_name='Фамилия')
    first_name = models.CharField(max_length=100, verbose_name='Имя')
    patronymic = models.CharField(max_length=100, verbose_name='Отчество')
    birth_date = models.DateField(verbose_name='Дата рождения')
    inn = models.CharField(max_length=12, unique=True, verbose_name='ИНН')
    passport_series = models.CharField(max_length=10, verbose_name='Серия паспорта')
    passport_number = models.CharField(max_length=20, verbose_name='Номер паспорта')
    car = models.ForeignKey(
        Car,
        on_delete=models.CASCADE,
        related_name='drivers',
        verbose_name='Машина'
    )

    def __str__(self):
        return f"{self.last_name} {self.first_name} {self.patronymic}"

    class Meta:
        verbose_name = 'Водитель'
        verbose_name_plural = 'Водители'


class Order(models.Model):
    order_date = models.DateField(verbose_name='Дата')
    order_time = models.TimeField(verbose_name='Время')
    pickup_address = models.CharField(max_length=255, verbose_name='Адрес подачи такси')
    destination_address = models.CharField(max_length=255, verbose_name='Предположительный адрес следования')
    passengers_count = models.PositiveIntegerField(verbose_name='Количество пассажиров')
    route_length = models.DecimalField(
        max_digits=6,
        decimal_places=2,
        verbose_name='Ориентировочная длина маршрута (км)'
    )
    driver = models.ForeignKey(
        Driver,
        on_delete=models.CASCADE,
        related_name='orders',
        verbose_name='Водитель'
    )

    def __str__(self):
        return f"Заказ {self.order_date} {self.order_time} — {self.pickup_address}"

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

    