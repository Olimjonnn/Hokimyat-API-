# Generated by Django 3.2.9 on 2022-03-25 17:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_alter_hujjat_title'),
    ]

    operations = [
        migrations.CreateModel(
            name='Savol_Javob',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('jovoblar', models.ManyToManyField(blank=True, to='main.Javob')),
            ],
        ),
    ]
