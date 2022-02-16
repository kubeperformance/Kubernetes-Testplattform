
from apps.test_service.models import Test,TestEvent
from apps.test_service.cluster_gateway.cluster_gateway import ClusterGateway
from apps.test_service.testevent.event_service import TestEventService
from apps.test_service.monitoring.test_monitoring import TestMonitoring
from apps.test_service.yaml_rendering.yaml_service import CR_Generator

import datetime


class TestService:
    """
    A class responsible for creating test objects. The class also implements specific service functions for managing
    and querying tests.
    
    """


    @staticmethod
    def create_new_test(test_name, test_category, request, plural):
        '''
        Creates a new test object based on the parameters. If the test creation
        was successfull the test is saved to the database. The Method creates
        a new test event after saving the test.

            Parameters:
                        test_name (str): Name of the test
                        test_category (str): Category of the test
                        request (HttpRequest): Django Request Object
                        plural (str): Plural of the test

            Returns:
                        new_test (Test): The created test
        '''    
        
        
        new_test = Test(custom_test_name=request.POST.get('testname', 'no_name_found').lower().replace(" ",""),
        test_name=test_name,
        test_status=Test.TestStatusTypes.CREATED_LOCALLY,
        test_category = test_category,
        namespace=request.POST.get('namespace', 'default'),
        plural=plural
        )        
        
        new_test.save()              

        TestEventService.create_test_event(new_test, datetime.datetime.utcnow(), "Resource Created", TestEvent.EventStates.CREATED_LOCALLY)

        return new_test




    @staticmethod
    def start_new_fio_test(test, fio_test_config):
        '''
        Iniitiates a new FIO-Test. Therefore, the CRD-Generation Service is used to generate
        a Custom Resource as a dictionary. 


            Parameters:
                        test (Test): Test model object
                        fio_test_config (FioTestConfig): Configuration of the test

            Returns:
                        new_test (Test): The created test
        '''
        test_name = test.custom_test_name
        namespace = test.namespace

        crd_as_dict = CR_Generator.generate_fio_crd_as_dict(fio_test_config.IO_depth, fio_test_config.block_size, fio_test_config.file_size, 
        fio_test_config.access_mode, test_name, fio_test_config.node_name ,fio_test_config.pv_size, fio_test_config.pv_claim_name)        
        
        
        return TestService.start_test_for_crd(test, crd_as_dict, namespace) 
       



    @staticmethod
    def start_new_iPerf3_test(test, iPerf_config):
        '''
        Iniitiates a new iperf3-Test. Therefore, the CRD-Generation Service is used to generate
        a Custom Resource as a dictionary. 


            Parameters:
                        test (Test): Test model object
                        iperf_config (iPerfTestConfig): Configuration of the test
                        request (HttpRequest): Django Request Object

            Returns:
                        new_test (Test): The created test
        '''
        test_name = test.custom_test_name
        crd_as_dict = CR_Generator.generate_iperf_crd_as_dict(test_name, iPerf_config.client_node, iPerf_config.server_node)
        namespace = test.namespace

        return TestService.start_test_for_crd(test, crd_as_dict, namespace)


    @staticmethod
    def start_new_pgbench_test(test, pgbench_testconfig):
        '''
        Iniitiates a new pgbench-Test. Therefore, the CRD-Generation Service is used to generate
        a Custom Resource as a dictionary. 


            Parameters:
                        test (Test): Test model object
                        pgbench_testconfig (PGBenchTestConfig): Configuration of the test
                        request (HttpRequest): Django Request Object

            Returns:
                        new_test (Test): The created test
        '''
        test_name = test.custom_test_name
        
        crd_as_dict = CR_Generator.generate_pgbench_crd_as_dict(custom_test_name=test_name, host=pgbench_testconfig.host, db_name=pgbench_testconfig.db_name,
        db_user=pgbench_testconfig.db_user, db_pw=pgbench_testconfig.db_pw, port=pgbench_testconfig.port, number_of_clients=pgbench_testconfig.number_of_clients,
        selects_only=pgbench_testconfig.selects_only, duration=pgbench_testconfig.duration_in_seconds, scaling_factor=pgbench_testconfig.scaling_factor, 
        thread_count=pgbench_testconfig.thread_count, node_name=pgbench_testconfig.node_name)

        namespace = test.namespace

        return TestService.start_test_for_crd(test, crd_as_dict, namespace)


    @staticmethod
    def start_test_for_crd(test, cr_as_dict, namespace):
        '''
        Starts a new Performancetest in the Kubernetes-Cluster. The Clustergateway class
        is used for communication. If the test creation was successfull, the function starts
        the monitoring process.


            Parameters:
                        test (Test): Test model object
                        cr_as_dict (dict): CRD as Dictionary
                        namespace (str): The namespace the test should be deployed to

            Returns:
                        resource_created (Boolean): True if resource creation was successfull false otherwise
        '''
        
        resource_created = ClusterGateway.create_cr_in_cluster(cr_as_dict, test.plural, namespace)

        if resource_created:            
            
            TestEventService.create_test_event(test=test, timestamp=datetime.datetime.utcnow(), message="CR Created", state=TestEvent.EventStates.CRD_CREATED)
            TestMonitoring.start_test_monitoring(test_id=test.id, namespace=namespace)
        
        return resource_created

    
    @staticmethod
    def get_counts_for_test_type():
        '''
        Counts the number of tests for each test type. Returns a Dictionary


            Parameters:
                       
            Returns:
                        testcounts (dict): A mapping between Test.SupportedTest.Types and the number of tests
                        in that category
        '''

        fio_count = 0
        pgbench_count = 0
        iperf3_count= 0

        testcounts = {}

        tests = Test.objects.all()
        for test in tests:

            if test.test_name == Test.SupportedTests.FIO:
               fio_count+=1
            elif test.test_name == Test.SupportedTests.PGBENCH:
                pgbench_count+=1
            elif test.test_name == Test.SupportedTests.IPERF3:
                iperf3_count+=1

            


        testcounts[str(Test.SupportedTests.FIO)] = fio_count
        testcounts[Test.SupportedTests.IPERF3] = iperf3_count
        testcounts[Test.SupportedTests.PGBENCH] = pgbench_count

        return testcounts

 
    
    
    @staticmethod
    def test_name_exists(name):
        '''
        Checks if the passed testname already exists. 


            Parameters:
                        name (str): Testname to check
                       
            Returns:
                        (Boolean): True if testname already exists, false otherwise
        '''

        tests = Test.objects.all()
        
        for test in tests:
            if test.custom_test_name == name: return True

        return False