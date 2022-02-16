# Generated by Django 3.2.6 on 2021-12-09 14:59

import apps.test_service.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Test',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('test_name', models.CharField(choices=[('FIO', 'Fio'), ('SYSBENCH', 'Sysbench'), ('Iperf3', 'Iperf3'), ('UNKOWN', 'Unknown')], default='UNKNOWN', max_length=15)),
                ('test_category', models.CharField(choices=[('NODE', 'Node'), ('INFRASTRUCTURE', 'Infrastructure'), ('APPLICATION', 'Application'), ('NO_TYPE', 'No Type')], default='NO_TYPE', max_length=20)),
                ('time_created', models.DateTimeField(auto_now_add=True)),
                ('custom_test_name', models.CharField(max_length=60)),
                ('test_status', models.CharField(choices=[('RUNNING', 'Running'), ('CREATED LOCALLY', 'Created Locally'), ('CREATED', 'Created'), ('POD CREATED', 'Completed'), ('FAILED', 'Failed'), ('STARTED', 'Started'), ('UNKOWN', 'Unknown')], default='UNKOWN', max_length=30)),
                ('raw_output', models.CharField(max_length=5000)),
                ('pod_name', models.CharField(default='', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='FioTestConfig',
            fields=[
                ('test', models.OneToOneField(blank=True, on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='fioTestConfig', serialize=False, to='test_service.test')),
                ('node_name', models.CharField(max_length=100, null=True)),
                ('fio_type', models.CharField(choices=[('READ', 'Read'), ('WRITE', 'Write'), ('READWRITE', 'Readwrite'), ('NO_TYPE', 'No Type')], default='NO_TYPE', max_length=15)),
                ('IO_depth', models.IntegerField()),
                ('block_size', models.CharField(max_length=5)),
                ('file_size', models.CharField(max_length=10)),
                ('access_mode', models.CharField(max_length=30)),
                ('reset_refillbuffer', models.BooleanField(default=False)),
                ('pv_size', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='FioTestResult',
            fields=[
                ('test', models.OneToOneField(blank=True, on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='fioTestResult', serialize=False, to='test_service.test')),
                ('total_input_output_size_read', models.CharField(blank=True, max_length=30)),
                ('total_iops_read', models.IntegerField(blank=True, default=0)),
                ('total_read_write_speed_read', models.CharField(blank=True, max_length=20)),
                ('total_run_time_read', models.CharField(blank=True, max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='iPerfTestConfig',
            fields=[
                ('test', models.OneToOneField(blank=True, on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='iPerf3Config', serialize=False, to='test_service.test')),
                ('client_node', models.CharField(max_length=100)),
                ('server_node', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='iPerfTestResult',
            fields=[
                ('test', models.OneToOneField(blank=True, on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='iPerf3TestResult', serialize=False, to='test_service.test')),
                ('result_as_json', models.JSONField(default=apps.test_service.models.iPerfTestResult.result_default)),
            ],
        ),
        migrations.CreateModel(
            name='TestEvent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField()),
                ('message', models.CharField(default='', max_length=100)),
                ('state', models.CharField(choices=[('Running', 'Running'), ('Created Locally', 'Created Locally'), ('Custom Resource Created', 'Crd Created'), ('Pod Created', 'Pod Created'), ('Started Container', 'Started Container'), ('Failed', 'Failed'), ('Completed', 'Completed'), ('Uknown', 'Unknown')], default='Uknown', max_length=30)),
                ('test', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='events', to='test_service.test')),
            ],
        ),
    ]