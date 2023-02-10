from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=30)
    category_img = models.ImageField(upload_to='category_images/')
    description = models.CharField(max_length=30, null=True, blank=True)

    def __str__(self):
        return self.name


class Manufacture(models.Model):
    name = models.CharField(max_length=30)
    logo = models.ImageField(upload_to='category_images/')
    description = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=30)
    model = models.CharField(max_length=30, blank=True, null=True)
    technical_parameters = models.JSONField(default=dict)
    description = models.CharField(max_length=60)
    product_img = models.ImageField(upload_to='product_images/')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    manufacture = models.ForeignKey(Manufacture, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        result = f'{self.name} from {self.category} producer: {self.manufacture}'
        return result
