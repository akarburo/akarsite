# Generated by Django 2.2.5 on 2021-03-05 10:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('akar', '0011_auto_20210305_1157'),
    ]

    operations = [
        migrations.AlterField(
            model_name='demand',
            name='agent',
            field=models.ForeignKey(default=17, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, verbose_name='Kimin Müşterisi'),
        ),
    ]
