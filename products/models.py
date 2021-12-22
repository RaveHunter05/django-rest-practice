from django.db import models

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        verbose_name = "Products Category"
        verbose_name_plural = "Product Categories"
        ordering = ["name"]

    def __str__(self):
        return "%s %s" % (self.name)


class Brand(models.Model):
    name = models.CharField(max_length=50)
    phoneNumber = models.CharField(max_length=50)

    class Meta:
        verbose_name = "Product Brand"
        verbose_name_plural = "Product Brands"
        ordering = ["name"]

    def __str__(self):
        return "%s %s" % (self.name)


class Products(models.Model):
    name = models.CharField(max_length=50)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"
        ordering = ["name"]

    def __str__(self):
        return "%s %s" % (self.name)
