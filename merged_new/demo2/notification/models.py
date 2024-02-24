from django.db import models
from django.contrib.auth.models import User


# Create your models here.
# Username, title, message, time
'''
CREATE TABLE `notification_notification` (`id` bigint AUT
O_INCREMENT NOT NULL PRIMARY KEY, `title` varchar(100) NO
T NULL, `message` longtext NOT NULL, `created_at` datetim
e(6) NOT NULL, `user_id` integer NOT NULL);
ALTER TABLE `notification_notification` ADD CONSTRAINT `n
otification_notification_user_id_e9d6f5f4_fk_auth_user_id
` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`); 
'''
class Notification(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
