# hostel-management-systems
BRACU CSE370 Project Hostel Manage System Web application.


* project name: hostel_manage
* Database Name: hostelDB

### Django Admin Credentials
* username: omi971
* password: 123

you can create your own superuser by this command below
```shell
python manage.py createsuperuser
```

### Add User Using Shell
```shell
python manage.py shell

from users.models import User
User.objects.all()
User.objects.create(username='Omi123', password='123', first_name='Nazmul', last
_name='Haque', email='Omi971@gmail.com', phone='123456', user_type='Member', hostel_
id='1')

```

### auth_user

username: ramim69
password: 123456789


### Hasibul Hostel Database

username: omi123 </br>
password: 123


### If database not updating 
Try This

```commandline
python manage.py makemigrations add_name
python manage.py migrate
```
