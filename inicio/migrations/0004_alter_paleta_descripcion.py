# Generated by Django 4.2.6 on 2023-11-09 01:34

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inicio', '0003_rename_pepito_paleta'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paleta',
            name='descripcion',
            field=ckeditor.fields.RichTextField(),
        ),
    ]
