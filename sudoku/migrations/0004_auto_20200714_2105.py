# Generated by Django 3.0 on 2020-07-14 21:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sudoku', '0003_auto_20200714_1956'),
    ]

    operations = [
        migrations.RenameField(
            model_name='game',
            old_name='user',
            new_name='owner',
        ),
    ]