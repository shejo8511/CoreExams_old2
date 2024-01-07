# Generated by Django 4.2.6 on 2023-12-29 04:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0022_city_provincie'),
    ]

    operations = [
        migrations.AddField(
            model_name='city',
            name='country',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.PROTECT, related_name='Pais_ciudad', to='company.country', verbose_name='Pais'),
            preserve_default=False,
        ),
    ]
