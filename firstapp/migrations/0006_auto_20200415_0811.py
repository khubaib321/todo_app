# Generated by Django 3.0.5 on 2020-04-15 08:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0005_auto_20200415_0803'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='short_desc',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
