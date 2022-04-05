# Generated by Django 4.0.3 on 2022-03-31 18:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produit', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='produit',
            name='DOM',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='produit',
            name='DOP',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='produit',
            name='mark',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='produit',
            name='name',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='produit',
            name='quantity',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='produit',
            name='GTIN',
            field=models.CharField(max_length=14),
        ),
    ]
