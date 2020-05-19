# Generated by Django 3.0.6 on 2020-05-17 23:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trabalho3', '0006_auto_20200517_1914'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='costumerbill',
            name='price',
        ),
        migrations.RemoveField(
            model_name='providerbill',
            name='price',
        ),
        migrations.AddField(
            model_name='costumerbill',
            name='quantity',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='price',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='providerbill',
            name='quantity',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]