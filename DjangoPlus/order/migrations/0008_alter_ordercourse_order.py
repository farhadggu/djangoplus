# Generated by Django 3.2.8 on 2021-10-18 04:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0007_remove_ordercourse_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ordercourse',
            name='order',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='orders', to='order.order'),
        ),
    ]