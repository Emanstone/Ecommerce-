from django.db import models
from shortuuid.django_fields import ShortUUIDField
from django.utils.safestring import mark_safe
from authentication.models import Registration
from vendor.models import Vendor
from django.utils.translation import gettext as _

# Create your models here.

class Category(models.Model):
    category_id = ShortUUIDField(unique=True, length=10, prefix="cat", max_length=30, alphabet="abdc30")
    # Incase I want just numbers and one alphabet on each ID generated ;
    # category_id = ShortUUIDField(unique=True, length=11, prefix="cat", max_length=30, alphabet="0123456789abcdefghijklmnopqrstuvwxyz")
    name = models.CharField( max_length=100)
    image = models.ImageField(upload_to="category")
    date =  models.DateTimeField( auto_now_add=True)

    class Meta:
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name
    
    def category_image(self):
        return mark_safe('<img src="%s" width="90" height="40" />' % (self.image.url))





STATUSES = [
    ('draft', 'Draft'),
    ('rejected', 'Rejected'),
    ('in review', 'In Review'),
    ('approved', 'Approved'),
]


class Product(models.Model):
    product_id = ShortUUIDField(unique=True, length=20, prefix="pro", max_length=30, alphabet="abdc30")
    name = models.CharField(max_length=100)
    # user = models.ForeignKey(Registration, on_delete=models.CASCADE)
    user = models.ForeignKey(Registration, on_delete=models.CASCADE, related_name='vendors', limit_choices_to={'is_vendor': True, 'vendor_application_status': 'approved'})
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE, null=True, related_name='product')
    image = models.ImageField(_(""), upload_to="product_image")
    description = models.TextField(_(""))
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, related_name='product')
    product_details = models.TextField(_(""))
    old_price = models.DecimalField(max_digits=60, decimal_places=2)
    specification = models.TextField(_(""))
    # product_status = models.CharField(choices=[('status', 'Status')], max_length=50, default='in review')
    product_status = models.CharField(choices=STATUSES, max_length=50, default='in review')
    in_stock = models.BooleanField(default=False)
    features = models.BooleanField(default=False)
    digital = models.BooleanField(default=False)
    my_stock = models.CharField(max_length=50)
    date = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(null=True, blank=True)


    class Meta:
        verbose_name_plural = 'products'

    def __str__(self):
        return self.name
    
    def product_image(self):
        return mark_safe('<img src="%s" width="40" height="40" />' % (self.image.url))









# STATUSES = [
#     ('draft', 'Draft'),
#     ('rejected', 'Rejected'),
#     ('in review', 'In Review'),
#     ('approved', 'Approved'),
    
# ]


# class Product(models.Model):
#     product_id = ShortUUIDField(unique=True, length=20, prefix="pro", max_length=30, alphabet="abdc30")
#     name = models.CharField( max_length=100)
#     user = models.ForeignKey(Registration, on_delete=models.CASCADE)
#     vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE, null=True, related_name='product')
#     image = models.ImageField(_(""), upload_to="product_image")
#     description=models.TextField(_(""))
#     category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, related_name='product')
#     product_details = models.TextField(_(""))
#     old_price = models.DecimalField(max_digits=60, decimal_places=2)
#     specification = models.TextField(_(""))
#     # product_status = models.CharField(choices=[('status', 'Status')], max_length=50, default='in review')
#     product_status = models.CharField(choices=STATUSES, max_length=50, default='in review')
#     in_stock = models.BooleanField(default=False)
#     features = models.BooleanField(default=False)
#     digital = models.BooleanField(default=False)
#     my_stock = models.CharField(max_length=50)
#     date = models.DateTimeField(_(""), auto_now_add=True)
#     last_updated = models.DateTimeField(null=True, blank=True)


#     class Meta:
#         verbose_name_plural = 'products'

#     def __str__(self):
#         return self.name
    
#     def product_image(self):
#         return mark_safe('<img src="%s" width="40" height="40" />' % (self.image.url))




