# Generated by Django 4.2.5 on 2023-10-03 21:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0008_stepsix'),
    ]

    operations = [
        migrations.CreateModel(
            name='stepSeven',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userId', models.IntegerField()),
                ('teamId', models.IntegerField()),
                ('date_updated', models.DateTimeField(auto_now_add=True)),
                ('testing', models.CharField(default='', max_length=1200)),
                ('positive', models.CharField(default='', max_length=1200)),
                ('negative', models.CharField(default='', max_length=1200)),
            ],
        ),
    ]
