# Generated by Django 5.1.3 on 2024-11-18 22:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0002_alter_userprofile_telefone'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='nome_completo',
            field=models.CharField(default='Nome não informado', max_length=100),
        ),
    ]
