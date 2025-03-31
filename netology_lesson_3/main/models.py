from django.db import models
from imagekit.processors import ResizeToFill
from imagekit.models import ProcessedImageField

class Client(models.Model):
    name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=50)
    date_of_birth = models.DateField()
    phone_number = models.CharField(max_length=20)

    def __str__(self):
        return f'{self.name} {self.middle_name} {self.last_name}'

GEARBOX_CHOICES = (
    ('manual', 'Механика'),
    ('automatic', 'Автомат'),
    ('вариатор', 'CVT'),
    ('robot', 'Робот')
)

FUEL_TYPE_CHOICES = (
    ('gasoline', 'Бензин'),
    ('diesel', 'Дизель'),
    ('hybrid', 'Гибрид'),
    ('electro', 'Электро')
)

BODY_TYPE_CHOICES = (
    ('sedan', 'Седан'),
    ('hatchback', 'Хэтчбек'),
    ('SUV', 'Внедорожник'),
    ('wagon', 'Универсал'),
    ('minivan', 'Минивэн'),
    ('pickup', 'Пикап'),
    ('coupe', 'Купе'),
    ('cabrio', 'Кабриолет')
)

DRIVE_UNIT_CHOICES = (
    ('rear', 'Задний'),
    ('front', 'Передний'),
    ('full', 'Полный')
)

class Car(models.Model):
    model = models.CharField(max_length=50, default='KIA')
    year = models.IntegerField(default = 2025)
    color = models.CharField(max_length=50, default='black')
    mileage = models.IntegerField(default=0)
    volume = models.FloatField(default=1.6)
    body_type = models.CharField(max_length=50, choices=BODY_TYPE_CHOICES, default='sedan')
    drive_unit = models.CharField(max_length=50, choices=DRIVE_UNIT_CHOICES, default='full')
    gearbox = models.CharField(max_length=50, choices=GEARBOX_CHOICES, default='automatic')
    fuel_type = models.CharField(max_length=50, choices=FUEL_TYPE_CHOICES, default='gasoline')
    price = models.IntegerField(default=500000)
    image = ProcessedImageField(
        upload_to='cars/',
        processors=[ResizeToFill(360, 267)],
        format='JPEG',
        options={'quality': 80},
        blank=True,
        null=True
    )

    def __str__(self):
        return f'{self.model} {self.year} {self.color}'

class Sale(models.Model):
    client = models.ForeignKey(Client, on_delete = models.CASCADE, default="1")
    car = models.ForeignKey(Car, on_delete = models.CASCADE, default="1")
    created_at = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return f'{self.client} {self.car} {self.created_at}'