# Generated by Django 4.2.16 on 2024-12-19 10:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tournaments', '0002_alter_tournamentbase_template_tournament_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tournamentcompetitor',
            name='status',
            field=models.CharField(choices=[('active', 'active'), ('eliminated', 'eliminated'), ('finished', 'finished')], default='active', max_length=255),
        ),
        migrations.AlterField(
            model_name='tournamentround',
            name='round_number',
            field=models.PositiveIntegerField(default=1),
        ),
    ]
