from django.db import models
from django.db.models.base import Model

# Create your models here.
# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Test(models.Model):
    '''
    A Django Model class representing a Test Object in the context of the Kubernetes Testplattform. 
    
    '''

    class TestStatusTypes(models.TextChoices):
        '''
        A class describing the different status types for a performance test. 
    
        '''
        RUNNING = 'RUNNING'
        CREATED_LOCALLY = 'CREATED LOCALLY'
        CREATED = 'CREATED'
        COMPLETED = 'COMPLETED'
        FAILED = 'FAILED'
        STARTED = 'STARTED'
        UNKNOWN = 'UNKOWN'


    class SupportedTests(models.TextChoices):
        '''
        A class describing the different supported tests of the plattform.
    
        '''
        FIO = 'FIO'
        PGBENCH = 'PGBENCH'
        IPERF3 = 'Iperf3'
        UNKNOWN = 'UNKOWN'
    
    class TestCategory(models.TextChoices):
        '''
        A class describing the 3 different test categories.
    
        '''
        NODE = 'NODE',
        INFRASTRUCTURE = 'INFRASTRUCTURE'
        APPLICATION = 'APPLICATION'
        NO_TYPE = 'NO_TYPE'


    test_name = models.CharField(choices=SupportedTests.choices, max_length=15, default='UNKNOWN')   
    test_category = models.CharField(choices=TestCategory.choices, max_length=20, default='NO_TYPE')
    time_created = models.DateTimeField(auto_now_add=True)
    namespace = models.CharField(max_length=200)
    plural = models.CharField(max_length=200)
    
    custom_test_name = models.CharField(max_length=60)        
    test_status = models.CharField(choices=TestStatusTypes.choices, max_length=30, default='UNKOWN')    
    raw_output = models.CharField(max_length=5000)   
    pod_name = models.CharField(max_length=100, default='')
    
    def __str__(self):
            return self.test_name

#https://medium.com/@drsantos20/generic-viewsets-for-abstract-base-classes-in-django-rest-framework-4cf8eb4155df


class Node(models.Model):
    '''
    A Django Model class representing a Kubernetes node.
    
    '''
    ip_address = models.CharField(max_length=60)
    name = models.CharField(max_length=120)
    os = models.CharField(max_length=120)
    architecture = models.CharField(max_length=60)

class iPerfTestConfig(models.Model):
    '''
    A Django Model class representing a configuration for an iperf3 performance test.
    
    '''
    
    def plural():
        return 'iperf3s'

    test = models.OneToOneField(Test, on_delete=models.CASCADE, primary_key=True, related_name='iPerf3Config', blank=True)
    client_node = models.CharField(max_length=100)
    server_node = models.CharField(max_length=100)

class iPerfTestResult(models.Model):
    '''
    A Django Model class representing an iperf3 test result.
    
    '''
    def result_default():
        return {"result": "exampleResult"}

    test = models.OneToOneField(Test, on_delete=models.CASCADE, primary_key=True, related_name='iPerf3TestResult', blank=True)
    result_as_json = models.JSONField(default=result_default)
    client_ip = models.CharField(max_length=16)
    server_ip = models.CharField(max_length=16)
    protocol = models.CharField(max_length=3)
    duration = models.CharField(max_length=10)
    sent_MB_s = models.CharField(max_length=15)
    received_MB_s = models.CharField(max_length=15)
    system_info = models.CharField(max_length=80)
    transmission_rate_per_second = models.CharField(max_length=100)




class FioTestConfig(models.Model):
    '''
    A Django Model class representing a configuration for an FIO performance test.
    
    '''
    
    def plural():
        return 'fios'

    test = models.OneToOneField(Test, on_delete=models.CASCADE, primary_key=True, related_name='fioTestConfig', blank=True)
    node_name = models.CharField(max_length=100, null=True)
   
    FioTypes = models.TextChoices('FioTypes', 'READ WRITE READWRITE NO_TYPE')
    fio_type = models.CharField(choices=FioTypes.choices, max_length=15, default='NO_TYPE')  

    IO_depth = models.IntegerField()
    block_size = models.CharField(max_length=5)
    file_size = models.CharField(max_length=10)
    access_mode = models.CharField(max_length=30)
    reset_refillbuffer = models.BooleanField(default=False)
    pv_size = models.CharField(max_length=10)
    pv_claim_name = models.CharField(max_length=150)





class FioTestResult(models.Model):
    '''
    A Django Model class representing an fio test result.
    
    '''

    test = models.OneToOneField(Test, on_delete=models.CASCADE, primary_key=True, related_name='fioTestResult', blank=True)
    total_input_output_size_read = models.CharField(max_length=30, blank=True)
    total_iops_read = models.IntegerField(blank=True, default=0)
    total_read_write_speed_read = models.CharField(max_length=20, blank=True)
    total_run_time_read = models.CharField(max_length=30, blank=True)



class PGBenchTestConfig(models.Model):
    '''
    A Django Model class representing a configuration for an pgbench performance test.
    
    '''

    def plural():
        return 'pgbenches'

    test = models.OneToOneField(Test, on_delete=models.CASCADE, primary_key=True, related_name='pgbenchTestConfig', blank=True)
    host = models.CharField(max_length=100, blank=True)
    db_name  = models.CharField(max_length=100, blank=True)
    db_user =  models.CharField(max_length=60, blank=True)
    db_pw =  models.CharField(max_length=100, blank=True)
    port = models.CharField(max_length=20, blank=True)
    number_of_clients = models.CharField(max_length=5, blank=True)
    selects_only = models.CharField(max_length=10, blank=True)
    duration_in_seconds =  models.CharField(max_length=10, blank=True)
    thread_count = models.CharField(max_length=5, blank=True)
    scaling_factor = models.CharField(max_length=5, blank=True)
    node_name = models.CharField(max_length=100, null=True)
    


class PGBenchTestResult(models.Model):
    '''
    A Django Model class representing an fio test result.
    
    '''
    test = models.OneToOneField(Test, on_delete=models.CASCADE, primary_key=True, related_name='pgbenchTestResult', blank=True)
    scaling_factor = models.IntegerField(blank=True, default=0)
    duration_in_seconds = models.IntegerField(blank=True, default=0)
    initial_connection_time_in_ms = models.IntegerField(blank=True, default=0)
    number_of_clients = models.IntegerField(blank=True, default=0)
    number_of_threads = models.IntegerField(blank=True, default=0)
    latency_average_in_ms = models.IntegerField(blank=True, default=0)
    transactions_per_second = models.IntegerField(blank=True, default=0)
    number_of_transactions_processed = models.IntegerField(blank=True, default=0)
    


class TestEvent(models.Model):
    '''
    A Django Model class representing a test event in the context of Test Object. 
    
    '''

    class EventStates(models.TextChoices):
        '''
        A class describing the different event types for a TestEvent object.
    
        '''
        RUNNING = 'Running'
        CREATED_LOCALLY = 'Created Locally'        
        CRD_CREATED = 'Custom Resource Created'
        POD_CREATED = 'Pod Created'
        STARTED_CONTAINER = 'Started Container'
        FAILED = 'Failed'
        COMPLETED = 'Completed'
        UNKNOWN = 'Unknown'
        JOB_COMPLETED = 'Job Completed'
        RESOURCE_DELETED = 'Deleted Resource'


    test = models.ForeignKey(Test, on_delete=models.CASCADE, related_name='events')
    timestamp = models.DateTimeField()
    message  = models.CharField(max_length=100, default="")
    state = models.CharField(choices=EventStates.choices, max_length=30, default=EventStates.UNKNOWN)