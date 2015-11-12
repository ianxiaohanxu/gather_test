#!/usr/bin/env python
# -*- coding: utf-8 -*-
import data, setup
import datetime, random
import simplejson as json
from time import sleep, time
import Nurse_A.Scenario.android_scenario

'''
Rewrite this method to set_server automatically
'''
def set_server(server='http://192.168.0.135:8000' , PORT=4723):
    phone = Nurse_A.Scenario.android_scenario.ANDROID(PORT=PORT)
    phone.verify(data.DM_AND_WELCOME_ENTER)
    phone.press('Back')
    phone.verify(data.DM_AND_SERVER_ADDRESS)
    phone.clear(data.DM_AND_SERVER_ADDRESS)
    phone.enter(server)
    phone.click(data.DM_AND_SERVER_SUBMIT)
    phone.verify(data.DM_AND_WELCOME_ENTER)
    phone.teardown()

def set_bg_goal(goals, patient_id, ACCOUNT=data.DOCTOR, PASSWORD=setup.demo_data[0]):
    security_key = setup.generate_security_key(ACCOUNT, PASSWORD)
    for index in range(7):
        if (goals >> index) % 2:
            goals_data = {
                          "id": 0,
                          "patient": "",
                          "created": "",
                          "updated": "",
                          "goal_task": "0",
                          "goal_task_friendly": "",
                          "is_active": True,
                          "expiration": "",
                          "frequency": "0",
                          "frequency_friendly": "",
                          "meal_time": "%d" %(7-index),
                          "meal_time_friendly": "",
                          "time_of_day": "",
                          "days_of_week": 0,
                          "days_of_week_friendly": "",
                          "day_of_month": 0,
                          "extras": "",
                          "goal_type_specific_info": ""
                         }
            response = setup.request_interface('/api/v1/patients/%s/goals/bg.json' %patient_id, 'POST', DATA=goals_data, security=security_key)
            assert(response.status_code == 201),'Response status code is %d' %response.status_code

def set_med_goal(goals, patient_id, ACCOUNT=data.DOCTOR, PASSWORD=setup.demo_data[0]):
    security_key = setup.generate_security_key(ACCOUNT, PASSWORD)
    if goals % 2:
        original_pres = setup.request_interface('/api/v1/patients/%s/prescriptions.json' %patient_id, 'GET', security=security_key)
        assert (original_pres.status_code == 200),'Response status code is %d' %original_pres.status_code
        original_pres = json.loads(original_pres.text)
        hash_str = original_pres['hash']
        goals_list = original_pres['prescriptions']
        goals_data = [{
                        'name':         'black',
                        'type':         '7',
                        'strength':     '5',
                        'units':        '2',
                        'timing':       '8',
                        'frequency':    '0',
                        'application':  '0',
                        'goals':        [{
                                        'timing':   '15:00',
                                        'amount':   '6'
                            }]
                      }]
        goals_list.extend(goals_data)
        pres_data = {
                        'hash':             hash_str,
                        'prescriptions':    goals_list
                    }
        response = setup.request_interface('/api/v1/patients/%s/prescriptions.json' %patient_id, 'PATCH', DATA=pres_data, security=security_key)
        assert(response.status_code == 200),'Response status code is %d' %response.status_code
    if (goals >> 1) % 2:
        original_pres = setup.request_interface('/api/v1/patients/%s/prescriptions.json' %patient_id, 'GET', security=security_key)
        assert (original_pres.status_code == 200),'Response status code is %d' %original_pres.status_code
        original_pres = json.loads(original_pres.text)
        hash_str = original_pres['hash']
        goals_list = original_pres['prescriptions']
        goals_data = [{
                        'name':         'blue',
                        'type':         '3',
                        'strength':     '6',
                        'units':        '1',
                        'timing':       '8',
                        'frequency':    '0',
                        'application':  '0',
                        'goals':        [{
                                        'timing':   'breakfast',
                                        'amount':   '5',
                            }]
                      }]
        goals_list.extend(goals_data)
        pres_data = {
                        'hash':             hash_str,
                        'prescriptions':    goals_list,
                    }
        response = setup.request_interface('/api/v1/patients/%s/prescriptions.json' %patient_id, 'PATCH', DATA=pres_data, security=security_key)
        assert(response.status_code == 200),'Response status code is %d' %response.status_code
    if (goals >> 2) % 2:
        original_pres = setup.request_interface('/api/v1/patients/%s/prescriptions.json' %patient_id, 'GET', security=security_key)
        assert (original_pres.status_code == 200),'Response status code is %d' %original_pres.status_code
        original_pres = json.loads(original_pres.text)
        hash_str = original_pres['hash']
        goals_list = original_pres['prescriptions']
        goals_data = [{
                        'name':         'purple',
                        'type':         '2',
                        'strength':     '',
                        'units':        '4',
                        'timing':       '8',
                        'frequency':    '0',
                        'application':  '0',
                        'goals':        [{
                                        'timing':   'breakfast',
                                        'amount':   '4',
                            }]
                      }]
        goals_list.extend(goals_data)
        pres_data = {
                        'hash':             hash_str,
                        'prescriptions':    goals_list,
                    }
        response = setup.request_interface('/api/v1/patients/%s/prescriptions.json' %patient_id, 'PATCH', DATA=pres_data, security=security_key)
        assert(response.status_code == 200),'Response status code is %d' %response.status_code
    if (goals >> 3) % 2:
        original_pres = setup.request_interface('/api/v1/patients/%s/prescriptions.json' %patient_id, 'GET', security=security_key)
        assert (original_pres.status_code == 200),'Response status code is %d' %original_pres.status_code
        original_pres = json.loads(original_pres.text)
        hash_str = original_pres['hash']
        goals_list = original_pres['prescriptions']
        goals_data = [
                        {
                        'name':         'specail_plus',
                        'type':         '3',
                        'strength':     '2+3',
                        'units':        '4',
                        'timing':       '8',
                        'frequency':    '0',
                        'application':  '0',
                        'goals':        [{
                                        'timing':   'breakfast',
                                        'amount':   '4+5',
                            }]
                        },
                        {
                        'name':         'specail_slash',
                        'type':         '5',
                        'strength':     '2/3',
                        'units':        '5',
                        'timing':       '8',
                        'frequency':    '0',
                        'application':  '0',
                        'goals':        [{
                                        'timing':   'breakfast',
                                        'amount':   '4/5',
                            }]
                        },
                        {
                        'name':         'specail_comma',
                        'type':         '6',
                        'strength':     '2,3',
                        'units':        '6',
                        'timing':       '8',
                        'frequency':    '0',
                        'application':  '0',
                        'goals':        [{
                                        'timing':   'breakfast',
                                        'amount':   '4,5',
                            }]
                        },
                        {
                        'name':         'specail_dot',
                        'type':         '7',
                        'strength':     '2.3',
                        'units':        '2',
                        'timing':       '8',
                        'frequency':    '0',
                        'application':  '0',
                        'goals':        [{
                                        'timing':   'breakfast',
                                        'amount':   '4.5',
                            }]
                        },
                      ]
        goals_list.extend(goals_data)
        pres_data = {
                        'hash':             hash_str,
                        'prescriptions':    goals_list,
                    }
        response = setup.request_interface('/api/v1/patients/%s/prescriptions.json' %patient_id, 'PATCH', DATA=pres_data, security=security_key)
        assert(response.status_code == 200),'Response status code is %d' %response.status_code

def get_patient_token(email, password):
    # Get a patient token
    patient_data = {
                    'username':    email,
                    'password': password,
                   }
    response = setup.request_interface('/oauth2/new/', 'POST', DATA=patient_data)
    assert(response.status_code == 200), 'Response status code is %d' %response.status_code
    token = 'Bearer %s' %json.loads(response.text)["access_token"]
    return token

def set_password(email, password):
    # Set password for a new patient
    password_data = {
                        'email':    email,
                        'password': password,
                    }
    response = setup.request_interface('/api/v1/users/setpw.json', 'POST', DATA=password_data)
    assert(response.status_code == 200), 'Response status code is %d' %response.status_code

def set_dob(dob, ACCOUNT, PASSWORD):
    # Set dob for a patient and accept user agreement
    token = get_patient_token(ACCOUNT, PASSWORD)
    dob_data = {
                "dob":              dob,
                "terms_agreed":     True,
               }
    response = setup.request_interface('/api/v1/users/self.json', 'PATCH', DATA=dob_data, security=token)
    assert(response.status_code == 200), 'Response status code is %d' %response.status_code

def set_meal_times(patient_id, ACCOUNT, PASSWORD, brk_time='08:00:00', lun_time='13:30:00', din_time='21:00:00', bed_time='23:30:00'):
    # Set meal times for a patient
    token = get_patient_token(ACCOUNT, PASSWORD)
    meal_time_data = {
                        'breakfast_time':   brk_time,
                        'lunch_time':       lun_time,
                        'dinner_time':      din_time,
                        'night_time':       bed_time,
                     }
    response = setup.request_interface('/api/v1/patients/%d/prefs.json' %patient_id, 'PATCH', DATA=meal_time_data, security=token)
    assert(response.status_code == 200), 'Response status code is %d' %response.status_code

def get_new_patient_account(practice_id=setup.demo_data[1], email=None, state=2,
        name=None, country_code='91', number='1234567890', billing=True,
        ACCOUNT=data.DOCTOR, PASSWORD=setup.demo_data[0], bg=None, med=None, after_sign_up=False
):
    # Create a new patient and return the email
    random_str = str(int(time())) + str(random.randint(0,1000))
    if email == None:
        email = 'test%s@test.com' %random_str
    if name == None:
        name = 'test%s' %random_str
    patient_data = {
                    'first_name'            : name,
                    'last_name'             : 'test',
                    'care_phone'            : number[:-1]+'1',
                    'care_phone_country'    : country_code,
                    'language'              : 'en',
                    'phone1_country'        : country_code,
                    'phone1'                : number,
                    'is_study'              : False,
                    'practice_id'           : practice_id,
                    'sex'                   : '0',
                    'study_id'              : '',
                    'state'                 : state,
                    'dob'                   : '1965-09-12',
                    'patient_phone_type'    : '',
                    'email'                 : email
                   }
    security_key = setup.generate_security_key(ACCOUNT, PASSWORD)
    patient = setup.request_interface('/api/v1/patients.json', 'POST', DATA=patient_data, security=security_key)
    assert (patient.status_code == 201),'Response status code is %d' %patient.status_code
    patient = json.loads(patient.text)
    assert 'id' in patient
    assert 'email' in patient
    assert 'first_name' in patient
    today = datetime.datetime.now().strftime('%Y-%m-%d')
    register_data = {
                    'practice'              : practice_id,
                    'patient_register_date' : today,
                    'guru_last_contact'     : today,
                    }
    registration = setup.request_interface('/api/v1/patients/%d/registrations.json' %patient['id'], 'POST', DATA=register_data, security=security_key)
    assert (registration.status_code == 201),'Response status code is %d' %registration.status_code
    if state == 2 and billing:
        subscription_data = {
                             'currency'     : 3,
                             'months'       : '1',
                             'price'        : '0',
                             'utc_offset'   : 330,
                            }
        subscription = setup.request_interface('/api/v1/patients/%d/subscription_transactions.json' %patient['id'], 'POST', DATA=subscription_data, security=security_key)
        assert (subscription.status_code == 201),'Response status code is %d' %subscription.status_code
    if bg != None:
        set_bg_goal(bg, patient['id'], ACCOUNT=ACCOUNT, PASSWORD=PASSWORD)
    if med != None:
        set_med_goal(med, patient['id'], ACCOUNT=ACCOUNT, PASSWORD=PASSWORD)
    if after_sign_up:
        set_password(patient['email'], data.PASSWORD)
        set_meal_times(patient['id'], patient['email'], data.PASSWORD)
        set_dob('1965-09-09', patient['email'], data.PASSWORD)
    return patient

patient_clean = get_new_patient_account(name='patient_clean', after_sign_up=True)
patient_bg = get_new_patient_account(name='patient_bg', bg=0b1000000, after_sign_up=True)
patient_med = get_new_patient_account(name='patient_med', med=0b100, after_sign_up=True)
patient_bg_med = get_new_patient_account(name='patient_bg_med', bg=0b1000000, med=0b100, after_sign_up=True)
patient_smed = get_new_patient_account(name='patient_smed', med=0b1000, after_sign_up=True)

#set_server()
