# Generated by Django 2.1.1 on 2018-09-24 14:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20180920_0853'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ticket',
            name='criado_por',
        ),
        migrations.AddField(
            model_name='ticket',
            name='iniciado_em',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
