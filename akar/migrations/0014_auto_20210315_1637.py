# Generated by Django 2.2.5 on 2021-03-15 13:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('akar', '0013_auto_20210315_1635'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
