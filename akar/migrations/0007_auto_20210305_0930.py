# Generated by Django 2.2.5 on 2021-03-05 06:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('akar', '0006_auto_20210226_0949'),
    ]

    operations = [
        migrations.AddField(
            model_name='demand',
            name='agent',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, verbose_name='Kimin Müşterisi'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='service',
            name='agent',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, verbose_name='Kimin Müşterisi'),
            preserve_default=False,
        ),
    ]
