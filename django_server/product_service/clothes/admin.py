from django.contrib import admin

# Register your models here.
from clothes.models import Clothes,Styles,Producer

admin.site.register(Clothes)
admin.site.register(Styles)
admin.site.register(Producer)