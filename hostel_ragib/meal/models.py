from django.db import models
from users.models import User

class Meal(models.Model):
    user_name = models.ForeignKey(User, on_delete=models.CASCADE)
    cost = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField()
    rating = models.IntegerField(choices=[(i, i) for i in range(1, 6)])
    class Meta:
        db_table = "meal"

    def __str__(self):
        return f'{self.quantity} Meal eaten by {self.user_name}'
    
 
class MealCount(models.Model):
    user_name = models.OneToOneRel(User, on_delete=models.CASCADE)
    total_meal = models.PositiveIntegerField(default=0)
    total_cost = models.DecimalField(max_digits=10, decimal_places=2, default=0)


    class Meta:
        db_table = "mealcount"

    def __str__(self):
        # permeal = self.total_cost/self.total_cost
        return f'User {self.user_name} details'
    
    # @property
    # def net_total_cost(self):
    #     print(Meal.objects.all().aaggregate(models.Sum("cost")))
    #     return 0