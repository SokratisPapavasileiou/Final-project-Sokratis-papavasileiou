# Generated by Django 3.2.8 on 2021-12-12 22:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first', '0002_alter_userdata_email'),
    ]

    operations = [
        migrations.CreateModel(
            name='test2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.RemoveField(
            model_name='test',
            name='description',
        ),
        migrations.RemoveField(
            model_name='test',
            name='firstprojectwebpage',
        ),
        migrations.AlterField(
            model_name='test',
            name='name',
            field=models.CharField(max_length=100),
        ),
    ]
