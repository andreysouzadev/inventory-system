# Generated by Django 5.1.3 on 2024-11-18 21:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='telefone',
            field=models.CharField(max_length=15),
        ),
    ]
