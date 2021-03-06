# Generated by Django 3.0.7 on 2020-07-03 12:52

from django.db import migrations, models
import safm.models


class Migration(migrations.Migration):

    dependencies = [
        ('safm', '0010_auto_20200702_1512'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sample',
            name='key',
            field=models.CharField(blank=True, choices=[(' ', 'None'), ('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E'), ('F', 'F'), ('G', 'G')], default=' ', max_length=1),
        ),
        migrations.AlterField(
            model_name='sample',
            name='mode',
            field=models.CharField(blank=True, choices=[(' ', 'None'), ('min', 'Minor'), ('maj', 'Major')], default=' ', max_length=3),
        ),
    ]
