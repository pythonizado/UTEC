# Generated by Django 5.1.6 on 2025-03-09 17:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('diagnostico', '0003_alter_respuesta_seleccion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='respuesta',
            name='seleccion',
            field=models.CharField(blank=True, choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D')], max_length=1, null=True),
        ),
    ]
