# Generated by Django 4.2.14 on 2024-07-15 14:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0009_alter_reviewmodel_ratting'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reviewmodel',
            name='ratting',
            field=models.IntegerField(choices=[('4', '⭐⭐⭐⭐'), ('1', '⭐'), ('3', '⭐⭐⭐'), ('2', '⭐⭐'), ('5', '⭐⭐⭐⭐⭐')]),
        ),
    ]
