# Generated by Django 4.2.14 on 2024-07-13 16:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0007_remove_service_average_rating_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reviewmodel',
            name='ratting',
            field=models.IntegerField(choices=[('5', '⭐⭐⭐⭐⭐'), ('4', '⭐⭐⭐⭐'), ('2', '⭐⭐'), ('3', '⭐⭐⭐'), ('1', '⭐')]),
        ),
    ]
