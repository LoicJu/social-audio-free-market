# Generated by Django 3.0.5 on 2020-04-19 09:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import safm.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Sample',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('file', models.FileField(max_length=255, upload_to=safm.models.Sample.user_directory_path)),
                ('duration', models.FloatField(blank=True, null=True)),
                ('tempo', models.PositiveIntegerField(blank=True, null=True)),
                ('tone', models.CharField(blank=True, choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E'), ('F', 'F'), ('G', 'G')], max_length=1)),
                ('mode', models.CharField(blank=True, choices=[('m', 'Minor'), ('M', 'Major')], max_length=1)),
                ('datetime_upload', models.DateTimeField(auto_now_add=True)),
                ('nb_dl_unauthenticated', models.PositiveIntegerField(default=0)),
                ('tags', models.ManyToManyField(to='safm.Tag')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
