from django.db import models

# Create your models here.
# delivery/models.py


# class Client(models.Model):
#     name = models.CharField(max_length=100)
#     email = models.EmailField()
#     phone = models.CharField(max_length=15)
#     # Добавьте другие поля по необходимости


# class Employee(models.Model):
#     name = models.CharField(max_length=100)
#     position = models.CharField(max_length=100)

#     def change_position(self, new_position):
#         self.position = new_position
#         self.save()


# class Order(models.Model):
#     STATUS_CHOICES = [
#         ('Pending', 'Pending'),
#         ('Processing', 'Processing'),
#         ('Shipped', 'Shipped'),
#         ('Delivered', 'Delivered'),
#         ('Canceled', 'Canceled'),
#     ]

#     client = models.ForeignKey(Client, on_delete=models.CASCADE)
#     employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
#     date_created = models.DateTimeField(auto_now_add=True)
#     status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Pending')

#     def update_status(self, new_status):
#         self.status = new_status
#         self.save()


# from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='product_images/', null=True, blank=True)

    def __str__(self):
        return self.name


# class PostalShipment(models.Model):
#     STATUS_CHOICES = [
#         ('Pending', 'Pending'),
#         ('In transit', 'In transit'),
#         ('Out for delivery', 'Out for delivery'),
#         ('Delivered', 'Delivered'),
#         ('Failed', 'Failed'),
#     ]

#     sender_name = models.CharField(max_length=100)
#     recipient_name = models.CharField(max_length=100)
#     sender_address = models.CharField(max_length=200)
#     recipient_address = models.CharField(max_length=200)
#     status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Pending')
#     # Добавьте другие поля по необходимости
