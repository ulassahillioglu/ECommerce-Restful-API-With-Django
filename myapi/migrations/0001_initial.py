# Generated by Django 4.2.11 on 2024-03-31 14:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categories',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'categories',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Onsale',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=250, null=True)),
                ('price', models.DecimalField(blank=True, decimal_places=5, max_digits=10, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('category', models.CharField(blank=True, max_length=20, null=True)),
                ('image_url', models.CharField(blank=True, max_length=250, null=True)),
                ('instock', models.IntegerField(blank=True, db_column='inStock', null=True)),
                ('ordercount', models.IntegerField(blank=True, db_column='orderCount', null=True)),
            ],
            options={
                'db_table': 'onSale',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(blank=True, null=True)),
                ('price', models.FloatField(blank=True, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('category', models.TextField(blank=True, null=True)),
                ('imageurl', models.TextField(blank=True, db_column='imageUrl', null=True)),
                ('instock', models.IntegerField(blank=True, db_column='inStock', null=True)),
                ('ordercount', models.IntegerField(blank=True, db_column='orderCount', null=True)),
            ],
            options={
                'db_table': 'products',
                'managed': False,
            },
        ),
    ]
