# Generated by Django 2.1.7 on 2019-03-15 19:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('helpdesk', '0022_auto_20190311_1635'),
    ]

    operations = [
        migrations.AddField(
            model_name='ticket',
            name='tipo_de_item',
            field=models.IntegerField(blank=6, choices=[(1, 'Dúvida'), (2, 'Melhoria do Sistema'), (3, 'Acompanhamento Técnico'), (4, 'Configuração'), (5, 'Desenvolvimento'), (6, 'Suporte'), (7, 'Conversão de Dados')], default=6),
        ),
    ]
