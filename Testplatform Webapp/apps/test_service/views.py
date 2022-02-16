from django.http.response import HttpResponse
from django.shortcuts import redirect, render

from django.contrib.auth.decorators import login_required
from django.contrib import messages, sessions
from apps.test_service.models import PGBenchTestConfig, Test, FioTestConfig, iPerfTestConfig

from apps.test_service.performancetest.test_service import TestService
from apps.test_service.testevent.event_service import TestEventService
from apps.test_service.testconfig.testconfig_service import TestConfigService
from apps.test_service.cluster_gateway.cluster_gateway import ClusterGateway

import sys

'''
This file contains all the Django Views utilized in the context of the test service.

'''


@login_required(login_url="/login/")
def test_overview(request):
    '''
    Returns a rendered view of all test instances as list and the number of tests    

    Parameters:
                    request (HttpRequest): Django Request Object    
    '''
    all_tests_as_list = list(Test.objects.all())
    test_count = len(all_tests_as_list)
    
    #Continue
    if(test_count > 0):
        test = all_tests_as_list[0]
       # result = test.fioTestResult
       # rawoutput = test.raw_output

    #print(all_tests_as_list[0].test_name)
   
    return render(request, "testoverview.html", {'testsAsList': all_tests_as_list, 'numberOfTests':test_count})


@login_required(login_url="/login/")
def get_test(request, test_id):
    '''
    Returns a test overview page for the requested test.
    Each testobject is queried with regard to its type. 
    Depending on the type, the corresponding HTML page
    is returned and rendered. 

        Parameters:
                    request (HttpRequest): Django Request Object
                    test_id (int): ID of the requested test as int
    '''
    
    test = Test.objects.get(pk=test_id) 
    print("Trying to get test with ID " + str(test_id), file=sys.stderr)   
        
    try:
        test = Test.objects.get(pk=test_id)
      

    except Test.DoesNotExist as e:
        print("Test Does not Exist exception")
        return render(request, "page-404.html", {})


    if test.test_name == Test.SupportedTests.FIO:
        config = test.fioTestConfig
        result = test.fioTestResult

        return render(request, "fio-test-overview.html", {'test': test, 'fio_test_config': config,
        'fio_test_result': result, 'node_name':config.node_name})
        
     

    elif test.test_name == Test.SupportedTests.IPERF3:
        config = test.iPerf3Config
        result = test.iPerf3TestResult
    
        return render(request, "iperf3-test-overview.html", {'test': test, 'iperf3_config': config,
        'iperf3result': result, 'node_name':config.client_node})

    elif test.test_name == Test.SupportedTests.PGBENCH:
        config = test.pgbenchTestConfig
        result = test.pgbenchTestResult

        
        return render(request, "pgbench-test-overview.html", {'test': test, 'pgbench_config': config,
        'pgbench_result': result, 'node_name':config.node_name})


@login_required(login_url="/login/")
def delete_test(request, test_id):
    '''
    Deletes the test and its associated objects with the requested
    id in the Database

        Parameters:
                    request (HttpRequest): Django Request Object
                    test_id (int): ID of the requested test as int
                
    '''
    
    
    print("Trying to delete test with ID " + str(test_id), file=sys.stderr)   
        
    try:
        test = Test.objects.get(pk=test_id)
        test.delete()
        return redirect(test_overview)


      

    except Test.DoesNotExist as e:
        print("Test Does not Exist exception")
        return render(request, "page-404.html", {})        
        



@login_required(login_url="/login/")
def new_fio_test(request):
    '''
    Renders the HTML page for creating a new FIO test.
    In case the Method is POST, a new test object is created and 
    the new test is initiated. Returns a rendered test-status page. 

        Parameters:
                    request (HttpRequest): Django Request Object
    '''
    if request.method == 'POST':        

        if TestService.test_name_exists(request.POST.get('testname', 'no_name_found').lower().replace(" ", "")):
            messages.error(request, 'Testname already exists')

            return render(request, "newfiotest.html", {})
        
        new_test = TestService.create_new_test(Test.SupportedTests.FIO, Test.TestCategory.NODE, request, FioTestConfig.plural())
        fio_test_config = TestConfigService.create_fio_testconfig(request, new_test)
        
        TestService.start_new_fio_test(new_test, fio_test_config)
         
        messages.success(request, str(new_test.id))
        return render(request, "test-status-fragment.html", {"test": new_test})

    else:        
        messages.success(request, str(""))
        return render(request, "newfiotest.html", {})


@login_required(login_url="/login/")
def new_iperf3_test(request):
    '''
    Renders the HTML page for creating a new iperf3 test.
    In case the Method is POST, a new test object is created and 
    the new test is initiated. Returns a rendered test-status page. 

        Parameters:
                    request (HttpRequest): Django Request Object
    '''
    if request.method == 'POST':        
        
        #Check for name
        if TestService.test_name_exists(request.POST.get('testname', 'no_name_found').lower().replace(" ", "")):
            messages.error(request, 'Testname already exists')

            return render(request, "newiperf3test.html", {})


        new_test = TestService.create_new_test(Test.SupportedTests.IPERF3, Test.TestCategory.INFRASTRUCTURE, request,  iPerfTestConfig.plural())
        iperf_test_config = TestConfigService.create_iPerf3_testconfig(request, new_test)
        #test_result = TestResultService.create_iPerf3_testresult(new_test)        
        
        TestService.start_new_iPerf3_test(new_test, iperf_test_config)
        
     
        messages.success(request, str(new_test.id))
        return render(request, "test-status-fragment.html", {"test": new_test})

    else:
       
        messages.success(request, str(""))
        return render(request, "newiperf3test.html", {})


@login_required(login_url="/login/")
def new_pg_bench_test(request):
    '''
    Renders the HTML page for creating a new FIO test.
    In case the Method is POST, a new test object is created and 
    the new test is initiated. Returns a rendered test-status page. 

        Parameters:
                    request (HttpRequest): Django Request Object                
    '''
    if request.method == 'POST':     

        if TestService.test_name_exists(request.POST.get('testname', 'no_name_found').lower().replace(" ", "")):
            messages.error(request, 'Testname already exists')

            return render(request, "newpgbenchtest.html", {})   
        
        new_test = TestService.create_new_test(Test.SupportedTests.PGBENCH, Test.TestCategory.APPLICATION, request,  PGBenchTestConfig.plural())
        pgbench_test_config =TestConfigService.create_pgbench_testconfig(request, new_test) 
      
        #test_result = TestResultService.create_iPerf3_testresult(new_test)        
        
        TestService.start_new_pgbench_test(new_test, pgbench_test_config)
        
        messages.success(request, str(new_test.id))
        return render(request, "test-status-fragment.html", {"test": new_test})

    else:
       
        messages.success(request, str(""))
        return render(request, "newpgbenchtest.html", {})


@login_required(login_url="/login/")
def get_events_for_test(request, test_id):
    '''
    Returns a HTTP-Response Object in JSON-Fomrat containing all events of the
    requested test. Only responds to GET-Requests.

        Parameters:
                    request (HttpRequest): Django Request Object
                    test_id (int): ID of the requested test as int
    '''

    if request.method == 'GET':             
        events_as_json = TestEventService.get_events_for_test_as_json(test_id)
        #print(events_as_json)     
        
        return HttpResponse(events_as_json, content_type='application/json')


@login_required(login_url="/login/")
def home(request):
    '''
    Returns a rendered HTML-Homepage. The method queries the counts of each testtype
    and the nodes of the kubernetes-cluster. 

        Parameters:
                    request (HttpRequest): Django Request Object                    
    '''
    
    nodes = []
    nodes = ClusterGateway.get_nodes()
    testcounts = TestService.get_counts_for_test_type()
    iper3_test_count = testcounts[Test.SupportedTests.IPERF3]
    fio_test_count = testcounts[Test.SupportedTests.FIO]
    pgbench_test_count = testcounts[Test.SupportedTests.PGBENCH]


    print("HOME")

    return render(request, "index.html", {"nodes": nodes, "iperf3_test_count":iper3_test_count,
    "fio_test_count":fio_test_count,
    "pgbench_test_count":pgbench_test_count})