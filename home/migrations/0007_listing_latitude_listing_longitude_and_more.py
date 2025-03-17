# Generated by Django 4.2.4 on 2025-03-17 14:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_alter_buyrequest_buyer_alter_buyrequest_listing_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing',
            name='latitude',
            field=models.DecimalField(blank=True, decimal_places=6, max_digits=9, null=True),
        ),
        migrations.AddField(
            model_name='listing',
            name='longitude',
            field=models.DecimalField(blank=True, decimal_places=6, max_digits=9, null=True),
        ),
        migrations.AlterField(
            model_name='listing',
            name='category',
            field=models.CharField(choices=[('Mobile', 'Mobile'), ('Laptop', 'Laptop'), ('Vehicle', 'Vehicle'), ('Other', 'Other')], default='Mobile', max_length=50),
        ),
    ]
