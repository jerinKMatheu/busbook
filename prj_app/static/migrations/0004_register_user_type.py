# Generated by Django 5.0.2 on 2024-02-24 14:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prj_app', '0003_register'),
    ]

    operations = [
        migrations.AddField(
            model_name='register',
            name='user_type',
            field=models.CharField(default='public', max_length=50),
        ),
    ]