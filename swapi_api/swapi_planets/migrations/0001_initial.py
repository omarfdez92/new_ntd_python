# Generated by Django 5.0.6 on 2024-06-05 20:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Planet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
                ('population', models.CharField(blank=True, max_length=255, null=True)),
                ('terrains', models.JSONField(default=list)),
                ('climates', models.JSONField(default=list)),
            ],
        ),
    ]
