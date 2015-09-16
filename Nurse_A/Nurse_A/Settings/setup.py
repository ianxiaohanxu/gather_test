#!/usr/bin/env python
# -*- coding: utf-8 -*-
import requests, urllib2, urllib
import simplejson as json
import data

def request_interface(url, method, parameter=None, security=data.SECURITY_KEY):
    method = method.upper()
    if method not in ['GET', 'POST', 'DELETE']:
        raise Exception('Method %s not yet supported.' % method)
    full_url = '%s%s' %(data.HOST, url)
    auth = 'Basic %s' %security
    req = urllib2.Request(full_url)
    req.add_header('Authorization', auth)
    if parameter != None:
        req.add_data(urllib.urlencode(parameter))
    if method == 'DELETE':
        req.get_method = lambda: 'DELETE'
    response = urllib2.urlopen(req)
    return response
    
                             
def generate_test_demo(billing=True, 
    country=data.INDIA, bg_unit=data.MG_DL, 
    height_unit=data.CM, validity=12, 
    language=data.ENGLISH, demo_conf=data.DEMO_TEST
):
    demo_data = {
        'doctor_name':      'doctor_test',
        'nurse_name':       'nurse_test',
        'bg_units':         bg_unit,
        'height_units':     height_unit,
        'language_code':    language,
        'country':          country,
        'period':           validity,
        'data':             demo_conf,
        'billing_enabled':  billing,
        'notes':            'abc'
    }
    
    demo_conf = request_interface('/api/v1/demo.json', 'POST', parameter=demo_data)
    assert (demo_conf.code == 200)
    demo_conf = eval(demo_conf.read())
    # Grab the password
    assert 'key' in demo_conf
    assert 'id' in demo_conf
    return demo_conf['key'], demo_conf['id']
    
def delete_test_demo(demo_id):
    demo_id = str(demo_id)
    url = '/api/v1/demo/%s.json' %demo_id
    response = request_interface(url, 'DELETE')
    assert (response.code == 204)
    
demo_data = generate_test_demo()