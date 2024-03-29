# Generated by Django 3.1 on 2024-03-22 03:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tienda', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Variation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('variation_categoria', models.CharField(choices=[('color', 'color'), ('talla', 'talla')], max_length=200)),
                ('variation_valor', models.CharField(max_length=100)),
                ('esta_activo', models.BooleanField(default=True)),
                ('fecha_creada', models.DateTimeField(auto_now=True)),
                ('producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tienda.producto')),
            ],
        ),
    ]
