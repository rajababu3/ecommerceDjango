from django.core.urlresolvers import reverse
from django.db import models
from django_extensions.db.models import TitleSlugDescriptionModel

class Category(models.Model):
    categoryName = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.categoryName

class Product(models.Model):
    category = models.ForeignKey(Category, default=1)
    title = models.CharField(max_length=250)
    description = models.TextField(max_length=300)
    price = models.DecimalField(decimal_places=2, max_digits=100)
    sale_price = models.DecimalField(decimal_places=2, max_digits=100, default=0.0, null=True, blank=True)
    slug = models.SlugField(unique=True)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ('title',)
        index_together = (('id', 'slug'),)


    def get_absolute_url(self):
        return reverse('product_detail', kwargs={"id":self.id, "slug": self.slug})
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

class VariationManager(models.Manager):
    def all(self):
        return super(VariationManager, self).filter(active=True)

    def sizes(self):
        return self.all().filter(category = 'size')

    def colors(self):
        return self.all().filter(category = 'color')

VAR_CATEGORY = (
    ('size', 'size'),
    ('color', 'color'),
    ('package', 'package')
)

class Variation(models.Model):
    product = models.ForeignKey(Product)
    category = models.CharField(max_length=120, choices=VAR_CATEGORY, default='size')
    title = models.CharField(max_length=120)
    image = models.ForeignKey(ProductImage, null=True, blank=True)
    price = models.DecimalField(max_digits=100, decimal_places=2, null=True, blank=True)
    active = models.BooleanField(default=True)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    object = VariationManager()

    def __str__(self):
        return self.title