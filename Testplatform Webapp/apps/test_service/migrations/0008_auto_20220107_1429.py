# Generated by Django 3.2.6 on 2022-01-07 13:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('test_service', '0007_auto_20220104_1452'),
    ]

    operations = [
        migrations.CreateModel(
            name='PGBenchTestConfig',
            fields=[
                ('test', models.OneToOneField(blank=True, on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='pgbenchTestConfig', serialize=False, to='test_service.test')),
                ('host', models.CharField(blank=True, max_length=100)),
                ('db_name', models.CharField(blank=True, max_length=100)),
                ('db_user', models.CharField(blank=True, max_length=60)),
                ('db_pw', models.CharField(blank=True, max_length=60)),
                ('number_of_clients', models.IntegerField(blank=True)),
                ('selects_only', models.BooleanField(default=False)),
                ('vacuum', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='PGBenchTestResult',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_transactions', models.IntegerField(blank=True, default=0)),
                ('number_of_clients', models.IntegerField(blank=True, default=0)),
                ('number_of_threads', models.IntegerField(blank=True, default=0)),
                ('latency_average', models.CharField(blank=True, max_length=100)),
                ('transactions_per_second', models.IntegerField(blank=True, default=0)),
                ('number_of_transactions_processed', models.CharField(blank=True, max_length=50)),
            ],
        ),
        migrations.AlterField(
            model_name='testevent',
            name='state',
            field=models.CharField(choices=[('Running', 'Running'), ('Created Locally', 'Created Locally'), ('Custom Resource Created', 'Crd Created'), ('Pod Created', 'Pod Created'), ('Started Container', 'Started Container'), ('Failed', 'Failed'), ('Completed', 'Completed'), ('Unknown', 'Unknown'), ('Job Completed', 'Job Completed'), ('Deleted Resource', 'Resource Deleted')], default='Unknown', max_length=30),
        ),
    ]