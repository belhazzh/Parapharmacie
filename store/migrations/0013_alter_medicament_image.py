# Generated by Django 4.0.2 on 2022-02-18 12:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0012_alter_medicament_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='medicament',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='medicament-images/%y/%m'),
        ),
    ]
