
from django.db import models
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import Meal, MealCount


def update_meal_count(user):
    total_meal = Meal.objects.filter(user_name=user).aggregate(models.Sum('quantity'))['quantity__sum']
    total_cost = Meal.objects.filter(user_name=user).aggregate(models.Sum('cost'))['cost__sum']

    meal_count, created = MealCount.objects.get_or_create(user_name=user)
    meal_count.total_meal = total_meal if total_meal is not None else 0
    meal_count.total_cost = total_cost if total_cost is not None else 0
    meal_count.save()


@receiver(post_save, sender=Meal)
@receiver(post_delete, sender=Meal)
def meal_change(sender, instance, **kwargs):
    update_meal_count(instance.user_name)
