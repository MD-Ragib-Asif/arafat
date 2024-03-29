# Generated by Django 4.2.7 on 2023-12-05 03:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('username', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('password', models.CharField(default='123', max_length=20)),
                ('first_name', models.CharField(max_length=10)),
                ('last_name', models.CharField(max_length=10)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=14)),
                ('user_type', models.CharField(default='Member', max_length=10)),
                ('hostel_id', models.CharField(max_length=10)),
            ],
        ),
    ]
