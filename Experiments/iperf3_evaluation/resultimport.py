from iperf3 import TestResult
import os
# Import Files
cwd = os.getcwd()
with open(cwd + '\\results\\result31.json', 'r') as stream:
    try:
        loaded = stream.read()
        result31 = TestResult(loaded)
    
    except Exception as exc:
        print(exc)

with open(cwd + '\\results\\result32.json', 'r') as stream:
    try:
        loaded = stream.read()
        result32 = TestResult(loaded)
    
    except Exception as exc:
        print(exc)

with open(cwd + '\\results\\result33.json', 'r') as stream:
    try:
        loaded = stream.read()
        result33 = TestResult(loaded)
    
    except Exception as exc:
        print(exc)


with open(cwd + '\\results\\result34.json', 'r') as stream:
    try:
        loaded = stream.read()
        result34 = TestResult(loaded)
    
    except Exception as exc:
        print(exc)

with open(cwd + '\\results\\result35.json', 'r') as stream:
    try:
        loaded = stream.read()
        result35 = TestResult(loaded)
    
    except Exception as exc:
        print(exc)




# 4 Results
with open(cwd + '\\results\\result41.json', 'r') as stream:
    try:
        loaded = stream.read()
        result41 = TestResult(loaded)
    
    except Exception as exc:
        print(exc)

with open(cwd + '\\results\\result42.json', 'r') as stream:
    try:
        loaded = stream.read()
        result42 = TestResult(loaded)
    
    except Exception as exc:
        print(exc)

with open(cwd + '\\results\\result43.json', 'r') as stream:
    try:
        loaded = stream.read()
        result43 = TestResult(loaded)
    
    except Exception as exc:
        print(exc)

        

with open(cwd + '\\results\\result44.json', 'r') as stream:
    try:
        loaded = stream.read()
        result44 = TestResult(loaded)
    
    except Exception as exc:
        print(exc)


with open(cwd + '\\results\\result45.json', 'r') as stream:
    try:
        loaded = stream.read()
        result45 = TestResult(loaded)
    
    except Exception as exc:
        print(exc)
