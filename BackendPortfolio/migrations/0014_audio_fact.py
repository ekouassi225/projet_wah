# Generated by Django 4.2.6 on 2023-12-06 09:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BackendPortfolio', '0013_contact_message_object'),
    ]

    operations = [
        migrations.CreateModel(
            name='audio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('audio', models.FileField(upload_to=None)),
            ],
            options={
                'verbose_name': 'audio',
                'verbose_name_plural': 'audios',
            },
        ),
        migrations.CreateModel(
            name='fact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Jaime', models.IntegerField()),
                ('visite', models.IntegerField()),
            ],
            options={
                'verbose_name': 'fact_header',
                'verbose_name_plural': 'Facts_Headers',
            },
        ),
    ]