# Generated by Django 3.0.6 on 2020-05-17 01:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Costumer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=100)),
                ('neighborhood', models.CharField(max_length=100)),
                ('address_number', models.IntegerField(max_length=10)),
                ('email', models.EmailField(max_length=254)),
                ('number', models.CharField(max_length=15)),
            ],
            options={
                'db_table': 'costumer',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('quantity', models.CharField(max_length=5)),
            ],
            options={
                'db_table': 'product',
            },
        ),
        migrations.CreateModel(
            name='Provider',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('number', models.CharField(max_length=15)),
            ],
            options={
                'db_table': 'provider',
            },
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=100)),
                ('neighborhood', models.CharField(max_length=100)),
                ('address_number', models.IntegerField(max_length=10)),
                ('email', models.EmailField(max_length=254)),
                ('number', models.CharField(max_length=15)),
                ('provider', models.ForeignKey(default='null', on_delete=django.db.models.deletion.CASCADE, to='trabalho3.Provider')),
            ],
            options={
                'db_table': 'employee',
            },
        ),
        migrations.CreateModel(
            name='Bill',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.CharField(max_length=10)),
                ('costumer', models.ForeignKey(default='null', on_delete=django.db.models.deletion.CASCADE, to='trabalho3.Costumer')),
                ('provider', models.ForeignKey(default='null', on_delete=django.db.models.deletion.CASCADE, to='trabalho3.Provider')),
            ],
            options={
                'db_table': 'bill',
            },
        ),
    ]
