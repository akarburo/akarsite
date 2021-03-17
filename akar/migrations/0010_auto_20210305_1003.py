# Generated by Django 2.2.5 on 2021-03-05 07:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('akar', '0009_agent_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='demand',
            name='agent',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='akar.Agent', verbose_name='Kimin Müşterisi'),
        ),
        migrations.AlterField(
            model_name='service',
            name='agent',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.PROTECT, to='akar.Agent', verbose_name='Kimin Müşterisi'),
        ),
    ]
