from django.shortcuts import render
from .models import 
# Create your views here.
from django.contrib import messages

def mealview(request, *args, **kargs):
    if request.method == 'POST':
        meal_number = request.POST.get('mealNumber')
        meal_cost = request.POST.get('mealCost')

        user = request.user
        
        
        Meal.objects.create(user_name=user, cost=meal_cost, quantity=meal_number)

        messages.success(request, 'Meal added successfully!')

        return redirect('')

    context = {
        'all': # Add your context data here if needed
    }
    return render(request, 'addmeal.html', context)