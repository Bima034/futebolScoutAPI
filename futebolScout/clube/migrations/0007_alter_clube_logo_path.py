# Generated by Django 5.1 on 2024-08-29 14:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clube', '0006_alter_clube_fundacao'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clube',
            name='logo_path',
            field=models.ImageField(blank=True, null=True, upload_to='imagens/clube/'),
        ),
    ]
