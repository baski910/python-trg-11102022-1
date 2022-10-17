# Generated by Django 3.2.13 on 2022-10-17 07:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('booktitle', models.CharField(max_length=50)),
                ('bookauthor', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'books',
            },
        ),
    ]
