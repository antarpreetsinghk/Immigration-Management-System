from django.contrib import admin
from .models import Lead, Application, Payment, Branch


admin.site.register(Lead)
admin.site.register(Application)
admin.site.register(Payment)
admin.site.register(Branch)
