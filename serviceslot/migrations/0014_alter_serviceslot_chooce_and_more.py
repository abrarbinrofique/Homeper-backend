# Generated by Django 5.1.1 on 2024-10-28 20:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('serviceslot', '0013_customerorderinfo_alter_serviceslot_chooce_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='serviceslot',
            name='chooce',
            field=models.CharField(choices=[('saturday 9AM to 2PM', 'saturday 9AM to 2PM'), ('sunday 2PM to 5PM', 'sunday 2PM to 5PM'), ('Monday 5PM to 8PM', 'Monday 5PM to 8PM')], max_length=50),
        ),
        migrations.AlterField(
            model_name='serviceslot',
            name='service_status',
            field=models.CharField(blank=True, choices=[('cancel', 'cancel'), ('pending', 'pending'), ('Done', 'Done')], default='pending', max_length=50, null=True),
        ),
    ]
