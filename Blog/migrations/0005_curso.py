# Generated by Django 5.0 on 2023-12-23 21:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0004_alter_publicacion_fecha'),
    ]

    operations = [
        migrations.CreateModel(
            name='Curso',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('curso', models.CharField(max_length=30)),
                ('camada', models.IntegerField()),
            ],
        ),
    ]
