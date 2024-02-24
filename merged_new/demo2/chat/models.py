from django.db import models
from django.contrib.auth.models import User

'''
CREATE TABLE `chat_chat` (`conv_id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY, 
`content` longtext NOT NULL, `dt`
 longtext NOT NULL, `user_id` integer NOT NULL);
ALTER TABLE `chat_chat` ADD CONSTRAINT `chat_chat_user_id
_bbe8a5b9_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERE
NCES `auth_user` (`id`);

'''
class Chat(models.Model):
    conv_id = models.AutoField(primary_key=True, null=False)
    content = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    dt = models.TextField(default='12')
