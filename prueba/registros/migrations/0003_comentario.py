# Generated by Django 3.2.4 on 2021-07-02 17:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('registros', '0002_auto_20210630_1441'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comentario',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='Clave')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Registrado')),
                ('coment', models.TextField(verbose_name='Comentario')),
                ('alumno', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='registros.alumnos', verbose_name='Alumno')),
            ],
            options={
                'verbose_name': 'Comentario',
                'verbose_name_plural': 'Comentarios',
                'ordering': ['-created'],
            },
        ),
    ]
