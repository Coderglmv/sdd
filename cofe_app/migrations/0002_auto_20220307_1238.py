# Generated by Django 3.2.8 on 2022-03-07 08:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cofe_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='about_product',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='products',
            name='return_policy',
            field=models.TextField(blank=True, null=True),
        ),
    ]