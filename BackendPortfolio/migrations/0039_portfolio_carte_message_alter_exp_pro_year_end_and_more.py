# Generated by Django 4.2.6 on 2024-01-18 01:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BackendPortfolio', '0038_delete_testimonials_delete_testimonials_header'),
    ]

    operations = [
        migrations.AddField(
            model_name='portfolio_carte',
            name='Message',
            field=models.TextField(blank=True, default=None),
        ),
        migrations.AlterField(
            model_name='exp_pro',
            name='Year_end',
            field=models.DateField(blank=True),
        ),
        migrations.AlterField(
            model_name='formation',
            name='Year_end',
            field=models.DateField(blank=True),
        ),
        migrations.AlterField(
            model_name='portfolio_carte',
            name='Carte_suplementaire',
            field=models.ImageField(blank=True, default=None, upload_to='Backend\\media\\media_cdn'),
        ),
        migrations.AlterField(
            model_name='portfolio_carte',
            name='Url',
            field=models.CharField(blank=True, default=None, max_length=50),
        ),
    ]