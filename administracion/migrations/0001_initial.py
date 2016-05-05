# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-05-04 19:23
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0007_alter_validators_add_error_messages'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=40)),
                ('apellido', models.CharField(max_length=40)),
                ('email', models.EmailField(max_length=254)),
                ('telefono', models.CharField(max_length=20)),
                ('direccion', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='MiembroEquipo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'default_permissions': (),
                'verbose_name_plural': 'miembros equipo',
            },
        ),
        migrations.CreateModel(
            name='Proyecto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=40)),
                ('estado', models.CharField(choices=[('PL', 'Planificacion'), ('EJ', 'Ejecutandose'), ('PE', 'Pendiente'), ('CA', 'Cancelado'), ('TE', 'Terminado')], default='PE', max_length=2)),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True)),
                ('fecha_inicio', models.DateTimeField()),
                ('fecha_fin', models.DateTimeField()),
                ('equipo', models.ManyToManyField(through='administracion.MiembroEquipo', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'permissions': (('listar_proyectos', 'Listar todos los proyectos disponibles'), ('listar_proyectos_usuario', 'Listar todos los proyectos de un Usuario'), ('ver_proyecto', 'ver detalles del proyecto'), ('asignar_equipo', 'asignar los miembros del equipo'), ('aprobar_proyecto', 'permiso para aprobar el proyecto')),
            },
        ),
        migrations.AddField(
            model_name='miembroequipo',
            name='proyecto',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='administracion.Proyecto'),
        ),
        migrations.AddField(
            model_name='miembroequipo',
            name='roles',
            field=models.ManyToManyField(to='auth.Group'),
        ),
        migrations.AddField(
            model_name='miembroequipo',
            name='usuario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='cliente',
            name='proyecto',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='administracion.Proyecto'),
        ),
        migrations.AlterUniqueTogether(
            name='miembroequipo',
            unique_together=set([('usuario', 'proyecto')]),
        ),
    ]