# Generated by Django 4.2 on 2023-07-04 23:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rayoMakween', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='formulario',
            name='comuna',
        ),
        migrations.RemoveField(
            model_name='formulario',
            name='region',
        ),
    ]
