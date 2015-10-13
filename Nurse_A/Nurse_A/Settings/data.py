# -*- coding: utf-8 -*-

# SECURITY_KEY                =   u'YWxleEBnYXRoZXJoZWFsdGguY29tOmdhb3h1MTIz'
SECURITY_KEY                =   u'YWxleEBnYXRoZXJoZWFsdGguY29tOjEyMzQ1Ng=='
HK_DOCTOR                   =   'alex+hk@gatherhealth.com'
HK_NURSE                    =   'alex+hk+n@gatherhealth.com'
INDIA_DOCTOR                =   'alex+in@gatherhealth.com'
INDIA_NURSE                 =   'alex+innurse@gatherhealth.com'
DOCTOR_FREE                 =   'alex+free@gatherhealth.com'
NURSE_FREE                  =   'alex+freenurse@gatherhealth.com'
US_DOCTOR                   =   'alex+us@gatherhealth.com'
US_NURSE                    =   'alex+us+n@gatherhealth.com'
DOCTOR                      =   'doctor@gatherhealth.com'
NURSE                       =   'nurse@gatherhealth.com'
PASSWORD                    =   '123456'

Stag0                       =   'http://stag0.gatherhealth.com/provider'
Stag1                       =   'https://stag1.gatherhealth.com/provider'
Stag2                       =   'https://stag2.gatherhealth.com/provider'
Stag3                       =   'https://stag3.gatherhealth.com/provider'
Stag4                       =   'https://stag4.gatherhealth.com/provider'
Production                  =   'https://www.gatherhealth.com/provider'
Localhost                   =   'http://localhost:8000/provider'
SERVER                      =   Localhost

if SERVER == Localhost:
    HOST                    =   'http://localhost:8081'
else:
    HOST                    =   SERVER[:-9]
    
DIRECTORY_PATH              =   SERVER+'/directory'
FEED_PATH                   =   SERVER+'/feed'

# Color
GREY_CONFIRM                =   u'rgba(0, 0, 0, 0.25)'
BLUE_CONFIRM                =   u'rgba(50, 179, 230, 1)'
GREEN_CONFIRM               =   u'rgba(127, 210, 67, 1)'

# Country
INDIA                       =   'IN'
US                          =   'US'
CHINA                       =   'CN'
HK                          =   'HK'

# Language
ENGLISH                     =   'en'
SIMPLE_CHINESE              =   'zh-cn'
TRADITIONAL_CHINESE         =   'zh-tw'
INDIAN                      =   'hi'

# BG units
MG_DL                       =   '0'
MMO_L                       =   '1'

# Height units
CM                          =   '0'
IN                          =   '1'

# Weight units
KG                          =   '0'
LB                          =   '1'

# BP units
MMHG                        =   '0'
KPA                         =   '1'

# Units group
SI                          =   '8239'
CONV                        =   '1128'

# Country code          
US_COUNTRY_CODE             =   '1'
IN_COUNTRY_CODE             =   '91'
HK_COUNTRY_CODE             =   '852'
CH_COUNTRY_CODE             =   '86'

# Filter
FILTER_ALL_PATIENT          =   ''
FILTER_STUDY_PATIENT        =   'IsOnStudy = \"True\"'
FILTER_TYPE_ONE             =   'Type = \"1\"'
FILTER_TYPE_TWO             =   'Type = \"2\"'
FILTER_GESTATIONAL          =   'Type = \"Gest\"'
FILTER_PRE_DIABETES         =   'Type = \"Pre\"'
FILTER_OTHER                =   'Type = \"Other\"'
FILTER_ACTIVE               =   'Status = Active'
FILTER_INACTIVE             =   'Status = Inactive'
FILTER_NOT_INSTALL          =   'Status = \"Not Installed\"'
FILTER_EHR_ONLY             =   'Status = EHR'
FILTER_A1C                  =   'A1C > 7'
FILTER_BG_CONTROL           =   'BGControl < 30'
FILTER_MEDADH               =   'MedAdh < 50'
FILTER_NEXT_APPOINTMENT     =   'NextAppointment >= today'
FILTER_WILL_EXPIRE          =   'DaysLeft >= 0 AND DaysLeft <= 14'
FILTER_EXPIRED              =   'DaysLeft < 0 AND IsOnStudy = \"False\"'

# Patient directory columns
LAST                        =   '1'
FIRST                       =   '2'
MED_ADH                     =   '3'
BG_CONTROL                  =   '4'
PRACTICE_NAME               =   '5'
NEXT_APPT                   =   '6'
LAST_APPT                   =   '7'
STATUS                      =   '8'
LAST_BG                     =   '9'
LAST_CONTACT                =   '10'
JOINED                      =   '11'
SUBSCRIPTION                =   '12'
EXPIRES                     =   '13'
TYPE                        =   '14'
A1C                         =   '15'
AGE                         =   '16'

# Sign up steps name
SIGN_UP_CONFIRM_INFO        =   'Confirm info'
SIGN_UP_SIGN_AGREEMENT      =   'Sign agreement'
SIGN_UP_PRACTICE_CONTACT    =   'Practice contact'
SIGN_UP_UPLOAD_PHOTO        =   'Upload photo'
SIGN_UP_ADD_PHONE           =   'Add phone'
SIGN_UP_INVITE_STAFF        =   'Invite staff'

# Demo configuration
DEMO_TEST                   =   '4100'

# Different language version 'Account'
ACCOUNT_HK                  =   '帳戶'
ACCOUNT_IN                  =   'खाता'
ACCOUNT_CH                  =   '用户设置'
ACCOUNT_US                  =   'ACCOUNT'


PR_LOGIN_TITLE              =   u'Gather \u22c5 Login'
PR_FEED_TITLE               =   u'Gather \u22c5 Patient Feed'
HKID                        =   'X356888'
HKID_CHECK                  =   'A'
ADD_PATIENT                 =   u'ADD PATIENT'

MED_GOALS                   =   [
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

WEEKDAY                     =   ['mon', 'tue', 'wed', 'thu', 'fri', 'sat', 'sun']
MEAL                        =   ['brk', 'lun', 'din']
NIGHT                       =   'night'
PRE_POST                    =   ['pre', 'post']

# Message content
MES_CONTENT_BIGGEST_SUCCESS                 =   "It appears you're lagging on your blood sugar measurements, so I wanted to help you make a plan to fit them into your life. When in the past have you been successful in making a change in your life and how did you do it?"
MES_GROUP_SMS_SUCCESS                       =   "Your SMS is in the queue now and will go out shortly."
MES_GROUP_SMS_FAIL                          =   "We are having technical problems sending out your SMS. Please try again later."
MES_PATIENT_SEARCH_NO_RESULT                =   "No results"

# Error messages
EM_PR_ACCOUNT_PASSWORD_LENGH                =   'Password must be between 6 and 64 characters.'
EM_PR_ACCOUNT_PASSWORD_MATCH                =   'Value must match.'
EM_PR_ACCOUNT_PASSWROD_STRENGTH_WEAK        =   'weak'
EM_PR_ACCOUNT_PASSWROD_STRENGTH_TOO_WEAK    =   'too weak'
EM_PR_ACCOUNT_CELL_NUM_IN_US                =   'Phone number must be 10 digits, numbers only.'
EM_PR_ACCOUNT_CELL_NUM_HK                   =   'Phone number must be 8 digits, numbers only.'
EM_PR_ACCOUNT_CELL_NUM_CH                   =   'Phone number must be 11 digits, numbers only.'

EM_PR_MANAGE_PRACTICE_CELL_NUM_IN_US        =   EM_PR_ACCOUNT_CELL_NUM_IN_US
EM_PR_MANAGE_PRACTICE_CELL_NUM_HK           =   EM_PR_ACCOUNT_CELL_NUM_HK
EM_PR_MANAGE_PRACTICE_CELL_NUM_CH           =   EM_PR_ACCOUNT_CELL_NUM_CH

EM_PR_NPF_EMPTY_SURNAME                     =   'Surname field must be filled out'
EM_PR_NPF_EMPTY_GIVEN_NAME                  =   'Given names field must be filled out'
EM_PR_NPF_EMPTY_PATIENT_CELL                =   'Patient cell field must be filled out'
EM_PR_NPF_EMPTY_GENDER                      =   'Gender must be selected.'
EM_PR_NPF_INVALID_P_NUMBER                  =   'Invalid patient phone number'
EM_PR_NPF_EMPTY_EMAIL                       =   'Email address field must be filled out'
EM_PR_NPF_EMPTY_MONTHLY_RATE                =   'Enter a non-zero value'
EM_PR_NPF_INVALID_EMAIL                     =   'Invalid patient email'
EM_PR_NPF_DUPLICATE_EMAIL                   =   'A user with this email already exists'
EM_PR_NPF_INVALID_LO_NUMBER                 =   'Invalid loved one phone number'
EM_PR_NPF_DUPLICATE_NUMBER_WITH_PATIENT     =   'Patient and loved one phone number can not be the same.'

EM_PR_PRESCRIPTION_REQUIRED                 =   'This field is required.'
EM_PR_PRESCRIPTION_STRENGTH                 =   'This field can contain only numbers and punctuation.'
# EM_PR_PRESCRIPTION_DOSAGE                   =   'This field must be a number.'
EM_PR_PRESCRIPTION_DOSAGE                   =   EM_PR_PRESCRIPTION_STRENGTH
EM_PR_PRESCRIPTION_DOSAGE_NON_ZERO          =   'This field must be a non-zero number.'

EM_SIGN_UP_REQUIRED                         =   EM_PR_PRESCRIPTION_REQUIRED
EM_SIGN_UP_PASSWORD_LENGH                   =   'Password must be at least 6 characters.'
EM_SIGN_UP_PASSWORD_MATCH                   =   EM_PR_ACCOUNT_PASSWORD_MATCH
EM_SIGN_UP_SIGNATURE_SERVER_ERROR           =   'Signature can contain only letters, commas, periods, dashes, apostrophes, quotation marks, and spaces.'
EM_SIGN_UP_CELL_NUMBER_IN_US                =   EM_PR_ACCOUNT_CELL_NUM_IN_US
EM_SIGN_UP_CELL_NUMBER_HK                   =   EM_PR_ACCOUNT_CELL_NUM_HK
EM_SIGN_UP_CELL_NUMBER_CH                   =   EM_PR_ACCOUNT_CELL_NUM_CH
EM_SIGN_UP_INVITE_SHORT_ERROR               =   'Please complete the form.'
EM_SIGN_UP_INVITE_LONG_ERROR                =   'Guru name, email, and role are required.'
EM_SIGN_UP_INVALID_EMAIL                    =   'Invalid email address.'

# Locator
PR_TUTORIAL_WELCOME                         =   '.walkthrough_start'
PR_TUTORIAL_WELCOME_CLOSE                   =   '.walkthrough_start .close'
PR_TUTORIAL_TOOLTIP_HELP                    =   '.tut_bubble'
PR_TUTORIAL_TOOLTIP_HELP_CLOSE              =   '.tut_bubble .submit'

PR_NAV_FEED                                 =   '.feed a'
PR_NAV_ADD_PATIENT                          =   '.normal .add a'
PR_NAV_OPTION_MENU                          =   '.dropdown-toggle .avatar'
PR_NAV_OPTION_MENU_LOGOUT                   =   '.user .dropdown-menu>li:nth-last-child(1) a'
PR_NAV_OPTION_MENU_ACCOUNT                  =   '.user .dropdown-menu>li:nth-child(1) a'
'''It is history now.'''
# PR_NAV_OPTION_MENU_MANAGE_PRACTICE          =   '.user .dropdown-menu>li:nth-child(2) a'

PR_NAV_OPTION_MENU_FIRST_PRACTICE           =   '.user .dropdown-menu .practices li:nth-child(1) a'
PR_NAV_OPTION_MENU_PRACTICE                 =   '.user .dropdown-menu .practices li a'
PR_NAV_SWITCH                               =   '.demo ul a'

PR_ADD_PATIENT_SURNAME                      =   'input[name="last_name"]'
PR_ADD_PATIENT_GIVENAME                     =   'input[name="first_name"]'
PR_ADD_PATIENT_PRACTICE                     =   'select[name="practice_id"]'
PR_ADD_PATIENT_P_COUNTRY_CODE               =   'select[name="phone1_country"]'
PR_ADD_PATIENT_P_NUMBER                     =   'input[name="phone1"]'
PR_ADD_PATIENT_L_COUNTRY_CODE               =   'select[name="care_phone_country"]'
PR_ADD_PATIENT_L_NUMBER                     =   'input[name="care_phone"]'
PR_ADD_PATIENT_NORMAL_PATIENT               =   'normal_patient'
PR_ADD_PATIENT_APP_PATIENT                  =   'app_patient'
PR_ADD_PATIENT_EMAIL                        =   'input[name="email"]'
PR_ADD_PATIENT_LANGUAGE                     =   'select[name="language"]'
PR_ADD_PATIENT_GENDER_MALE                  =   'input[name="sex"][value="0"]'
PR_ADD_PATIENT_GENDER_FEMALE                =   'input[name="sex"][value="1"]'
PR_ADD_PATIENT_HAS_HKID_NO                  =   'input[name="has_hkid"][value="false"]'
PR_ADD_PATIENT_HAS_HKID_YES                 =   'input[name="has_hkid"][value="true"]'
PR_ADD_PATIENT_HKID                         =   'input[name="hkid"]'
PR_ADD_PATIENT_HKID_CHECK                   =   'input[name="hkid_check"]'
PR_ADD_PATIENT_PREMIUM_TRIAL                =   '#premium_trial_subscription'
PR_ADD_PATIENT_INVITE_BUTTON                =   'input.full_width'
PR_ADD_PATIENT_BASIC_ERROR                  =   '.patient_create_submit div.error div'
PR_ADD_PATIENT_FINAL_BUTTON                 =   'button.final'
PR_ADD_PATIENT_TITLE                        =   '.heading h1'
PR_ADD_PATIENT_BILL_TIME                    =   'subscription.months'
PR_ADD_PATIENT_BILL_RATE                    =   'subscription.price'
PR_ADD_PATIENT_BILL_RATE_ERROR              =   '.payments div.validation_errors'
PR_ADD_PATIENT_PATIENT_TYPE                 =   'patient_type'
PR_ADD_PATIENT_PATIENT_YEAR                 =   'diagnosis_date'
PR_ADD_PATIENT_PATIENT_COMORBIDITIES        =   'textarea.comos'
PR_ADD_PATIENT_PATIENT_NOTES                =   'patient_notes'
PR_ADD_PATIENT_PRE_LOWER_LIMIT              =   'pre_lower_limit'
PR_ADD_PATIENT_PRE_UPPER_LIMIT              =   'pre_upper_limit'
PR_ADD_PATIENT_POST_LOWER_LIMIT             =   'post_lower_limit'
PR_ADD_PATIENT_POST_UPPER_LIMET             =   'post_upper_limit'
PR_ADD_PATIENT_EVERY_PRE_BRK                =   'every_pre_brk'
PR_ADD_PATIENT_EVERY_POST_BRK               =   'every_post_brk'
PR_ADD_PATIENT_EVERY_PRE_LUN                =   'every_pre_lun'
PR_ADD_PATIENT_EVERY_POST_LUN               =   'every_post_lun'
PR_ADD_PATIENT_EVERY_PRE_DIN                =   'every_pre_din'
PR_ADD_PATIENT_EVERY_POST_DIN               =   'every_post_din'
PR_ADD_PATIENT_EVERY_NIGHT                  =   'every_night'
PR_ADD_PATIENT_EVERY                        =   [PR_ADD_PATIENT_EVERY_PRE_BRK, PR_ADD_PATIENT_EVERY_POST_BRK,
                                                 PR_ADD_PATIENT_EVERY_PRE_LUN, PR_ADD_PATIENT_EVERY_POST_LUN,
                                                 PR_ADD_PATIENT_EVERY_PRE_DIN, PR_ADD_PATIENT_EVERY_POST_DIN,
                                                 PR_ADD_PATIENT_EVERY_NIGHT,]
PR_ADD_PATIENT_OTHER_MED                    =   '.other_meds'                                                 
PR_ADD_PATIENT_MED_GOALS_BUTTON             =   '.med button'
PR_ADD_PATIENT_HEIGHT                       =   'input[name="height"]'
PR_ADD_PATIENT_WEIGHT                       =   'weight'
PR_ADD_PATIENT_WAIST                        =   'waist'
PR_ADD_PATIENT_A1C                          =   'a1c'
PR_ADD_PATIENT_BP_SYS                       =   'bp_sys'
PR_ADD_PATIENT_BP_DIA                       =   'bp_dia'

PR_SIGN_UP_STEP_LINE                        =   'section.steps'
PR_SIGN_UP_ACTIVE_STEP                      =   'div.active>div.legend'
PR_SIGN_UP_LAST_NAME                        =   'input[name="last_name"]'
PR_SIGN_UP_LAST_NAME_VALIDATION             =   'input[name="last_name"]+div.validation_errors'
PR_SIGN_UP_FIRST_NAME                       =   'input[name="first_name"]'
PR_SIGN_UP_FIRST_NAME_VALIDATION            =   'input[name="first_name"]+div.validation_errors'
PR_SIGN_UP_DOCTOR_ID                        =   'input[name="registration_number"]'
PR_SIGN_UP_DOCTOR_ID_VALIDATION             =   'input[name="registration_number"]+div.validation_errors'
PR_SIGN_UP_DEFAULT_LANG                     =   'select[name="language"]'
PR_SIGN_UP_PASSWORD                         =   'input[name="password"]'
PR_SIGN_UP_PASSWORD_VALIDATION              =   'input[name="password"]+div.validation_errors'
PR_SIGN_UP_PASSWORD_CONFIRM                 =   'input[name="password_confirm"]'
PR_SIGN_UP_PASSWORD_CONFIRM_VALIDATION      =   'input[name="password_confirm"]+div.validation_errors'
PR_SIGN_UP_NEXT_BUTTON                      =   'button#next'
PR_SIGN_UP_ACCEPT_CHECKBOX                  =   'input[name="terms_agreed"]'
PR_SIGN_UP_SIGNATURE                        =   'input[name="signature"]'
PR_SIGN_UP_SIGNATURE_ERROR                  =   'span.server_error'
PR_SIGN_UP_COUNTRY_CODE                     =   'select[name="phone_country"]'
PR_SIGN_UP_PRACTICE_NUMBER                  =   'input[name="phone_number"]'
PR_SIGN_UP_PRACTICE_NUMBER_VALIDATION       =   'input[name="phone_number"]+div.validation_errors'
PR_SIGN_UP_CELL_NUMBER                      =   'input[name="phone_number"]'
PR_SIGN_UP_CELL_NUMBER_VALIDATION           =   'input[name="phone_number"]+div.validation_errors'
PR_SIGN_UP_VERIFY_SEND_BUTTON               =   'button.send_confirmation'
PR_SIGN_UP_STAFF_NAME                       =   'input[name="name"]'
PR_SIGN_UP_STAFF_EMAIL                      =   'input[name="email"]'
PR_SIGN_UP_STAFF_ROLE                       =   'select[name="role"]'
PR_SIGN_UP_STAFF_LANG                       =   'select[name="language"]'
PR_SIGN_UP_STAFF_RIGHT                      =   'select[name="is_practice_admin"]'
PR_SIGN_UP_STAFF_INVITE_BUTTON              =   'button#invite_submit'
PR_SIGN_UP_STAFF_INVITE_ERROR               =   'div#invite_error'


PR_PRESCRIPTION_DIALOG                      =   'div.medications'
PR_PRESCRIPTION_TITLE                       =   'div.medications h3'
PR_PRESCRIPTION_VISIBLE_ENTRY               =   '//tr[@class="prescription_input"]'
PR_PRESCRIPTION_ENTRY                       =   'div.medications tr.prescription_input'
PR_PRESCRIPTION_ENTRY_NAME                  =   '.med_name input'
PR_PRESCRIPTION_ENTRY_TYPE                  =   '.med_type select'
PR_PRESCRIPTION_ENTRY_STRENGTH              =   '.med_strength input'
PR_PRESCRIPTION_ENTRY_UNIT                  =   '.med_units select'
PR_PRESCRIPTION_ENTRY_INSTRUCTION           =   '.med_instructions input'
PR_PRESCRIPTION_ENTRY_PRE_POST              =   'select.med_meal'
PR_PRESCRIPTION_ENTRY_FREQUENCY             =   'select.med_frequency'
PR_PRESCRIPTION_ENTRY_DOSAGE_BRE            =   '.breakfast input'
PR_PRESCRIPTION_ENTRY_DOSAGE_LUN            =   '.lunch input'
PR_PRESCRIPTION_ENTRY_DOSAGE_DIN            =   '.dinner input'
PR_PRESCRIPTION_ENTRY_DOSAGE_NIG            =   '.night input'
PR_PRESCRIPTION_ENTRY_DOSAGE_TIME           =   '.specific_time input'
PR_PRESCRIPTION_ENTRY_TIME                  =   '.specific_time select'
PR_PRESCRIPTION_ENTRY_DURATION              =   '.duration input'
PR_PRESCRIPTION_ENTRY_DELETE                =   'td.delete>div.delete'
PR_PRESCRIPTION_ENTRY_VALIDATION            =   'div.g_validation_errors'
PR_PRESCRIPTION_ADD_NEW                     =   'div.medications div.add'
PR_PRESCRIPTION_SAVE                        =   'div.medications button.submit'
PR_PRESCRIPTION_CLOSE                       =   'div.medications div.close'
PR_PRESCRIPTION_DOCTOR_DROPDOWN             =   'div.medications select[name="guru"]'
PR_PRESCRIPTION_PRINT                       =   'div.medications .medications_print'

PR_PRESCRIPTION_CONFIRM_DIALOG              =   'div.medications_confirm'
PR_PRESCRIPTION_CONFIRM_CANCEL              =   'div.medications_confirm button.cancel'
PR_PRESCRIPTION_CONFIRM_SAVE                =   'div.medications_confirm button.submit'

    
PR_BG_GOALS_CLOSE_BUTTON                    =   '.smbg_goals .close'
PR_BG_GOALS_SAVE_BUTTON                     =   '.smbg_goals .submit'

PR_PATIENT_RECORD_ID                        =   '.id span'
PR_PATIENT_RECORD_NAME                      =   'h1.name'
PR_PATIENT_RECORD_NAME_DIALOG               =   'div.edit_patient_name'
PR_PATIENT_RECORD_NAME_SURNAME              =   'input[name="last_name"]'
PR_PATIENT_RECORD_NAME_GIVEN_NAME           =   'input[name="first_name"]'
PR_PATIENT_RECORD_NAME_CANCEL               =   'div.edit_patient_name div.cancel'
PR_PATIENT_RECORD_NAME_SAVE                 =   'div.edit_patient_name div.submit'
PR_PATIENT_RECORD_NAME_CLOSE                =   'div.edit_patient_name div.close'
PR_PATIENT_RECORD_INFO                      =   '.indicator li.status'
PR_PATIENT_RECORD_MEDICATION_NAMES          =   'div.new_rx table tr div.name'
PR_PATIENT_RECORD_CHAT                      =   '.indicator li.messaging'
PR_PATIENT_RECORD_CHAT_QUICK_BUTTON         =   'quick_msg'
PR_PATIENT_RECORD_QUICK_MES_TITLE           =   '.quick_msg_modal h3'
PR_PATIENT_RECORD_QUICK_MES_BIG_SUCCESS     =   'dl.open dd:nth-child(6)'
PR_PATIENT_RECORD_QUICK_MES_SEND            =   '.msg_input .btn'
PR_PATIENT_RECORD_CHAT_TEXTAREA             =   '.patientdetail-msg-compose'
PR_PATIENT_RECORD_CHAT_SEND_BUTTON          =   '#patientdetail-msg-form input[type="submit"]'
PR_PATIENT_RECORD_CHAT_SECOND_MES           =   '.scroller-content li:nth-child(2) div.text'
PR_PATIENT_RECORD_CHAT_LATEST_MES           =   '.scroller-content li:nth-last-child(3) div.text'
PR_PATIENT_RECORD_SMBG                      =   '.smbg'
PR_PATIENT_RECORD_SMBG_COUNTER              =   '.smbg_counter'
PR_PATIENT_RECORD_SMBG_TITLE                =   '.smbg_goals h3'
# PR_PATIENT_RECORD_MED_GOALS                 =   '.meds_schedule'
# PR_PATIENT_RECORD_MED_GOALS_UNCONFIRM       =   '.meds_schedule .alert.med-ack'
PR_PATIENT_RECORD_PRESCRIPTION              =   '.new_rx'
PR_PATIENT_RECORD_PRESCRIPTION_UNCONFIRM    =   '.new_rx .alert.med-ack'
PR_PATIENT_RECORD_PRE_MEAL_RANGE            =   '.pre_meal'
PR_PATIENT_RECORD_POST_MEAL_RANGE           =   '.post_meal'
PR_PATIENT_RECORD_PRE_MEAL_BG_UNIT          =   '.smbg .units'
PR_PATIENT_RECORD_POST_MEAL_BG_UNIT         =   '.smbg .post_meal+span'
PR_PATIENT_RECORD_BILLING                   =   'billing_tab_select'
PR_PATIENT_RECORD_BILLING_OVERVIEW          =   '#billing .overview'
PR_PATIENT_RECORD_BILLING_BASIC_PLAN        =   '#billing .basic .value'
PR_PATIENT_RECORD_BILLING_END_DATE          =   '.expire_date'
PR_PATIENT_RECORD_BILLING_PREMIUM_RADIO     =   'premium_subscription'
PR_PATIENT_RECORD_BILLING_FREE_TRIAL_RADIO  =   'premium_trial_subscription'
PR_PATIENT_RECORD_BILLING_MONTH_RATE        =   'subscription.price'
PR_PATIENT_RECORD_BILLING_TOTAL             =   'subscription.total'
PR_PATIENT_RECORD_BILLING_RATE_ERROR        =   '.validation_errors'
PR_PATIENT_RECORD_BILLING_SUBMIT            =   '#billing .right'
PR_PATIENT_RECORD_BILLING_HISTOR_ENTRY      =   '#billing-history tbody tr'
PR_PATIENT_RECORD_BILLING_FIRST_VOID        =   '#billing td>a'
PR_PATIENT_RECORD_BILLING_FIRST_M           =   '#billing table tr td:nth-child(3)'
PR_PATIENT_RECORD_BILLING_FIRST_R           =   '#billing table tr td:nth-child(4)'
PR_PATIENT_RECORD_BILLING_FIRST_VOIDED      =   'tr.voided'
PR_PATIENT_RECORD_BILLING_P_CONFIRM         =   '.premium-subscription-confirm'
PR_PATIENT_RECORD_BILLING_P_CONFIRM_BACK    =   '.premium-subscription-confirm .revert'
PR_PATIENT_RECORD_BILLING_P_CONFIRM_SUBMIT  =   '.premium-subscription-confirm .submit'
PR_PATIENT_RECORD_BILLING_P_CONFIRM_DATE    =   '.premium-subscription-confirm .new_end_date'
PR_PATIENT_RECORD_BILLING_F_CONFIRM         =   '.trial-subscription-confirm'
PR_PATIENT_RECORD_BILLING_F_CONFIRM_BACK    =   '.trial-subscription-confirm .revert'
PR_PATIENT_RECORD_BILLING_F_CONFIRM_SUBMIT  =   '.trial-subscription-confirm .submit'
PR_PATIENT_RECORD_BILLING_F_CONFIRM_DATE    =   '.trial-subscription-confirm .new_end_date'
PR_PATIENT_RECORD_BILLING_V_CONFIRM         =   '.void-subscription-confirm'
PR_PATIENT_RECORD_BILLING_V_CONFIRM_BASIC   =   '.void-subscription-confirm .basic_plan .value'
PR_PATIENT_RECORD_BILLING_V_CONFIRM_BACK    =   '.void-subscription-confirm .revert'
PR_PATIENT_RECORD_BILLING_V_CONFIRM_SUBMIT  =   '.void-subscription-confirm .submit'
PR_PATIENT_RECORD_BILLING_V_CONFIRM_DATE    =   '.void-subscription-confirm .new_end_date'
PR_PATIENT_RECORD_SUMMARY_TAG               =   'data-tab-summary'
PR_PATIENT_RECORD_SUMMARY_DIV               =   'div[data-tab-name="graph-summary"]'
PR_PATIENT_RECORD_SUMMARY_BG_Y_LABEL        =   '.summary_graph .y.label'
PR_PATIENT_RECORD_SUMMARY_MED_LAST_HISTORY  =   'a.summary_last'
PR_PATIENT_RECORD_BG_TAG                    =   '#data-tab-bg-data'
PR_PATIENT_RECORD_BG_DIV                    =   'div[data-tab-name="graph-bg-data"]'
PR_PATIENT_RECORD_VISIT_TAG                 =   'data-tab-visits'
PR_PATIENT_RECORD_VISIT_CONTENT             =   '#visits'
PR_PATIENT_RECORD_VISIT_NEW_BUTTON          =   '#visits .new'
PR_PATIENT_RECORD_VISIT_OLD_BUTTON          =   '#visits .old'
PR_PATIENT_RECORD_VISIT_EMPTY_HISTORY       =   '#visits .empty'
PR_PATIENT_RECORD_VISIT_AGGREGATE           =   '#visits .aggregate'
PR_PATIENT_RECORD_VISIT_AGGREGATE_EXPLAIN   =   '#visits .explain'
PR_PATIENT_RECORD_VISIT_DATE                =   'input.today'
PR_PATIENT_RECORD_VISIT_DATEPICKER          =   '.datepicker'
PR_PATIENT_RECORD_VISIT_DATE_LAST_MONTH     =   '.datepicker-days .prev'
PR_PATIENT_RECORD_VISIT_DATE_SOME_DAY       =   '.datepicker-days tbody>tr:nth-child(2)>td'
PR_PATIENT_RECORD_VISIT_NOTES               =   '#visits [name="notes"]'
PR_PATIENT_RECORD_VISIT_NOTES_CONFIRM       =   '#visits [name="notes"]+button'
PR_PATIENT_RECORD_VISIT_NOTES_DELETE        =   '#visits [name="notes"]+button+button'
PR_PATIENT_RECORD_VISIT_HEIGHT              =   '#visits [name="height"]'
PR_PATIENT_RECORD_VISIT_HEIGHT_CONFIRM      =   '#visits [name="height"]+div+button'
PR_PATIENT_RECORD_VISIT_HEIGHT_DELETE       =   '#visits [name="height"]+div+button+button'
PR_PATIENT_RECORD_VISIT_WEIGHT              =   '#visits [name="weight"]'
PR_PATIENT_RECORD_VISIT_WEIGHT_CONFIRM      =   '#visits [name="weight"]+div+button'
PR_PATIENT_RECORD_VISIT_WEIGHT_DELETE       =   '#visits [name="weight"]+div+button+button'
PR_PATIENT_RECORD_VISIT_WAIST               =   '#visits [name="waist"]'
PR_PATIENT_RECORD_VISIT_WAIST_CONFIRM       =   '#visits [name="waist"]+div+button'
PR_PATIENT_RECORD_VISIT_WAIST_DELETE        =   '#visits [name="waist"]+div+button+button'
PR_PATIENT_RECORD_VISIT_TEMPERATURE         =   '#visits [name="temperature"]'
PR_PATIENT_RECORD_VISIT_TEMPERATURE_CONFIRM =   '#visits [name="temperature"]+div+div+button'
PR_PATIENT_RECORD_VISIT_TEMPERATURE_DELETE  =   '#visits [name="temperature"]+div+div+button+button'
PR_PATIENT_RECORD_VISIT_BGROUP              =   '#visits [name="blood_group"]'
PR_PATIENT_RECORD_VISIT_BGROUP_CONFIRM      =   '#visits [name="blood_group"]+button'
PR_PATIENT_RECORD_VISIT_BGROUP_DELETE       =   '#visits [name="blood_group"]+button+button'
PR_PATIENT_RECORD_VISIT_RHBGROUP            =   '#visits [name="rh_blood_group"]'
PR_PATIENT_RECORD_VISIT_RHBGROUP_CONFIRM    =   '#visits [name="rh_blood_group"]+button'
PR_PATIENT_RECORD_VISIT_RHBGROUP_DELETE     =   '#visits [name="rh_blood_group"]+button+button'
PR_PATIENT_RECORD_VISIT_TOBACCO             =   '#visits [name="tobacco"]'
PR_PATIENT_RECORD_VISIT_TOBACCO_CONFIRM     =   '#visits [name="tobacco"]+button'
PR_PATIENT_RECORD_VISIT_TOBACCO_DELETE      =   '#visits [name="tobacco"]+button+button'
PR_PATIENT_RECORD_VISIT_ALCOHOL             =   '#visits [name="alcohol"]'
PR_PATIENT_RECORD_VISIT_ALCOHOL_CONFIRM     =   '#visits [name="alcohol"]+button'
PR_PATIENT_RECORD_VISIT_ALCOHOL_DELETE      =   '#visits [name="alcohol"]+button+button'
PR_PATIENT_RECORD_VISIT_EXERCISE            =   '#visits [name="exercise"]'
PR_PATIENT_RECORD_VISIT_EXERCISE_CONFIRM    =   '#visits [name="exercise"]+button'
PR_PATIENT_RECORD_VISIT_EXERCISE_DELETE     =   '#visits [name="exercise"]+button+button'
PR_PATIENT_RECORD_VISIT_DIET                =   '#visits [name="diet"]'
PR_PATIENT_RECORD_VISIT_DIET_CONFIRM        =   '#visits [name="diet"]+button'
PR_PATIENT_RECORD_VISIT_DIET_DELETE         =   '#visits [name="diet"]+button+button'
PR_PATIENT_RECORD_VISIT_EYE                 =   '#visits [name="eye"]'
PR_PATIENT_RECORD_VISIT_EYE_CONFIRM         =   '#visits [name="eye"]+button'
PR_PATIENT_RECORD_VISIT_EYE_DELETE          =   '#visits [name="eye"]+button+button'
PR_PATIENT_RECORD_VISIT_FOOT                =   '#visits [name="foot"]'
PR_PATIENT_RECORD_VISIT_FOOT_CONFIRM        =   '#visits [name="foot"]+div+button'
PR_PATIENT_RECORD_VISIT_FOOT_DELETE         =   '#visits [name="foot"]+div+button+button'
PR_PATIENT_RECORD_VISIT_ALBUMIN             =   '#visits [name="albumin"]'
PR_PATIENT_RECORD_VISIT_ALBUMIN_CONFIRM     =   '#visits [name="albumin"]+div+div+button'
PR_PATIENT_RECORD_VISIT_ALBUMIN_DELETE      =   '#visits [name="albumin"]+div+div+button+button'
PR_PATIENT_RECORD_VISIT_CREATININE          =   '#visits [name="creatinine"]'
PR_PATIENT_RECORD_VISIT_CREATININE_CONFIRM  =   '#visits [name="creatinine"]+div+div+button'
PR_PATIENT_RECORD_VISIT_CREATININE_DELETE   =   '#visits [name="creatinine"]+div+div+button+button'
PR_PATIENT_RECORD_VISIT_ACR                 =   '#visits [name="acr"]'
PR_PATIENT_RECORD_VISIT_ACR_CONFIRM         =   '#visits [name="acr"]+div+div+button'
PR_PATIENT_RECORD_VISIT_ACR_DELETE          =   '#visits [name="acr"]+div+div+button+button'
PR_PATIENT_RECORD_VISIT_EGFR                =   '#visits [name="egfr"]'
PR_PATIENT_RECORD_VISIT_EGFR_CONFIRM        =   '#visits [name="egfr"]+div+div+button'
PR_PATIENT_RECORD_VISIT_EGFR_DELETE         =   '#visits [name="egfr"]+div+div+button+button'
PR_PATIENT_RECORD_VISIT_BUN                 =   '#visits [name="bun"]'
PR_PATIENT_RECORD_VISIT_BUN_CONFIRM         =   '#visits [name="bun"]+div+div+button'
PR_PATIENT_RECORD_VISIT_BUN_DELETE          =   '#visits [name="bun"]+div+div+button+button'
PR_PATIENT_RECORD_VISIT_URIC                =   '#visits [name="uric"]'
PR_PATIENT_RECORD_VISIT_URIC_CONFIRM        =   '#visits [name="uric"]+div+div+button'
PR_PATIENT_RECORD_VISIT_URIC_DELETE         =   '#visits [name="uric"]+div+div+button+button'
PR_PATIENT_RECORD_VISIT_TSH                 =   '#visits [name="tsh"]'
PR_PATIENT_RECORD_VISIT_TSH_CONFIRM         =   '#visits [name="tsh"]+div+div+button'
PR_PATIENT_RECORD_VISIT_TSH_DELETE          =   '#visits [name="tsh"]+div+div+button+button'
PR_PATIENT_RECORD_VISIT_T3                  =   '#visits [name="t3"]'
PR_PATIENT_RECORD_VISIT_T3_CONFIRM          =   '#visits [name="t3"]+div+div+button'
PR_PATIENT_RECORD_VISIT_T3_DELETE           =   '#visits [name="t3"]+div+div+button+button'
PR_PATIENT_RECORD_VISIT_T4                  =   '#visits [name="t4"]'
PR_PATIENT_RECORD_VISIT_T4_CONFIRM          =   '#visits [name="t4"]+div+div+button'
PR_PATIENT_RECORD_VISIT_T4_DELETE           =   '#visits [name="t4"]+div+div+button+button'
PR_PATIENT_RECORD_VISIT_BG_FASTING          =   '#visits [name="bg_fasting"]'
PR_PATIENT_RECORD_VISIT_BG_FASTING_CONFIRM  =   '#visits [name="bg_fasting"]+div+div+button'
PR_PATIENT_RECORD_VISIT_BG_FASTING_DELETE   =   '#visits [name="bg_fasting"]+div+div+button+button'
PR_PATIENT_RECORD_VISIT_BG_POST             =   '#visits [name="bg_postprandial"]'
PR_PATIENT_RECORD_VISIT_BG_POST_CONFIRM     =   '#visits [name="bg_postprandial"]+div+div+button'
PR_PATIENT_RECORD_VISIT_BG_POST_DELETE      =   '#visits [name="bg_postprandial"]+div+div+button+button'
PR_PATIENT_RECORD_VISIT_BG_RANDOM           =   '#visits [name="bg_random"]'
PR_PATIENT_RECORD_VISIT_BG_RANDOM_CONFIRM   =   '#visits [name="bg_random"]+div+div+button'
PR_PATIENT_RECORD_VISIT_BG_RANDOM_DELETE    =   '#visits [name="bg_random"]+div+div+button+button'
PR_PATIENT_RECORD_VISIT_BP_SYS              =   '#visits [name="bp_sys"]'
PR_PATIENT_RECORD_VISIT_BP_DIA              =   '#visits [name="bp_dia"]'
PR_PATIENT_RECORD_VISIT_BP_CONFIRM          =   '#visits [name="bp_dia"]+div+div+button'
PR_PATIENT_RECORD_VISIT_BP_DELETE           =   '#visits [name="bp_dia"]+div+div+button+button'
PR_PATIENT_RECORD_VISIT_HBA1C               =   '#visits [name="hba1c"]'
PR_PATIENT_RECORD_VISIT_HBA1C_CONFIRM       =   '#visits [name="hba1c"]+div+div+button'
PR_PATIENT_RECORD_VISIT_HBA1C_DELETE        =   '#visits [name="hba1c"]+div+div+button+button'
PR_PATIENT_RECORD_VISIT_HDL                 =   '#visits [name="hdl"]'
PR_PATIENT_RECORD_VISIT_HDL_CONFIRM         =   '#visits [name="hdl"]+div+div+button'
PR_PATIENT_RECORD_VISIT_HDL_DELETE          =   '#visits [name="hdl"]+div+div+button+button'
PR_PATIENT_RECORD_VISIT_LDL                 =   '#visits [name="ldl"]'
PR_PATIENT_RECORD_VISIT_LDL_CONFIRM         =   '#visits [name="ldl"]+div+div+button'
PR_PATIENT_RECORD_VISIT_LDL_DELETE          =   '#visits [name="ldl"]+div+div+button+button'
PR_PATIENT_RECORD_VISIT_VLDL                =   '#visits [name="vldl"]'
PR_PATIENT_RECORD_VISIT_VLDL_CONFIRM        =   '#visits [name="vldl"]+div+div+button'
PR_PATIENT_RECORD_VISIT_VLDL_DELETE         =   '#visits [name="vldl"]+div+div+button+button'
PR_PATIENT_RECORD_VISIT_TRI                 =   '#visits [name="tri"]'
PR_PATIENT_RECORD_VISIT_TRI_CONFIRM         =   '#visits [name="tri"]+div+div+button'
PR_PATIENT_RECORD_VISIT_TRI_DELETE          =   '#visits [name="tri"]+div+div+button+button'
PR_PATIENT_RECORD_VISIT_CALCIUM             =   '#visits [name="calcium"]'
PR_PATIENT_RECORD_VISIT_CALCIUM_CONFIRM     =   '#visits [name="calcium"]+div+div+button'
PR_PATIENT_RECORD_VISIT_CALCIUM_DELETE      =   '#visits [name="calcium"]+div+div+button+button'
PR_PATIENT_RECORD_VISIT_VITB12              =   '#visits [name="vitamin_b12"]'
PR_PATIENT_RECORD_VISIT_VITB12_CONFIRM      =   '#visits [name="vitamin_b12"]+div+div+button'
PR_PATIENT_RECORD_VISIT_VITB12_DELETE       =   '#visits [name="vitamin_b12"]+div+div+button+button'
PR_PATIENT_RECORD_VISIT_VITD                =   '#visits [name="vit_d_25_ohd"]'
PR_PATIENT_RECORD_VISIT_VITD_CONFIRM        =   '#visits [name="vit_d_25_ohd"]+div+div+button'
PR_PATIENT_RECORD_VISIT_VITD_DELETE         =   '#visits [name="vit_d_25_ohd"]+div+div+button+button'
PR_PATIENT_RECORD_VISIT_ECG                 =   '#visits [name="ecg"]'
PR_PATIENT_RECORD_VISIT_ECG_DATE            =   '#visits [data-name="ecg"] .date'
PR_PATIENT_RECORD_VISIT_ECG_CONFIRM         =   '#visits [name="ecg"]+button'
PR_PATIENT_RECORD_VISIT_ECG_DELETE          =   '#visits [name="ecg"]+button+button'
PR_PATIENT_RECORD_VISIT_C_PEP               =   '#visits [name="c_peptide"]'
PR_PATIENT_RECORD_VISIT_C_PEP_CONFIRM       =   '#visits [name="c_peptide"]+div+div+button'
PR_PATIENT_RECORD_VISIT_C_PEP_DELETE        =   '#visits [name="c_peptide"]+div+div+button+button'
PR_PATIENT_RECORD_VISIT_INSULIN_A           =   '#visits [name="insulin_assay"]'
PR_PATIENT_RECORD_VISIT_INSULIN_A_CONFIRM   =   '#visits [name="insulin_assay"]+div+div+button'
PR_PATIENT_RECORD_VISIT_INSULIN_A_DELETE    =   '#visits [name="insulin_assay"]+div+div+button+button'
PR_PATIENT_RECORD_VISIT_GAD                 =   '#visits [name="gad_antibodies"]'
PR_PATIENT_RECORD_VISIT_GAD_CONFIRM         =   '#visits [name="gad_antibodies"]+div+div+button'
PR_PATIENT_RECORD_VISIT_GAD_DELETE          =   '#visits [name="gad_antibodies"]+div+div+button+button'
PR_PATIENT_RECORD_VISIT_AST                 =   '#visits [name="ast"]'
PR_PATIENT_RECORD_VISIT_AST_CONFIRM         =   '#visits [name="ast"]+div+div+button'
PR_PATIENT_RECORD_VISIT_AST_DELETE          =   '#visits [name="ast"]+div+div+button+button'
PR_PATIENT_RECORD_VISIT_ALT                 =   '#visits [name="alt"]'
PR_PATIENT_RECORD_VISIT_ALT_CONFIRM         =   '#visits [name="alt"]+div+div+button'
PR_PATIENT_RECORD_VISIT_ALT_DELETE          =   '#visits [name="alt"]+div+div+button+button'
PR_PATIENT_RECORD_VISIT_PROTEIN             =   '#visits [name="protein"]'
PR_PATIENT_RECORD_VISIT_PROTEIN_CONFIRM     =   '#visits [name="protein"]+div+div+button'
PR_PATIENT_RECORD_VISIT_PROTEIN_DELETE      =   '#visits [name="protein"]+div+div+button+button'
PR_PATIENT_RECORD_VISIT_LATEST_HISTORY      =   '#visits .dates .normal'
PR_PATIENT_RECORD_VISIT_SECOND_HISTORY      =   '#visits .dates li.normal:nth-child(4)'
PR_PATIENT_RECORD_VISIT_THIRD_HISTORY       =   '#visits .dates li.normal:nth-child(5)'
PR_PATIENT_RECORD_VISIT_DELETE_CONFIRM      =   '.delete_event'
PR_PATIENT_RECORD_VISIT_DELETE_CONFIRM_Y    =   '.delete_event button'
PR_PATIENT_RECORD_VISIT_FASTING_BG_UNIT     =   '[data-name="bg_fasting"] .unit'
PR_PATIENT_RECORD_VISIT_POST_BG_UNIT        =   '[data-name="bg_postprandial"] .unit'
PR_PATIENT_RECORD_VISIT_RANDOM_BG_UNIT      =   '[data-name="bg_random"] .unit'
PR_PATIENT_RECORD_VISIT_RBC                 =   '#visits [name="rbc"]'
PR_PATIENT_RECORD_VISIT_RBC_CONFIRM         =   '#visits [name="rbc"]+div+div+button'
PR_PATIENT_RECORD_VISIT_RBC_DELETE          =   '#visits [name="rbc"]+div+div+button+button'
PR_PATIENT_RECORD_VISIT_HB                  =   '#visits [name="hemoglobin_hb"]'
PR_PATIENT_RECORD_VISIT_HB_CONFIRM          =   '#visits [name="hemoglobin_hb"]+div+div+button'
PR_PATIENT_RECORD_VISIT_HB_DELETE           =   '#visits [name="hemoglobin_hb"]+div+div+button+button'
PR_PATIENT_RECORD_VISIT_HCT                 =   '#visits [name="hct_pcv"]'
PR_PATIENT_RECORD_VISIT_HCT_CONFIRM         =   '#visits [name="hct_pcv"]+div+div+button'
PR_PATIENT_RECORD_VISIT_HCT_DELETE          =   '#visits [name="hct_pcv"]+div+div+button+button'
PR_PATIENT_RECORD_VISIT_MCV                 =   '#visits [name="mcv"]'
PR_PATIENT_RECORD_VISIT_MCV_CONFIRM         =   '#visits [name="mcv"]+div+div+button'
PR_PATIENT_RECORD_VISIT_MCV_DELETE          =   '#visits [name="mcv"]+div+div+button+button'
PR_PATIENT_RECORD_VISIT_MCH                 =   '#visits [name="mch"]'
PR_PATIENT_RECORD_VISIT_MCH_CONFIRM         =   '#visits [name="mch"]+div+div+button'
PR_PATIENT_RECORD_VISIT_MCH_DELETE          =   '#visits [name="mch"]+div+div+button+button'
PR_PATIENT_RECORD_VISIT_MCHC                =   '#visits [name="mchc"]'
PR_PATIENT_RECORD_VISIT_MCHC_CONFIRM        =   '#visits [name="mchc"]+div+div+button'
PR_PATIENT_RECORD_VISIT_MCHC_DELETE         =   '#visits [name="mchc"]+div+div+button+button'
PR_PATIENT_RECORD_VISIT_RDW                 =   '#visits [name="rdw"]'
PR_PATIENT_RECORD_VISIT_RDW_CONFIRM         =   '#visits [name="rdw"]+div+div+button'
PR_PATIENT_RECORD_VISIT_RDW_DELETE          =   '#visits [name="rdw"]+div+div+button+button'
PR_PATIENT_RECORD_VISIT_PLATELET            =   '#visits [name="platelets"]'
PR_PATIENT_RECORD_VISIT_PLATELET_CONFIRM    =   '#visits [name="platelets"]+div+div+button'
PR_PATIENT_RECORD_VISIT_PLATELET_DELETE     =   '#visits [name="platelets"]+div+div+button+button'
PR_PATIENT_RECORD_VISIT_MPV                 =   '#visits [name="mpv"]'
PR_PATIENT_RECORD_VISIT_MPV_CONFIRM         =   '#visits [name="mpv"]+div+div+button'
PR_PATIENT_RECORD_VISIT_MPV_DELETE          =   '#visits [name="mpv"]+div+div+button+button'
PR_PATIENT_RECORD_VISIT_WBC                 =   '#visits [name="wbc"]'
PR_PATIENT_RECORD_VISIT_WBC_CONFIRM         =   '#visits [name="wbc"]+div+div+button'
PR_PATIENT_RECORD_VISIT_WBC_DELETE          =   '#visits [name="wbc"]+div+div+button+button'
PR_PATIENT_RECORD_VISIT_NEU                 =   '#visits [name="neutrophils"]'
PR_PATIENT_RECORD_VISIT_NEU_CONFIRM         =   '#visits [name="neutrophils"]+div+div+button'
PR_PATIENT_RECORD_VISIT_NEU_DELETE          =   '#visits [name="neutrophils"]+div+div+button+button'
PR_PATIENT_RECORD_VISIT_EOS                 =   '#visits [name="eosinophils"]'
PR_PATIENT_RECORD_VISIT_EOS_CONFIRM         =   '#visits [name="eosinophils"]+div+div+button'
PR_PATIENT_RECORD_VISIT_EOS_DELETE          =   '#visits [name="eosinophils"]+div+div+button+button'
PR_PATIENT_RECORD_VISIT_LYM                 =   '#visits [name="lymphocytes"]'
PR_PATIENT_RECORD_VISIT_LYM_CONFIRM         =   '#visits [name="lymphocytes"]+div+div+button'
PR_PATIENT_RECORD_VISIT_LYM_DELETE          =   '#visits [name="lymphocytes"]+div+div+button+button'
PR_PATIENT_RECORD_VISIT_MON                 =   '#visits [name="monocytes"]'
PR_PATIENT_RECORD_VISIT_MON_CONFIRM         =   '#visits [name="monocytes"]+div+div+button'
PR_PATIENT_RECORD_VISIT_MON_DELETE          =   '#visits [name="monocytes"]+div+div+button+button'
PR_PATIENT_RECORD_VISIT_BAS                 =   '#visits [name="basophils"]'
PR_PATIENT_RECORD_VISIT_BAS_CONFIRM         =   '#visits [name="basophils"]+div+div+button'
PR_PATIENT_RECORD_VISIT_BAS_DELETE          =   '#visits [name="basophils"]+div+div+button+button'
PR_PATIENT_RECORD_MEDICAL_HISTORY           =   'li[data-tracking="PR-MedHistory-ClickTab"]'
PR_PATIENT_RECORD_MEDICAL_HISTORY_GENDER    =   'select[g-measurement="gender"]'
PR_PATIENT_RECORD_MEDICAL_HISTORY_DOB       =   'input[g-measurement="dob"]'
PR_PATIENT_RECORD_MEDICAL_HISTORY_CC        =   'textarea[g-measurement="chief_complaints"]'
PR_PATIENT_RECORD_MEDICAL_HISTORY_TYPE      =   'select[g-measurement="diabetes_type"]'
PR_PATIENT_RECORD_MEDICAL_HISTORY_TYPE_YEAR =   'input[name="diagnosis_date"]'
PR_PATIENT_RECORD_MEDICAL_HISTORY_CVD       =   'textarea[g-measurement="cardiovascular"]'
PR_PATIENT_RECORD_MEDICAL_HISTORY_CVD_YEAR  =   'select[g-measurement-since="cardiovascular"]'
PR_PATIENT_RECORD_MEDICAL_HISTORY_HYPE      =   'textarea[g-measurement="hypertension"]'
PR_PATIENT_RECORD_MEDICAL_HISTORY_HYPE_YEAR =   'select[g-measurement-since="hypertension"]'
PR_PATIENT_RECORD_MEDICAL_HISTORY_DYSL      =   'textarea[g-measurement="dyslipidemia"]'
PR_PATIENT_RECORD_MEDICAL_HISTORY_DYSL_YEAR =   'select[g-measurement-since="dyslipidemia"]'
PR_PATIENT_RECORD_MEDICAL_HISTORY_CVA       =   'textarea[g-measurement="stroke"]'
PR_PATIENT_RECORD_MEDICAL_HISTORY_CVA_YEAR  =   'select[g-measurement-since="stroke"]'
PR_PATIENT_RECORD_MEDICAL_HISTORY_THYR      =   'textarea[g-measurement="thyroid"]'
PR_PATIENT_RECORD_MEDICAL_HISTORY_THYR_YEAR =   'select[g-measurement-since="thyroid"]'
PR_PATIENT_RECORD_MEDICAL_HISTORY_PSYC      =   'textarea[g-measurement="psychiatric_illness"]'
PR_PATIENT_RECORD_MEDICAL_HISTORY_PSYC_YEAR =   'select[g-measurement-since="psychiatric_illness"]'
PR_PATIENT_RECORD_MEDICAL_HISTORY_ANEM      =   'textarea[g-measurement="anemia"]'
PR_PATIENT_RECORD_MEDICAL_HISTORY_ANEM_YEAR =   'select[g-measurement-since="anemia"]'
PR_PATIENT_RECORD_MEDICAL_HISTORY_ASTH      =   'textarea[g-measurement="bronchial_asthma"]'
PR_PATIENT_RECORD_MEDICAL_HISTORY_ASTH_YEAR =   'select[g-measurement-since="bronchial_asthma"]'
PR_PATIENT_RECORD_MEDICAL_HISTORY_OTHER     =   'textarea[g-measurement="other_history"]'
PR_PATIENT_RECORD_MEDICAL_HISTORY_NEUR      =   'textarea[g-measurement="peripheral_neuropathy"]'
PR_PATIENT_RECORD_MEDICAL_HISTORY_NEPH      =   'textarea[g-measurement="nephropathy"]'
PR_PATIENT_RECORD_MEDICAL_HISTORY_RETI      =   'textarea[g-measurement="retinopathy"]'
PR_PATIENT_RECORD_MEDICAL_HISTORY_FOOT      =   'textarea[g-measurement="diabetic_foot_problems"]'
PR_PATIENT_RECORD_MEDICAL_HISTORY_COLO      =   'textarea[g-measurement="colonoscopy"]'
PR_PATIENT_RECORD_MEDICAL_HISTORY_COLO_YEAR =   'select[g-measurement-since="colonoscopy"]'
PR_PATIENT_RECORD_MEDICAL_HISTORY_MOLE      =   'textarea[g-measurement="mole_check"]'
PR_PATIENT_RECORD_MEDICAL_HISTORY_MOLE_YEAR =   'select[g-measurement-since="mole_check"]'
PR_PATIENT_RECORD_MEDICAL_HISTORY_VACC      =   'textarea[g-measurement="vaccinations"]'
PR_PATIENT_RECORD_MEDICAL_HISTORY_VACC_YEAR =   'select[g-measurement-since="vaccinations"]'
PR_PATIENT_RECORD_MEDICAL_HISTORY_MAMM      =   'textarea[g-measurement="mammogram_history"]'
PR_PATIENT_RECORD_MEDICAL_HISTORY_MAMM_YEAR =   'select[g-measurement-since="mammogram_history"]'
PR_PATIENT_RECORD_MEDICAL_HISTORY_PAP       =   'textarea[g-measurement="pap_smear"]'
PR_PATIENT_RECORD_MEDICAL_HISTORY_PAP_YEAR  =   'select[g-measurement-since="pap_smear"]'
PR_PATIENT_RECORD_MEDICAL_HISTORY_PSA       =   'textarea[g-measurement="prostate_specific_antigen"]'
PR_PATIENT_RECORD_MEDICAL_HISTORY_PSA_YEAR  =   'select[g-measurement-since="prostate_specific_antigen"]'
PR_PATIENT_RECORD_MEDICAL_HISTORY_SMOKE     =   'textarea[g-measurement="tobacco"]'
PR_PATIENT_RECORD_MEDICAL_HISTORY_ALCO      =   'textarea[g-measurement="alcohol"]'
PR_PATIENT_RECORD_MEDICAL_HISTORY_EXER      =   'textarea[g-measurement="exercise"]'
PR_PATIENT_RECORD_MEDICAL_HISTORY_DIET      =   'textarea[g-measurement="diet"]'
PR_PATIENT_RECORD_MEDICAL_HISTORY_DRUG      =   'textarea[g-measurement="drugs_history"]'
PR_PATIENT_RECORD_MEDICAL_HISTORY_MARI      =   'textarea[g-measurement="marital_history"]'
PR_PATIENT_RECORD_MEDICAL_HISTORY_PREG      =   'textarea[g-measurement="pregnancy_history"]'
PR_PATIENT_RECORD_MEDICAL_HISTORY_BIRTH     =   'textarea[g-measurement="birth_history"]'
PR_PATIENT_RECORD_MEDICAL_HISTORY_SEX       =   'textarea[g-measurement="sexual_preference"]'
PR_PATIENT_RECORD_MEDICAL_HISTORY_STD       =   'textarea[g-measurement="std_history"]'
PR_PATIENT_RECORD_MEDICAL_HISTORY_DIAB_HIS  =   'textarea[g-measurement="fam_history_diabetes"]'
PR_PATIENT_RECORD_MEDICAL_HISTORY_HYPE_HIS  =   'textarea[g-measurement="fam_history_hypertension"]'
PR_PATIENT_RECORD_MEDICAL_HISTORY_DYSL_HIS  =   'textarea[g-measurement="fam_history_dyslipidemia"]'
PR_PATIENT_RECORD_MEDICAL_HISTORY_THYR_HIS  =   'textarea[g-measurement="fam_history_thyroid"]'
PR_PATIENT_RECORD_MEDICAL_HISTORY_CANC_HIS  =   'textarea[g-measurement="fam_history_cancer"]'
PR_PATIENT_RECORD_MEDICAL_HISTORY_CVD_HIS   =   'textarea[g-measurement="fam_history_heart_disease"]'
PR_PATIENT_RECORD_MEDICAL_HISTORY_CVA_HIS   =   'textarea[g-measurement="fam_history_stroke"]'
PR_PATIENT_RECORD_MEDICAL_HISTORY_ADMI      =   'textarea[g-measurement="hospital_admissions"]'
PR_PATIENT_RECORD_MEDICAL_HISTORY_SURG      =   'textarea[g-measurement="hospital_surgeries"]'
PR_PATIENT_RECORD_MEDICAL_HISTORY_MEDI      =   'textarea[g-measurement="allergies_medications"]'
PR_PATIENT_RECORD_MEDICAL_HISTORY_FOOD      =   'textarea[g-measurement="allergies_foods"]'
PR_PATIENT_RECORD_MEDICAL_HISTORY_LATEX     =   'textarea[g-measurement="allergies_latex"]'
PR_PATIENT_RECORD_MEDICAL_HISTORY_ENVI      =   'textarea[g-measurement="allergies_environmental"]'
PR_PATIENT_RECORD_MEDICAL_HISTORY_SAVE_OK   =   'div.indicator.success'
PR_PATIENT_RECORD_MEDICAL_HISTORY_SAVE_BUT  =   '.medical_history button'
PR_PATIENT_RECORD_MEDICAL_HISTORY_FIELDLIST =   [
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



PR_DIRECTORY_REMOVE_CONFIRM                 =   '.delete_patient .right.submit'
PR_DIRECTORY_TITLE                          =   '.directory-content h3'
PR_DIRECTORY_FIRST_PATIENT                  =   '//table[@id="directory_table"]/tbody/tr[1]/td[1]/a'
PR_DIRECTORY_PATIENT_ENTRY                  =   'a[href="/provider/patient/%s"]'
PR_DIRECTORY_PATIENT_DELETE                 =   '//tr/td/a[@href="/provider/patient/%s"]/../../td[last()]/a'
PR_DIRECTORY_PATIENT_NEXT_APPT              =   '//tr/td/a[@href="/provider/patient/%s"]/../..//div[@class="appointments add button blue"]'
PR_DIRECTORY_PATIENT_LAST_APPT              =   '//tr/td/a[@href="/provider/patient/%s"]/../../td[6]'
PR_DIRECTORY_LAST_NAME                      =   '#directory_table>tbody>tr>td:nth-child(%s)>a' %LAST
PR_DIRECTORY_FIRST_NAME                     =   '#directory_table>tbody>tr>td:nth-child(%s)>a' %FIRST
PR_DIRECTORY_MED_ADH                        =   '#directory_table>tbody>tr>td:nth-child(%s)' %MED_ADH
PR_DIRECTORY_BG_CONTROL                     =   '#directory_table>tbody>tr>td:nth-child(%s)' %BG_CONTROL
PR_DIRECTORY_PRACTICE_NAME                  =   '#directory_table>tbody>tr>td:nth-child(%s)' %PRACTICE_NAME
PR_DIRECTORY_NEXT_APPT                      =   '#directory_table>tbody>tr>td:nth-child(%s)>div' %NEXT_APPT
PR_DIRECTORY_LAST_APPT                      =   '#directory_table>tbody>tr>td:nth-child(%s)' %LAST_APPT
PR_DIRECTORY_STATUS                         =   '#directory_table>tbody>tr>td:nth-child(%s)' %STATUS
PR_DIRECTORY_LAST_BG                        =   '#directory_table>tbody>tr>td:nth-child(%s)' %LAST_BG
PR_DIRECTORY_LAST_CONTACT                   =   '#directory_table>tbody>tr>td:nth-child(%s)' %LAST_CONTACT
PR_DIRECTORY_JOINED                         =   '#directory_table>tbody>tr>td:nth-child(%s)' %JOINED
PR_DIRECTORY_SUBSCRIPTION                   =   '#directory_table>tbody>tr>td:nth-child(%s)' %SUBSCRIPTION
PR_DIRECTORY_EXPIRES                        =   '#directory_table>tbody>tr>td:nth-child(%s)' %EXPIRES
PR_DIRECTORY_TYPE                           =   '#directory_table>tbody>tr>td:nth-child(%s)' %TYPE
PR_DIRECTORY_A1C                            =   '#directory_table>tbody>tr>td:nth-child(%s)' %A1C
PR_DIRECTORY_AGE                            =   '#directory_table>tbody>tr>td:nth-child(%s)' %AGE
PR_DIRECTORY_LAST_NAME_SORT                 =   '#directory_table>thead>tr>th:nth-child(%s)>i' %LAST
PR_DIRECTORY_FIRST_NAME_SORT                =   '#directory_table>thead>tr>th:nth-child(%s)>i' %FIRST
PR_DIRECTORY_MED_ADH_SORT                   =   '#directory_table>thead>tr>th:nth-child(%s)>i' %MED_ADH
PR_DIRECTORY_BG_CONTROL_SORT                =   '#directory_table>thead>tr>th:nth-child(%s)>i' %BG_CONTROL
PR_DIRECTORY_PRACTICE_NAME_SORT             =   '#directory_table>thead>tr>th:nth-child(%s)>i' %PRACTICE_NAME
PR_DIRECTORY_NEXT_APPT_SORT                 =   '#directory_table>thead>tr>th:nth-child(%s)>i' %NEXT_APPT
PR_DIRECTORY_LAST_APPT_SORT                 =   '#directory_table>thead>tr>th:nth-child(%s)>i' %LAST_APPT
PR_DIRECTORY_STATUS_SORT                    =   '#directory_table>thead>tr>th:nth-child(%s)>i' %STATUS
PR_DIRECTORY_LAST_BG_SORT                   =   '#directory_table>thead>tr>th:nth-child(%s)>i' %LAST_BG
PR_DIRECTORY_LAST_CONTACT_SORT              =   '#directory_table>thead>tr>th:nth-child(%s)>i' %LAST_CONTACT
PR_DIRECTORY_JOINED_SORT                    =   '#directory_table>thead>tr>th:nth-child(%s)>i' %JOINED
PR_DIRECTORY_SUBSCRIPTION_SORT              =   '#directory_table>thead>tr>th:nth-child(%s)>i' %SUBSCRIPTION
PR_DIRECTORY_EXPIRES_SORT                   =   '#directory_table>thead>tr>th:nth-child(%s)>i' %EXPIRES
PR_DIRECTORY_TYPE_SORT                      =   '#directory_table>thead>tr>th:nth-child(%s)>i' %TYPE
PR_DIRECTORY_A1C_SORT                       =   '#directory_table>thead>tr>th:nth-child(%s)>i' %A1C
PR_DIRECTORY_AGE_SORT                       =   '#directory_table>thead>tr>th:nth-child(%s)>i' %AGE
PR_DIRECTORY_NO_PATIENT                     =   '.no_patient td'
PR_DIRECTORY_SMS_BUTTON                     =   '#compose_sms'
PR_DIRECTORY_SEARCH_BUTTON                  =   '#submit'
PR_DIRECTORY_SEARCH_FIELD                   =   '#keyword'
PR_DIRECTORY_FILTER                         =   'select[name="filters"]'
PR_DIRECTORY_FILTER_OPTION_ALL_PATIENT      =   'option[value=""]'
PR_DIRECTORY_FILTER_OPTION_STUDY_PATIENT    =   'option[value=\'%s\']'%FILTER_STUDY_PATIENT
PR_DIRECTORY_FILTER_OPTION_TYPE_ONE         =   'option[value=\'%s\']'%FILTER_TYPE_ONE
PR_DIRECTORY_FILTER_OPTION_TYPE_TWO         =   'option[value=\'%s\']'%FILTER_TYPE_TWO         
PR_DIRECTORY_FILTER_OPTION_GEST             =   'option[value=\'%s\']'%FILTER_GESTATIONAL      
PR_DIRECTORY_FILTER_OPTION_PRE_DIA          =   'option[value=\'%s\']'%FILTER_PRE_DIABETES     
PR_DIRECTORY_FILTER_OPTION_OTHER            =   'option[value=\'%s\']'%FILTER_OTHER            
PR_DIRECTORY_FILTER_OPTION_ACTIVE           =   'option[value=\'%s\']'%FILTER_ACTIVE           
PR_DIRECTORY_FILTER_OPTION_INACTIVE         =   'option[value=\'%s\']'%FILTER_INACTIVE         
PR_DIRECTORY_FILTER_OPTION_NOT_INSTALLED    =   'option[value=\'%s\']'%FILTER_NOT_INSTALL      
PR_DIRECTORY_FILTER_OPTION_EHR              =   'option[value=\'%s\']'%FILTER_EHR_ONLY         
PR_DIRECTORY_FILTER_OPTION_A1C              =   'option[value=\'%s\']'%FILTER_A1C              
PR_DIRECTORY_FILTER_OPTION_BG_CONTROL       =   'option[value=\'%s\']'%FILTER_BG_CONTROL       
PR_DIRECTORY_FILTER_OPTION_MEDADH           =   'option[value=\'%s\']'%FILTER_MEDADH           
PR_DIRECTORY_FILTER_OPTION_NEXT_APPO        =   'option[value=\'%s\']'%FILTER_NEXT_APPOINTMENT 
PR_DIRECTORY_FILTER_OPTION_WILL_EXPIRE      =   'option[value=\'%s\']'%FILTER_WILL_EXPIRE      
PR_DIRECTORY_FILTER_OPTION_EXPIRED          =   'option[value=\'%s\']'%FILTER_EXPIRED          
PR_DIRECTORY_SEARCH_RESULT_INFO             =   'span.result-stats'
PR_DIRECTORY_GROUP_SMS_DIALOG               =   '.group_sms'
PR_DIRECTORY_GROUP_SMS_TITLE                =   'div.group_sms h3'
PR_DIRECTORY_GROUP_SMS_CLOSE                =   'div.group_sms h3 .close'
PR_DIRECTORY_GROUP_SMS_SMS_NUMBER           =   'td.count_sms'
PR_DIRECTORY_GROUP_SMS_APP_NUMBER           =   'td.count_app'
PR_DIRECTORY_GROUP_SMS_TOTAL_NUMBER         =   'td.count_total'
PR_DIRECTORY_GROUP_SMS_TEXT_FIELD           =   'div.group_sms textarea'
PR_DIRECTORY_GROUP_SMS_CHECK_BOX            =   'input[name="send_message_copy"]'
PR_DIRECTORY_GROUP_SMS_COUTRY_CODE          =   '#group_sms > div:nth-child(2) > div > select'
PR_DIRECTORY_GROUP_SMS_CELL_NUMBER          =   '#group_sms > div:nth-child(2) > div > div > input'
PR_DIRECTORY_GROUP_SMS_CELL_VALIDATION      =   '#group_sms > div:nth-child(2) > div > div > div'
PR_DIRECTORY_GROUP_SMS_COUNTER              =   '#character_count'
PR_DIRECTORY_GROUP_SMS_CANCEL               =   '#group_sms > div.cleared > button.button.left.cancel'
PR_DIRECTORY_GROUP_SMS_SEND                 =   '#group_sms > div.cleared > button.button.right.submit'
PR_DIRECTORY_GROUP_SMS_RESULT_DIALOG        =   'div.group_sms_result'
PR_DIRECTORY_GROUP_SMS_RESULT_TITLE_SUCCESS =   'span.sms_success'
PR_DIRECTORY_GROUP_SMS_RESULT_TITLE_FAIL    =   'span.sms_error'
PR_DIRECTORY_GROUP_SMS_RESULT_CLOSE         =   '.group_sms_result .close'
PR_DIRECTORY_GROUP_SMS_RESULT_SUCCESS       =   'div.sms_success'
PR_DIRECTORY_GROUP_SMS_RESULT_FAIL          =   'div.sms_error'


PR_APPOINTMENT_TITLE                        =   '.appointments h3'
PR_APPOINTMENT_TITLE_ADD                    =   '.appointments h3 .add'
PR_APPOINTMENT_TITLE_EDIT                   =   '.appointments h3 .edit'
PR_APPOINTMENT_DATE                         =   'date'
PR_APPOINTMENT_TODAY                        =   'div.button[g-appts-offset-days="0"]'
PR_APPOINTMENT_THREE_MONTH                  =   'div.button[g-appts-offset-days="90"]'
PR_APPOINTMENT_SIX_MONTH                    =   'div.button[g-appts-offset-days="180"]'
PR_APPOINTMENT_TIME                         =   '.ui-timepicker-input'
PR_APPOINTMENT_NOTE                         =   '.notes textarea'
PR_APPOINTMENT_SAVE                         =   '.controls .submit'
PR_APPOINTMENT_COMPLETE                     =   '.complete'
PR_APPOINTMENT_DELETE                       =   '.delete'
PR_APPOINTMENT_CLOSE                        =   '.appointments .close'

PR_FEED_CONTENT                             =   '#content.feed'
PR_FEED_FIRST_WARNING                       =   'div.warning'
PR_FEED_FORWARD                             =   'div.fwd'
PR_FEED_CLOSE                               =   'div.close'
PR_FEED_FORWARD_TO                          =   'forward_to'
PR_FEED_FORWARD_FIRST_OPTION                =   '[name="forward_to"] option:nth-child(2)'
PR_FEED_FORWARD_NOTE                        =   '.fwd_group textarea'
PR_FEED_FORWARD_BUTTON                      =   '.fwd_actions .submit'
PR_FEED_FORWARD_CANCEL                      =   '.fwd_actions .cancel_fwd'
PR_FEED_WARNING_FORWARD_BY                  =   'div.warning .fwd_by'
PR_FEED_FIRST_MESSAGE                       =   'div.message.patient'
PR_FEED_PATIENT_NAME                        =   '.vitals .name'   
PR_FEED_EMPTY_LOGO                          =   '.logo_gather'


PR_INFO_NAME                                =   'h1.name'
PR_INFO_PATIENT_DATA                        =   '.blurb'
PR_INFO_COMORBIDITIES                       =   '.patient-data li.chiclet'
PR_INFO_OTHER_MED                           =   '.other li.chiclet'
PR_INFO_NOTE                                =   '.dummy'
PR_INFO_EMAIL                               =   '.email div'
PR_INFO_NUMBER                              =   '.cell div'

PR_ACCOUNT_TITLE                            =   '.heading h1'
PR_ACCOUNT_SURNAME                          =   'input[name="last_name"]'
PR_ACCOUNT_GIVEN_NAME                       =   'input[name="first_name"]'
PR_ACCOUNT_LANGUAGE                         =   'select[name="prefs.language_code"]'
PR_ACCOUNT_BIRTHDATE                        =   'input[name="dob"]'
PR_ACCOUNT_NEW_PASSWORD                     =   'password1'
PR_ACCOUNT_CONFIRM_PASSWORD                 =   'password2'
PR_ACCOUNT_PASSWORD_ERROR                   =   '.validation_errors'
PR_ACCOUNT_PASSWORD_STRENGTH                =   '.password_strength span'
PR_ACCOUNT_SAVE_ALL_BUTTON                  =   'next'
PR_ACCOUNT_COUNTRY_CODE                     =   '.phone_country'
PR_ACCOUNT_CELL_NUMBER                      =   '.phone_number'
PR_ACCOUNT_SEND_SMS_BUTTON                  =   '.send_confirmation'
PR_ACCOUNT_CELL_ERROR                       =   '.halves .validation_errors'
PR_ACCOUNT_SHOW_SUMMARY                     =   'input[name="prefs.graph_layout"][value="1"]'
PR_ACCOUNT_SHOW_BG                          =   'input[name="prefs.graph_layout"][value="2"]'
PR_ACCOUNT_SHOW_VISIT                       =   'input[name="prefs.graph_layout"][value="3"]'

PR_MANAGE_PRACTICE_TITLE                    =   '.edit_profile h1'
PR_MANAGE_PRACTICE_YELLOW_AREA              =   'div.yellow'
PR_MANAGE_PRACTICE_NAME_IN_YELLOW           =   'div.yellow span'
PR_MANAGE_PRACTICE_STAFF_ENTRY              =   '#directory_table>tbody>tr'
PR_MANAGE_PRACTICE_ADD_STAFF_BUTTON         =   '#add_guru'
PR_MANAGE_PRACTICE_INVITE_STAFF_DIALOG      =   'div.add_guru'
PR_MANAGE_PRACTICE_INVITE_STAFF_NAME        =   'input[name="name"]'
PR_MANAGE_PRACTICE_INVITE_STAFF_EMAIL       =   'input[name="email"]'
PR_MANAGE_PRACTICE_INVITE_STAFF_ROLE        =   'select[name="role"]'
PR_MANAGE_PRACTICE_INVITE_STAFF_LANG        =   'select[name="language"]'
PR_MANAGE_PRACTICE_INVITE_STAFF_RIGHT       =   'select[name="is_practice_admin"]'
PR_MANAGE_PRACTICE_INVITE_STAFF_SUBMIT      =   'div.add_guru input.submit'
PR_MANAGE_PRACTICE_INVITE_STAFF_CLOSE       =   'div.add_guru div.close'
PR_MANAGE_PRACTICE_PRACTICE_NAME            =   'practice_name'
PR_MANAGE_PRACTICE_HEIGHT_UNIT              =   'height_units'
PR_MANAGE_PRACTICE_WEIGHT_UNIT              =   'weight_units'
PR_MANAGE_PRACTICE_BP_UNIT                  =   'bp_units'
PR_MANAGE_PRACTICE_BG_UNIT                  =   '[name="bg_units"]'
PR_MANAGE_PRACTICE_CRITICAL_LOW_MG          =   'hypo_alert'
PR_MANAGE_PRACTICE_CRITICAL_LOW_MMO         =   'hypo_alert_mmol'
PR_MANAGE_PRACTICE_CRITICAL_UPPER_MG        =   'hyper_alert'
PR_MANAGE_PRACTICE_CRITICAL_UPPER_MMO       =   'hyper_alert_mmol'
PR_MANAGE_PRACTICE_COUNTRY_CODE             =   'phone_country'
PR_MANAGE_PRACTICE_NUMBER                   =   'phone_number'
PR_MANAGE_PRACTICE_NUMBER_ERROR             =   '.validation_errors'
PR_MANAGE_PRACTICE_UNIT_GROUP               =   'unit_cluster_type'
PR_MANAGE_PRACTICE_SAVE_BUTTON              =   'update_range'
PR_MANAGE_PRACTICE_SAVE_SUCCESS             =   'div.info.clear'

PR_LOGIN_USERNAME                           =   'id_username'
PR_LOGIN_PASSWORD                           =   'id_password'
PR_LOGIN_SUBMIT                             =   'input[name="submit"]'
PR_LOGIN_FORGOT_PASSWORD                    =   '.forgotpw'

