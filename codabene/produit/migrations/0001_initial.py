# Generated by Django 4.0.3 on 2022-03-31 17:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Produit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('GTIN', models.CharField(max_length=14, unique=True)),
            ],
        ),
    ]
