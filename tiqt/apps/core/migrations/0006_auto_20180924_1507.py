# Generated by Django 2.1.1 on 2018-09-24 18:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_auto_20180924_1106'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='responsavel',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='responsavel_por', to=settings.AUTH_USER_MODEL),
        ),
    ]
