# Generated by Django 5.1.3 on 2024-12-27 12:45

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('EMUSIC_Application', '0003_song_songrequest'),
    ]

    operations = [
        migrations.AddField(
            model_name='genre',
            name='description',
            field=models.TextField(default='Default description'),
        ),
        migrations.AddField(
            model_name='songcategory',
            name='description',
            field=models.TextField(default='Default description'),
        ),
        migrations.AlterField(
            model_name='category',
            name='description',
            field=models.TextField(default='Default description'),
        ),
        migrations.AlterField(
            model_name='musictrack',
            name='price',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True),
        ),
        migrations.AlterField(
            model_name='subscriptionplan',
            name='duration',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='subscriptionplan',
            name='features',
            field=models.TextField(),
        ),
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.CharField(max_length=255)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('is_read', models.BooleanField(default=False)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
