# Generated by Django 2.1.2 on 2018-10-10 18:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_auto_20180924_1507'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comentario',
            options={'ordering': ['-criado_em']},
        ),
        migrations.AddField(
            model_name='ticket',
            name='contato',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='iniciado_em',
            field=models.DateTimeField(blank=True, editable=False, null=True),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='responsavel',
            field=models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='responsavel_por', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='status',
            field=models.SmallIntegerField(choices=[(0, 'Aberto'), (1, 'Em atendimento'), (2, 'Encerrado'), (3, 'Cancelado')], default=0, editable=False),
        ),
    ]
