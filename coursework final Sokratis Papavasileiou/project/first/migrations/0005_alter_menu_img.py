# Generated by Django 3.2.8 on 2021-12-13 13:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first', '0004_menu_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menu',
            name='img',
            field=models.ImageField(blank=True, null=True, upload_to='img'),
        ),
    ]