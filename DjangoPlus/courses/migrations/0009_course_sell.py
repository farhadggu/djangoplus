# Generated by Django 3.2.8 on 2021-10-31 17:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0008_contactus'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='sell',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
