# Generated by Django 3.0.5 on 2020-05-27 10:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('safm', '0003_auto_20200519_1838'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sample',
            name='duration',
            field=models.DecimalField(blank=True, decimal_places=1, max_digits=4, null=True),
        ),
        migrations.AlterField(
            model_name='sample',
            name='mode',
            field=models.CharField(blank=True, choices=[('min', 'Minor'), ('maj', 'Major')], max_length=3),
        ),
    ]
