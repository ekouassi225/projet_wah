# Generated by Django 4.2.6 on 2024-01-18 05:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('BackendPortfolio', '0042_remove_justme_lastdiploma_pic'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='portfolio_carte',
            name='Carte_suplementaire',
        ),
        migrations.RemoveField(
            model_name='portfolio_carte',
            name='Message',
        ),
        migrations.CreateModel(
            name='portfolio_ajout_photo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(blank=True, default=None, upload_to='Backend\\media\\media_cdn')),
                ('NomProjet', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='BackendPortfolio.portfolio_categorie')),
            ],
            options={
                'verbose_name': 'portfolio_photo',
                'verbose_name_plural': 'Portfolio_photos',
            },
        ),
    ]