# Generated by Django 4.0.4 on 2022-05-03 21:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_product_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='address',
            name='zip',
            field=models.CharField(default=4100, max_length=10),
            preserve_default=False,
        ),
    ]