# Generated by Django 4.2.14 on 2024-07-16 07:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0010_alter_reviewmodel_ratting'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reviewmodel',
            name='ratting',
            field=models.IntegerField(choices=[(1, '⭐'), (5, '⭐⭐⭐⭐⭐'), (2, '⭐⭐'), (4, '⭐⭐⭐⭐'), (3, '⭐⭐⭐')]),
        ),
    ]
