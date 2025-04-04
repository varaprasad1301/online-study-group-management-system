# Generated by Django 5.2 on 2025-04-04 11:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='VirtualSession',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('scheduled_time', models.DateTimeField()),
                ('meeting_link', models.URLField(blank=True, null=True)),
            ],
        ),
    ]
