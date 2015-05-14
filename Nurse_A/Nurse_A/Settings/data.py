SECURITY_KEY                =   u'YWxleEBnYXRoZXJoZWFsdGguY29tOmdhb3h1MTIz'
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
Production                  =   'https://www.gatherhealth.com/provider'
Localhost                   =   'http://localhost:8000/provider'
SERVER                      =   Localhost

if SERVER == Localhost:
    HOST                    =   'http://localhost:8080'
else:
    HOST                    =   SERVER[:-9]
    
DIRECTORY_PATH              =   SERVER+'/directory'

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

# Demo configuration
DEMO_TEST                   =   '4100'


PR_LOGIN_TITLE              =   u'Gather \u22c5 Login'
PR_FEED_TITLE               =   u'Gather \u22c5 Patient Feed'
HKID                        =   'X356888'
HKID_CHECK                  =   'A'
ADD_PATIENT                 =   u'ADD PATIENT'

MED_GOALS                   =   [['G1', 0, 0, [5, 0], [6, 0], [5, 0], [5, 0], [5, 0, '09:00:00']],
                                 ['G2', 1, 1, [200, 5], [200, 5], [200, 5], [200, 5], [200, 5, '20:00:00']],
                                ]

WEEKDAY                     =   ['mon', 'tue', 'wed', 'thu', 'fri', 'sat', 'sun']
MEAL                        =   ['brk', 'lun', 'din']
NIGHT                       =   'night'
PRE_POST                    =   ['pre', 'post']

# Message content
MES_CONTENT_BIGGEST_SUCCESS                 =   "It appears you're lagging on your blood sugar measurements, so I wanted to help you make a plan to fit them into your life. When in the past have you been successful in making a change in your life and how did you do it?"

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

# Locator
PR_TUTORIAL_WELCOME                         =   '.walkthrough_start'
PR_TUTORIAL_WELCOME_CLOSE                   =   '.walkthrough_start .close'
PR_TUTORIAL_TOOLTIP_HELP                    =   '.tut_bubble'
PR_TUTORIAL_TOOLTIP_HELP_CLOSE              =   '.tut_bubble .submit'

PR_NAV_FEED                                 =   '.feed a'
PR_NAV_ADD_PATIENT                          =   '.normal .add a'
PR_NAV_OPTION_MENU                          =   '.dropdown-toggle .avatar'
PR_NAV_OPTION_MENU_LOGOUT                   =   '.user .dropdown-menu li:nth-last-child(1) a'
PR_NAV_OPTION_MENU_ACCOUNT                  =   '.user .dropdown-menu li:nth-child(1) a'
PR_NAV_OPTION_MENU_MANAGE_PRACTICE          =   '.user .dropdown-menu li:nth-child(2) a'
PR_NAV_OPTION_MENU_FIRST_PRACTICE           =   '.user .dropdown-menu .practices li:nth-child(1) a'
PR_NAV_SWITCH                               =   '.demo ul a'

PR_ADD_PATIENT_SURNAME                      =   'input[name="last_name"]'
PR_ADD_PATIENT_GIVENAME                     =   'input[name="first_name"]'
PR_ADD_PATIENT_P_COUNTRY_CODE               =   'select[name="phone1_country"]'
PR_ADD_PATIENT_P_NUMBER                     =   'input[name="phone1"]'
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
PR_ADD_PATIENT_FINAL_BUTTON                 =   'button.final'
PR_ADD_PATIENT_TITLE                        =   '.heading h1'
PR_ADD_PATIENT_BILL_TIME                    =   'subscription.months'
PR_ADD_PATIENT_BILL_RATE                    =   'subscription.price'
PR_ADD_PATIENT_PATIENT_TYPE                 =   'patient_type'
PR_ADD_PATIENT_PATIENT_YEAR                 =   'diagnosis_year'
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

PR_MED_GOALS_TITLE                          =   '.med-goals h3'
PR_MED_GOALS_FORM                           =   '.med-goals form'
PR_MED_GOALS_FORM_NAME                      =   '.med_name' 
PR_MED_GOALS_FORM_ORAL                      =   '.oral'
PR_MED_GOALS_FORM_INSULIN                   =   '.insulin'
PR_MED_GOALS_FORM_PRE                       =   '.pre'
PR_MED_GOALS_FORM_POST                      =   '.post'
PR_MED_GAOLS_FORM_DELETE                    =   '.med .delete'
PR_MED_GOALS_FORM_BRK_DOSAGE                =   '.breakfast .dosage'
PR_MED_GOALS_FORM_BRK_AMOUNT                =   '.breakfast .amount'
PR_MED_GOALS_FORM_LUN_DOSAGE                =   '.lunch .dosage'
PR_MED_GOALS_FORM_LUN_AMOUNT                =   '.lunch .amount'
PR_MED_GOALS_FORM_DIN_DOSAGE                =   '.dinner .dosage'
PR_MED_GOALS_FORM_DIN_AMOUNT                =   '.dinner .amount'
PR_MED_GOALS_FORM_NIGHT_DOSAGE              =   '.night .dosage'
PR_MED_GOALS_FORM_NIGHT_AMOUNT              =   '.night .amount'
PR_MED_GOALS_FORM_FREEFORM_DOSAGE           =   '.freeform .dosage'
PR_MED_GOALS_FORM_FREEFORM_AMOUNT           =   '.freeform .amount'
PR_MED_GOALS_FORM_FREEFORM_SELECT           =   '.freeform select'
PR_MED_GOALS_NEW_BUTTON                     =   '.med-goals .button'
PR_MED_GOALS_SUBMIT_BUTTON                  =   '.med-goals .submit'
PR_MED_GOALS_CLOSE_BUTTON                   =   '.med-goals .close'

PR_MED_GOALS_CONFIRM_DIALOG                 =   'div.modal.med-conf'
PR_MED_GOALS_CONFIRM_TITLE                  =   '.med-conf h3'
PR_MED_GOALS_CONFIRM_BACK_BUTTON            =   '.med-conf .revert'
PR_MED_GOALS_CONFIRM_SUBMIT_BUTTON          =   '.med-conf .submit'
    
PR_BG_GOALS_CLOSE_BUTTON                    =   '.smbg_goals .close'
PR_BG_GOALS_SAVE_BUTTON                     =   '.smbg_goals .submit'

PR_PATIENT_RECORD_ID                        =   '.id span'
PR_PATIENT_RECORD_INFO                      =   '.indicator li.status'
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
PR_PATIENT_RECORD_SMBG_TITLE                =   '.smbg_goals h3'
PR_PATIENT_RECORD_MED_GOALS                 =   '.meds_schedule'
PR_PATIENT_RECORD_PRE_MEAL_RANGE            =   '.pre_meal'
PR_PATIENT_RECORD_POST_MEAL_RANGE           =   '.post_meal'
PR_PATIENT_RECORD_PRE_MEAL_BG_UNIT          =   '.smbg .units'
PR_PATIENT_RECORD_POST_MEAL_BG_UNIT         =   '.smbg .post_meal+span'
PR_PATIENT_RECORD_BILLING                   =   'billing_tab_select'
PR_PATIENT_RECORD_BILLING_OVERVIEW          =   '#billing .overview'
PR_PATIENT_RECORD_BILLING_FIRST_M           =   '#billing table tr td:nth-child(3)'
PR_PATIENT_RECORD_BILLING_FIRST_R           =   '#billing table tr td:nth-child(4)'
PR_PATIENT_RECORD_SUMMARY_TAG               =   'data-tab-summary'
PR_PATIENT_RECORD_SUMMARY_BG_Y_LABEL        =   '.summary_graph .y.label'
PR_PATIENT_RECORD_VISIT_TAG                 =   'data-tab-visits'
PR_PATIENT_RECORD_VISIT_NEW_BUTTON          =   '#visits .new'
PR_PATIENT_RECORD_VISIT_FASTING_BG_UNIT     =   '[data-name="bg_fasting"] .unit'
PR_PATIENT_RECORD_VISIT_POST_BG_UNIT        =   '[data-name="bg_postprandial"] .unit'
PR_PATIENT_RECORD_VISIT_RANDOM_BG_UNIT      =   '[data-name="bg_random"] .unit'

PR_DIRECTORY_REMOVE_CONFIRM                 =   '.cleared .right.submit'
PR_DIRECTORY_TITLE                          =   '.directory-content h3'
PR_DIRECTORY_FIRST_PATIENT                  =   '//table[@id="directory_table"]/tbody/tr[1]/td[1]/a'
PR_DIRECTORY_PATIENT_ENTRY                  =   'a[href="/provider/patient/%s"]'
PR_DIRECTORY_PATIENT_DELETE                 =   '//tr/td/a[@href="/provider/patient/%s"]/../../td[last()]/a'
PR_DIRECTORY_PATIENT_NEXT_APPT              =   '//tr/td/a[@href="/provider/patient/%s"]/../..//div[@class="appointments add button blue"]'
PR_DIRECTORY_PATIENT_LAST_APPT              =   '//tr/td/a[@href="/provider/patient/%s"]/../../td[6]'

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

PR_FEED_FIRST_WARNING                       =   'div.warning'
PR_FEED_FORWARD                             =   'div.fwd'
PR_FEED_CLOSE                               =   'div.close'
PR_FEED_FORWARD_TO                          =   'forward_to'
PR_FEED_FORWARD_FIRST_OPTION                =   '[name="forward_to"] option:nth-child(2)'
PR_FEED_FORWARD_NOTE                        =   '.fwd_group textarea'
PR_FEED_FORWARD_BUTTON                      =   '.fwd_actions .submit'
PR_FEED_FORWARD_CANCEL                      =   '.fwd_actions .cancel_fwd'
PR_FEED_FIRST_MESSAGE                       =   'div.message.patient'
PR_FEED_EMPTY_LOGO                          =   '.logo_gather'


PR_INFO_NAME                                =   'h1.name'
PR_INFO_PATIENT_DATA                        =   '.patient-data li'
PR_INFO_COMORBIDITIES                       =   '.patient-data li.chiclet'
PR_INFO_OTHER_MED                           =   '.other li.chiclet'
PR_INFO_NOTE                                =   '.dummy'
PR_INFO_EMAIL                               =   '.email div'
PR_INFO_NUMBER                              =   '.cell div'

PR_ACCOUNT_TITLE                            =   '.heading h1'
PR_ACCOUNT_NEW_PASSWORD                     =   'password1'
PR_ACCOUNT_CONFIRM_PASSWORD                 =   'password2'
PR_ACCOUNT_PASSWORD_ERROR                   =   '.validation_errors'
PR_ACCOUNT_PASSWORD_STRENGTH                =   '.password_strength span'
PR_ACCOUNT_SAVE_ALL_BUTTON                  =   'next'
PR_ACCOUNT_COUNTRY_CODE                     =   '.phone_country'
PR_ACCOUNT_CELL_NUMBER                      =   '.phone_number'
PR_ACCOUNT_SEND_SMS_BUTTON                  =   '.send_confirmation'
PR_ACCOUNT_CELL_ERROR                       =   '.halves .validation_errors'

PR_MANAGE_PRACTICE_TITLE                    =   '.edit_profile h1'
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

