# Generated by Django 5.0.2 on 2024-05-05 21:51

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CatalogoDelito',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('delito', models.CharField(max_length=255)),
                ('fechaCreacion', models.DateTimeField(auto_now_add=True)),
                ('fechaModificacion', models.DateField(auto_now=True)),
                ('status', models.BooleanField()),
            ],
            options={
                'verbose_name': 'Delito',
                'verbose_name_plural': 'Delitos',
                'ordering': ['-fechaCreacion'],
            },
        ),
        migrations.CreateModel(
            name='CatalogoPersona',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo_persona', models.CharField(max_length=255)),
                ('fechaCreacion', models.DateTimeField(auto_now_add=True)),
                ('fechaModificacion', models.DateField(auto_now=True)),
                ('status', models.BooleanField()),
                ('id_catalogoDelito', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='consulta.catalogodelito')),
            ],
            options={
                'verbose_name': 'Tipo persona',
                'verbose_name_plural': 'Tipo personas',
                'ordering': ['-fechaCreacion'],
            },
        ),
        migrations.CreateModel(
            name='RegistroDelitos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('registro', models.CharField(max_length=255)),
                ('fechaCreacion', models.DateTimeField(auto_now_add=True)),
                ('fechaModificacion', models.DateField(auto_now=True)),
                ('delito', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='consulta.catalogodelito')),
                ('tipo_persona', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='consulta.catalogopersona')),
            ],
            options={
                'verbose_name': 'Registro',
                'verbose_name_plural': 'Registros',
                'ordering': ['-fechaCreacion'],
            },
        ),
    ]