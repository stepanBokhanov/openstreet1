# Generated by Django 3.1.4 on 2020-12-08 17:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0040_auto_20201208_1743'),
    ]

    operations = [
        migrations.AlterField(
            model_name='portfoliostats',
            name='name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='name', to='articles.portfolio', unique=True),
        ),
    ]
