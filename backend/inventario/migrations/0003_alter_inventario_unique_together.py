# Generated by Django 4.1.2 on 2022-10-27 23:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventario', '0002_alter_contaservico_nome_and_more'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='inventario',
            unique_together={('projeto', 'conta_servico', 'integracao', 'servidor')},
        ),
    ]
