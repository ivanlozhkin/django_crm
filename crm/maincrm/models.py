from django.db import models


class Loyalty(models.Model):
    type_loyalty = models.CharField(max_length=50)
    date = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.type_loyalty


class StatusOrder(models.Model):
    status = models.CharField(max_length=50)
    date = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.status


class TypeOfWork(models.Model):
    type_of_work = models.CharField(max_length=50)
    date = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.type_of_work


class Customer(models.Model):
    company_name = models.CharField(max_length=200)
    customer_name = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    loyal = models.ForeignKey(
        Loyalty,
        on_delete=models.PROTECT,
        related_name='customer',
        null=True,
    )
    phone = models.CharField(max_length=15)

    def __str__(self):
        return self.customer_name


class Order(models.Model):
    # id = models.PrimaryKey()
    customer = models.ForeignKey(Customer, related_name='order', on_delete=models.CASCADE, null=True)
    type_of_work = models.ForeignKey(TypeOfWork, related_name='order_type', on_delete=models.CASCADE, null=True)
    description = models.TextField(max_length=500)
    status = models.ForeignKey(StatusOrder,related_name='order_status', on_delete=models.CASCADE, null=True)
    price = models.IntegerField()

    def __str__(self):
        return self.customer


