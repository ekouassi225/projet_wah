# Generated by Django 4.2.6 on 2023-12-02 23:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BackendPortfolio', '0007_alter_service_categorie_categorie'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact_message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('NomPrenom', models.CharField(max_length=100)),
                ('Mail', models.EmailField(max_length=254)),
                ('Message', models.TextField()),
            ],
            options={
                'verbose_name': 'Contact_message',
                'verbose_name_plural': 'Contacts_Messages',
            },
        ),
    ]
