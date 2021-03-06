# Generated by Django 3.2.9 on 2021-12-04 23:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Telefone',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero', models.CharField(max_length=13)),
            ],
        ),
        migrations.CreateModel(
            name='Pessoa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sexo', models.CharField(choices=[('M', 'Masculino'), ('F', 'Feminino')], default='M', max_length=1)),
                ('nome', models.CharField(max_length=255)),
                ('data_nascimento', models.DateField()),
                ('cpf', models.CharField(max_length=15, unique=True)),
                ('foto', models.ImageField(blank=True, null=True, upload_to='fotos_presos')),
                ('datacadastro', models.DateTimeField(auto_now_add=True)),
                ('telefone', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='pessoas.telefone')),
            ],
        ),
    ]
