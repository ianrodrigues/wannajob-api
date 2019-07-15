# Generated by Django 2.2.3 on 2019-07-14 23:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('company', models.CharField(max_length=100)),
                ('seniority_level', models.CharField(choices=[('JUNIOR', 'Junior'), ('MIDDLE', 'Middle'), ('SENIOR', 'Senior'), ('TECH_MANAGEMENT', 'Tech Management')], max_length=15)),
                ('salary', models.IntegerField()),
                ('city', models.CharField(max_length=50)),
                ('country', models.CharField(max_length=2)),
            ],
        ),
    ]
