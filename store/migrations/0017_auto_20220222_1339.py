# Generated by Django 3.2.8 on 2022-02-22 12:39

from django.db import migrations, models
import store.validators


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0016_customer'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='lastname',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='customer',
            name='tel',
            field=models.PositiveIntegerField(blank=True, null=True, validators=[store.validators.validate_length]),
        ),
        migrations.AlterField(
            model_name='customer',
            name='gender',
            field=models.CharField(choices=[('homme', 'homme'), ('femme', 'femme')], default='homme', max_length=10),
        ),
        migrations.AlterField(
            model_name='customer',
            name='username',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]