from apps.test_service.models import FioTestConfig, PGBenchTestConfig, iPerfTestConfig

class TestConfigService:
    """
    A class responsible for creating test configuration objects for performance tests.
    
    """


    @staticmethod
    def create_fio_testconfig(request, test):
        '''
        Creates a new FIO testconfig object in the database based on the passed HttpRequest object. The 
        function extracts the relevant parameters from the request object.


            Parameters:
                        test (Test): Test model object
                        request (HttpRequest): Django HTTP Request Object
            Returns:
                        test_config (FioTestConfig): The created test config object
        '''

        test_config = FioTestConfig(
         node_name=request.POST.get('nodename', "no_name_found"),
         test=test, 
         IO_depth=2, 
         block_size=request.POST.get('block_size', '0'),
         file_size=request.POST.get('filesize', '0'),
         access_mode=request.POST.get('access_mode', 'default'),
         pv_claim_name=request.POST.get('pv_claim_name', 'default'))

        test_config.save()

        return test_config

    @staticmethod
    def create_iPerf3_testconfig(request, test):
        '''
        Creates a new iperf3 testconfig object in the database based on the passed HttpRequest object. The 
        function extracts the relevant parameters from the request object.


            Parameters:
                        request (HttpRequest): Django HttP Request Object
                        test (Test): Test model object
            Returns:
                        test_config (iPerfTestConfig): The created test config object
        '''
        test_config = iPerfTestConfig(
            test=test, 
            client_node = request.POST.get('clientNode', "no_name_found"),
            server_node = request.POST.get('serverNode', "no_name_found"),           

        )

        test_config.save()

        return test_config

    @staticmethod
    def create_pgbench_testconfig(request, test):
        '''
        Creates a new pgbench testconfig object in the database based on the passed HttpRequest object. The 
        function extracts the relevant parameters from the request object.


            Parameters:
                        request (HttpRequest): Django HttP Request Object
                        test (Test): Test model object
            Returns:
                        test_config (PGBenchTestConfig): The created test config object
        '''
        print("")

        test_config = PGBenchTestConfig(
            test=test, 
            host=request.POST.get('dbhost', "db_host"),
            node_name = request.POST.get('nodename', ""),
            db_name = request.POST.get('dbname', "db_name"),
            db_user = request.POST.get('dbuser', "db_user"),
            db_pw = request.POST.get('dbpassword', "db_password"),
            port = request.POST.get('dbport', "0000"),
            number_of_clients = request.POST.get('numberofclients', '0'),
            selects_only = request.POST.get('selectsonly', 'false'),
            duration_in_seconds= request.POST.get('duration', '0'),
            scaling_factor = request.POST.get('scalingfactor', '1'),
            thread_count = request.POST.get('threadcount', '1')

        )

        test_config.save()

        return test_config