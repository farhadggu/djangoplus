# Generated by Django 3.2.8 on 2021-10-16 06:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0003_auto_20211016_0939'),
    ]

    operations = [
        migrations.AddField(
            model_name='episode',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='episode', to='courses.episode'),
        ),
    ]