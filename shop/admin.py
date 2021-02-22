from django.contrib import admin

# Register your models here.
from .models import product, contactus, aboutus, orders

admin.site.register(product)
admin.site.register(aboutus)
admin.site.register(contactus)
admin.site.register(orders)
