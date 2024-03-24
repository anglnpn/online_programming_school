from django.contrib import admin

from payments.models import Payments, Subscribe

admin.site.register(Payments)

admin.site.register(Subscribe)
