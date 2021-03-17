# Generated by Django 2.2.5 on 2021-02-19 12:59

from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('akar', '0003_auto_20210219_1556'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='brand',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='akar.Brand'),
        ),
        migrations.AlterField(
            model_name='service',
            name='content',
            field=models.TextField(max_length=1000, verbose_name='Açıklama'),
        ),
        migrations.AlterField(
            model_name='service',
            name='mail',
            field=models.EmailField(max_length=254, verbose_name='E-Mail Adresiniz'),
        ),
        migrations.AlterField(
            model_name='service',
            name='phone',
            field=phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None, verbose_name='Telefon Numaranız'),
        ),
    ]