# Generated by Django 5.1.5 on 2025-02-07 22:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aria_music', '0003_alter_product_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(upload_to='aria_music/static/aria_music'),
        ),
    ]
