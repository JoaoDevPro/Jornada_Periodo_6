# Generated by Django 5.0.6 on 2024-08-19 18:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_renault', '0002_rename_nome_usuario_name_alter_risco_id_usuario'),
    ]

    operations = [
        migrations.CreateModel(
            name='item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
    ]
