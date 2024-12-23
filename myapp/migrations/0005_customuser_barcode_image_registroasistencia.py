# Generated by Django 5.1.1 on 2024-11-01 07:11

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_customuser_cbarra'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='barcode_image',
            field=models.ImageField(blank=True, null=True, upload_to='barcodes/'),
        ),
        migrations.CreateModel(
            name='RegistroAsistencia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('entrada', models.DateTimeField(auto_now_add=True)),
                ('salida', models.DateTimeField(blank=True, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
