# Generated by Django 4.1.7 on 2023-04-02 22:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tercera', '0003_compras_rename_apellido_personas_apellido_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='materias',
            old_name='descrpcion',
            new_name='descripcion',
        ),
        migrations.AddField(
            model_name='compras',
            name='cantidad',
            field=models.IntegerField(default=0, max_length=5),
        ),
        migrations.AddField(
            model_name='compras',
            name='producto',
            field=models.TextField(default='nada', max_length=15),
        ),
        migrations.AlterField(
            model_name='materias',
            name='estado',
            field=models.TextField(default='por hacer', max_length=20),
        ),
    ]