# Generated by Django 5.1 on 2024-08-28 22:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clube', '0004_alter_clube_logo_path_alter_clube_presidente_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clube',
            name='estadio',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
    ]
