# Generated by Django 5.1 on 2024-09-01 13:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clube', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clube',
            name='logo_path',
            field=models.ImageField(blank=True, null=True, upload_to='clube/'),
        ),
    ]
