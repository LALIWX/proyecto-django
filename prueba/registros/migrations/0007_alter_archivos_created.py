# Generated by Django 3.2.4 on 2021-07-23 17:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registros', '0006_archivos'),
    ]

    operations = [
        migrations.AlterField(
            model_name='archivos',
            name='created',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
