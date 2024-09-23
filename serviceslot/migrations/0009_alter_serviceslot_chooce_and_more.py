# Generated by Django 5.1.1 on 2024-09-23 16:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('serviceslot', '0008_alter_serviceslot_service_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='serviceslot',
            name='chooce',
            field=models.CharField(choices=[('saturday 9AM to 2PM', 'saturday 9AM to 2PM'), ('Monday 5PM to 8PM', 'Monday 5PM to 8PM'), ('sunday 2PM to 5PM', 'sunday 2PM to 5PM')], max_length=50),
        ),
        migrations.AlterField(
            model_name='serviceslot',
            name='service_status',
            field=models.CharField(blank=True, choices=[('Done', 'Done'), ('cancel', 'cancel'), ('pending', 'pending')], default='pending', max_length=50, null=True),
        ),
    ]
