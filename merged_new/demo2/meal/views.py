# views.py inside the meal app
from django.shortcuts import render, redirect
from .models import Meal
from django.contrib.auth.decorators import login_required


@login_required
def add_meal(request):
    print("----------1-----------------")
    if request.method == 'POST':
        meal_count = request.POST.get('meal_count')
        per_meal_cost = request.POST.get('per_meal_cost')
        user = request.user

        meal, created = Meal.objects.get_or_create(user=user)
        meal.meal_count += int(meal_count)
        # meal.per_meal_cost = float(per_meal_cost)
        meal.save()
        print("------------2---------------")
        # return redirect('meal/view_meal_cost.html')
        return render(request, 'users/index.html')

    print("-----------3----------------")
    return render(request, 'meal/add_meal.html')


@login_required
def view_meal_cost(request):
    user = request.user
    print(f"user: {user}")
    meal = Meal.objects.get(user=user)
    print(f"meal: {meal}")
    total_cost = meal.calculate_meal_cost()
    print(f"cost: {total_cost}")

    return render(request, 'meal/view_meal_cost.html', {'total_cost': total_cost})
