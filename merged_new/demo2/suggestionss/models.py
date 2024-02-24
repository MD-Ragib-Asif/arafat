from django.db import models

from django.contrib.auth.models import User


'''
CREATE TABLE `suggestionss_suggestions` (`sugg_id` intege
r AUTO_INCREMENT NOT NULL PRIMARY KEY, `content` longtext
 NOT NULL, `dt` longtext NOT NULL, `user_id` integer NOT 
NULL);
ALTER TABLE `suggestionss_suggestions` ADD CONSTRAINT `su
ggestionss_suggestions_user_id_36a0bc20_fk_auth_user_id` 
FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);  
'''

class Suggestions(models.Model):
    sugg_id = models.AutoField(primary_key=True, null=False)
    content = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    dt = models.TextField(default='12')
