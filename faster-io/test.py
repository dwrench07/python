#!/usr/bin/env python

"""
__author__ = "David Wrench, Your Name Here"
__copyright__ = ""
__credits__ = []
__license__ = "GPLv2"
__version__ = "1.0"
__maintainer__ = ""
__email__ = ""
__status__ = "Test"
"""


import os
import platform
import multiprocessing


# TODO:
# ask user to run multiprocessing? Y/N
# show user their system info (CPU's, Platform, psutils)
# show query to be executed, give chance to alter params


# Get CPU Count
try:
    cpu_count = os.cpu_count()
    print('CPU Count: ' + cpu_count)
except OSError:
    cpu_count = multiprocessing.cpu_count()
    print('CPU Count: ' + cpu_count)
else:
    print('Could not determine multiprocessing.')

# Check Platform for hyper threading
user_platform = platform.system()
if user_platform == 'OSX':
    v_cpu = os.popen('sysctl hw').readlines()[1:10]
    print('vCPU Count: ' + v_cpu)
elif user_platform == 'Linux':
    v_cpu = os.popen('lscpu').readlines()
    print('vCPU Count: ' + v_cpu)
else:
    v_cpu = os.popen('C:\Windows>echo %NUMBER_OF_PROCESSORS%').readlines()
    print('vCPU Count: ' + v_cpu)

"""
OR
import psutil
psutil.cpu_count()
psutil.cpu_count(logical=False)
"""

"""
Use pandas to query database
"""
import pandas as pandas

thread_limit = 10
con = ''

# Estimate records, does this also warm up the cache???
print('Estimating Records')
est_records  = pandas.io.sql.read_sql('COUNT(*)', con,)
print(est_records + ' Estimated Records')

"""
Example: est_threads = 10,000,000,000 (10 Billion)
for each billion records add 1 thread LIMIT=none
    for each 100 million records in each thread add 1 worker

"""

sql = ''

pandas.io.sql.read_sql(sql, 
                       con, 
                       index_col=None, 
                       coerce_float=True, 
                       params=None, 
                       parse_dates=None, 
                       columns=None)

"""
PyPy extension to utilize IO for task.
"""
#include "Python.h"
...

PyObject *pyfunc(PyObject *self, PyObject *args) {
   ...
   Py_BEGIN_ALLOW_THREADS
   // Threaded C code.  Must not use Python API functions
   ...
   Py_END_ALLOW_THREADS
   ...
   return result;
}