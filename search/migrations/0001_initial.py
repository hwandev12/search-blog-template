# Generated by Django 4.0.4 on 2022-04-28 08:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Candidate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('age', models.IntegerField(default=15)),
                ('job', models.CharField(max_length=200)),
            ],
            options={
                'verbose_name': 'Candidate',
                'verbose_name_plural': 'My Candidates',
            },
        ),
    ]
