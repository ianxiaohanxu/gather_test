# -*- coding: utf-8 -*-

# SECURITY_KEY                	=   u'YWxleEBnYXRoZXJoZWFsdGguY29tOmdhb3h1MTIz'
SECURITY_KEY                	=   u'Basic YWxleEBnYXRoZXJoZWFsdGguY29tOjEyMzQ1Ng=='
HK_DOCTOR                   	=   'alex+hk@gatherhealth.com'
HK_NURSE                    	=   'alex+hk+n@gatherhealth.com'
INDIA_DOCTOR                	=   'alex+in@gatherhealth.com'
INDIA_NURSE                 	=   'alex+innurse@gatherhealth.com'
DOCTOR_FREE                 	=   'alex+free@gatherhealth.com'
NURSE_FREE                  	=   'alex+freenurse@gatherhealth.com'
US_DOCTOR                   	=   'alex+us@gatherhealth.com'
US_NURSE                    	=   'alex+us+n@gatherhealth.com'
DOCTOR                      	=   'doctor@gatherhealth.com'
NURSE                       	=   'nurse@gatherhealth.com'
PASSWORD                    	=   '123456'

Stag0                       	=   'http://stag0.gatherhealth.com/provider'
Stag1                       	=   'https://stag1.gatherhealth.com/provider'
Stag2                       	=   'https://stag2.gatherhealth.com/provider'
Stag3                       	=   'https://stag3.gatherhealth.com/provider'
Stag4                       	=   'https://stag4.gatherhealth.com/provider'
Production                  	=   'https://www.gatherhealth.com/provider'
Localhost                   	=   'http://localhost:8000/provider'
SERVER                      	=   Localhost

# if SERVER == Localhost:
#     HOST                    	=   'http://localhost:8081'
# else:
HOST                        	=   SERVER[:-9]

DIRECTORY_PATH              	=   SERVER+'/directory'
FEED_PATH                   	=   SERVER+'/feed'

# Color
GREY_CONFIRM                	=   u'rgba(0, 0, 0, 0.25)'
BLUE_CONFIRM                	=   u'rgba(50, 179, 230, 1)'
GREEN_CONFIRM               	=   u'rgba(127, 210, 67, 1)'

# Country
INDIA                       	=   'IN'
US                          	=   'US'
CHINA                       	=   'CN'
HK                          	=   'HK'

# Branding
GH_BRAND                    	=   'gather-health'

# Language
ENGLISH                     	=   'en'
SIMPLE_CHINESE              	=   'zh-cn'
TRADITIONAL_CHINESE         	=   'zh-tw'
INDIAN                      	=   'hi'

# BG units
MG_DL                       	=   '0'
MMO_L                       	=   '1'

# Height units
CM                          	=   '0'
IN                          	=   '1'

# Weight units
KG                          	=   '0'
LB                          	=   '1'

# BP units
MMHG                        	=   '0'
KPA                         	=   '1'

# Units group
SI                          	=   '8239'
CONV                        	=   '1128'

# Country code          
US_COUNTRY_CODE             	=   '1'
IN_COUNTRY_CODE             	=   '91'
HK_COUNTRY_CODE             	=   '852'
CH_COUNTRY_CODE             	=   '86'

# Filter
FILTER_ALL_PATIENT          	=   ''
FILTER_STUDY_PATIENT        	=   'IsOnStudy = \"True\"'
FILTER_TYPE_ONE             	=   'Type = \"1\"'
FILTER_TYPE_TWO             	=   'Type = \"2\"'
FILTER_GESTATIONAL          	=   'Type = \"Gest\"'
FILTER_PRE_DIABETES         	=   'Type = \"Pre\"'
FILTER_OTHER                	=   'Type = \"Other\"'
FILTER_ACTIVE               	=   'Status = Active'
FILTER_INACTIVE             	=   'Status = Inactive'
FILTER_NOT_INSTALL          	=   'Status = \"Not Installed\"'
FILTER_EHR_ONLY             	=   'Status = EHR'
FILTER_A1C                  	=   'A1C > 7'
FILTER_BG_CONTROL           	=   'BGControl < 30'
FILTER_MEDADH               	=   'MedAdh < 50'
FILTER_NEXT_APPOINTMENT     	=   'NextAppointment >= today'
FILTER_WILL_EXPIRE          	=   'DaysLeft >= 0 AND DaysLeft <= 14'
FILTER_EXPIRED              	=   'DaysLeft < 0 AND IsOnStudy = \"False\"'

# Patient directory columns
LAST                        	=   '1'
FIRST                       	=   '2'
MED_ADH                     	=   '3'
SMBG_ADH                    	=   '4'
BG_CONTROL                  	=   '5'
PRACTICE_NAME               	=   '6'
NEXT_APPT                   	=   '7'
LAST_APPT                   	=   '8'
STATUS                      	=   '9'
LAST_BG                     	=   '10'
LAST_CONTACT                	=   '11'
JOINED                      	=   '12'
SUBSCRIPTION                	=   '13'
EXPIRES                     	=   '14'
TYPE                        	=   '15'
A1C                         	=   '16'
AGE                         	=   '17'

# Sign up steps name
SIGN_UP_CONFIRM_INFO        	=   'Confirm info'
SIGN_UP_SIGN_AGREEMENT      	=   'Sign agreement'
SIGN_UP_PRACTICE_CONTACT    	=   'Practice contact'
SIGN_UP_UPLOAD_PHOTO        	=   'Upload photo'
SIGN_UP_ADD_PHONE           	=   'Add phone'
SIGN_UP_INVITE_STAFF        	=   'Invite staff'

# Demo configuration
DEMO_TEST                   	=   '4100'

# Different language version 'Account'
ACCOUNT_HK                  	=   '帳戶'
ACCOUNT_IN                  	=   'खाता'
ACCOUNT_CH                  	=   '用户设置'
ACCOUNT_US                  	=   'ACCOUNT'


PR_LOGIN_TITLE              	=   u'Gather \u22c5 Login'
PR_FEED_TITLE               	=   u'Gather \u22c5 Patient Feed'
HKID                        	=   'X356888'
HKID_CHECK                  	=   'A'
ADD_PATIENT                 	=   u'ADD PATIENT'

MED_GOALS                   	=   [
                                 ['G1', '2', '', '4', 'abc', '8', '0', '5', '6', '5', '5', '5', '09:00'],
                                 ['ABC', '4', '5', '1', 'abc', '9', '0', '5', '5', '5', '5', '5', '20:00'],
                                 ['G2', '3', '5', '2', 'abc', '8', '0', '5', '6', '5', '5', '5', '09:00'],
                                 ['G3', '5', '5', '3', 'abc', '9', '4', '5', '5', '5', '5', '5', '20:00'],
                                 ['G4', '6', '5', '4', 'abc', '8', '5', '5', '6', '5', '5', '5', '09:00'],
                                 ['G5', '7', '5', '5', 'abc', '9', '6', '5', '5', '5', '5', '5', '20:00'],
                                 ['G6', '8', '5', '6', 'abc', '8', '7', '5', '6', '5', '5', '5', '09:00'],
                                 ['G7', '9', '5', '0', 'abc', '9', '8', '5', '5', '5', '5', '5', '20:00'],
                                 ['G8', '10', '5', '1', 'abc', '8', '9', '5', '6', '5', '5', '5', '09:00'],
                                 ['G9', '11', '5', '1', 'abc', '9', '10', '5', '5', '5', '5', '5', '20:00'],
                                 ['G10', '12', '5', '1', 'abc', '8', '2', '5', '6', '5', '5', '5', '09:00'],
                                 ['G11', '13', '5', '1', 'abc', '9', '3', '5', '5', '5', '5', '5', '20:00'],
                                 ['G12', '14', '5', '1', 'abc', '8', '0', '5', '6', '5', '5', '5', '09:00'],
                                 ['G13', '15', '5', '1', 'abc', '9', '0', '5', '5', '5', '5', '5', '20:00'],
                                 ['G14', '16', '5', '1', 'abc', '8', '0', '5', '6', '5', '5', '5', '09:00'],
                                ]

SMALL_MED_GOALS             	=   [
                                 ['G1', '2', '', '4', 'abc', '8', '0', '5', '', '', '', '', '09:00'],
                                 ['G2', '4', '5', '1', 'abc', '9', '0', '', '6', '', '', '', '09:00'],
                                ]

SPECIAL_MED_GOALS           	=   [
                                 ['G1', '2', '2+2', '2', 'abc', '8', '0', '5+2', '', '', '', '', '09:00'],
                                 ['G2', '4', '4/3', '1', 'abc', '9', '0', '', '6/4', '', '', '', '09:00'],
                                 ['G3', '4', '4.3', '3', 'abc', '9', '0', '', '6.5', '', '', '', '09:00'],
                                 ['G4', '4', '4,3', '5', 'abc', '9', '0', '', '6,3', '', '', '', '09:00'],
                                ]

WEEKDAY                     	=   ['mon', 'tue', 'wed', 'thu', 'fri', 'sat', 'sun']
MEAL                        	=   ['brk', 'lun', 'din']
NIGHT                       	=   'night'
PRE_POST                    	=   ['pre', 'post']

# Message content
MES_CONTENT_BIGGEST_SUCCESS                 	=   "It appears you're lagging on your blood sugar measurements, so I wanted to help you make a plan to fit them into your life. When in the past have you been successful in making a change in your life and how did you do it?"
MES_GROUP_SMS_SUCCESS                       	=   "Your SMS is in the queue now and will go out shortly."
MES_GROUP_SMS_FAIL                          	=   "We are having technical problems sending out your SMS. Please try again later."
MES_PATIENT_SEARCH_NO_RESULT                	=   "No results"

# Error messages
EM_PR_ACCOUNT_PASSWORD_LENGH                	=   'Password must be between 6 and 64 characters.'
EM_PR_ACCOUNT_PASSWORD_MATCH                	=   'Value must match.'
EM_PR_ACCOUNT_PASSWROD_STRENGTH_WEAK        	=   'weak'
EM_PR_ACCOUNT_PASSWROD_STRENGTH_TOO_WEAK    	=   'too weak'
EM_PR_ACCOUNT_CELL_NUM_IN_US                	=   'Phone number must be 10 digits, numbers only.'
EM_PR_ACCOUNT_CELL_NUM_HK                   	=   'Phone number must be 8 digits, numbers only.'
EM_PR_ACCOUNT_CELL_NUM_CH                   	=   'Phone number must be 11 digits, numbers only.'

EM_PR_MANAGE_PRACTICE_CELL_NUM_IN_US        	=   EM_PR_ACCOUNT_CELL_NUM_IN_US
EM_PR_MANAGE_PRACTICE_CELL_NUM_HK           	=   EM_PR_ACCOUNT_CELL_NUM_HK
EM_PR_MANAGE_PRACTICE_CELL_NUM_CH           	=   EM_PR_ACCOUNT_CELL_NUM_CH

EM_PR_NPF_EMPTY_SURNAME                     	=   'Surname field must be filled out'
EM_PR_NPF_EMPTY_GIVEN_NAME                  	=   'Given names field must be filled out'
EM_PR_NPF_EMPTY_PATIENT_CELL                	=   'Patient cell field must be filled out'
EM_PR_NPF_EMPTY_GENDER                      	=   'Gender must be selected.'
EM_PR_NPF_INVALID_P_NUMBER                  	=   'Invalid patient phone number'
EM_PR_NPF_EMPTY_EMAIL                       	=   'Email address field must be filled out'
EM_PR_NPF_EMPTY_MONTHLY_RATE                	=   'Enter a non-zero value'
EM_PR_NPF_INVALID_EMAIL                     	=   'Invalid patient email'
EM_PR_NPF_DUPLICATE_EMAIL                   	=   'A user with this email already exists'
EM_PR_NPF_INVALID_LO_NUMBER                 	=   'Invalid loved one phone number'
EM_PR_NPF_DUPLICATE_NUMBER_WITH_PATIENT     	=   'Patient and loved one phone number can not be the same.'

EM_PR_PRESCRIPTION_REQUIRED                 	=   'This field is required.'
EM_PR_PRESCRIPTION_STRENGTH                 	=   'This field can contain only numbers and punctuation.'
# EM_PR_PRESCRIPTION_DOSAGE                   	=   'This field must be a number.'
EM_PR_PRESCRIPTION_DOSAGE                   	=   EM_PR_PRESCRIPTION_STRENGTH
EM_PR_PRESCRIPTION_DOSAGE_NON_ZERO          	=   'This field must be a non-zero number.'

EM_SIGN_UP_REQUIRED                         	=   EM_PR_PRESCRIPTION_REQUIRED
EM_SIGN_UP_PASSWORD_LENGH                   	=   'Password must be at least 6 characters.'
EM_SIGN_UP_PASSWORD_MATCH                   	=   EM_PR_ACCOUNT_PASSWORD_MATCH
EM_SIGN_UP_SIGNATURE_SERVER_ERROR           	=   'Signature can contain only letters, commas, periods, dashes, apostrophes, quotation marks, and spaces.'
EM_SIGN_UP_CELL_NUMBER_IN_US                	=   EM_PR_ACCOUNT_CELL_NUM_IN_US
EM_SIGN_UP_CELL_NUMBER_HK                   	=   EM_PR_ACCOUNT_CELL_NUM_HK
EM_SIGN_UP_CELL_NUMBER_CH                   	=   EM_PR_ACCOUNT_CELL_NUM_CH
EM_SIGN_UP_INVITE_SHORT_ERROR               	=   'Please complete the form.'
EM_SIGN_UP_INVITE_LONG_ERROR                	=   'Guru name, email, and role are required.'
EM_SIGN_UP_INVALID_EMAIL                    	=   'Invalid email address.'

# Locator
PR_TUTORIAL_WELCOME                         	=   '.walkthrough_start'
PR_TUTORIAL_WELCOME_CLOSE                   	=   '.walkthrough_start .close'
PR_TUTORIAL_TOOLTIP_HELP                    	=   '.tut_bubble'
PR_TUTORIAL_TOOLTIP_HELP_CLOSE              	=   '.tut_bubble .submit'

PR_NAV_FEED                                 	=   '.feed a'
PR_NAV_ADD_PATIENT                          	=   '.normal .add a'
PR_NAV_OPTION_MENU                          	=   '.dropdown-toggle .avatar'
PR_NAV_OPTION_MENU_LOGOUT                   	=   '.user .dropdown-menu>li:nth-last-child(1) a'
PR_NAV_OPTION_MENU_ACCOUNT                  	=   '.user .dropdown-menu>li:nth-child(1) a'
'''It is history now.'''
# PR_NAV_OPTION_MENU_MANAGE_PRACTICE          	=   '.user .dropdown-menu>li:nth-child(2) a'

PR_NAV_OPTION_MENU_FIRST_PRACTICE           	=   '.user .dropdown-menu .practices li:nth-child(1) a'
PR_NAV_OPTION_MENU_PRACTICE                 	=   '.user .dropdown-menu .practices li a'
PR_NAV_SWITCH                               	=   '.demo ul a'

PR_ADD_PATIENT_SURNAME                      	=   'input[name="last_name"]'
PR_ADD_PATIENT_GIVENAME                     	=   'input[name="first_name"]'
PR_ADD_PATIENT_PRACTICE                     	=   'select[name="practice_id"]'
PR_ADD_PATIENT_P_COUNTRY_CODE               	=   'select[name="phone1_country"]'
PR_ADD_PATIENT_P_NUMBER                     	=   'input[name="phone1"]'
PR_ADD_PATIENT_L_COUNTRY_CODE               	=   'select[name="care_phone_country"]'
PR_ADD_PATIENT_L_NUMBER                     	=   'input[name="care_phone"]'
PR_ADD_PATIENT_NORMAL_PATIENT               	=   'normal_patient'
PR_ADD_PATIENT_APP_PATIENT                  	=   'app_patient'
PR_ADD_PATIENT_EMAIL                        	=   'input[name="email"]'
PR_ADD_PATIENT_LANGUAGE                     	=   'select[name="language"]'
PR_ADD_PATIENT_GENDER_MALE                  	=   'input[name="sex"][value="0"]'
PR_ADD_PATIENT_GENDER_FEMALE                	=   'input[name="sex"][value="1"]'
PR_ADD_PATIENT_HAS_HKID_NO                  	=   'input[name="has_hkid"][value="false"]'
PR_ADD_PATIENT_HAS_HKID_YES                 	=   'input[name="has_hkid"][value="true"]'
PR_ADD_PATIENT_HKID                         	=   'input[name="hkid"]'
PR_ADD_PATIENT_HKID_CHECK                   	=   'input[name="hkid_check"]'
PR_ADD_PATIENT_PREMIUM_TRIAL                	=   '#premium_trial_subscription'
PR_ADD_PATIENT_INVITE_BUTTON                	=   'input.full_width'
PR_ADD_PATIENT_BASIC_ERROR                  	=   '.patient_create_submit div.error div'
PR_ADD_PATIENT_FINAL_BUTTON                 	=   'button.final'
PR_ADD_PATIENT_TITLE                        	=   '.heading h1'
PR_ADD_PATIENT_BILL_TIME                    	=   'subscription.months'
PR_ADD_PATIENT_BILL_RATE                    	=   'subscription.price'
PR_ADD_PATIENT_BILL_RATE_ERROR              	=   '.payments div.validation_errors'
PR_ADD_PATIENT_PATIENT_TYPE                 	=   'patient_type'
PR_ADD_PATIENT_PATIENT_YEAR                 	=   'diagnosis_date'
PR_ADD_PATIENT_PATIENT_COMORBIDITIES        	=   'textarea.comos'
PR_ADD_PATIENT_PATIENT_NOTES                	=   'patient_notes'
PR_ADD_PATIENT_PRE_LOWER_LIMIT              	=   'bg.pre_lower_limit'
PR_ADD_PATIENT_PRE_UPPER_LIMIT              	=   'bg.pre_upper_limit'
PR_ADD_PATIENT_POST_LOWER_LIMIT             	=   'bg.post_lower_limit'
PR_ADD_PATIENT_POST_UPPER_LIMET             	=   'bg.post_upper_limit'
PR_ADD_PATIENT_EVERY_PRE_BRK                	=   'bg.every_pre_brk'
PR_ADD_PATIENT_EVERY_POST_BRK               	=   'bg.every_post_brk'
PR_ADD_PATIENT_EVERY_PRE_LUN                	=   'bg.every_pre_lun'
PR_ADD_PATIENT_EVERY_POST_LUN               	=   'bg.every_post_lun'
PR_ADD_PATIENT_EVERY_PRE_DIN                	=   'bg.every_pre_din'
PR_ADD_PATIENT_EVERY_POST_DIN               	=   'bg.every_post_din'
PR_ADD_PATIENT_EVERY_NIGHT                  	=   'bg.every_night'
PR_ADD_PATIENT_EVERY                        	=   [PR_ADD_PATIENT_EVERY_PRE_BRK, PR_ADD_PATIENT_EVERY_POST_BRK,
                                                 PR_ADD_PATIENT_EVERY_PRE_LUN, PR_ADD_PATIENT_EVERY_POST_LUN,
                                                 PR_ADD_PATIENT_EVERY_PRE_DIN, PR_ADD_PATIENT_EVERY_POST_DIN,
                                                 PR_ADD_PATIENT_EVERY_NIGHT,]
SMALL_BG_GOALS                              	=   [PR_ADD_PATIENT_EVERY_PRE_BRK, PR_ADD_PATIENT_EVERY_POST_LUN]
PR_ADD_PATIENT_OTHER_MED                    	=   '.other_meds'
PR_ADD_PATIENT_MED_GOALS_BUTTON             	=   '.med button'
PR_ADD_PATIENT_BP_FREQUENCY                 	=   'select[name="bp.frequency"]'
VALUE_ADD_PATIENT_BPWEIGHT_FREQUENCY_NEVER  	=   'never'
VALUE_AND_PATIENT_BPWEIGHT_FREQUENCY_DAILY  	=   'daily_weekly'
VALUE_AND_PATIENT_BPWEIGHT_FREQUENCY_2WEEK  	=   '2weeks'
VALUE_AND_PATIENT_BPWEIGHT_FREQUENCY_4WEEK  	=   '4weeks'
PR_ADD_PATIENT_BP_DAILY_TABLE               	=   'section.bp table.entry-measurement-goal'
PR_ADD_PATIENT_BP_EVERY_PRE_BRK             	=   'bp.every_pre_brk'
PR_ADD_PATIENT_BP_EVERY_PRE_LUN             	=   'bp.every_pre_lun'
PR_ADD_PATIENT_BP_EVERY_PRE_DIN             	=   'bp.every_pre_din'
PR_ADD_PATIENT_BP_EVERY_NIGHT               	=   'bp.every_night'
PR_ADD_PATIENT_BP_WEEKDAY                   	=   'select[name="bp.weekday"]'
PR_ADD_PATIENT_BP_NEXT_MEASURE_DAY          	=   'section.bp span.next_measurement_day'
PR_ADD_PATIENT_WEIGHT_TARGET                	=   'input[name="weight.target_weight"]'
PR_ADD_PATIENT_WEIGHT_FREQUENCY             	=   'select[name="weight.frequency"]'
PR_ADD_PATIENT_WEIGHT_DAILY_TABLE           	=   'section.weight table.entry-measurement-goal'
PR_ADD_PATIENT_WEIGHT_EVERY_PRE_BRK         	=   'weight.every_pre_brk'
PR_ADD_PATIENT_WEIGHT_EVERY_PRE_LUN         	=   'weight.every_pre_lun'
PR_ADD_PATIENT_WEIGHT_EVERY_PRE_DIN         	=   'weight.every_pre_din'
PR_ADD_PATIENT_WEIGHT_EVERY_NIGHT           	=   'weight.every_night'
PR_ADD_PATIENT_WEIGHT_WEEKDAY               	=   'select[name="weight.weekday"]'
PR_ADD_PATIENT_WEIGHT_NEXT_MEASURE_DAY      	=   'section.weight span.next_measurement_day'
PR_ADD_PATIENT_HEIGHT                       	=   'input[name="height"]'
PR_ADD_PATIENT_WEIGHT                       	=   'weight'
PR_ADD_PATIENT_WAIST                        	=   'waist'
PR_ADD_PATIENT_A1C                          	=   'a1c'
PR_ADD_PATIENT_BP_SYS                       	=   'bp_sys'
PR_ADD_PATIENT_BP_DIA                       	=   'bp_dia'

PR_SIGN_UP_STEP_LINE                        	=   'section.steps'
PR_SIGN_UP_ACTIVE_STEP                      	=   'div.active>div.legend'
PR_SIGN_UP_LAST_NAME                        	=   'input[name="last_name"]'
PR_SIGN_UP_LAST_NAME_VALIDATION             	=   'input[name="last_name"]+div.validation_errors'
PR_SIGN_UP_FIRST_NAME                       	=   'input[name="first_name"]'
PR_SIGN_UP_FIRST_NAME_VALIDATION            	=   'input[name="first_name"]+div.validation_errors'
PR_SIGN_UP_DOCTOR_ID                        	=   'input[name="registration_number"]'
PR_SIGN_UP_DOCTOR_ID_VALIDATION             	=   'input[name="registration_number"]+div.validation_errors'
PR_SIGN_UP_DEFAULT_LANG                     	=   'select[name="language"]'
PR_SIGN_UP_PASSWORD                         	=   'input[name="password"]'
PR_SIGN_UP_PASSWORD_VALIDATION              	=   'input[name="password"]+div.validation_errors'
PR_SIGN_UP_PASSWORD_CONFIRM                 	=   'input[name="password_confirm"]'
PR_SIGN_UP_PASSWORD_CONFIRM_VALIDATION      	=   'input[name="password_confirm"]+div.validation_errors'
PR_SIGN_UP_NEXT_BUTTON                      	=   'button#next'
PR_SIGN_UP_ACCEPT_CHECKBOX                  	=   'input[name="terms_agreed"]'
PR_SIGN_UP_SIGNATURE                        	=   'input[name="signature"]'
PR_SIGN_UP_SIGNATURE_ERROR                  	=   'span.server_error'
PR_SIGN_UP_COUNTRY_CODE                     	=   'select[name="phone_country"]'
PR_SIGN_UP_PRACTICE_NUMBER                  	=   'input[name="phone_number"]'
PR_SIGN_UP_PRACTICE_NUMBER_VALIDATION       	=   'input[name="phone_number"]+div.validation_errors'
PR_SIGN_UP_CELL_NUMBER                      	=   'input[name="phone_number"]'
PR_SIGN_UP_CELL_NUMBER_VALIDATION           	=   'input[name="phone_number"]+div.validation_errors'
PR_SIGN_UP_VERIFY_SEND_BUTTON               	=   'button.send_confirmation'
PR_SIGN_UP_STAFF_NAME                       	=   'input[name="name"]'
PR_SIGN_UP_STAFF_EMAIL                      	=   'input[name="email"]'
PR_SIGN_UP_STAFF_ROLE                       	=   'select[name="role"]'
PR_SIGN_UP_STAFF_LANG                       	=   'select[name="language"]'
PR_SIGN_UP_STAFF_RIGHT                      	=   'select[name="is_practice_admin"]'
PR_SIGN_UP_STAFF_INVITE_BUTTON              	=   'button#invite_submit'
PR_SIGN_UP_STAFF_INVITE_ERROR               	=   'div#invite_error'


PR_PRESCRIPTION_DIALOG                      	=   'div.medications'
PR_PRESCRIPTION_TITLE                       	=   'div.medications h3'
PR_PRESCRIPTION_VISIBLE_ENTRY               	=   '//tr[@class="prescription_input"]'
PR_PRESCRIPTION_ENTRY                       	=   'div.medications tr.prescription_input'
PR_PRESCRIPTION_ENTRY_NAME                  	=   '.med_name input'
PR_PRESCRIPTION_ENTRY_TYPE                  	=   '.med_type select'
PR_PRESCRIPTION_ENTRY_STRENGTH              	=   '.med_strength input'
PR_PRESCRIPTION_ENTRY_UNIT                  	=   '.med_units select'
PR_PRESCRIPTION_ENTRY_INSTRUCTION           	=   '.med_instructions input'
PR_PRESCRIPTION_ENTRY_PRE_POST              	=   'select.med_meal'
PR_PRESCRIPTION_ENTRY_FREQUENCY             	=   'select.med_frequency'
PR_PRESCRIPTION_ENTRY_DOSAGE_BRE            	=   '.breakfast input'
PR_PRESCRIPTION_ENTRY_DOSAGE_LUN            	=   '.lunch input'
PR_PRESCRIPTION_ENTRY_DOSAGE_DIN            	=   '.dinner input'
PR_PRESCRIPTION_ENTRY_DOSAGE_NIG            	=   '.night input'
PR_PRESCRIPTION_ENTRY_DOSAGE_TIME           	=   '.specific_time input'
PR_PRESCRIPTION_ENTRY_TIME                  	=   '.specific_time select'
PR_PRESCRIPTION_ENTRY_DURATION              	=   '.duration input'
PR_PRESCRIPTION_ENTRY_DELETE                	=   'td.delete>div.delete'
PR_PRESCRIPTION_ENTRY_VALIDATION            	=   'div.g_validation_errors'
PR_PRESCRIPTION_ADD_NEW                     	=   'div.medications div.add'
PR_PRESCRIPTION_SAVE                        	=   'div.medications button.submit'
PR_PRESCRIPTION_CLOSE                       	=   'div.medications div.close'
PR_PRESCRIPTION_DOCTOR_DROPDOWN             	=   'div.medications select[name="guru"]'
PR_PRESCRIPTION_PRINT                       	=   'div.medications .medications_print'

PR_PRESCRIPTION_CONFIRM_DIALOG              	=   'div.medications_confirm'
PR_PRESCRIPTION_CONFIRM_CANCEL              	=   'div.medications_confirm button.cancel'
PR_PRESCRIPTION_CONFIRM_SAVE                	=   'div.medications_confirm button.submit'

    
PR_BG_GOALS_CLOSE_BUTTON                    	=   '.smbg_goals .close'
PR_BG_GOALS_SAVE_BUTTON                     	=   '.smbg_goals .submit'

PR_PATIENT_RECORD_ID                        	=   '.id span'
PR_PATIENT_RECORD_NAME                      	=   'h1.name'
PR_PATIENT_RECORD_NAME_DIALOG               	=   'div.edit_patient_name'
PR_PATIENT_RECORD_NAME_SURNAME              	=   'input[name="last_name"]'
PR_PATIENT_RECORD_NAME_GIVEN_NAME           	=   'input[name="first_name"]'
PR_PATIENT_RECORD_NAME_CANCEL               	=   'div.edit_patient_name div.cancel'
PR_PATIENT_RECORD_NAME_SAVE                 	=   'div.edit_patient_name div.submit'
PR_PATIENT_RECORD_NAME_CLOSE                	=   'div.edit_patient_name div.close'
PR_PATIENT_RECORD_INFO                      	=   '.indicator li.status'
PR_PATIENT_RECORD_MEDICATION_NAMES          	=   'div.new_rx table tr div.name'
PR_PATIENT_RECORD_CHAT                      	=   '.indicator li.messaging'
PR_PATIENT_RECORD_CHAT_QUICK_BUTTON         	=   'quick_msg'
PR_PATIENT_RECORD_QUICK_MES_TITLE           	=   '.quick_msg_modal h3'
PR_PATIENT_RECORD_QUICK_MES_BIG_SUCCESS     	=   'dl.open dd:nth-child(6)'
PR_PATIENT_RECORD_QUICK_MES_SEND            	=   '.msg_input .btn'
PR_PATIENT_RECORD_CHAT_TEXTAREA             	=   '.patientdetail-msg-compose'
PR_PATIENT_RECORD_CHAT_SEND_BUTTON          	=   '#patientdetail-msg-form input[type="submit"]'
PR_PATIENT_RECORD_CHAT_SECOND_MES           	=   '.scroller-content li:nth-child(2) div.text'
PR_PATIENT_RECORD_CHAT_LATEST_MES           	=   '.scroller-content li:nth-last-child(3) div.text'
PR_PATIENT_RECORD_SMBG                      	=   '.smbg'
PR_PATIENT_RECORD_SMBG_COUNTER              	=   '.smbg_counter'
VALUE_PATIENT_RECORD_SMBG_COUNTER_TEXT          =   'Measure %s times weekly'
PR_PATIENT_RECORD_SMBG_TITLE                	=   '.smbg_goals h3'
PR_PATIENT_RECORD_EVERY_PRE_BRK                	=   'every_pre_brk'
PR_PATIENT_RECORD_EVERY_POST_BRK               	=   'every_post_brk'
PR_PATIENT_RECORD_EVERY_PRE_LUN                	=   'every_pre_lun'
PR_PATIENT_RECORD_EVERY_POST_LUN               	=   'every_post_lun'
PR_PATIENT_RECORD_EVERY_PRE_DIN                	=   'every_pre_din'
PR_PATIENT_RECORD_EVERY_POST_DIN               	=   'every_post_din'
PR_PATIENT_RECORD_EVERY_NIGHT                  	=   'every_night'
PR_PATIENT_RECORD_EVERY                         =   [PR_PATIENT_RECORD_EVERY_PRE_BRK, PR_PATIENT_RECORD_EVERY_POST_BRK, PR_PATIENT_RECORD_EVERY_PRE_LUN,
                                                     PR_PATIENT_RECORD_EVERY_POST_LUN, PR_PATIENT_RECORD_EVERY_PRE_DIN, PR_PATIENT_RECORD_EVERY_POST_DIN,
                                                     PR_PATIENT_RECORD_EVERY_NIGHT,]
PR_PATIENT_RECORD_BP_NONE                   	=   'div.bp li.none'
PR_PATIENT_RECORD_BP_COUNTER                	=   'li.bp_counter'
PR_PATIENT_RECORD_BP_DIALOG                 	=   'div.bp_goals'
PR_PATIENT_RECORD_BP_DIALOG_CLOSE_BTN       	=   'div.bp_goals div.close'
PR_PATIENT_RECORD_BP_DIALOG_SAVE_BTN        	=   'div.bp_goals input.submit'
PR_PATIENT_RECORD_BP_DIALOG_FREQUENCY       	=   'div.bp_goals select[name="frequency"]'
VALUE_PATIENT_BPWEIGHT_FREQUENCY_NEVER      	=   'never'
VALUE_PATIENT_BPWEIGHT_FREQUENCY_DAILY      	=   'daily_weekly'
VALUE_PATIENT_BPWEIGHT_FREQUENCY_2WEEK      	=   '2weeks'
VALUE_PATIENT_BPWEIGHT_FREQUENCY_4WEEK      	=   '4weeks'
PR_PATIENT_RECORD_BP_DIALOG_DAILY_TABLE     	=   'div.bp_goals table.entry-measurement-goal'
PR_PATIENT_RECORD_BP_DIALOG_EVERY_PRE_BRK   	=   'div.bp_goals input[name="every_pre_brk"]'
PR_PATIENT_RECORD_BP_DIALOG_EVERY_PRE_LUN   	=   'div.bp_goals input[name="every_pre_lun"]'
PR_PATIENT_RECORD_BP_DIALOG_EVERY_PRE_DIN   	=   'div.bp_goals input[name="every_pre_din"]'
PR_PATIENT_RECORD_BP_DIALOG_EVERY_NIGHT     	=   'div.bp_goals input[name="every_night"]'
PR_PATIENT_RECORD_BP_DIALOG_WEEKDAY         	=   'div.bp_goals select[name="weekday"]'
PR_PATIENT_RECORD_BP_DIALOG_NEXT_DAY        	=   'div.bp_goals span.next_measurement_day'
PR_PATIENT_RECORD_WEIGHT_NONE               	=   'div.weight li.none'
PR_PATIENT_RECORD_WEIGHT_COUNTER            	=   'li.weight_counter'
PR_PATIENT_RECORD_WEIGHT_TARGET             	=   'span.target_weight'
PR_PATIENT_RECORD_WEIGHT_DIALOG                 =   'div.weight_goals'
PR_PATIENT_RECORD_WEIGHT_DIALOG_CLOSE_BTN       =   'div.weight_goals div.close'
PR_PATIENT_RECORD_WEIGHT_DIALOG_SAVE_BTN        =   'div.weight_goals input.submit'
PR_PATIENT_RECORD_WEIGHT_DIALOG_FREQUENCY       =   'div.weight_goals select[name="frequency"]'
PR_PATIENT_RECORD_WEIGHT_DIALOG_TARGET          =   'div.weight_goals input[name="target_weight"]'
PR_PATIENT_RECORD_WEIGHT_DIALOG_DAILY_TABLE     =   'div.weight_goals table.entry-measurement-goal'
PR_PATIENT_RECORD_WEIGHT_DIALOG_EVERY_PRE_BRK   =   'div.weight_goals input[name="every_pre_brk"]'
PR_PATIENT_RECORD_WEIGHT_DIALOG_EVERY_PRE_LUN   =   'div.weight_goals input[name="every_pre_lun"]'
PR_PATIENT_RECORD_WEIGHT_DIALOG_EVERY_PRE_DIN   =   'div.weight_goals input[name="every_pre_din"]'
PR_PATIENT_RECORD_WEIGHT_DIALOG_EVERY_NIGHT     =   'div.weight_goals input[name="every_night"]'
PR_PATIENT_RECORD_WEIGHT_DIALOG_WEEKDAY         =   'div.weight_goals select[name="weekday"]'
PR_PATIENT_RECORD_WEIGHT_DIALOG_NEXT_DAY        =   'div.weight_goals span.next_measurement_day'
VALUE_PATIENT_RECORD_BPWEIGHT_FREQUENCY_1   	=   'Measure %s times weekly'
VALUE_PATIENT_RECORD_BPWEIGHT_FREQUENCY_2   	=   'Measure every 2 weeks'
VALUE_PATIENT_RECORD_BPWEIGHT_FREQUENCY_3   	=   'Measure every 4 weeks'
# PR_PATIENT_RECORD_MED_GOALS                 	=   '.meds_schedule'
# PR_PATIENT_RECORD_MED_GOALS_UNCONFIRM       	=   '.meds_schedule .alert.med-ack'
PR_PATIENT_RECORD_PRESCRIPTION              	=   '.new_rx'
PR_PATIENT_RECORD_PRESCRIPTION_UNCONFIRM    	=   '.new_rx .alert.med-ack'
PR_PATIENT_RECORD_PRE_MEAL_RANGE            	=   '.pre_meal'
PR_PATIENT_RECORD_POST_MEAL_RANGE           	=   '.post_meal'
PR_PATIENT_RECORD_PRE_MEAL_BG_UNIT          	=   '.smbg .units'
PR_PATIENT_RECORD_POST_MEAL_BG_UNIT         	=   '.smbg .post_meal+span'
PR_PATIENT_RECORD_BILLING                   	=   'billing_tab_select'
PR_PATIENT_RECORD_BILLING_OVERVIEW          	=   '#billing .overview'
PR_PATIENT_RECORD_BILLING_BASIC_PLAN        	=   '#billing .basic .value'
PR_PATIENT_RECORD_BILLING_END_DATE          	=   '.expire_date'
PR_PATIENT_RECORD_BILLING_PREMIUM_RADIO     	=   'premium_subscription'
PR_PATIENT_RECORD_BILLING_FREE_TRIAL_RADIO  	=   'premium_trial_subscription'
PR_PATIENT_RECORD_BILLING_MONTH_RATE        	=   'subscription.price'
PR_PATIENT_RECORD_BILLING_TOTAL             	=   'subscription.total'
PR_PATIENT_RECORD_BILLING_RATE_ERROR        	=   '.validation_errors'
PR_PATIENT_RECORD_BILLING_SUBMIT            	=   '#billing .right'
PR_PATIENT_RECORD_BILLING_HISTOR_ENTRY      	=   '#billing-history tbody tr'
PR_PATIENT_RECORD_BILLING_FIRST_VOID        	=   '#billing td>a'
PR_PATIENT_RECORD_BILLING_FIRST_M           	=   '#billing table tr td:nth-child(3)'
PR_PATIENT_RECORD_BILLING_FIRST_R           	=   '#billing table tr td:nth-child(4)'
PR_PATIENT_RECORD_BILLING_FIRST_VOIDED      	=   'tr.voided'
PR_PATIENT_RECORD_BILLING_P_CONFIRM         	=   '.premium-subscription-confirm'
PR_PATIENT_RECORD_BILLING_P_CONFIRM_BACK    	=   '.premium-subscription-confirm .revert'
PR_PATIENT_RECORD_BILLING_P_CONFIRM_SUBMIT  	=   '.premium-subscription-confirm .submit'
PR_PATIENT_RECORD_BILLING_P_CONFIRM_DATE    	=   '.premium-subscription-confirm .new_end_date'
PR_PATIENT_RECORD_BILLING_F_CONFIRM         	=   '.trial-subscription-confirm'
PR_PATIENT_RECORD_BILLING_F_CONFIRM_BACK    	=   '.trial-subscription-confirm .revert'
PR_PATIENT_RECORD_BILLING_F_CONFIRM_SUBMIT  	=   '.trial-subscription-confirm .submit'
PR_PATIENT_RECORD_BILLING_F_CONFIRM_DATE    	=   '.trial-subscription-confirm .new_end_date'
PR_PATIENT_RECORD_BILLING_V_CONFIRM         	=   '.void-subscription-confirm'
PR_PATIENT_RECORD_BILLING_V_CONFIRM_BASIC   	=   '.void-subscription-confirm .basic_plan .value'
PR_PATIENT_RECORD_BILLING_V_CONFIRM_BACK    	=   '.void-subscription-confirm .revert'
PR_PATIENT_RECORD_BILLING_V_CONFIRM_SUBMIT  	=   '.void-subscription-confirm .submit'
PR_PATIENT_RECORD_BILLING_V_CONFIRM_DATE    	=   '.void-subscription-confirm .new_end_date'
PR_PATIENT_RECORD_SUMMARY_TAG               	=   'data-tab-summary'
PR_PATIENT_RECORD_SUMMARY_DIV               	=   'div[data-tab-name="graph-summary"]'
PR_PATIENT_RECORD_SUMMARY_BG_Y_LABEL        	=   '.summary_graph .y.label'
PR_PATIENT_RECORD_SUMMARY_MED_LAST_HISTORY  	=   'a.summary_last'
PR_PATIENT_RECORD_BG_TAG                    	=   '#data-tab-bg-data'
PR_PATIENT_RECORD_BG_DIV                    	=   'div[data-tab-name="graph-bg-data"]'
PR_PATIENT_RECORD_VISIT_TAG                 	=   'data-tab-visits'
PR_PATIENT_RECORD_VISIT_CONTENT             	=   '#visits'
PR_PATIENT_RECORD_VISIT_NEW_BUTTON          	=   '#visits .new'
PR_PATIENT_RECORD_VISIT_OLD_BUTTON          	=   '#visits .old'
PR_PATIENT_RECORD_VISIT_EMPTY_HISTORY       	=   '#visits .empty'
PR_PATIENT_RECORD_VISIT_AGGREGATE           	=   '#visits .aggregate'
PR_PATIENT_RECORD_VISIT_AGGREGATE_EXPLAIN   	=   '#visits .explain'
PR_PATIENT_RECORD_VISIT_DATE                	=   'input.today'
PR_PATIENT_RECORD_VISIT_DATEPICKER          	=   '.datepicker'
PR_PATIENT_RECORD_VISIT_DATE_LAST_MONTH     	=   '.datepicker-days .prev'
PR_PATIENT_RECORD_VISIT_DATE_SOME_DAY       	=   '.datepicker-days tbody>tr:nth-child(2)>td'
PR_PATIENT_RECORD_VISIT_NOTES               	=   '#visits [name="notes"]'
PR_PATIENT_RECORD_VISIT_NOTES_CONFIRM       	=   '#visits [name="notes"]+button'
PR_PATIENT_RECORD_VISIT_NOTES_DELETE        	=   '#visits [name="notes"]+button+button'
PR_PATIENT_RECORD_VISIT_HEIGHT              	=   '#visits [name="height"]'
PR_PATIENT_RECORD_VISIT_HEIGHT_CONFIRM      	=   '#visits [name="height"]+div+button'
PR_PATIENT_RECORD_VISIT_HEIGHT_DELETE       	=   '#visits [name="height"]+div+button+button'
PR_PATIENT_RECORD_VISIT_WEIGHT              	=   '#visits [name="weight"]'
PR_PATIENT_RECORD_VISIT_WEIGHT_CONFIRM      	=   '#visits [name="weight"]+div+button'
PR_PATIENT_RECORD_VISIT_WEIGHT_DELETE       	=   '#visits [name="weight"]+div+button+button'
PR_PATIENT_RECORD_VISIT_WAIST               	=   '#visits [name="waist"]'
PR_PATIENT_RECORD_VISIT_WAIST_CONFIRM       	=   '#visits [name="waist"]+div+button'
PR_PATIENT_RECORD_VISIT_WAIST_DELETE        	=   '#visits [name="waist"]+div+button+button'
PR_PATIENT_RECORD_VISIT_TEMPERATURE         	=   '#visits [name="temperature"]'
PR_PATIENT_RECORD_VISIT_TEMPERATURE_CONFIRM 	=   '#visits [name="temperature"]+div+div+button'
PR_PATIENT_RECORD_VISIT_TEMPERATURE_DELETE  	=   '#visits [name="temperature"]+div+div+button+button'
PR_PATIENT_RECORD_VISIT_BGROUP              	=   '#visits [name="blood_group"]'
PR_PATIENT_RECORD_VISIT_BGROUP_CONFIRM      	=   '#visits [name="blood_group"]+button'
PR_PATIENT_RECORD_VISIT_BGROUP_DELETE       	=   '#visits [name="blood_group"]+button+button'
PR_PATIENT_RECORD_VISIT_RHBGROUP            	=   '#visits [name="rh_blood_group"]'
PR_PATIENT_RECORD_VISIT_RHBGROUP_CONFIRM    	=   '#visits [name="rh_blood_group"]+button'
PR_PATIENT_RECORD_VISIT_RHBGROUP_DELETE     	=   '#visits [name="rh_blood_group"]+button+button'
PR_PATIENT_RECORD_VISIT_TOBACCO             	=   '#visits [name="tobacco"]'
PR_PATIENT_RECORD_VISIT_TOBACCO_CONFIRM     	=   '#visits [name="tobacco"]+button'
PR_PATIENT_RECORD_VISIT_TOBACCO_DELETE      	=   '#visits [name="tobacco"]+button+button'
PR_PATIENT_RECORD_VISIT_ALCOHOL             	=   '#visits [name="alcohol"]'
PR_PATIENT_RECORD_VISIT_ALCOHOL_CONFIRM     	=   '#visits [name="alcohol"]+button'
PR_PATIENT_RECORD_VISIT_ALCOHOL_DELETE      	=   '#visits [name="alcohol"]+button+button'
PR_PATIENT_RECORD_VISIT_EXERCISE            	=   '#visits [name="exercise"]'
PR_PATIENT_RECORD_VISIT_EXERCISE_CONFIRM    	=   '#visits [name="exercise"]+button'
PR_PATIENT_RECORD_VISIT_EXERCISE_DELETE     	=   '#visits [name="exercise"]+button+button'
PR_PATIENT_RECORD_VISIT_DIET                	=   '#visits [name="diet"]'
PR_PATIENT_RECORD_VISIT_DIET_CONFIRM        	=   '#visits [name="diet"]+button'
PR_PATIENT_RECORD_VISIT_DIET_DELETE         	=   '#visits [name="diet"]+button+button'
PR_PATIENT_RECORD_VISIT_EYE                 	=   '#visits [name="eye"]'
PR_PATIENT_RECORD_VISIT_EYE_CONFIRM         	=   '#visits [name="eye"]+button'
PR_PATIENT_RECORD_VISIT_EYE_DELETE          	=   '#visits [name="eye"]+button+button'
PR_PATIENT_RECORD_VISIT_FOOT                	=   '#visits [name="foot"]'
PR_PATIENT_RECORD_VISIT_FOOT_CONFIRM        	=   '#visits [name="foot"]+div+button'
PR_PATIENT_RECORD_VISIT_FOOT_DELETE         	=   '#visits [name="foot"]+div+button+button'
PR_PATIENT_RECORD_VISIT_ALBUMIN             	=   '#visits [name="albumin"]'
PR_PATIENT_RECORD_VISIT_ALBUMIN_CONFIRM     	=   '#visits [name="albumin"]+div+div+button'
PR_PATIENT_RECORD_VISIT_ALBUMIN_DELETE      	=   '#visits [name="albumin"]+div+div+button+button'
PR_PATIENT_RECORD_VISIT_CREATININE          	=   '#visits [name="creatinine"]'
PR_PATIENT_RECORD_VISIT_CREATININE_CONFIRM  	=   '#visits [name="creatinine"]+div+div+button'
PR_PATIENT_RECORD_VISIT_CREATININE_DELETE   	=   '#visits [name="creatinine"]+div+div+button+button'
PR_PATIENT_RECORD_VISIT_ACR                 	=   '#visits [name="acr"]'
PR_PATIENT_RECORD_VISIT_ACR_CONFIRM         	=   '#visits [name="acr"]+div+div+button'
PR_PATIENT_RECORD_VISIT_ACR_DELETE          	=   '#visits [name="acr"]+div+div+button+button'
PR_PATIENT_RECORD_VISIT_EGFR                	=   '#visits [name="egfr"]'
PR_PATIENT_RECORD_VISIT_EGFR_CONFIRM        	=   '#visits [name="egfr"]+div+div+button'
PR_PATIENT_RECORD_VISIT_EGFR_DELETE         	=   '#visits [name="egfr"]+div+div+button+button'
PR_PATIENT_RECORD_VISIT_BUN                 	=   '#visits [name="bun"]'
PR_PATIENT_RECORD_VISIT_BUN_CONFIRM         	=   '#visits [name="bun"]+div+div+button'
PR_PATIENT_RECORD_VISIT_BUN_DELETE          	=   '#visits [name="bun"]+div+div+button+button'
PR_PATIENT_RECORD_VISIT_URIC                	=   '#visits [name="uric"]'
PR_PATIENT_RECORD_VISIT_URIC_CONFIRM        	=   '#visits [name="uric"]+div+div+button'
PR_PATIENT_RECORD_VISIT_URIC_DELETE         	=   '#visits [name="uric"]+div+div+button+button'
PR_PATIENT_RECORD_VISIT_TSH                 	=   '#visits [name="tsh"]'
PR_PATIENT_RECORD_VISIT_TSH_CONFIRM         	=   '#visits [name="tsh"]+div+div+button'
PR_PATIENT_RECORD_VISIT_TSH_DELETE          	=   '#visits [name="tsh"]+div+div+button+button'
PR_PATIENT_RECORD_VISIT_T3                  	=   '#visits [name="t3"]'
PR_PATIENT_RECORD_VISIT_T3_CONFIRM          	=   '#visits [name="t3"]+div+div+button'
PR_PATIENT_RECORD_VISIT_T3_DELETE           	=   '#visits [name="t3"]+div+div+button+button'
PR_PATIENT_RECORD_VISIT_T4                  	=   '#visits [name="t4"]'
PR_PATIENT_RECORD_VISIT_T4_CONFIRM          	=   '#visits [name="t4"]+div+div+button'
PR_PATIENT_RECORD_VISIT_T4_DELETE           	=   '#visits [name="t4"]+div+div+button+button'
PR_PATIENT_RECORD_VISIT_BG_FASTING          	=   '#visits [name="bg_fasting"]'
PR_PATIENT_RECORD_VISIT_BG_FASTING_CONFIRM  	=   '#visits [name="bg_fasting"]+div+div+button'
PR_PATIENT_RECORD_VISIT_BG_FASTING_DELETE   	=   '#visits [name="bg_fasting"]+div+div+button+button'
PR_PATIENT_RECORD_VISIT_BG_POST             	=   '#visits [name="bg_postprandial"]'
PR_PATIENT_RECORD_VISIT_BG_POST_CONFIRM     	=   '#visits [name="bg_postprandial"]+div+div+button'
PR_PATIENT_RECORD_VISIT_BG_POST_DELETE      	=   '#visits [name="bg_postprandial"]+div+div+button+button'
PR_PATIENT_RECORD_VISIT_BG_RANDOM           	=   '#visits [name="bg_random"]'
PR_PATIENT_RECORD_VISIT_BG_RANDOM_CONFIRM   	=   '#visits [name="bg_random"]+div+div+button'
PR_PATIENT_RECORD_VISIT_BG_RANDOM_DELETE    	=   '#visits [name="bg_random"]+div+div+button+button'
PR_PATIENT_RECORD_VISIT_BP_SYS              	=   '#visits [name="bp_sys"]'
PR_PATIENT_RECORD_VISIT_BP_DIA              	=   '#visits [name="bp_dia"]'
PR_PATIENT_RECORD_VISIT_BP_CONFIRM          	=   '#visits [name="bp_dia"]+div+div+button'
PR_PATIENT_RECORD_VISIT_BP_DELETE           	=   '#visits [name="bp_dia"]+div+div+button+button'
PR_PATIENT_RECORD_VISIT_HBA1C               	=   '#visits [name="hba1c"]'
PR_PATIENT_RECORD_VISIT_HBA1C_CONFIRM       	=   '#visits [name="hba1c"]+div+div+button'
PR_PATIENT_RECORD_VISIT_HBA1C_DELETE        	=   '#visits [name="hba1c"]+div+div+button+button'
PR_PATIENT_RECORD_VISIT_HDL                 	=   '#visits [name="hdl"]'
PR_PATIENT_RECORD_VISIT_HDL_CONFIRM         	=   '#visits [name="hdl"]+div+div+button'
PR_PATIENT_RECORD_VISIT_HDL_DELETE          	=   '#visits [name="hdl"]+div+div+button+button'
PR_PATIENT_RECORD_VISIT_LDL                 	=   '#visits [name="ldl"]'
PR_PATIENT_RECORD_VISIT_LDL_CONFIRM         	=   '#visits [name="ldl"]+div+div+button'
PR_PATIENT_RECORD_VISIT_LDL_DELETE          	=   '#visits [name="ldl"]+div+div+button+button'
PR_PATIENT_RECORD_VISIT_VLDL                	=   '#visits [name="vldl"]'
PR_PATIENT_RECORD_VISIT_VLDL_CONFIRM        	=   '#visits [name="vldl"]+div+div+button'
PR_PATIENT_RECORD_VISIT_VLDL_DELETE         	=   '#visits [name="vldl"]+div+div+button+button'
PR_PATIENT_RECORD_VISIT_TRI                 	=   '#visits [name="tri"]'
PR_PATIENT_RECORD_VISIT_TRI_CONFIRM         	=   '#visits [name="tri"]+div+div+button'
PR_PATIENT_RECORD_VISIT_TRI_DELETE          	=   '#visits [name="tri"]+div+div+button+button'
PR_PATIENT_RECORD_VISIT_CALCIUM             	=   '#visits [name="calcium"]'
PR_PATIENT_RECORD_VISIT_CALCIUM_CONFIRM     	=   '#visits [name="calcium"]+div+div+button'
PR_PATIENT_RECORD_VISIT_CALCIUM_DELETE      	=   '#visits [name="calcium"]+div+div+button+button'
PR_PATIENT_RECORD_VISIT_VITB12              	=   '#visits [name="vitamin_b12"]'
PR_PATIENT_RECORD_VISIT_VITB12_CONFIRM      	=   '#visits [name="vitamin_b12"]+div+div+button'
PR_PATIENT_RECORD_VISIT_VITB12_DELETE       	=   '#visits [name="vitamin_b12"]+div+div+button+button'
PR_PATIENT_RECORD_VISIT_VITD                	=   '#visits [name="vit_d_25_ohd"]'
PR_PATIENT_RECORD_VISIT_VITD_CONFIRM        	=   '#visits [name="vit_d_25_ohd"]+div+div+button'
PR_PATIENT_RECORD_VISIT_VITD_DELETE         	=   '#visits [name="vit_d_25_ohd"]+div+div+button+button'
PR_PATIENT_RECORD_VISIT_ECG                 	=   '#visits [name="ecg"]'
PR_PATIENT_RECORD_VISIT_ECG_DATE            	=   '#visits [data-name="ecg"] .date'
PR_PATIENT_RECORD_VISIT_ECG_CONFIRM         	=   '#visits [name="ecg"]+button'
PR_PATIENT_RECORD_VISIT_ECG_DELETE          	=   '#visits [name="ecg"]+button+button'
PR_PATIENT_RECORD_VISIT_C_PEP               	=   '#visits [name="c_peptide"]'
PR_PATIENT_RECORD_VISIT_C_PEP_CONFIRM       	=   '#visits [name="c_peptide"]+div+div+button'
PR_PATIENT_RECORD_VISIT_C_PEP_DELETE        	=   '#visits [name="c_peptide"]+div+div+button+button'
PR_PATIENT_RECORD_VISIT_INSULIN_A           	=   '#visits [name="insulin_assay"]'
PR_PATIENT_RECORD_VISIT_INSULIN_A_CONFIRM   	=   '#visits [name="insulin_assay"]+div+div+button'
PR_PATIENT_RECORD_VISIT_INSULIN_A_DELETE    	=   '#visits [name="insulin_assay"]+div+div+button+button'
PR_PATIENT_RECORD_VISIT_GAD                 	=   '#visits [name="gad_antibodies"]'
PR_PATIENT_RECORD_VISIT_GAD_CONFIRM         	=   '#visits [name="gad_antibodies"]+div+div+button'
PR_PATIENT_RECORD_VISIT_GAD_DELETE          	=   '#visits [name="gad_antibodies"]+div+div+button+button'
PR_PATIENT_RECORD_VISIT_AST                 	=   '#visits [name="ast"]'
PR_PATIENT_RECORD_VISIT_AST_CONFIRM         	=   '#visits [name="ast"]+div+div+button'
PR_PATIENT_RECORD_VISIT_AST_DELETE          	=   '#visits [name="ast"]+div+div+button+button'
PR_PATIENT_RECORD_VISIT_ALT                 	=   '#visits [name="alt"]'
PR_PATIENT_RECORD_VISIT_ALT_CONFIRM         	=   '#visits [name="alt"]+div+div+button'
PR_PATIENT_RECORD_VISIT_ALT_DELETE          	=   '#visits [name="alt"]+div+div+button+button'
PR_PATIENT_RECORD_VISIT_PROTEIN             	=   '#visits [name="protein"]'
PR_PATIENT_RECORD_VISIT_PROTEIN_CONFIRM     	=   '#visits [name="protein"]+div+div+button'
PR_PATIENT_RECORD_VISIT_PROTEIN_DELETE      	=   '#visits [name="protein"]+div+div+button+button'
PR_PATIENT_RECORD_VISIT_LATEST_HISTORY      	=   '#visits .dates .normal'
PR_PATIENT_RECORD_VISIT_SECOND_HISTORY      	=   '#visits .dates li.normal:nth-child(4)'
PR_PATIENT_RECORD_VISIT_THIRD_HISTORY       	=   '#visits .dates li.normal:nth-child(5)'
PR_PATIENT_RECORD_VISIT_DELETE_CONFIRM      	=   '.delete_event'
PR_PATIENT_RECORD_VISIT_DELETE_CONFIRM_Y    	=   '.delete_event button'
PR_PATIENT_RECORD_VISIT_FASTING_BG_UNIT     	=   '[data-name="bg_fasting"] .unit'
PR_PATIENT_RECORD_VISIT_POST_BG_UNIT        	=   '[data-name="bg_postprandial"] .unit'
PR_PATIENT_RECORD_VISIT_RANDOM_BG_UNIT      	=   '[data-name="bg_random"] .unit'
PR_PATIENT_RECORD_VISIT_RBC                 	=   '#visits [name="rbc"]'
PR_PATIENT_RECORD_VISIT_RBC_CONFIRM         	=   '#visits [name="rbc"]+div+div+button'
PR_PATIENT_RECORD_VISIT_RBC_DELETE          	=   '#visits [name="rbc"]+div+div+button+button'
PR_PATIENT_RECORD_VISIT_HB                  	=   '#visits [name="hemoglobin_hb"]'
PR_PATIENT_RECORD_VISIT_HB_CONFIRM          	=   '#visits [name="hemoglobin_hb"]+div+div+button'
PR_PATIENT_RECORD_VISIT_HB_DELETE           	=   '#visits [name="hemoglobin_hb"]+div+div+button+button'
PR_PATIENT_RECORD_VISIT_HCT                 	=   '#visits [name="hct_pcv"]'
PR_PATIENT_RECORD_VISIT_HCT_CONFIRM         	=   '#visits [name="hct_pcv"]+div+div+button'
PR_PATIENT_RECORD_VISIT_HCT_DELETE          	=   '#visits [name="hct_pcv"]+div+div+button+button'
PR_PATIENT_RECORD_VISIT_MCV                 	=   '#visits [name="mcv"]'
PR_PATIENT_RECORD_VISIT_MCV_CONFIRM         	=   '#visits [name="mcv"]+div+div+button'
PR_PATIENT_RECORD_VISIT_MCV_DELETE          	=   '#visits [name="mcv"]+div+div+button+button'
PR_PATIENT_RECORD_VISIT_MCH                 	=   '#visits [name="mch"]'
PR_PATIENT_RECORD_VISIT_MCH_CONFIRM         	=   '#visits [name="mch"]+div+div+button'
PR_PATIENT_RECORD_VISIT_MCH_DELETE          	=   '#visits [name="mch"]+div+div+button+button'
PR_PATIENT_RECORD_VISIT_MCHC                	=   '#visits [name="mchc"]'
PR_PATIENT_RECORD_VISIT_MCHC_CONFIRM        	=   '#visits [name="mchc"]+div+div+button'
PR_PATIENT_RECORD_VISIT_MCHC_DELETE         	=   '#visits [name="mchc"]+div+div+button+button'
PR_PATIENT_RECORD_VISIT_RDW                 	=   '#visits [name="rdw"]'
PR_PATIENT_RECORD_VISIT_RDW_CONFIRM         	=   '#visits [name="rdw"]+div+div+button'
PR_PATIENT_RECORD_VISIT_RDW_DELETE          	=   '#visits [name="rdw"]+div+div+button+button'
PR_PATIENT_RECORD_VISIT_PLATELET            	=   '#visits [name="platelets"]'
PR_PATIENT_RECORD_VISIT_PLATELET_CONFIRM    	=   '#visits [name="platelets"]+div+div+button'
PR_PATIENT_RECORD_VISIT_PLATELET_DELETE     	=   '#visits [name="platelets"]+div+div+button+button'
PR_PATIENT_RECORD_VISIT_MPV                 	=   '#visits [name="mpv"]'
PR_PATIENT_RECORD_VISIT_MPV_CONFIRM         	=   '#visits [name="mpv"]+div+div+button'
PR_PATIENT_RECORD_VISIT_MPV_DELETE          	=   '#visits [name="mpv"]+div+div+button+button'
PR_PATIENT_RECORD_VISIT_WBC                 	=   '#visits [name="wbc"]'
PR_PATIENT_RECORD_VISIT_WBC_CONFIRM         	=   '#visits [name="wbc"]+div+div+button'
PR_PATIENT_RECORD_VISIT_WBC_DELETE          	=   '#visits [name="wbc"]+div+div+button+button'
PR_PATIENT_RECORD_VISIT_NEU                 	=   '#visits [name="neutrophils"]'
PR_PATIENT_RECORD_VISIT_NEU_CONFIRM         	=   '#visits [name="neutrophils"]+div+div+button'
PR_PATIENT_RECORD_VISIT_NEU_DELETE          	=   '#visits [name="neutrophils"]+div+div+button+button'
PR_PATIENT_RECORD_VISIT_EOS                 	=   '#visits [name="eosinophils"]'
PR_PATIENT_RECORD_VISIT_EOS_CONFIRM         	=   '#visits [name="eosinophils"]+div+div+button'
PR_PATIENT_RECORD_VISIT_EOS_DELETE          	=   '#visits [name="eosinophils"]+div+div+button+button'
PR_PATIENT_RECORD_VISIT_LYM                 	=   '#visits [name="lymphocytes"]'
PR_PATIENT_RECORD_VISIT_LYM_CONFIRM         	=   '#visits [name="lymphocytes"]+div+div+button'
PR_PATIENT_RECORD_VISIT_LYM_DELETE          	=   '#visits [name="lymphocytes"]+div+div+button+button'
PR_PATIENT_RECORD_VISIT_MON                 	=   '#visits [name="monocytes"]'
PR_PATIENT_RECORD_VISIT_MON_CONFIRM         	=   '#visits [name="monocytes"]+div+div+button'
PR_PATIENT_RECORD_VISIT_MON_DELETE          	=   '#visits [name="monocytes"]+div+div+button+button'
PR_PATIENT_RECORD_VISIT_BAS                 	=   '#visits [name="basophils"]'
PR_PATIENT_RECORD_VISIT_BAS_CONFIRM         	=   '#visits [name="basophils"]+div+div+button'
PR_PATIENT_RECORD_VISIT_BAS_DELETE          	=   '#visits [name="basophils"]+div+div+button+button'
PR_PATIENT_RECORD_MEDICAL_HISTORY           	=   'li[data-tracking="PR-MedHistory-ClickTab"]'
PR_PATIENT_RECORD_MEDICAL_HISTORY_GENDER    	=   'select[g-measurement="gender"]'
PR_PATIENT_RECORD_MEDICAL_HISTORY_DOB       	=   'input[g-measurement="dob"]'
PR_PATIENT_RECORD_MEDICAL_HISTORY_CC        	=   'textarea[g-measurement="chief_complaints"]'
PR_PATIENT_RECORD_MEDICAL_HISTORY_TYPE      	=   'select[g-measurement="diabetes_type"]'
PR_PATIENT_RECORD_MEDICAL_HISTORY_TYPE_YEAR 	=   'input[name="diagnosis_date"]'
PR_PATIENT_RECORD_MEDICAL_HISTORY_CVD       	=   'textarea[g-measurement="cardiovascular"]'
PR_PATIENT_RECORD_MEDICAL_HISTORY_CVD_YEAR  	=   'select[g-measurement-since="cardiovascular"]'
PR_PATIENT_RECORD_MEDICAL_HISTORY_HYPE      	=   'textarea[g-measurement="hypertension"]'
PR_PATIENT_RECORD_MEDICAL_HISTORY_HYPE_YEAR 	=   'select[g-measurement-since="hypertension"]'
PR_PATIENT_RECORD_MEDICAL_HISTORY_DYSL      	=   'textarea[g-measurement="dyslipidemia"]'
PR_PATIENT_RECORD_MEDICAL_HISTORY_DYSL_YEAR 	=   'select[g-measurement-since="dyslipidemia"]'
PR_PATIENT_RECORD_MEDICAL_HISTORY_CVA       	=   'textarea[g-measurement="stroke"]'
PR_PATIENT_RECORD_MEDICAL_HISTORY_CVA_YEAR  	=   'select[g-measurement-since="stroke"]'
PR_PATIENT_RECORD_MEDICAL_HISTORY_THYR      	=   'textarea[g-measurement="thyroid"]'
PR_PATIENT_RECORD_MEDICAL_HISTORY_THYR_YEAR 	=   'select[g-measurement-since="thyroid"]'
PR_PATIENT_RECORD_MEDICAL_HISTORY_PSYC      	=   'textarea[g-measurement="psychiatric_illness"]'
PR_PATIENT_RECORD_MEDICAL_HISTORY_PSYC_YEAR 	=   'select[g-measurement-since="psychiatric_illness"]'
PR_PATIENT_RECORD_MEDICAL_HISTORY_ANEM      	=   'textarea[g-measurement="anemia"]'
PR_PATIENT_RECORD_MEDICAL_HISTORY_ANEM_YEAR 	=   'select[g-measurement-since="anemia"]'
PR_PATIENT_RECORD_MEDICAL_HISTORY_ASTH      	=   'textarea[g-measurement="bronchial_asthma"]'
PR_PATIENT_RECORD_MEDICAL_HISTORY_ASTH_YEAR 	=   'select[g-measurement-since="bronchial_asthma"]'
PR_PATIENT_RECORD_MEDICAL_HISTORY_OTHER     	=   'textarea[g-measurement="other_history"]'
PR_PATIENT_RECORD_MEDICAL_HISTORY_NEUR      	=   'textarea[g-measurement="peripheral_neuropathy"]'
PR_PATIENT_RECORD_MEDICAL_HISTORY_NEPH      	=   'textarea[g-measurement="nephropathy"]'
PR_PATIENT_RECORD_MEDICAL_HISTORY_RETI      	=   'textarea[g-measurement="retinopathy"]'
PR_PATIENT_RECORD_MEDICAL_HISTORY_FOOT      	=   'textarea[g-measurement="diabetic_foot_problems"]'
PR_PATIENT_RECORD_MEDICAL_HISTORY_COLO      	=   'textarea[g-measurement="colonoscopy"]'
PR_PATIENT_RECORD_MEDICAL_HISTORY_COLO_YEAR 	=   'select[g-measurement-since="colonoscopy"]'
PR_PATIENT_RECORD_MEDICAL_HISTORY_MOLE      	=   'textarea[g-measurement="mole_check"]'
PR_PATIENT_RECORD_MEDICAL_HISTORY_MOLE_YEAR 	=   'select[g-measurement-since="mole_check"]'
PR_PATIENT_RECORD_MEDICAL_HISTORY_VACC      	=   'textarea[g-measurement="vaccinations"]'
PR_PATIENT_RECORD_MEDICAL_HISTORY_VACC_YEAR 	=   'select[g-measurement-since="vaccinations"]'
PR_PATIENT_RECORD_MEDICAL_HISTORY_MAMM      	=   'textarea[g-measurement="mammogram_history"]'
PR_PATIENT_RECORD_MEDICAL_HISTORY_MAMM_YEAR 	=   'select[g-measurement-since="mammogram_history"]'
PR_PATIENT_RECORD_MEDICAL_HISTORY_PAP       	=   'textarea[g-measurement="pap_smear"]'
PR_PATIENT_RECORD_MEDICAL_HISTORY_PAP_YEAR  	=   'select[g-measurement-since="pap_smear"]'
PR_PATIENT_RECORD_MEDICAL_HISTORY_PSA       	=   'textarea[g-measurement="prostate_specific_antigen"]'
PR_PATIENT_RECORD_MEDICAL_HISTORY_PSA_YEAR  	=   'select[g-measurement-since="prostate_specific_antigen"]'
PR_PATIENT_RECORD_MEDICAL_HISTORY_SMOKE     	=   'textarea[g-measurement="tobacco"]'
PR_PATIENT_RECORD_MEDICAL_HISTORY_ALCO      	=   'textarea[g-measurement="alcohol"]'
PR_PATIENT_RECORD_MEDICAL_HISTORY_EXER      	=   'textarea[g-measurement="exercise"]'
PR_PATIENT_RECORD_MEDICAL_HISTORY_DIET      	=   'textarea[g-measurement="diet"]'
PR_PATIENT_RECORD_MEDICAL_HISTORY_DRUG      	=   'textarea[g-measurement="drugs_history"]'
PR_PATIENT_RECORD_MEDICAL_HISTORY_MARI      	=   'textarea[g-measurement="marital_history"]'
PR_PATIENT_RECORD_MEDICAL_HISTORY_PREG      	=   'textarea[g-measurement="pregnancy_history"]'
PR_PATIENT_RECORD_MEDICAL_HISTORY_BIRTH     	=   'textarea[g-measurement="birth_history"]'
PR_PATIENT_RECORD_MEDICAL_HISTORY_SEX       	=   'textarea[g-measurement="sexual_preference"]'
PR_PATIENT_RECORD_MEDICAL_HISTORY_STD       	=   'textarea[g-measurement="std_history"]'
PR_PATIENT_RECORD_MEDICAL_HISTORY_DIAB_HIS  	=   'textarea[g-measurement="fam_history_diabetes"]'
PR_PATIENT_RECORD_MEDICAL_HISTORY_HYPE_HIS  	=   'textarea[g-measurement="fam_history_hypertension"]'
PR_PATIENT_RECORD_MEDICAL_HISTORY_DYSL_HIS  	=   'textarea[g-measurement="fam_history_dyslipidemia"]'
PR_PATIENT_RECORD_MEDICAL_HISTORY_THYR_HIS  	=   'textarea[g-measurement="fam_history_thyroid"]'
PR_PATIENT_RECORD_MEDICAL_HISTORY_CANC_HIS  	=   'textarea[g-measurement="fam_history_cancer"]'
PR_PATIENT_RECORD_MEDICAL_HISTORY_CVD_HIS   	=   'textarea[g-measurement="fam_history_heart_disease"]'
PR_PATIENT_RECORD_MEDICAL_HISTORY_CVA_HIS   	=   'textarea[g-measurement="fam_history_stroke"]'
PR_PATIENT_RECORD_MEDICAL_HISTORY_ADMI      	=   'textarea[g-measurement="hospital_admissions"]'
PR_PATIENT_RECORD_MEDICAL_HISTORY_SURG      	=   'textarea[g-measurement="hospital_surgeries"]'
PR_PATIENT_RECORD_MEDICAL_HISTORY_MEDI      	=   'textarea[g-measurement="allergies_medications"]'
PR_PATIENT_RECORD_MEDICAL_HISTORY_FOOD      	=   'textarea[g-measurement="allergies_foods"]'
PR_PATIENT_RECORD_MEDICAL_HISTORY_LATEX     	=   'textarea[g-measurement="allergies_latex"]'
PR_PATIENT_RECORD_MEDICAL_HISTORY_ENVI      	=   'textarea[g-measurement="allergies_environmental"]'
PR_PATIENT_RECORD_MEDICAL_HISTORY_SAVE_OK   	=   'div.indicator.success'
PR_PATIENT_RECORD_MEDICAL_HISTORY_SAVE_BUT  	=   '.medical_history button'
PR_PATIENT_RECORD_MEDICAL_HISTORY_FIELDLIST 	=   [
                                                PR_PATIENT_RECORD_MEDICAL_HISTORY_CC, PR_PATIENT_RECORD_MEDICAL_HISTORY_CVD, PR_PATIENT_RECORD_MEDICAL_HISTORY_HYPE,
                                                PR_PATIENT_RECORD_MEDICAL_HISTORY_DYSL, PR_PATIENT_RECORD_MEDICAL_HISTORY_CVA, PR_PATIENT_RECORD_MEDICAL_HISTORY_THYR,
                                                PR_PATIENT_RECORD_MEDICAL_HISTORY_PSYC, PR_PATIENT_RECORD_MEDICAL_HISTORY_ANEM, PR_PATIENT_RECORD_MEDICAL_HISTORY_ASTH,
                                                PR_PATIENT_RECORD_MEDICAL_HISTORY_OTHER, PR_PATIENT_RECORD_MEDICAL_HISTORY_NEUR, PR_PATIENT_RECORD_MEDICAL_HISTORY_NEPH,
                                                PR_PATIENT_RECORD_MEDICAL_HISTORY_RETI, PR_PATIENT_RECORD_MEDICAL_HISTORY_FOOT, PR_PATIENT_RECORD_MEDICAL_HISTORY_COLO,
                                                PR_PATIENT_RECORD_MEDICAL_HISTORY_MOLE, PR_PATIENT_RECORD_MEDICAL_HISTORY_VACC, PR_PATIENT_RECORD_MEDICAL_HISTORY_MAMM,
                                                PR_PATIENT_RECORD_MEDICAL_HISTORY_PAP, PR_PATIENT_RECORD_MEDICAL_HISTORY_PSA, PR_PATIENT_RECORD_MEDICAL_HISTORY_SMOKE,
                                                PR_PATIENT_RECORD_MEDICAL_HISTORY_ALCO, PR_PATIENT_RECORD_MEDICAL_HISTORY_EXER, PR_PATIENT_RECORD_MEDICAL_HISTORY_DIET,
                                                PR_PATIENT_RECORD_MEDICAL_HISTORY_DRUG, PR_PATIENT_RECORD_MEDICAL_HISTORY_MARI, PR_PATIENT_RECORD_MEDICAL_HISTORY_PREG,
                                                PR_PATIENT_RECORD_MEDICAL_HISTORY_BIRTH, PR_PATIENT_RECORD_MEDICAL_HISTORY_SEX, PR_PATIENT_RECORD_MEDICAL_HISTORY_STD,
                                                PR_PATIENT_RECORD_MEDICAL_HISTORY_DIAB_HIS, PR_PATIENT_RECORD_MEDICAL_HISTORY_HYPE_HIS, PR_PATIENT_RECORD_MEDICAL_HISTORY_DYSL_HIS,
                                                PR_PATIENT_RECORD_MEDICAL_HISTORY_THYR_HIS, PR_PATIENT_RECORD_MEDICAL_HISTORY_CANC_HIS, PR_PATIENT_RECORD_MEDICAL_HISTORY_CVD_HIS,
                                                PR_PATIENT_RECORD_MEDICAL_HISTORY_CVA_HIS, PR_PATIENT_RECORD_MEDICAL_HISTORY_ADMI, PR_PATIENT_RECORD_MEDICAL_HISTORY_SURG,
                                                PR_PATIENT_RECORD_MEDICAL_HISTORY_MEDI, PR_PATIENT_RECORD_MEDICAL_HISTORY_FOOD, PR_PATIENT_RECORD_MEDICAL_HISTORY_LATEX,
                                                PR_PATIENT_RECORD_MEDICAL_HISTORY_ENVI, 
                                                ]



PR_DIRECTORY_REMOVE_CONFIRM                 	=   '.delete_patient .right.submit'
PR_DIRECTORY_TITLE                          	=   '.directory-content h3'
PR_DIRECTORY_FIRST_PATIENT                  	=   '//table[@id="directory_table"]/tbody/tr[1]/td[1]/a'
PR_DIRECTORY_PATIENT_ENTRY                  	=   'a[href="/provider/patient/%s"]'
PR_DIRECTORY_PATIENT_DELETE                 	=   '//tr/td/a[@href="/provider/patient/%s"]/../../td[last()]/a'
PR_DIRECTORY_PATIENT_NEXT_APPT              	=   '//tr/td/a[@href="/provider/patient/%s"]/../..//div[@class="appointments add button blue"]'
PR_DIRECTORY_PATIENT_LAST_APPT              	=   '//tr/td/a[@href="/provider/patient/%s"]/../../td[7]'
PR_DIRECTORY_LAST_NAME                      	=   '#directory_table>tbody>tr>td:nth-child(%s)>a' %LAST
PR_DIRECTORY_FIRST_NAME                     	=   '#directory_table>tbody>tr>td:nth-child(%s)>a' %FIRST
PR_DIRECTORY_MED_ADH                        	=   '#directory_table>tbody>tr>td:nth-child(%s)' %MED_ADH
PR_DIRECTORY_BG_CONTROL                     	=   '#directory_table>tbody>tr>td:nth-child(%s)' %BG_CONTROL
PR_DIRECTORY_PRACTICE_NAME                  	=   '#directory_table>tbody>tr>td:nth-child(%s)' %PRACTICE_NAME
PR_DIRECTORY_NEXT_APPT                      	=   '#directory_table>tbody>tr>td:nth-child(%s)>div' %NEXT_APPT
PR_DIRECTORY_LAST_APPT                      	=   '#directory_table>tbody>tr>td:nth-child(%s)' %LAST_APPT
PR_DIRECTORY_STATUS                         	=   '#directory_table>tbody>tr>td:nth-child(%s)' %STATUS
PR_DIRECTORY_LAST_BG                        	=   '#directory_table>tbody>tr>td:nth-child(%s)' %LAST_BG
PR_DIRECTORY_LAST_CONTACT                   	=   '#directory_table>tbody>tr>td:nth-child(%s)' %LAST_CONTACT
PR_DIRECTORY_JOINED                         	=   '#directory_table>tbody>tr>td:nth-child(%s)' %JOINED
PR_DIRECTORY_SUBSCRIPTION                   	=   '#directory_table>tbody>tr>td:nth-child(%s)' %SUBSCRIPTION
PR_DIRECTORY_EXPIRES                        	=   '#directory_table>tbody>tr>td:nth-child(%s)' %EXPIRES
PR_DIRECTORY_TYPE                           	=   '#directory_table>tbody>tr>td:nth-child(%s)' %TYPE
PR_DIRECTORY_A1C                            	=   '#directory_table>tbody>tr>td:nth-child(%s)' %A1C
PR_DIRECTORY_AGE                            	=   '#directory_table>tbody>tr>td:nth-child(%s)' %AGE
PR_DIRECTORY_LAST_NAME_SORT                 	=   '#directory_table>thead>tr>th:nth-child(%s)>i' %LAST
PR_DIRECTORY_FIRST_NAME_SORT                	=   '#directory_table>thead>tr>th:nth-child(%s)>i' %FIRST
PR_DIRECTORY_MED_ADH_SORT                   	=   '#directory_table>thead>tr>th:nth-child(%s)>i' %MED_ADH
PR_DIRECTORY_BG_CONTROL_SORT                	=   '#directory_table>thead>tr>th:nth-child(%s)>i' %BG_CONTROL
PR_DIRECTORY_PRACTICE_NAME_SORT             	=   '#directory_table>thead>tr>th:nth-child(%s)>i' %PRACTICE_NAME
PR_DIRECTORY_NEXT_APPT_SORT                 	=   '#directory_table>thead>tr>th:nth-child(%s)>i' %NEXT_APPT
PR_DIRECTORY_LAST_APPT_SORT                 	=   '#directory_table>thead>tr>th:nth-child(%s)>i' %LAST_APPT
PR_DIRECTORY_STATUS_SORT                    	=   '#directory_table>thead>tr>th:nth-child(%s)>i' %STATUS
PR_DIRECTORY_LAST_BG_SORT                   	=   '#directory_table>thead>tr>th:nth-child(%s)>i' %LAST_BG
PR_DIRECTORY_LAST_CONTACT_SORT              	=   '#directory_table>thead>tr>th:nth-child(%s)>i' %LAST_CONTACT
PR_DIRECTORY_JOINED_SORT                    	=   '#directory_table>thead>tr>th:nth-child(%s)>i' %JOINED
PR_DIRECTORY_SUBSCRIPTION_SORT              	=   '#directory_table>thead>tr>th:nth-child(%s)>i' %SUBSCRIPTION
PR_DIRECTORY_EXPIRES_SORT                   	=   '#directory_table>thead>tr>th:nth-child(%s)>i' %EXPIRES
PR_DIRECTORY_TYPE_SORT                      	=   '#directory_table>thead>tr>th:nth-child(%s)>i' %TYPE
PR_DIRECTORY_A1C_SORT                       	=   '#directory_table>thead>tr>th:nth-child(%s)>i' %A1C
PR_DIRECTORY_AGE_SORT                       	=   '#directory_table>thead>tr>th:nth-child(%s)>i' %AGE
PR_DIRECTORY_NO_PATIENT                     	=   '.no_patient td'
PR_DIRECTORY_SMS_BUTTON                     	=   '#compose_sms'
PR_DIRECTORY_SEARCH_BUTTON                  	=   '#submit'
PR_DIRECTORY_SEARCH_FIELD                   	=   '#keyword'
PR_DIRECTORY_FILTER                         	=   'select[name="filters"]'
PR_DIRECTORY_FILTER_OPTION_ALL_PATIENT      	=   'option[value=""]'
PR_DIRECTORY_FILTER_OPTION_STUDY_PATIENT    	=   'option[value=\'%s\']'%FILTER_STUDY_PATIENT
PR_DIRECTORY_FILTER_OPTION_TYPE_ONE         	=   'option[value=\'%s\']'%FILTER_TYPE_ONE
PR_DIRECTORY_FILTER_OPTION_TYPE_TWO         	=   'option[value=\'%s\']'%FILTER_TYPE_TWO         
PR_DIRECTORY_FILTER_OPTION_GEST             	=   'option[value=\'%s\']'%FILTER_GESTATIONAL      
PR_DIRECTORY_FILTER_OPTION_PRE_DIA          	=   'option[value=\'%s\']'%FILTER_PRE_DIABETES     
PR_DIRECTORY_FILTER_OPTION_OTHER            	=   'option[value=\'%s\']'%FILTER_OTHER            
PR_DIRECTORY_FILTER_OPTION_ACTIVE           	=   'option[value=\'%s\']'%FILTER_ACTIVE           
PR_DIRECTORY_FILTER_OPTION_INACTIVE         	=   'option[value=\'%s\']'%FILTER_INACTIVE         
PR_DIRECTORY_FILTER_OPTION_NOT_INSTALLED    	=   'option[value=\'%s\']'%FILTER_NOT_INSTALL      
PR_DIRECTORY_FILTER_OPTION_EHR              	=   'option[value=\'%s\']'%FILTER_EHR_ONLY         
PR_DIRECTORY_FILTER_OPTION_A1C              	=   'option[value=\'%s\']'%FILTER_A1C              
PR_DIRECTORY_FILTER_OPTION_BG_CONTROL       	=   'option[value=\'%s\']'%FILTER_BG_CONTROL       
PR_DIRECTORY_FILTER_OPTION_MEDADH           	=   'option[value=\'%s\']'%FILTER_MEDADH           
PR_DIRECTORY_FILTER_OPTION_NEXT_APPO        	=   'option[value=\'%s\']'%FILTER_NEXT_APPOINTMENT 
PR_DIRECTORY_FILTER_OPTION_WILL_EXPIRE      	=   'option[value=\'%s\']'%FILTER_WILL_EXPIRE      
PR_DIRECTORY_FILTER_OPTION_EXPIRED          	=   'option[value=\'%s\']'%FILTER_EXPIRED          
PR_DIRECTORY_SEARCH_RESULT_INFO             	=   'span.result-stats'
PR_DIRECTORY_GROUP_SMS_DIALOG               	=   '.group_sms'
PR_DIRECTORY_GROUP_SMS_TITLE                	=   'div.group_sms h3'
PR_DIRECTORY_GROUP_SMS_CLOSE                	=   'div.group_sms h3 .close'
PR_DIRECTORY_GROUP_SMS_SMS_NUMBER           	=   'td.count_sms'
PR_DIRECTORY_GROUP_SMS_APP_NUMBER           	=   'td.count_app'
PR_DIRECTORY_GROUP_SMS_TOTAL_NUMBER         	=   'td.count_total'
PR_DIRECTORY_GROUP_SMS_TEXT_FIELD           	=   'div.group_sms textarea'
PR_DIRECTORY_GROUP_SMS_CHECK_BOX            	=   'input[name="send_message_copy"]'
PR_DIRECTORY_GROUP_SMS_COUTRY_CODE          	=   '#group_sms > div:nth-child(2) > div > select'
PR_DIRECTORY_GROUP_SMS_CELL_NUMBER          	=   '#group_sms > div:nth-child(2) > div > div > input'
PR_DIRECTORY_GROUP_SMS_CELL_VALIDATION      	=   '#group_sms > div:nth-child(2) > div > div > div'
PR_DIRECTORY_GROUP_SMS_COUNTER              	=   '#character_count'
PR_DIRECTORY_GROUP_SMS_CANCEL               	=   '#group_sms > div.cleared > button.button.left.cancel'
PR_DIRECTORY_GROUP_SMS_SEND                 	=   '#group_sms > div.cleared > button.button.right.submit'
PR_DIRECTORY_GROUP_SMS_RESULT_DIALOG        	=   'div.group_sms_result'
PR_DIRECTORY_GROUP_SMS_RESULT_TITLE_SUCCESS 	=   'span.sms_success'
PR_DIRECTORY_GROUP_SMS_RESULT_TITLE_FAIL    	=   'span.sms_error'
PR_DIRECTORY_GROUP_SMS_RESULT_CLOSE         	=   '.group_sms_result .close'
PR_DIRECTORY_GROUP_SMS_RESULT_SUCCESS       	=   'div.sms_success'
PR_DIRECTORY_GROUP_SMS_RESULT_FAIL          	=   'div.sms_error'


PR_APPOINTMENT_TITLE                        	=   '.appointments h3'
PR_APPOINTMENT_TITLE_ADD                    	=   '.appointments h3 .add'
PR_APPOINTMENT_TITLE_EDIT                   	=   '.appointments h3 .edit'
PR_APPOINTMENT_DATE                         	=   'date'
PR_APPOINTMENT_TODAY                        	=   'div.button[g-appts-offset-days="0"]'
PR_APPOINTMENT_THREE_MONTH                  	=   'div.button[g-appts-offset-days="90"]'
PR_APPOINTMENT_SIX_MONTH                    	=   'div.button[g-appts-offset-days="180"]'
PR_APPOINTMENT_TIME                         	=   '.ui-timepicker-input'
PR_APPOINTMENT_NOTE                         	=   '.notes textarea'
PR_APPOINTMENT_SAVE                         	=   '.controls .submit'
PR_APPOINTMENT_COMPLETE                     	=   '.complete'
PR_APPOINTMENT_DELETE                       	=   '.delete'
PR_APPOINTMENT_CLOSE                        	=   '.appointments .close'

PR_FEED_CONTENT                             	=   '#content.feed'
PR_FEED_FIRST_WARNING                       	=   'div.warning'
PR_FEED_FORWARD                             	=   'div.fwd'
PR_FEED_CLOSE                               	=   'div.close'
PR_FEED_FORWARD_TO                          	=   'forward_to'
PR_FEED_FORWARD_FIRST_OPTION                	=   '[name="forward_to"] option:nth-child(2)'
PR_FEED_FORWARD_NOTE                        	=   '.fwd_group textarea'
PR_FEED_FORWARD_BUTTON                      	=   '.fwd_actions .submit'
PR_FEED_FORWARD_CANCEL                      	=   '.fwd_actions .cancel_fwd'
PR_FEED_WARNING_FORWARD_BY                  	=   'div.warning .fwd_by'
PR_FEED_FIRST_MESSAGE                       	=   'div.message.patient'
PR_FEED_PATIENT_NAME                        	=   '.vitals .name'   
PR_FEED_EMPTY_LOGO                          	=   '.logo_gather'


PR_INFO_NAME                                	=   'h1.name'
PR_INFO_PATIENT_DATA                        	=   '.blurb'
PR_INFO_COMORBIDITIES                       	=   '.patient-data li.chiclet'
PR_INFO_OTHER_MED                           	=   '.other li.chiclet'
PR_INFO_NOTE                                	=   '.dummy'
PR_INFO_EMAIL                               	=   '.email div'
PR_INFO_NUMBER                              	=   '.cell div'

PR_ACCOUNT_TITLE                            	=   '.heading h1'
PR_ACCOUNT_SURNAME                          	=   'input[name="last_name"]'
PR_ACCOUNT_GIVEN_NAME                       	=   'input[name="first_name"]'
PR_ACCOUNT_LANGUAGE                         	=   'select[name="prefs.language_code"]'
PR_ACCOUNT_BIRTHDATE                        	=   'input[name="dob"]'
PR_ACCOUNT_NEW_PASSWORD                     	=   'password1'
PR_ACCOUNT_CONFIRM_PASSWORD                 	=   'password2'
PR_ACCOUNT_PASSWORD_ERROR                   	=   '.validation_errors'
PR_ACCOUNT_PASSWORD_STRENGTH                	=   '.password_strength span'
PR_ACCOUNT_SAVE_ALL_BUTTON                  	=   'next'
PR_ACCOUNT_COUNTRY_CODE                     	=   '.phone_country'
PR_ACCOUNT_CELL_NUMBER                      	=   '.phone_number'
PR_ACCOUNT_SEND_SMS_BUTTON                  	=   '.send_confirmation'
PR_ACCOUNT_CELL_ERROR                       	=   '.halves .validation_errors'
PR_ACCOUNT_SHOW_SUMMARY                     	=   'input[name="prefs.graph_layout"][value="1"]'
PR_ACCOUNT_SHOW_BG                          	=   'input[name="prefs.graph_layout"][value="2"]'
PR_ACCOUNT_SHOW_VISIT                       	=   'input[name="prefs.graph_layout"][value="3"]'

PR_MANAGE_PRACTICE_TITLE                    	=   '.edit_profile h1'
PR_MANAGE_PRACTICE_YELLOW_AREA              	=   'div.yellow'
PR_MANAGE_PRACTICE_NAME_IN_YELLOW           	=   'div.yellow span'
PR_MANAGE_PRACTICE_STAFF_ENTRY              	=   '#directory_table>tbody>tr'
PR_MANAGE_PRACTICE_ADD_STAFF_BUTTON         	=   '#add_guru'
PR_MANAGE_PRACTICE_INVITE_STAFF_DIALOG      	=   'div.add_guru'
PR_MANAGE_PRACTICE_INVITE_STAFF_NAME        	=   'input[name="name"]'
PR_MANAGE_PRACTICE_INVITE_STAFF_EMAIL       	=   'input[name="email"]'
PR_MANAGE_PRACTICE_INVITE_STAFF_ROLE        	=   'select[name="role"]'
PR_MANAGE_PRACTICE_INVITE_STAFF_LANG        	=   'select[name="language"]'
PR_MANAGE_PRACTICE_INVITE_STAFF_RIGHT       	=   'select[name="is_practice_admin"]'
PR_MANAGE_PRACTICE_INVITE_STAFF_SUBMIT      	=   'div.add_guru input.submit'
PR_MANAGE_PRACTICE_INVITE_STAFF_CLOSE       	=   'div.add_guru div.close'
PR_MANAGE_PRACTICE_PRACTICE_NAME            	=   'practice_name'
PR_MANAGE_PRACTICE_HEIGHT_UNIT              	=   'height_units'
PR_MANAGE_PRACTICE_WEIGHT_UNIT              	=   'weight_units'
PR_MANAGE_PRACTICE_BP_UNIT                  	=   'bp_units'
PR_MANAGE_PRACTICE_BG_UNIT                  	=   '[name="bg_units"]'
PR_MANAGE_PRACTICE_CRITICAL_LOW_MG          	=   'hypo_alert'
PR_MANAGE_PRACTICE_CRITICAL_LOW_MMO         	=   'hypo_alert_mmol'
PR_MANAGE_PRACTICE_CRITICAL_UPPER_MG        	=   'hyper_alert'
PR_MANAGE_PRACTICE_CRITICAL_UPPER_MMO       	=   'hyper_alert_mmol'
PR_MANAGE_PRACTICE_COUNTRY_CODE             	=   'phone_country'
PR_MANAGE_PRACTICE_NUMBER                   	=   'phone_number'
PR_MANAGE_PRACTICE_NUMBER_ERROR             	=   '.validation_errors'
PR_MANAGE_PRACTICE_UNIT_GROUP               	=   'unit_cluster_type'
PR_MANAGE_PRACTICE_SAVE_BUTTON              	=   'update_range'
PR_MANAGE_PRACTICE_SAVE_SUCCESS             	=   'div.info.clear'

PR_LOGIN_USERNAME                           	=   'id_username'
PR_LOGIN_PASSWORD                           	=   'id_password'
PR_LOGIN_SUBMIT                             	=   'input[name="submit"]'
PR_LOGIN_FORGOT_PASSWORD                    	=   '.forgotpw'


### Patient App elements
## Android

# Sign in page
#DM_AND_SIGN_IN_TITLE                        	=   'Sign In'
#DM_AND_SIGN_IN_BACK                         	=   'back_rl'
DM_AND_SIGN_IN_LOGO                         	=   'logo_iv'
DM_AND_SIGN_IN_WELCOME                      	=   'sign_up_welcome_tv'
DM_AND_SIGN_IN_HINT                         	=   'hint_tv'
DM_AND_SIGN_IN_NO_SPAM_HINT                 	=   'not_spam_tv'
DM_AND_SIGN_IN_FIELD                        	=   'email_et'
DM_AND_SIGN_IN_ERROR                        	=   'error_tv'
EM_DM_SIGN_IN_INVALID_EMAIL                 	=   'Please enter a valid email address.'
#EM_DM_SIGN_IN_NOT_REGISTER_EMAIL            	=   "Are you sure you entered the correct e-mail address? We couldn't find this one in our records."
DM_AND_SIGN_IN_BUTTON                       	=   'next_btn'

# Enter password page
DM_AND_PASSWORD_TITLE                       	=   'Enter password'
DM_AND_PASSWORD_BACK                        	=   'back_iv'
DM_AND_PASSWORD_FIELD                       	=   'input_pwd_et'
DM_AND_PASSWORD_ERROR                       	=   'error_tv'
EM_DM_PASSWORD_NOT_MATCH                    	=   'The password you entered does not match the e-mail address. Please double-check it.'
EM_DM_PASSWORD_INVALID_INPUT                	=   "Sorry, we can't accept the password you entered. Please use only letters, numbers, and underscores."
DM_AND_PASSWORD_FORGOT_PW                   	=   'reset_tv'
DM_AND_PASSWORD_SIGN_IN_BTN                 	=   'next_btn'

# Forgot password dialog
DM_AND_FORGOT_PW_FIELD                      	=   'resetpw_email'
DM_AND_FORGOT_PW_CANCEL_BTN                 	=   'resetpw_cancel'
DM_AND_FORGOT_PW_RESET_BTN                  	=   'resetpw_submit'
# Reset fail dialog
DM_AND_PW_RESET_FAIL_MESSAGE                	=   'Sorry, it looks like that address is not registered in our system.'
DM_AND_PW_RESET_FAIL_BTN                    	=   'button1'
# Reset success dialog
DM_AND_PW_RESET_SUCCESS_MESSAGE             	=   'An email has been sent to %s with password reset instructions.'
DM_AND_PW_RESET_SUCCESS_BTN                 	=   'button1'

# Set password page
DM_AND_SET_PASSWORD_TITLE                   	=   'Create A Password'
DM_AND_SET_PASSWORD_BACK                    	=   'back_iv'
DM_AND_SET_PASSWORD_PASSWORD_FIELD          	=   'enter_pwd_et'
DM_AND_SET_PASSWORD_CONFIRM_FIELD           	=   'reenter_pwd_et'
#DM_AND_SET_PASSWORD_FIRST_FIELD_ERROR       	=   'pwd_error_tv'
#DM_AND_SET_PASSWORD_SECOND_FIELD_ERROR      	=   'repwd_error_tv'
DM_AND_SET_PASSWORD_ERROR                   	=   'error_tv'
EM_DM_SET_PASSWORD_SHORT_ERROR              	=   'Please choose a password with a minimum length of 6 characters.'
EM_DM_SET_PASSWORD_NOT_MATCH                	=   'The passwords you entered do not match. Please double-check them.'
DM_AND_SET_PASSWORD_DTC_HINT                	=   'dtc_hint_tv'
DM_AND_SET_PASSWORD_TERM                    	=   'terms_tv'
DM_AND_SET_PASSWORD_BUTTON                  	=   'next_btn'

# Terms page
DM_AND_TERM_TITLE                           	=   'alertTitle'
VALUE_AND_TERM_TITLE                        	=   'User Agreement'
DM_AND_TERM_CONTENT                         	=   'content_tv'
DM_AND_TERM_BUTTON                          	=   'button1'

# Personal info page
DM_AND_PERSONAL_INFO_TITLE                  	=   'My Info'
DM_AND_PERSONAL_INFO_BACK                   	=   'back_iv'
DM_AND_PERSONAL_INFO_COUNTRY_CODE           	=   'country_code_ccs'
DM_AND_PERSONAL_INFO_COUNTRY_CODE_TEXT      	=   '//android.widget.RelativeLayout[@resource-id="com.gatherhealth.gatherdm:id/country_code_ccs"]//android.widget.TextView'
DM_AND_PERSONAL_INFO_COUNTRY_HK             	=   'Hong Kong (+852)'
DM_AND_PERSONAL_INFO_COUNTRY_IN             	=   'India (+91)'
DM_AND_PERSONAL_INFO_COUNTRY_US             	=   'USA (+1)'
DM_AND_PERSONAL_INFO_COUNTRY_CH             	=   'China (+86)'
DM_AND_PERSONAL_INFO_CELL_NUMBER            	=   'cell_number_et'
DM_AND_PERSONAL_INFO_CELL_ERROR             	=   'error_tv'
EM_DM_PERSONAL_INFO_INVALID_NUMBER          	=   'Please enter a valid phone number.'
DM_AND_PERSONAL_INFO_GENDER                 	=   'gender_gs'
DM_AND_PERSONAL_INFO_GENDER_TEXT            	=   '//android.widget.RelativeLayout[@resource-id="com.gatherhealth.gatherdm:id/gender_gs"]//android.widget.TextView'
DM_AND_PERSONAL_INFO_MALE                   	=   'Male'
DM_AND_PERSONAL_INFO_FEMALE                 	=   'Female'
DM_AND_PERSONAL_INFO_BIRTHDAY               	=   'birthdate_bs'
DM_AND_PERSONAL_INFO_BIRTHDAY_TEXT          	=   '//android.widget.RelativeLayout[@resource-id="com.gatherhealth.gatherdm:id/birthdate_bs"]//android.widget.TextView'
DM_AND_PERSONAL_INFO_DATE_MONTH_UP          	=   '//android.widget.NumberPicker[1]/android.widget.Button[1]'
DM_AND_PERSONAL_INFO_DATE_MONTH             	=   '//android.widget.NumberPicker[1]/android.widget.EditText'
DM_AND_PERSONAL_INFO_DATE_MONTH_DOWN        	=   '//android.widget.NumberPicker[1]/android.widget.Button[2]'
DM_AND_PERSONAL_INFO_DATE_DAY_UP            	=   '//android.widget.NumberPicker[2]/android.widget.Button[1]'
DM_AND_PERSONAL_INFO_DATE_DAY               	=   '//android.widget.NumberPicker[2]/android.widget.EditText'
DM_AND_PERSONAL_INFO_DATE_DAY_DOWN          	=   '//android.widget.NumberPicker[2]/android.widget.Button[2]'
DM_AND_PERSONAL_INFO_DATE_YEAR_UP           	=   '//android.widget.NumberPicker[3]/android.widget.Button[1]'
DM_AND_PERSONAL_INFO_DATE_YEAR              	=   '//android.widget.NumberPicker[3]/android.widget.EditText'
DM_AND_PERSONAL_INFO_DATE_YEAR_DOWN         	=   '//android.widget.NumberPicker[3]/android.widget.Button[2]'
DM_AND_PERSONAL_INFO_DATE_SET_BTN           	=   'button1'
DM_AND_PERSONAL_INFO_CHOOSE_PHOTO_BUTTON    	=   'select_pic_btn'
DM_AND_PERSONAL_INFO_BUTTON                 	=   'next_button'

# Loved one list
DM_AND_LOVED_ONE_LIST_TITLE                 	=   'My Loved Ones'
DM_AND_LOVED_ONE_LIST_ADD_ICON              	=   'actionbar_lo_plus_iv'
DM_AND_LOVED_ONE_LIST_DESCRIPTION           	=   'A Loved One is a family member or a close friend who can support you in managing your diabetes.'
DM_AND_LOVED_ONE_LIST_ADD_BTN               	=   'lo_empty_btn'
DM_AND_LOVED_ONE_LIST_NAME                  	=   'lo_name_tv'
DM_AND_LOVED_ONE_LIST_PENDING_MARK          	=   'pending_mark_tv'

# Loved one info
DM_AND_LOVED_ONE_ADD_TITLE                  	=   'Add a Loved One'
DM_AND_LOVED_ONE_DELETE_TITLE               	=   "Loved One's Info"
DM_AND_LOVED_ONE_CLOSE_ICON                 	=   'close_iv'
DM_AND_LOVED_ONE_LAST_NAME                  	=   'last_name_et'
DM_AND_LOVED_ONE_FIRST_NAME                 	=   'first_name_et'
DM_AND_LOVED_ONE_EMAIL                      	=   'email_et'
DM_AND_LOVED_ONE_EMAIL_ERROR                	=   'lo_email_error_tv'
EM_DM_LOVED_ONE_INVALID_EMAIL               	=   'Please enter a valid email address.'
DM_AND_LOVED_ONE_COUNTRY_CODE               	=   'country_code_ccs'
DM_AND_LOVED_ONE_COUNTRY_HK                 	=   DM_AND_PERSONAL_INFO_COUNTRY_HK
DM_AND_LOVED_ONE_COUNTRY_IN                 	=   DM_AND_PERSONAL_INFO_COUNTRY_IN
DM_AND_LOVED_ONE_COUNTRY_US                 	=   DM_AND_PERSONAL_INFO_COUNTRY_US
DM_AND_LOVED_ONE_COUNTRY_CH                 	=   DM_AND_PERSONAL_INFO_COUNTRY_CH
DM_AND_LOVED_ONE_CELL_NUMBER                	=   'cell_number_et'
DM_AND_LOVED_ONE_CELL_ERROR                 	=   'lo_cell_error_tv'
EM_DM_LOVED_ONE_INVALID_NUMBER              	=   'Please enter a valid phone number.'
EM_DM_LOVED_ONE_CONFLICT_NUMBER             	=   'You are already using this number as your personal phone number. Please enter a different phone number.'
DM_AND_LOVED_ONE_INVITE_BTN                 	=   'invite_btn'
DM_AND_LOVED_ONE_DELETE_BTN                 	=   'delete_btn'

# Set alert time page
DM_AND_SET_ALERT_TITLE                      	=   'Alert Times'
DM_AND_SET_ALERT_BACK                       	=   'back_iv'
DM_AND_SET_ALERT_BRK                        	=   'breakfast_ms'
DM_AND_SET_ALERT_BRK_ERROR                  	=   'breakfast_error_tv'
EM_DM_SET_ALERT_BRK_AFTER_LUN               	=   'Breakfast cannot be after lunch.'
EM_DM_SET_ALERT_BRK_AFTER_DIN               	=   'Breakfast cannot be after dinner.'
EM_DM_SET_ALERT_BRK_AFTER_NIG               	=   'Breakfast cannot be after night.'
DM_AND_SET_ALERT_HOUR                       	=   '//android.widget.TimePicker/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.NumberPicker[1]/android.widget.EditText'
DM_AND_SET_ALERT_MINUTE                     	=   '//android.widget.TimePicker/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.NumberPicker[2]/android.widget.EditText'
DM_AND_SET_ALERT_APM                        	=   '//android.widget.TimePicker/android.widget.LinearLayout/android.widget.NumberPicker/android.widget.EditText'
DM_AND_SET_ALERT_SET_BTN                    	=   'button1'
DM_AND_SET_ALERT_LUN                        	=   'lunch_ms'
DM_AND_SET_ALERT_LUN_ERROR                  	=   'lunch_error_tv'
EM_DM_SET_ALERT_LUN_AFTER_DIN               	=   'Lunch cannot be after dinner.'
EM_DM_SET_ALERT_LUN_AFTER_NIG               	=   'Lunch cannot be after night.'
DM_AND_SET_ALERT_DIN                        	=   'dinner_ms'
DM_AND_SET_ALERT_DIN_ERROR                  	=   'dinner_error_tv'
EM_DM_SET_ALERT_DIN_AFTER_NIG               	=   'Dinner cannot be after night.'
DM_AND_SET_ALERT_NIG                        	=   'night_ms'
DM_AND_SET_ALERT_NEXT_BUTTON                	=   'next_button'
VALUE_DM_SET_ALERT_BRK_IN                   	=   '8:00 AM'
VALUE_DM_SET_ALERT_LUN_IN                   	=   '1:30 PM'
VALUE_DM_SET_ALERT_DIN_IN                   	=   '9:00 PM'
VALUE_DM_SET_ALERT_NIG_IN                   	=   '11:30 PM'

# Medication change confirmation page
DM_AND_MED_CHANGE_DECLINE_BUTTON            	=   'medconf_decline_button'
DM_AND_MED_CHANGE_CONFIRM_BUTTON            	=   'medconf_continue_button'
DM_AND_MED_CHANGE_MED_INFO                  	=   'insulin_line_text'

# Goals list page
DM_AND_GOAL_DATE                            	=   'dateInfo'
DM_AND_GOAL_STATE_INFO                      	=   'goalStateInfo'
DM_AND_GOAL_PREVIOUS_DAY_BTN                	=   'button_prev'
DM_AND_GOAL_NEXT_DAY_BTN                    	=   'button_next'
DM_AND_GOAL_LAST_DAY_BTN                    	=   'button_last'
DM_AND_GOAL_EMPTY_MESSAGE                   	=   'txtErrorMsg'
EM_AND_GOAL_EMPTY_MESSAGE                   	=   "You currently don't have any goals\n\nDaily goals can help remind you when it's time to take your medication or measure your blood sugar. Ask your coach to set goals for you.\n"
DM_AND_GOAL_GO_TO_CHAT_BTN                  	=   'btnGoToChat'
DM_AND_GOAL_NO_NETWORK_MESSAGE              	=   'txtErrorMsg'
EM_AND_GOAL_NO_NETWORK_MESSAGE              	=   "We couldn't load your goals.\n\nYour device is not connected to the internet. Please connect to Wi-Fi or try again later.\n"
DM_AND_GOAL_NO_NETWORK_MORE_INFO            	=   'txtMoreInfo'
#DM_AND_GOAL_SAD_FACE                        	=   'imgHeadPortrait'
DM_AND_GOAL_LIST                            	=   'goalsList'
DM_AND_GOAL_ITEM                            	=   'goalrow_view_frame'
DM_AND_GOAL_GROUP_TIME                      	=   'groupDataBox'
DM_AND_GOAL_GROUP_TIME_TEXT                 	=   'groupName'
DM_AND_GOAL_UNCOMPLETED_STATUS              	=   'goalrow_status_uncompleted'
DM_AND_GOAL_COMPLETED_STATUS                	=   'goalrow_status_completed'
DM_AND_GOAL_HINT_LOG_EDIT                   	=   'goalrow_edit_log_text'
DM_AND_GOAL_NAME                            	=   'goalrow_subtext'
DM_AND_GOAL_DOSAGE_OR_UNIT                  	=   'goalrow_info'
DM_AND_GOAL_VALUE                           	=   'goalrow_bg'
DM_AND_GOAL_SELF_LOG_HINT                   	=   'goalrow_edit_log_text_self_log'

# BG edit page
DM_AND_GOAL_EDIT_DATE                       	=   'entry_date_tv'
DM_AND_GOAL_EDIT_MEAL_TIME                  	=   'entry_when_ms'
DM_AND_GOAL_EDIT_MEAL_TIME_TEXT             	=   '//android.widget.Spinner[@resource-id="com.gatherhealth.gatherdm:id/entry_when_ms"]/android.widget.TextView'
DM_AND_GOAL_EDIT_TIME                       	=   'entry_time_tv'
DM_AND_GOAL_EDIT_MED_NAME                   	=   '//android.widget.Spinner[@resource-id="com.gatherhealth.gatherdm:id/entry_med_ms"]/android.widget.TextView'
DM_AND_GOAL_EDIT_VALUE_FIELD                	=   'entry_reading_et'
DM_AND_GOAL_EDIT_UNIT                       	=   'entry_reading_unit_tv'
DM_AND_GOAL_EDIT_LOG_BTN                    	=   'submit_btn'
DM_AND_GOAL_EDIT_DELETE_BTN                 	=   'delete_btn'
DM_AND_GOAL_EDIT_DATE_PREVIEW               	=   'alertTitle'
DM_AND_GOAL_EDIT_DATE_MONTH                 	=   DM_AND_PERSONAL_INFO_DATE_MONTH
DM_AND_GOAL_EDIT_DATE_DAY                   	=   DM_AND_PERSONAL_INFO_DATE_DAY
DM_AND_GOAL_EDIT_DATE_YEAR                  	=   DM_AND_PERSONAL_INFO_DATE_YEAR
DM_AND_GOAL_EDIT_DATE_CANCEL_BTN            	=   'button2'
DM_AND_GOAL_EDIT_DATE_SET_BTN               	=   DM_AND_PERSONAL_INFO_DATE_SET_BTN
DM_AND_GOAL_EDIT_MEAL_TIME_PRE_BRK          	=   'Pre-breakfast'
DM_AND_GOAL_EDIT_MEAL_TIME_POST_BRK         	=   'Post-breakfast'
DM_AND_GOAL_EDIT_MEAL_TIME_PRE_LUN          	=   'Pre-lunch'
DM_AND_GOAL_EDIT_MEAL_TIME_POST_LUN         	=   'Post-lunch'
DM_AND_GOAL_EDIT_MEAL_TIME_PRE_DIN          	=   'Pre-dinner'
DM_AND_GOAL_EDIT_MEAL_TIME_POST_DIN         	=   'Post-dinner'
DM_AND_GOAL_EDIT_MEAL_TIME_NIGHT            	=   'Night'
DM_AND_GOAL_EDIT_MEAL_TIME_OTHER            	=   'Other'
DM_AND_GOAL_EDIT_TIME_PREVIEW               	=   'alertTitle'
DM_AND_GOAL_EDIT_TIME_HOUR                  	=   DM_AND_SET_ALERT_HOUR
DM_AND_GOAL_EDIT_TIME_MINUTE                	=   DM_AND_SET_ALERT_MINUTE
DM_AND_GOAL_EDIT_TIME_APM                   	=   DM_AND_SET_ALERT_APM
DM_AND_GOAL_EDIT_TIME_CANCEL_BTN            	=   DM_AND_GOAL_EDIT_DATE_CANCEL_BTN
DM_AND_GOAL_EDIT_TIME_SET_BTN               	=   DM_AND_PERSONAL_INFO_DATE_SET_BTN
DM_AND_GOAL_EDIT_LOW_BG_ALERT_TITLE         	=   'alertTitle'
DM_AND_GOAL_EDIT_LOW_BG_ALERT_MESSAGE       	=   'message'
DM_AND_GOAL_EDIT_LOW_BG_ALERT_CANCEL_BTN    	=   'button2'
DM_AND_GOAL_EDIT_LOW_BG_ALERT_LOG_BTN       	=   'button1'
VALUE_AND_GOAL_EDIT_LOW_BG_ALERT_MESSAGE    	=   'You have entered a blood sugar of %s. This is a very low reading. Please make sure this value is correct before submitting.'
VALUE_AND_GOAL_EDIT_LOW_BG_ALERT_TITLE      	=   'Is this value correct?'
DM_AND_GOAL_EDIT_HIGH_BG_ALERT_TITLE        	=   'alertTitle'
DM_AND_GOAL_EDIT_HIGH_BG_ALERT_MESSAGE      	=   'message'
DM_AND_GOAL_EDIT_HIGH_BG_ALERT_CANCEL_BTN   	=   'button2'
DM_AND_GOAL_EDIT_HIGH_BG_ALERT_LOG_BTN      	=   'button1'
VALUE_AND_GOAL_EDIT_HIGH_BG_ALERT_MESSAGE   	=   'You have entered a blood sugar of %s. This is a very high reading. Please make sure this value is correct before submitting.'
VALUE_AND_GOAL_EDIT_HIGH_BG_ALERT_TITLE     	=   'Is this value correct?'
DM_AND_GOAL_EDIT_SURVEY_WHY                 	=   'survey_why_tv'
VALUE_AND_GOAL_EDIT_SURVEY_WHY_HIGH         	=   'Why is your reading high?'
VALUE_AND_GOAL_EDIT_SURVEY_WHY_LOW          	=   'Why is your reading low?'
DM_AND_GOAL_EDIT_SURVEY_REASON_FOOD_1       	=   'I ate a large portion'
DM_AND_GOAL_EDIT_SURVEY_REASON_FOOD_2       	=   'I ate sugary food'
DM_AND_GOAL_EDIT_SURVEY_REASON_FOOD_3       	=   'I ate a high carb meal'
DM_AND_GOAL_EDIT_SURVEY_REASON_FOOD_4       	=   'I ate some new food'
DM_AND_GOAL_EDIT_SURVEY_REASON_FOOD_5       	=   'I ate early'
DM_AND_GOAL_EDIT_SURVEY_REASON_FOOD_6       	=   'I ate less than usual'
DM_AND_GOAL_EDIT_SURVEY_REASON_FOOD_7       	=   'I skipped a meal'
DM_AND_GOAL_EDIT_SURVEY_REASON_FOOD_8       	=   'I ate late'
DM_AND_GOAL_EDIT_SURVEY_REASON_MED_1        	=   'Too little medication'
DM_AND_GOAL_EDIT_SURVEY_REASON_MED_2        	=   'Incorrect med dosage'
DM_AND_GOAL_EDIT_SURVEY_REASON_MED_3        	=   'Forgot to take medication'
DM_AND_GOAL_EDIT_SURVEY_REASON_MED_4        	=   'Too much medication'
DM_AND_GOAL_EDIT_SURVEY_REASON_FEEL_1       	=   'Feeling excited'
DM_AND_GOAL_EDIT_SURVEY_REASON_FEEL_2       	=   'Feeling happy'
DM_AND_GOAL_EDIT_SURVEY_REASON_FEEL_3       	=   'Feeling upset'
DM_AND_GOAL_EDIT_SURVEY_REASON_FEEL_4       	=   'Feeling stressed out'
DM_AND_GOAL_EDIT_SURVEY_REASON_FEEL_5       	=   'Feeling anxious'
DM_AND_GOAL_EDIT_SURVEY_REASON_FEEL_6       	=   'Feeling ill'
DM_AND_GOAL_EDIT_SURVEY_REASON_EXEC_1       	=   'Too little exercise'
DM_AND_GOAL_EDIT_SURVEY_REASON_EXEC_2       	=   'New exercise'
DM_AND_GOAL_EDIT_SURVEY_REASON_EXEC_3       	=   'Too much exercise'
DM_AND_GOAL_EDIT_SURVEY_HIGH_REASONS        	=   [
                                                DM_AND_GOAL_EDIT_SURVEY_REASON_FOOD_1, DM_AND_GOAL_EDIT_SURVEY_REASON_FOOD_2,
                                                DM_AND_GOAL_EDIT_SURVEY_REASON_FOOD_3, DM_AND_GOAL_EDIT_SURVEY_REASON_FOOD_4,
                                                DM_AND_GOAL_EDIT_SURVEY_REASON_FOOD_5, DM_AND_GOAL_EDIT_SURVEY_REASON_MED_1,
                                                DM_AND_GOAL_EDIT_SURVEY_REASON_MED_2, DM_AND_GOAL_EDIT_SURVEY_REASON_MED_3,
                                                DM_AND_GOAL_EDIT_SURVEY_REASON_FEEL_1, DM_AND_GOAL_EDIT_SURVEY_REASON_FEEL_2,
                                                DM_AND_GOAL_EDIT_SURVEY_REASON_FEEL_3, DM_AND_GOAL_EDIT_SURVEY_REASON_FEEL_4,
                                                DM_AND_GOAL_EDIT_SURVEY_REASON_FEEL_5, DM_AND_GOAL_EDIT_SURVEY_REASON_FEEL_6,
                                                DM_AND_GOAL_EDIT_SURVEY_REASON_EXEC_1, DM_AND_GOAL_EDIT_SURVEY_REASON_EXEC_2,
                                                ]
DM_AND_GOAL_EDIT_SURVEY_LOW_REASONS         	=   [
                                                DM_AND_GOAL_EDIT_SURVEY_REASON_FOOD_6, DM_AND_GOAL_EDIT_SURVEY_REASON_FOOD_7,
                                                DM_AND_GOAL_EDIT_SURVEY_REASON_FOOD_4, DM_AND_GOAL_EDIT_SURVEY_REASON_FOOD_8,
                                                DM_AND_GOAL_EDIT_SURVEY_REASON_MED_4, DM_AND_GOAL_EDIT_SURVEY_REASON_MED_2,
                                                DM_AND_GOAL_EDIT_SURVEY_REASON_FEEL_1, DM_AND_GOAL_EDIT_SURVEY_REASON_FEEL_2,
                                                DM_AND_GOAL_EDIT_SURVEY_REASON_FEEL_3, DM_AND_GOAL_EDIT_SURVEY_REASON_FEEL_4,
                                                DM_AND_GOAL_EDIT_SURVEY_REASON_FEEL_5, DM_AND_GOAL_EDIT_SURVEY_REASON_FEEL_6,
                                                DM_AND_GOAL_EDIT_SURVEY_REASON_EXEC_3, DM_AND_GOAL_EDIT_SURVEY_REASON_EXEC_2,
                                                ]

# Edit BP page
DM_AND_BP_EDIT_DATE                         	=   DM_AND_GOAL_EDIT_DATE
DM_AND_BP_EDIT_TIME                         	=   DM_AND_GOAL_EDIT_TIME
DM_AND_BP_EDIT_SYSTOLIC_FIELD               	=   DM_AND_GOAL_EDIT_VALUE_FIELD
DM_AND_BP_EDIT_SYSTOLIC_UNIT                	=   DM_AND_GOAL_EDIT_UNIT
DM_AND_BP_EDIT_DIASTOLIC_FIELD              	=   'entry_reading2_et'
DM_AND_BP_EDIT_DISSTOLIC_UNIT               	=   'entry_reading_unit2_tv'
DM_AND_BP_EDIT_LOG_BTN                      	=   DM_AND_GOAL_EDIT_LOG_BTN
DM_AND_BP_EDIT_DELETE_BTN                   	=   DM_AND_GOAL_EDIT_DELETE_BTN
DM_AND_BP_EDIT_ABNORMAL_ALERT_TITLE         	=   'alertTitle'
DM_AND_BP_EDIT_ABNORMAL_ALERT_MESSAGE       	=   'message'
DM_AND_BP_EDIT_ABNORMAL_ALERT_CANCEL_BTN    	=   'button2'
DM_AND_BP_EDIT_ABNORMAL_ALERT_LOG_BTN       	=   'button1'
VALUE_AND_BP_EDIT_ABNORMAL_ALERT_TITLE      	=   'Is this value correct?'
VALUE_AND_BP_EDIT_ABNORMAL_ALERT_MESSAGE    	=   'You have entered a blood pressure of %s. This is a very abnormal reading. Please make sure this value is correct before submitting.'
DM_AND_BP_EDIT_REVERSE_ALERT_TITLE          	=   'alertTitle'
DM_AND_BP_EDIT_REVERSE_ALERT_MESSAGE        	=   'message'
DM_AND_BP_EDIT_REVERSE_ALERT_CANCEL_BTN     	=   'button2'
DM_AND_BP_EDIT_REVERSE_ALERT_LOG_BTN        	=   'button1'
VALUE_AND_BP_EDIT_REVERSE_ALERT_TITLE       	=   'Is this value correct?'
VALUE_AND_BP_EDIT_REVERSE_ALERT_MESSAGE     	=   'Your diastolic reading is higher than your systolic reading. Are you sure you want to log this measurement?'

# Edit weight page
DM_AND_WEIGHT_EDIT_DATE                     	=   DM_AND_GOAL_EDIT_DATE
DM_AND_WEIGHT_EDIT_TIME                     	=   DM_AND_GOAL_EDIT_TIME
DM_AND_WEIGHT_EDIT_FIELD                    	=   DM_AND_GOAL_EDIT_VALUE_FIELD
DM_AND_WEIGHT_EDIT_UNIT                     	=   DM_AND_GOAL_EDIT_UNIT
DM_AND_WEIGHT_EDIT_LOG_BTN                  	=   DM_AND_GOAL_EDIT_LOG_BTN
DM_AND_WEIGHT_EDIT_DELETE_BTN               	=   DM_AND_GOAL_EDIT_DELETE_BTN

# Bottom buttons
DM_AND_BOTTOM_GOALS                         	=   'main_button0_box'
DM_AND_BOTTOM_CHAT                          	=   'main_button1_box'
DM_AND_BOTTOM_GAMES                         	=   'main_button5_box'
DM_AND_BOTTOM_DATA                          	=   'main_button2_box'
DM_AND_BOTTOM_LOG                           	=   'main_button3_box'

# Self log menu
DM_AND_SELF_LOG_TITLE                       	=   'add_title'
DM_AND_SELF_LOG_CLOSE                       	=   'log_close_rl'
DM_AND_SELF_LOG_BG                          	=   'addBG'
DM_AND_SELF_LOG_MED                         	=   'addMed'
DM_AND_SELF_LOG_BP                          	=   'addBP'
DM_AND_SELF_LOG_WEIGHT                      	=   'weight_tv'

# Chat page
DM_AND_CHAT_FIELD                           	=   'chat_compose'
DM_AND_CHAT_SEND_BTN                        	=   'chat_send'
DM_AND_CHAT_ICON_LEFT                       	=   'chat_icon_left'
DM_AND_CHAT_ICON_RIGHT                      	=   'chat_icon_right'
DM_AND_CHAT_CONTENT                         	=   'chat_content'
DM_AND_CHAT_ERROR_RETRY                     	=   'chat_error_retry'

# Options menu
DM_AND_OPTIONS_MENU_BTN                     	=   'home'
DM_AND_OPTIONS_MY_DATA                      	=   'patientInfo'
DM_AND_OPTIONS_MANAGE_LO                    	=   'Manage my Loved Ones'
DM_AND_OPTIONS_FAQ                          	=   'FAQ'
DM_AND_OPTIONS_APP_SUPPORT                  	=   'App Support'
DM_AND_OPTIONS_SETTINGS                     	=   'Settings'

# FAQ page
DM_AND_FAQ_QUESTION                         	=   'faq_questiontitle'
DM_AND_FAQ_ANSWER                           	=   'faq_answercontent'
DM_AND_FAQ_QUES_1                           	=   'Should I use the Gather app in an emergency?'
DM_AND_FAQ_QUES_2                           	=   'How were my goals created?'
DM_AND_FAQ_QUES_3                           	=   'How do I change my goals?'
DM_AND_FAQ_QUES_4                           	=   'How do I complete a goal?'
DM_AND_FAQ_QUES_5                           	=   u'How do I log a blood sugar test, medication dose or blood pressure measurement that isn\u2019t one of my goals?'
DM_AND_FAQ_QUES_6                           	=   'How do I log goals from a previous day?'
DM_AND_FAQ_QUES_7                           	=   'How do I send my doctor a message?'
DM_AND_FAQ_QUES_8                           	=   'How long will it take my doctor to respond?'
DM_AND_FAQ_QUES_9                           	=   'How do I see a history of my blood sugar data?'
DM_AND_FAQ_QUES_10                          	=   'Can I print data on the blood sugar or blood pressure tables?'
DM_AND_FAQ_QUES_11                          	=   'How do I change notification settings, measurement units or other settings?'
DM_AND_FAQ_QUES_12                          	=   'How do I change my phone number, gender or date of birth?'
DM_AND_FAQ_QUES_13                          	=   'How do I log out?'
DM_AND_FAQ_QUES_14                          	=   'Why does the app require permissions to run?'
DM_AND_FAQ_QUES_15                          	=   'How do I change my email, picture or language?'
DM_AND_FAQ_QUES_16                          	=   'Why should I invite a loved one?'
DM_AND_FAQ_QUES_17                          	=   u"How do I change my loved one\u2019s phone number, email address or other details?"
DM_AND_FAQ_QUES_18                          	=   u"I can\u2019t connect to Gather Health!"
DM_AND_FAQ_QUES_19                          	=   'What do I do if the app freezes or crashes?'
DM_AND_FAQ_QUES_20                          	=   'How do I contact the Gather Health team with my problem or suggestion?'
DM_AND_FAQ_QUES_LIST                        	=   [
                                                DM_AND_FAQ_QUES_1, DM_AND_FAQ_QUES_2, DM_AND_FAQ_QUES_3, DM_AND_FAQ_QUES_4, DM_AND_FAQ_QUES_5, DM_AND_FAQ_QUES_6,
                                                DM_AND_FAQ_QUES_7, DM_AND_FAQ_QUES_8, DM_AND_FAQ_QUES_9, DM_AND_FAQ_QUES_10, DM_AND_FAQ_QUES_11, DM_AND_FAQ_QUES_12,
                                                DM_AND_FAQ_QUES_13, DM_AND_FAQ_QUES_14, DM_AND_FAQ_QUES_15, DM_AND_FAQ_QUES_16, DM_AND_FAQ_QUES_17, DM_AND_FAQ_QUES_18,
                                                DM_AND_FAQ_QUES_19, DM_AND_FAQ_QUES_20
                                                ]
DM_AND_FAQ_SUPPORT_BTN                      	=   'sendOtherQuestion'

# Freshdesk page
DM_AND_FRESHDESK_TITLE                      	=   'action_bar_title'
DM_AND_FRESHDESK_CONTACT_US_BTN             	=   'mobihelp_menu_item_contact_us'
DM_AND_FRESHDESK_DESCRIPTION                	=   "Send questions, problems and feedback to the Gather Health technical support team.\n\nTap here to send a message."
DM_AND_FRESHDESK_SUBMIT_BTN                 	=   'mobihelp_menu_item_submit'
DM_AND_FRESHDESK_INPUT_FIELD                	=   'mobihelp_feedback_problem_description'

# Patient ID dialog
DM_AND_PATIENT_ID_TITLE                     	=   'Your Patient ID is:'
DM_AND_PATIENT_ID_CONTENT                   	=   'patient_id_tv'
DM_AND_PATIENT_ID_BUTTON                    	=   'ok_btn'

# Language settings
DM_AND_LANGUAGE_TITLE                       	=   'alertTitle'
VALUE_DM_LANGUAGE_TITLE                     	=   'Language'
DM_AND_LANGUAGE_EN                          	=   'en_rb'
DM_AND_LANGUAGE_ZH                          	=   'zh_rb'
DM_AND_LANGUAGE_HI                          	=   'hi_rb'
DM_AND_LANGUAGE_CANCEL_BTN                  	=   'set_localetype_cancel'
DM_AND_LANGUAGE_SAVE_BTN                    	=   'set_localetype_save'

# No network alert
DM_AND_NO_NETWORK_TITLE                     	=   'No internet connection'
DM_AND_NO_NETWORK_CONTENT                   	=   'To send messages, please connect to Wi-Fi or try again later.'
DM_AND_NO_NETWORK_OK_BTN                    	=   'button2'
DM_AND_NO_NETWORK_HELP_BTN                  	=   'button1'
DM_AND_NO_NETWORK_HELP_TITLE                	=   'No connection'
DM_AND_NO_NETWORK_HELP_CLOSE_BTN            	=   'btnClose'
DM_AND_NO_NETWORK_HELP_CONTENT_TITLE        	=   'Your device is not connected to the internet.'
DM_AND_NO_NETWORK_BAR                       	=   'relNotNetBanner'
DM_AND_NO_NETWORK_BAR_TEXT                  	=   'txtNote'
DM_AND_NO_NETWORK_BAR_CLOSE_BTN             	=   'imgCloseBanner'

# Settings page
DM_AND_SETTINGS_LOG_OUT                     	=   'Log out'
DM_AND_SETTINGS_ALERTTIME_TITLE             	=   'SET NOTIFICATIONS TIMES'
DM_AND_SETTINGS_ALERTTIME                   	=   '//android.widget.ListView/android.widget.LinearLayout[4]//android.widget.TextView'
DM_AND_SETTINGS_MY_INFO                     	=   'My Info'
DM_AND_SETTINGS_LANGUAGE                    	=   'Language'
DM_AND_SETTINGS_PATIENT_ID                  	=   'Patient ID'
DM_AND_SETTINGS_USER_AGREEMENT              	=   'User Agreement'

# Server settings dialog
DM_AND_SERVER_ADDRESS                       	=   'debugserver_uri'
DM_AND_SERVER_SUBMIT                        	=   'debugserver_submit'






