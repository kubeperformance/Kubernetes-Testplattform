import re
from apps.test_service.models import PGBenchTestResult

class PGBenchAnalyser:
    '''
    A class responsible for analysing the result of pgbench performancetests.
    
    '''

    keywords = ['scaling factor', 'number of clients', 'number of threads', 'duration',
    'number of transactions actually processed', 'latency average', 'tps', 'initial connection time']

    result = {}

    
    def analyse(self, text):
        '''
        Analyses the pgbench output and fills the result array. Filter process is based on the
        keywords in the keywords-variable

            Parameters: 
                        self (PGBenchAnalyser): instance
                        text (str): raw pgbench string output
            Returns:
                       None
        '''
        
        for line in text.splitlines():
            
            for word in self.keywords:
                
                if(word in line):

                    self.result[word] = int(re.findall(r'\d+',line)[0])
                    break

        return None


             
    def get_result(self):
        '''
        Retrieves the result from test analytics process

            Parameters: 
                        self (PGBenchAnalyser): instance
            Returns:
                        result (Dict): Keyword value mapping for pgbench result
        '''
    
        return self.result

    def analyse_and_get_result_as_dict(self, result_text):
        '''
        Streamlines the analytics process. Calls analyse method and returns the result variable

            Parameters: 
                        self (PGBenchAnalyser): instance
                        result_text (Str): raw pgbench string output
            Returns:
                        result (Dict): Keyword value mapping for pgbench result
        '''
        self.analyse(result_text)
        return self.result



class PGBenchTestResultService:
    

    @staticmethod
    def create_pgbench_result_object_from_output(result_string):
        '''
        Transforms the CLI-Output of a pgbench test in PGBenchTestResult object. The function
        uses the PGBenchAnalyser class for mapping the output.

            Parameters:
                        json_output (str): result as json string
            Returns:
                        PGBenchTestResult (PGBenchTestResult): Result object containing the result information
        '''

        pgbench_analyser = PGBenchAnalyser()
        result_dict = pgbench_analyser.analyse_and_get_result_as_dict(result_string)

        pgbench_test_result = PGBenchTestResult(
            scaling_factor = result_dict['scaling factor'],
            duration_in_seconds = result_dict['duration'],
            initial_connection_time_in_ms = result_dict['initial connection time'],
            number_of_clients = result_dict['number of clients'],
            number_of_threads = result_dict['number of threads'],
            latency_average_in_ms = result_dict['latency average'],
            transactions_per_second = result_dict['tps'],
            number_of_transactions_processed = result_dict['number of transactions actually processed'],
        )
        


        return pgbench_test_result