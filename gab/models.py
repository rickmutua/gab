from django.db import models

from django.template.defaultfilters import slugify

# Create your models here.


class Category(models.Model):

    name = models.CharField(max_length=100, unique=True)

    image = models.ImageField(upload_to='categories/')

    slug = models.SlugField(max_length=50, unique=True)

    def __str__(self):

        return self.name

    @classmethod
    def single_category(cls, category_id, category_slug):

        category = cls.objects.filter(id=category_id, name=category_slug).all()

        return category


class Box(models.Model):

    category = models.ManyToManyField(Category)

    name = models.CharField(max_length=100, unique=True)

    slug = models.SlugField(max_length=100, unique=True)

    image = models.ImageField(upload_to='boxes/')

    quantity = models.CharField(max_length=250, blank=True)

    quality = models.CharField(max_length=250, blank=True)

    feeds = models.CharField(max_length=250, blank=True)

    price = models.DecimalField(max_digits=10, decimal_places=2)

    shipping = models.CharField(max_length=250, blank=True)

    def __str__(self):
        return self.name

    @classmethod
    def single_box(cls, box_id, box_slug):

        box = cls.objects.filter(id=box_id, slug=box_slug).all()

        return box

    @classmethod
    def add_to_cart(cls, box_id, box_slug):

        box = cls.objects.filter(id=box_id, slug=box_slug).all()

        return box


class Product(models.Model):

    box = models.ForeignKey(Box, on_delete=models.CASCADE)

    name = models.CharField(max_length=100)

    image = models.ImageField(upload_to='products')

    description = models.TextField()

    def __str__(self):

        return self.name


class Order(models.Model):

    name = models.CharField(max_length=100)

    id_no = models.CharField(max_length=20)

    address = models.CharField(max_length=100)

    phone_no = models.CharField(max_length=10)

    request = models.TextField()

    order_date = models.DateTimeField(auto_now_add=True)


