# Generated by Django 2.1.7 on 2019-04-01 19:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('helpdesk', '0024_auto_20190401_1452'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='tipo_de_suporte',
            field=models.IntegerField(choices=[(1, 'Dúvida'), (2, 'Melhoria do Sistema'), (3, 'Acompanhamento Técnico'), (4, 'Configuração'), (5, 'Desenvolvimento'), (6, 'Suporte'), (7, 'Conversão de Dados')], default=6, verbose_name='Tipo de Suporte'),
        ),
    ]
