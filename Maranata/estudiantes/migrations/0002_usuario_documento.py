# Generated by Django 4.1.1 on 2022-11-17 01:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('estudiantes', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='documento',
            field=models.CharField(default=1, max_length=20, verbose_name='Documento'),
            preserve_default=False,
        ),
    ]
