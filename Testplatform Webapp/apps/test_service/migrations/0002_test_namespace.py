# Generated by Django 3.2.6 on 2021-12-10 14:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('test_service', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='test',
            name='namespace',
            field=models.CharField(default='default', max_length=200),
            preserve_default=False,
        ),
    ]