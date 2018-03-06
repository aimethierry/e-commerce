from django.conf import settings
from django.db import models
from cart.models import Cart


class UserCheckout(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, null=True, blank=True)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.email


ADDRESS_TYPE = (
    ('billing', 'billing'),
    ('shipping', 'shipping'),
)

class UserAddress(models.Model):
    user = models.ForeignKey(UserCheckout)
    type = models.CharField(max_length=150, choices=ADDRESS_TYPE) 
    street = models.CharField(max_length=150)
    city = models.CharField(max_length=150)
    zipcode = models.CharField(max_length=150)


    def __str__(self):
        return self.street




class Order(models.Model):
    cart = models.ForeignKey(Cart)
    user = models.ForeignKey(UserCheckout)
    shipping_address = models.ForeignKey(UserAddress, related_name = 'shipping_address')
    billing_address = models.ForeignKey(UserAddress, related_name = 'billing_address')
    shipping_total_price = models.DecimalField(decimal_places=2, max_digits=50,default=5.99)
    order_total = models.DecimalField(decimal_places=2, max_digits=50)

    def __str__(self):
        return str(self.cart.id)


