# Generated by Django 4.1.2 on 2022-10-23 15:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schedule', '0003_rename_is_odd_pair_odd_week'),
    ]

    operations = [
        migrations.CreateModel(
            name='Week',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pair_nr', models.IntegerField()),
            ],
        ),
    ]
