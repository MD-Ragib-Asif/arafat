from django.contrib import admin

# Register your models here.
from .models import Meal, MealCount

class MealView(admin.ModelAdmin):
    list_display = [
        '__str__',
        'rating',
    ]

class MealCountView(admin.ModelAdmin):
    list_display = [
        'user_name',
    ]

admin.site.register(Meal, MealView)
admin.site.register(MealCount, MealCountView)