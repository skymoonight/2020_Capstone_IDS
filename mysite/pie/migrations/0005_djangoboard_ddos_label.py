# Generated by Django 3.0.3 on 2020-05-11 01:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pie', '0004_userinfo'),
    ]

    operations = [
        migrations.AddField(
            model_name='djangoboard',
            name='ddos_label',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
