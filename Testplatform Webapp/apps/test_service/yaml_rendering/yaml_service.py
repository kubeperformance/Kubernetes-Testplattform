import os
import yaml


class CR_Generator:
    """
    A class responsible for the generation of the Kubestone Custom Resources. There is 
    one function for each test. The CRs are generated as dictionaries. Each one 
    is an equivalent of a .yml file that can be applied to the cluster
    
    """

    @staticmethod
    def correctify_string(string):
        
        alphanumeric=""

        for character in string:
            if character.isalnum():

                alphanumeric += character
        return alphanumeric


    @staticmethod
    def generate_fio_crd_as_dict(io_depth, block_size, file_size, access_mode, custom_test_name, node_name, pv_size, pvc_name):
        
        '''
        Creates a new FIO CRD as a dictionary. 
        

            Parameters:
                        io_depth (int): FIO I/O Depth
                        block_size (int): FIO block size
                        file_size (int): File size of the file to be created
                        access_mode (str): Access mode e.g. random/sequential read/write
                        custom_test_name (str): Name of the test
                        node_name (str): Name of the node where the test should be executed
                        pv_size (str): Size of the persistent volume
                        pvc_name (str): Name of the persistent volume claim if exists

            Returns:
                        fio_crd_as_dict (dict): FIO CRD as dictionary
        '''
        config = '--name=' + custom_test_name +  ' --iodepth=' + str(io_depth) + ' --rw=randwrite' + ' --bs=' + str(block_size) + 'm'  + ' --size=' + str(file_size) + 'M' + '----output-format=normal'
        image_name = 'kubeperformance/fio:latest'
        pull_secret = ''
        

        fio_crd_as_dict = {
            "apiVersion": "perf.kubestone.xridge.io/v1alpha1",
            "kind": "Fio",
            "metadata": {"name": custom_test_name},
            "spec": {
                "cmdLineArgs": config,
                "podConfig": {"podScheduling": {"nodeName": node_name}},
                "image": {"name": image_name, "pullSecret":pull_secret},
                "volume": {"persistenVolumeClaimSpec": {"accessModes": [access_mode], "resources": {"requests" : {"storage" : pv_size}}}
                
                , "volumeSource" : {"persistentVolumeClaim" : {"claimName" : pvc_name}}}            
            }
        }

        print(fio_crd_as_dict["metadata"]["name"])

        return fio_crd_as_dict


    @staticmethod
    def generate_iperf_crd_as_dict(custom_test_name, client_name, server_name):
        '''
        Creates a new iperf3 CRD as a dictionary. 

            Parameters:
                        custom_test_name (str): Name of the test
                        client_name (str): Name of the client node (IP or DNS)
                        server_name (str): Name of the server node (IP or DNS)
                       
            Returns:
                        iperf_crd_as_dict (dict): iperf3 CRD as dictionary
        '''


        image_name = 'kubeperformance/iperf3:latest'
        pull_secret = ''

        iperf_crd_as_dict = {
            "apiVersion": "perf.kubestone.xridge.io/v1alpha1",
            "kind": "Iperf3",
            "metadata": {"name": custom_test_name},
            "spec": {                
                "image": {"name": image_name, "pullSecret": pull_secret},
                "serverConfiguration": {"cmdLineArgs": "--verbose", "podLabels" : {"iperf-mode" : "server"}, "podScheduling" : {"nodeName": server_name}, "hostNetwork" : False},
                "clientConfiguration": {"cmdLineArgs": "-J", "podScheduling" : {"nodeName": client_name}},
                "udp": False
                #Spec End
                }            
            }
        
        #print(iperf_crd_as_dict["metadata"]["name"])
        print(yaml.dump(iperf_crd_as_dict))

        return iperf_crd_as_dict    


    
    @staticmethod
    def generate_pgbench_crd_as_dict(custom_test_name, host, db_name, db_user, db_pw, port, number_of_clients, selects_only, duration, scaling_factor, thread_count, node_name):
        '''
        Creates a new pgbench CRD as a dictionary. 

            Parameters:
                        custom_test_name (str): Name of the test
                        host (str): DBs Hostname
                        db_name (str): Name of the DB instance
                        db_user (str): DB user
                        db_pw (str): DB PW
                        port (str): Port
                        number_of_clients (str): Number of clients accessing the DB simultaneously
                        selects_only (str): 'on' or 'off'. Determines if only SELECT operations should be performed
                        duration (str): Duration in seconds
                        scaling_factor (str): Factor by which the database should be blown up (see pgbench config)
                        thread_count (str): Number of Threads
                        node_name (str): Name of the node where the test should be executed
                       
            Returns:
                        pgbench_crd_as_dict (dict): iperf3 CRD as dictionary
        '''

        image_name = 'kubeperformance/pgbench:latest'
        pull_secret = ''

        init_args = '-s ' + scaling_factor
        args = '-c ' + number_of_clients

        if(duration != ""):
            args = args + " -T " + duration
        if(thread_count != ""):
            args = args + " -j " + thread_count
        if(selects_only == "on"):
            args = args + " -S"


        pgbench_crd_as_dict = {
            "apiVersion": "perf.kubestone.xridge.io/v1alpha1",
            "kind": "Pgbench",
            "metadata": {"name": custom_test_name},
            "spec": {
                "podConfig": {"podScheduling": {"nodeName": node_name}},                
                "image": {"name": image_name, "pullSecret": pull_secret},
                "postgres": {"host": host, "port" : int(port), "user": db_user, "password": db_pw, "database": db_name},
                "initArgs": init_args,
                "args": args
                #Spec End
                }            
            }
        
        #print(iperf_crd_as_dict["metadata"]["name"])
        print(yaml.dump(pgbench_crd_as_dict))

        return pgbench_crd_as_dict