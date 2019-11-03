# Generated by Django 2.2.3 on 2019-10-29 20:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Empresa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('CNPJ', models.CharField(max_length=18)),
            ],
        ),
        migrations.CreateModel(
            name='NotaFiscal',
            fields=[
                ('serie', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('numero', models.IntegerField(max_length=10)),
                ('nome_descricao', models.CharField(max_length=200)),
                ('peso', models.DecimalField(decimal_places=2, max_digits=10)),
                ('cubagem', models.DecimalField(decimal_places=2, max_digits=10)),
                ('data', models.DateTimeField()),
                ('empresa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalogs.Empresa')),
            ],
        ),
    ]