# Generated by Django 3.0.3 on 2020-09-16 02:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('organizacao', '0001_initial'),
        ('equipe', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='equipe',
            name='eqp_criador',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='organizacao.Organizacao'),
        ),
    ]