# Generated by Django 3.2.16 on 2022-11-24 17:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bankapp', '0005_alter_data_service'),
    ]

    operations = [
        migrations.AlterField(
            model_name='data',
            name='gender',
            field=models.CharField(choices=[('female', 'Female'), ('male', 'Male')], default='female', max_length=20),
        ),
    ]
