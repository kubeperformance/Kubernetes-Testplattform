# Kubernetes Testplatform


## Overview
The Kubernetes Testplatform enables users to execute performance tests inside a Kubernetes cluster. This project is based on a Master's thesis. Each test is executed from insde one or more containers, which are provisioned dynamcally at runtime

The following tests are supported :

1. Network test
2. Application test
3. Persistent memory test

The tests are based on the preexisting performance testing iperf3, pgbench and FIO.


## Features
  - Performance tests for:
    - Network bandwith
    - Database throughput
    - Persistent memory I/O speed
  - ARMv8 compatible
