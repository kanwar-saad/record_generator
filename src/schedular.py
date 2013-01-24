from __future__ import division

import sys, re
import simplejson as json
from ordereddict import OrderedDict
from pprint import pprint
import globals


def schedular_init():
    conf = globals.edg_conf
    for schema, params in conf['conf']['metadata_info'].items():
        params['delta'] = 1/params['output_rate']       # floating point number
        params['next_run_at'] = 0.0
        params['records_left'] = params['number_of_records']

    return True

def get_next_schedule():
    conf = globals.edg_conf
    sched_time = 0.0
    sched_schema = ''
    ret = {}

    # get schema which has nearest next_run_at value
    first = 1
    for schema, params in conf['conf']['metadata_info'].items():
        if first == 1:
            sched_time = params['next_run_at']
            first = 0

        if (params['next_run_at'] <= sched_time) and (params['records_left'] != 0):
            sched_time = params['next_run_at']
            sched_schema = schema

    # Update next run at value of selected schema

    if (sched_schema != ''):
        conf['conf']['metadata_info'][sched_schema]['next_run_at'] +=  conf['conf']['metadata_info'][sched_schema]['delta']
        conf['conf']['metadata_info'][sched_schema]['records_left'] -= 1
    
    #print conf['conf']['metadata_info'][sched_schema]['next_run_at']

    ret['schema'] = sched_schema
    ret['timestamp'] = sched_time

    return ret
        



