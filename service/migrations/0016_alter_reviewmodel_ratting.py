# Generated by Django 4.2.14 on 2024-08-08 10:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0015_alter_reviewmodel_ratting'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reviewmodel',
            name='ratting',
            field=models.IntegerField(choices=[(5, '⭐⭐⭐⭐⭐'), (2, '⭐⭐'), (3, '⭐⭐⭐'), (4, '⭐⭐⭐⭐'), (1, '⭐')]),
        ),
    ]
