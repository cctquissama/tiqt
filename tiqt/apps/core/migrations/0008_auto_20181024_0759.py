# Generated by Django 2.1.2 on 2018-10-24 10:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_auto_20181010_1530'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='ticket',
            options={'ordering': ['criado_em']},
        ),
        migrations.AddField(
            model_name='ticket',
            name='encerrado_em',
            field=models.DateTimeField(blank=True, editable=False, null=True),
        ),
        migrations.AlterField(
            model_name='comentario',
            name='criado_em',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='criado_em',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
