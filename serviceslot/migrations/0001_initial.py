# Generated by Django 4.2.14 on 2024-07-12 22:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('customer', '0001_initial'),
        ('service', '0004_alter_reviewmodel_ratting'),
    ]

    operations = [
        migrations.CreateModel(
            name='ServiceSlot',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('chooce', models.CharField(choices=[('saturday 9AM to 2PM', 'saturday 9AM to 2PM'), ('Monday 5PM to 8PM', 'Monday 5PM to 8PM'), ('sunday 2PM to 5PM', 'sunday 2PM to 5PM')], max_length=50)),
                ('created_time', models.TimeField(auto_now_add=True)),
                ('service_status', models.CharField(choices=[('Done', 'Done'), ('cancel', 'cancel'), ('pending', 'pending')], max_length=50)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='customer.customer')),
                ('service', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='service.service')),
            ],
        ),
    ]
