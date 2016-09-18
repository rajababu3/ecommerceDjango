from django.core.urlresolvers import reverse
from django.db import models

# Create your models here.

class Product(models.Model):
    title = models.CharField(max_length=250)
    description = models.TextField(max_length=300)
    price = models.DecimalField(decimal_places=2, max_digits=100)
    sale_price = models.DecimalField(decimal_places=2, max_digits=100, default=0.0, null=True, blank=True)
    slug = models.SlugField(unique=True)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)
    active = models.BooleanField(default=True)

    class Meta:
        unique_together = ('title', 'slug')


    def get_absolute_url(self):
        return reverse('single-product', kwargs={"slug": self.slug})
    def __str__(self):
        return str(self.title)

class ProductImage(models.Model):
    product = models.ForeignKey(Product)
    image = models.ImageField(upload_to='products/images/')
    featured = models.BooleanField(default=False)
    active = models.BooleanField(default=True)
    thumbnail = models.BooleanField(default=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return self.product.title