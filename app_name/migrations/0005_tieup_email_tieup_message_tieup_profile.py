# Generated by Django 4.2.2 on 2023-07-17 10:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_name', '0004_tieup'),
    ]

    operations = [
        migrations.AddField(
            model_name='tieup',
            name='email',
            field=models.EmailField(max_length=254, null=True),
        ),
        migrations.AddField(
            model_name='tieup',
            name='message',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='tieup',
            name='profile',
            field=models.TextField(null=True),
        ),
    ]