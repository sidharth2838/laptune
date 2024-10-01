# Generated by Django 5.1 on 2024-08-25 13:01

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Laptop',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand', models.CharField(max_length=100)),
                ('model', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='laptops/')),
                ('description', models.TextField()),
                ('base_price', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name='Purchase',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('payment_method', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Customization',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customization_name', models.CharField(max_length=100)),
                ('additional_cost', models.DecimalField(decimal_places=2, max_digits=10)),
                ('laptop', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='laptop.laptop')),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_name', models.CharField(max_length=100)),
                ('review_text', models.TextField()),
                ('rating', models.PositiveIntegerField()),
                ('brand', models.CharField(max_length=100)),
                ('laptop', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='laptop.laptop')),
            ],
        ),
    ]
