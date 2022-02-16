from apps.test_service import testresult
from apps.test_service.models import FioTestResult, Test
from apps.test_service.testresult.iperf3.iperf3 import iPerf3ResultService
from apps.test_service.testresult.pgbench.pgbench_result_service import PGBenchTestResultService



class TestResultService:
    '''
    A class responsible for creating new testresults after the completion of a performancetest.
    Distinguishes between different test types. 
    
    '''
    
    @staticmethod 
    def create_result_after_finsih(test_id):
        '''
        Delegates the creation process of the test type for a given test to the responsible function

            Parameters:
                        test_id (int):  
            Returns:
                        None
        '''

        test = Test.objects.get(pk=test_id) 

        if test.test_name == Test.SupportedTests.FIO:
            TestResultService.create_fio_testresult(test)
        elif test.test_name == Test.SupportedTests.IPERF3:
            TestResultService.create_iPerf3_testresult(test)
        elif test.test_name == Test.SupportedTests.PGBENCH:
            TestResultService.create_pgbench_test_result(test)

        return None
    
    @staticmethod
    def create_fio_testresult(test):
        '''
        TO BE IMPLEMENTED
        Calls the FioTestResult result service to analye the test result. Object is saved after result creation.

            Parameters:
                        test (Test): Test for the result to be created
            Returns:
                        fio_test_result (FioTestResult): Result object
        '''
        fio_test_result = FioTestResult(test=test)
        
        fio_test_result.save()

        return fio_test_result


    @staticmethod
    def create_iPerf3_testresult(test):
        '''
        Calls the ipfer3 result service to analye the test result. Object is saved after result creation.

            Parameters:
                        test (Test): Test for the result to be created
            Returns:
                        iperf_test_result (iPerfTestResult): Result object
        '''               
        
        iperf_test_result = iPerf3ResultService.create_result_object(json_output=test.raw_output)
        iperf_test_result.test = test
        #iPerfTestResult(test=test)

        iperf_test_result.save()

        return iperf_test_result

  
  
    @staticmethod
    def create_pgbench_test_result(test):
        '''
        Calls the PGBenchTestResultService to analye the test result. Object is saved after result creation.

            Parameters:
                        test (Test): Test for the result to be created
            Returns:
                        pgbench_test_result (PGBenchTestResult): Result object
        '''
        pgbench_test_result =  PGBenchTestResultService.create_pgbench_result_object_from_output(test.raw_output)
        pgbench_test_result.test = test
        pgbench_test_result.save()

        return pgbench_test_result






