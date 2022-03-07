from django.contrib import admin

# Register your models here.
from .models import MainPage, MainAboutProduct, About_us, Mini_aboutUs, Products


admin.site.register(MainAboutProduct)
admin.site.register(MainPage)
admin.site.register(About_us)
admin.site.register(Mini_aboutUs)
admin.site.register(Products)