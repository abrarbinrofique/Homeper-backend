# Generated by Django 4.2.14 on 2024-08-15 06:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('serviceslot', '0004_alter_serviceslot_chooce_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='serviceslot',
            name='chooce',
            field=models.CharField(choices=[('saturday 9AM to 2PM', 'saturday 9AM to 2PM'), ('Monday 5PM to 8PM', 'Monday 5PM to 8PM'), ('sunday 2PM to 5PM', 'sunday 2PM to 5PM')], max_length=50),
        ),
    ]
