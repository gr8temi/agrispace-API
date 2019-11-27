# Generated by Django 2.2.7 on 2019-11-25 07:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Information',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=150)),
                ('phone', models.CharField(max_length=50)),
                ('tagline', models.TextField()),
                ('email', models.EmailField(max_length=256)),
            ],
            options={
                'verbose_name': 'Information',
                'verbose_name_plural': 'Informations',
            },
        ),
    ]