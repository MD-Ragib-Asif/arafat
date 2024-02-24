# models.py inside the meal app
from django.contrib.auth.models import User
from django.db import models

'''
CREATE TABLE `meal_meal` (`id` bigint AUTO_INCREMENT NOT 
NULL PRIMARY KEY, `date` date NOT NULL, `meal_count` inte
ger NOT NULL, `user_id` integer NOT NULL);
ALTER TABLE `meal_usermealcost` ADD CONSTRAINT `meal_user
mealcost_user_id_b0578208_fk_auth_user_id` FOREIGN KEY (`
user_id`) REFERENCES `auth_user` (`id`);
ALTER TABLE `meal_usermealcost` ADD CONSTRAINT `meal_user
mealcost_week_id_70eb05dc_fk_meal_mealcost_id` FOREIGN KE
Y (`week_id`) REFERENCES `meal_mealcost` (`id`);
ALTER TABLE `meal_meal` ADD CONSTRAINT `meal_meal_user_id
_67ec0b32_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERE
NCES `auth_user` (`id`);

'''
class Meal(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    meal_count = models.PositiveIntegerField(default=0)
    per_meal_cost = models.DecimalField(max_digits=10, decimal_places=2, default=50)

    def calculate_meal_cost(self):
        return self.meal_count * self.per_meal_cost
