# Generated by Django 5.1.1 on 2024-10-28 15:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0012_alter_reviewmodel_ratting'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reviewmodel',
            name='ratting',
            field=models.IntegerField(choices=[(5, '⭐⭐⭐⭐⭐'), (2, '⭐⭐'), (3, '⭐⭐⭐'), (4, '⭐⭐⭐⭐'), (1, '⭐')]),
        ),
    ]
