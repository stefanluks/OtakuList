# Generated by Django 4.2 on 2023-05-02 13:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0002_feed'),
    ]

    operations = [
        migrations.AlterField(
            model_name='avaliacao',
            name='nota',
            field=models.IntegerField(default=0, verbose_name='Nota da obra'),
        ),
        migrations.CreateModel(
            name='Seguidores',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('segue', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='User_que_Segue', to='webapp.usuario')),
                ('seguido', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sendo_seguido', to='webapp.usuario')),
            ],
            options={
                'verbose_name': 'SEGUIDOR',
                'verbose_name_plural': 'SEGUIDORES',
            },
        ),
    ]