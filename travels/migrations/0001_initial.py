# Generated by Django 3.2.7 on 2021-09-27 23:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('login', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Travel',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('destino', models.CharField(max_length=40)),
                ('descripcion', models.CharField(max_length=40)),
                ('fechaDesde', models.DateField()),
                ('fechaHasta', models.DateField()),
                ('estado', models.IntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='usuario', to='login.user')),
            ],
        ),
    ]
