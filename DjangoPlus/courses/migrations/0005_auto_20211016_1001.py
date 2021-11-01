# Generated by Django 3.2.8 on 2021-10-16 06:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0004_episode_parent'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='episode',
            options={'ordering': ['created']},
        ),
        migrations.AlterField(
            model_name='episode',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='courses.episode'),
        ),
    ]
