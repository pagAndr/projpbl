# Generated by Django 4.1.2 on 2022-10-23 14:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pair',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=100)),
                ('cabinet', models.CharField(max_length=100)),
                ('professor', models.CharField(max_length=100)),
                ('occupant', models.CharField(max_length=100)),
                ('is_odd', models.BooleanField(default=True)),
            ],
        ),
    ]
