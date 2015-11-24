#!/usr/bin/env python
# -*- coding: utf-8 -*-
import requests, urllib2, urllib, base64
import simplejson as json
import data

def request_interface(url, method, parameter=None, DATA=None, security=data.SECURITY_KEY):
    method = method.lower()
    full_url = '%s%s' %(data.HOST, url)
    header = {
              'Authorization':  security,
              #'Content-type':   'application/json'
             }
    response = getattr(requests, method)(full_url, params=parameter, json=DATA, headers=header)
    return response
    
def generate_security_key(username, password):
    auth_hash = base64.b64encode(b'%s:%s' % (username, password)).decode('ascii')
    auth_hash = "Basic %s" %auth_hash
    return auth_hash
    
def generate_test_demo(billing=True,
    country=data.INDIA, bg_unit=data.MG_DL,
    height_unit=data.CM, validity=12, branding=data.GH_BRAND,
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
        'app_branding':     branding,
        'notes':            'abc'
    }
    
    demo_conf = request_interface('/api/v1/demo.json', 'POST', DATA=demo_data)
    assert (demo_conf.status_code == 200)
    demo_conf = eval(demo_conf.text)
    # Grab the password
    assert 'key' in demo_conf
    assert 'id' in demo_conf
    return demo_conf['key'], demo_conf['id']
    
def delete_test_demo(demo_id):
    demo_id = str(demo_id)
    url = '/api/v1/demo/%s.json' %demo_id
    response = request_interface(url, 'DELETE')
    assert (response.status_code == 204)
    
def enroll_new_staff(name, email, practice_id, security_key, role='0', language='en', is_practice_admin=True):
    practice_id = str(practice_id)
    staff_data = {
        'name':                 name,
        'email':                email,
        'role':                 role,
        'language':             language,
        'is_practice_admin':    is_practice_admin,
        'practice_id':          practice_id,
    }
    staff_conf = request_interface('/api/v1/gurus.json', 'POST', DATA=staff_data, security=security_key)
    assert (staff_conf.status_code == 201), 'Respones status code is %s' %staff_conf.status_code

def get_staff_invitation_email(security_key):
    staff_email = request_interface('/slave/invitations', 'GET', security=security_key)
    assert (staff_email.status_code == 200)
    staff_email = json.loads(staff_email.text)
    return staff_email
    
demo_data = generate_test_demo()
#demo_data1 = generate_test_demo()
#demo_data2 = generate_test_demo(country=data.US)
#doctor_account_demo1 = 'doctor-%s@gatherhealth.com' %demo_data1[0]
#doctor_account_demo2 = 'doctor-%s@gatherhealth.com' %demo_data2[0]
#demo2_security = generate_security_key('doctor@gatherhealth.com', demo_data2[0])
## Enroll demo1 doctor to demo2
#enroll_new_staff('doctor2', doctor_account_demo1, demo_data2[1], demo2_security)


