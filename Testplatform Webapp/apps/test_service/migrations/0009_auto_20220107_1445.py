# Generated by Django 3.2.6 on 2022-01-07 13:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('test_service', '0008_auto_20220107_1429'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pgbenchtestconfig',
            name='vacuum',
        ),
        migrations.AddField(
            model_name='pgbenchtestconfig',
            name='duration_in_seconds',
            field=models.IntegerField(blank=True, default=0),
            preserve_default=False,
        ),
    ]
