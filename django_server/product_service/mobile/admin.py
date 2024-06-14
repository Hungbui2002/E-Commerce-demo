from django.contrib import admin

# Register your models here.
from mobile.models import Mobile,Producer,Types

admin.site.register(Mobile)
admin.site.register(Types)
admin.site.register(Producer)