# Generated by Django 3.2.6 on 2021-12-16 14:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('test_service', '0004_auto_20211216_1131'),
    ]

    operations = [
        migrations.AddField(
            model_name='iperftestresult',
            name='system_info',
            field=models.CharField(default='Sysinfo', max_length=40),
            preserve_default=False,
        ),
    ]
