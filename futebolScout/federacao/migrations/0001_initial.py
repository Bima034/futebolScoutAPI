# Generated by Django 5.1 on 2024-08-29 14:58

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Afiliacoes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_criacao', models.DateTimeField(auto_now_add=True)),
                ('data_atualizacao', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='ComentariosFederacao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comentario', models.TextField()),
                ('data_criacao', models.DateTimeField(auto_now_add=True)),
                ('data_atualizacao', models.DateTimeField(auto_now=True)),
                ('pessoa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comentarios_pessoa_federacao', to='accounts.pessoa')),
            ],
        ),
        migrations.CreateModel(
            name='Federacao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('sigla', models.CharField(max_length=10)),
                ('localidade', models.CharField(max_length=100)),
                ('logo_path', models.ImageField(blank=True, null=True, upload_to='imagens/federacao/')),
                ('presidente', models.CharField(max_length=100)),
                ('fundacao', models.DateField()),
                ('descricao', models.TextField()),
                ('nota_media', models.FloatField(default=0.0, editable=False)),
                ('data_criacao', models.DateTimeField(auto_now_add=True)),
                ('data_atualizacao', models.DateTimeField(auto_now=True)),
                ('afiliada', models.ManyToManyField(blank=True, related_name='afiliacoes', through='federacao.Afiliacoes', to='federacao.federacao')),
                ('comentarios', models.ManyToManyField(blank=True, related_name='federacao_comentarios', through='federacao.ComentariosFederacao', to='accounts.pessoa')),
            ],
        ),
        migrations.AddField(
            model_name='comentariosfederacao',
            name='federacao',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comentarios_federacao', to='federacao.federacao'),
        ),
        migrations.AddField(
            model_name='afiliacoes',
            name='federacao',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='federacao', to='federacao.federacao'),
        ),
        migrations.AddField(
            model_name='afiliacoes',
            name='federacao_afiliada',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='federacao_afiliada', to='federacao.federacao'),
        ),
    ]
