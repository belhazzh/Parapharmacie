# Generated by Django 3.2.8 on 2022-02-22 21:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0024_commande'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='commande',
            name='medicaments',
        ),
        migrations.CreateModel(
            name='CommandeItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantite', models.PositiveIntegerField(blank=True, null=True)),
                ('product', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='store.medicament')),
            ],
        ),
        migrations.AddField(
            model_name='commande',
            name='item',
            field=models.ManyToManyField(to='store.CommandeItem'),
        ),
    ]
