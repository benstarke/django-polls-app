# Generated by Django 3.0.2 on 2020-03-04 12:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('today', '0010_auto_20200304_0439'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='postproblem',
            name='image',
        ),
    ]
