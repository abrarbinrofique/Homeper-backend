# Generated by Django 4.2.14 on 2024-08-15 06:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0004_alter_reviewmodel_ratting'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reviewmodel',
            name='ratting',
            field=models.IntegerField(choices=[(2, '⭐⭐'), (5, '⭐⭐⭐⭐⭐'), (1, '⭐'), (4, '⭐⭐⭐⭐'), (3, '⭐⭐⭐')]),
        ),
    ]