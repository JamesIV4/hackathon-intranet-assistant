 

# **KPI & Task Logging **

Requirements Specification

 

Version 1.62

 

16 February 2016

Eric Tober, PhD

Principal Speech Scientist, SEG

Interactive Intelligence

 

# **Revision History**

 

Date| Version| Summary of Changes| Revised By  
---|---|---|---  
**8/5/2014**| **1.0**| **Generated initial specification**| **Eric D. Tober**  
**8/14/2014**| **1.1**| **Added Section 5 and its subsections for the Handler Implementation Instructions  
Changed references to Session ID to InteractionID.**| **Jon W. McCain**  
**8/14/2014**| **1.2**| **Added "TaskComplete" and "TaskExited" to the allowed ExitReason list for TaskEnd events**| **Eric D. Tober**  
**8/22/2014**| **1.3**| **Added SSDG_Format_RecoResult and made it Section 5.1.8 moving the SSDG_ConvertUTCtoKPITime to Section 5.1.9.**** ****Added an implementation example for the generic tool step flow diagram even though a specific example is shown in the tool step instructions.  
  
Updated the revision on the title page to 1.3 and removed the text "(Initial Draft)"**** **| **Jon W. McCain**  
**8/24/2014**| **1.4**| **Updated Section 5 with some new handlers necessary for KPI Logging.**

  * **New Handlers**
    * **SSDG_KPI_Update_DB_Timer**
    * **SSDG_KPI_Update_DB**
    * **SSDG_ConvertUTCtoDateTime2_SQLServer**

**Added Section 6, KPI Database Data Dictionary**** **| **Jon W. McCain**  
**8/25/2014**| **1.5**| **Fixed the Footer pagination issue****Corrected Reco Result output error where the mode was missing in the trace**| **Eric D. Tober**  
**8/25/2014**| **1.6**| **Removed Handlers that are no longer needed for database updates in favor of the Logging Custom Passthrough report toolstep.  
  
Updated Database instructions as well to account for additional steps required to using this new method**| **Jon W. McCain**  
**8/27/2014**| **1.7**| **Added new Server Parameter, "Disable KPI DB Entries" to Section 5.****Added additional column start_time to IVR_SPEECH_PATH table****Added new handlers for report generation****Updated the Table of Contents to include the 3 rd header level**| **Jon W. McCain**  
**9/4/2014**| **1.8**| **DB SQL Create Script****Changed site_id data type from tinyint to int****Changed the call_path field size from 4000 to max which equates to around 8000 characters.**| **Jon W. McCain**  
**9/8/2014**| **1.9**| **Updated SSDG_StartTask_KPI_Logging with new parameter information**| **Jon W. McCain**  
**9/9/2014**| **1.10**| **Added Configuration Parameters Section****Updated SSDG_Genereate_TuningReport_Data**| **Jon W. McCain**  
**9/18/2014**| **1.11**| **Updated Handler sections with cross-references to tables as well as changes to incorrect descriptions or instructions.  
Updated DB Section with new tables and sections for the different types of indexes used in the new table structure.  
Removed the SQL Scripts from the document and referened them as separate files****Added "Mask Sensitive Data" parameter to SSDG_Format_RecoResult**| **Jon W. McCain**  
**9/26/2014**| **1.12**| **Expanded ExitReason on Call and Task End events to generic exits ( "Other").  Also expanded list of allowed ExitReason error codes (e.g. "MaxDisconfirms")**| **Eric D. Tober**  
**10/3/2014**| **1.13**| **Separated Implementation Instructions into separate document**| **Eric D. Tober**  
**11/3/2014**| **1.14**| **Added Footer to CallPath logs, capturing ExitType/ExitReason information.   New sequencing description added to Sec. ****4.3**| **Eric D. Tober**  
**11/10/2014**| **1.15**| **Added sample exit callpaths for various transfer types to show expected format.**| **Eric D. Tober**  
**11/18/2014**| **1.20**| **Added descriptors matching callpath codes to state types.   Added new "DS" callpath code to cover decision states.  Added new "SC" and "SR" codes for subdialog call and return states.**| **Eric D. Tober**  
**11/21/2014**| **1.21**| **Clarification added for multiple returns in CallPath events S, R, and P.   Added SiteID key to StartCall event and CallPath header.  Simplified DS field returns in CallPath.**| **Eric D. Tober**  
**1/8/2015**| **1.30**| **Updated to reflect Ralph 's JSON naming conventions**| **Eric D. Tober**  
**1/14/2015**| **1.35**| **Added event trace objects to call and task objects.   These allow compiling KPIs for events outside of standard call/task metrics.**| **Eric D. Tober**  
**1/19/2015**| **1.36**| **Added example for MO exit in Interaction string**| **Eric D. Tober**  
**3/5/2015**| **1.40**| **Separated Task logs into TaskStart and TaskEnd.   Enables easier tracking of nested tasks**| **Eric D. Tober**  
**10/8/2015**| **1.50**| **Add requirements for security: masking & encryption**| **Eric D. Tober**  
**12/8/2015**| **1.60**| **Added new call_customN fields to Call object in JSON**| **Eric D. Tober**  
**2/4/2016**| **1.61**| **Clarification added for endcall Interaction code syntax**| **Eric D. Tober**  
**2/5/2016**| **1.62**| **Added information for Interaction Code ED (Exit Dialog)**| **Hernan Mendez**  
  
 

 

# 1. Executive Summary

This document captures the key requirements for logging KPI and Task Analysis events within IVR applications.  The purpose of such logging is to enable the rapid generation of standardized, high-level performance reporting for ININ's IVR customers.  KPI and Task Reporting allow:

  1. Issue identification
  2. Trending analysis
  3. Proof of ROI



 

 

# 2\. KPI Logging Requirements

This section describes the basic logging requirements proposed for enabling high-level KPI measurements within the Speech Tuner tool. For basic KPI logging, there should be a JSON object, **Call, containing the** log entries set within the VXML code (or handler) and logged by the platform. Various elements of the Call object would be populated at the start and end of each call. The fields for each event are defined, below.

 

## 2.1 Call Object (Start of Call)

At the start of each call, the following information should be logged:

 

**Field**| **Required**| **Description**| **Allowed Values**  
---|---|---|---  
call_id| Yes| Platform session ID| alphanumeric  
call_start_time| Yes| Time at which the call began| YYYYMMDD.HH:MM:SS.mmm  
customer_name| No| Name of ININ customer| Text, no whitespace or special chars  
application_name| No| Name of IVR application| Text, no whitespace or special chars  
site_id| No| The Interaction SiteID.  Indicates where call has landed.| alphanumeric  
ani| No|  | Digits or SIP URL  
dnis| No|  | Digits or SIP URL  
caller_type| No| Description of caller type| Text, no whitespace or special chars  
app_server_url| No| URL of application server| URI format  
call_custom_start| No| an optional string for containing any pertinent information not listed above| Text, no special chars  
  
Note: When optional fields are not populated by the application code, the resulting log string should reflect no value to the right of the "=" sign.

 

## 2.2 Call Object (End of Call)

At the end of each call, the following information should be logged by the application:

 

**Field**| **Required**| **Description**| **Allowed Values**  
---|---|---|---  
call_end_time| Yes| Time at which the call ended| YYYYMMDD.HH:MM:SS.mmm  
call_exit_type| Yes| Method in which the call left the IVR| "hangup" or "transfer"  
call_exit_reason| Yes| Reason for IVR exit| 

  * "AgentRequestTransfer"
  * "BusinessRuleTransfer"
  * "CallerHangupNormal" (caller hungup after providing any input)
  * "SystemHangup"
  * "MaxNoMatch"
  * "MaxNoInput"
  * "SystemError" (e.g. syntax error, missing url, backend error)
  * "CallerHangupEarly" (caller hungup before providing any input)
  * "MaxDisconfirms" (caller disconfirmed, consecutively, maximum allowed times)
  * "MaxMainMenu" (caller consecutive "main menu" requests reached allowed maximum)
  * "MaxRepeats" (caller consecutive "repeat" requests reached allowed maximum)
  * "MaxMenuVisits" (caller menu visits reached allowed maximum for a given menu)
  *  "MaxHelp" (caller consecutive "help" requests reached allowed maximum)
  * "OtherContained" (generic catch-all for application specific contained exit reasons)
  * "OtherUncontained" (generic catch-all for application specific transferred exit reasons)

  
call_self_served| No| Indicates if the caller successfully completed a task (other than authentication) prior to the end of call| Boolean: "true" or "false"  
call_duration| Yes| Total duration for the call| Time in seconds rounded to tenths (e.g. 23.5)  
call_authenticated| No| Indicates if the caller successfully authenticated prior to the end of call| Boolean: "true" or "false"  
call_last_state| Yes| The final active state from which the call ended (dialog, decision, or backend). If there is a generic transfer handler in the VXML code, we would probably want to be able to skip this state, picking the previous one.| Dialog State Name  
call_audio_file| No| Path to any whole call recording generated by the platform| URI format  
call_custom_end| No| an optional string for containing any pertinent information not listed above| Text, no special chars  
call_event_trace| No| An array of event names to be tracked in a call| An array of text  
  
** **

## 2.3        Call Custom Fields

At any time throughout the call, the KPI Call object maintains five custom fields that may be populated with Customer specific strings.  The purpose of these fields is to enable additional logging customization to characterize a call via standardized logging fields (keys).

 

**Field**| **Required**| **Description**| **Allowed Values**  
---|---|---|---  
call_custom_1| No| Field for holding customer specific call data.  For example, line of business, open/closed hours, etc.)| Text: [a-zA-Z0-9 _]  
call_custom_2| No| same as above| same as above  
call_custom_3| No| same as above| same as above  
call_custom_4| No| same as above| same as above  
call_custom_5| No| same as above| same as above  
  
 

## 2.4        Sample Call Log Entry:

**    **

 

 

 

** **

# 3\. Task Logging Requirements

This section describes the basic logging requirements proposed for enabling Task Analysis measurements within the Speech Tuner tool. For Task logging, there should be a JSON object, **Task, containing the** log entries set within the VXML code (or handler) and logged by the platform. The object is an array containing a JSON string for each task attempt.  Various elements of the Task object would be populated at the start and end of each task. The fields for each event are defined, below.

## 3.1 TaskStart Object (start of task)

At the start of each task, the following information should be logged:

 

**Field**| **Required**| **Description**| **Allowed Values**  
---|---|---|---  
task_name| Yes| Name of task| Text, no whitespace or special chars  
task_start_time| Yes| Time at which the task began| YYYYMMDD.HH:MM:SS.mmm  
task_active_list| No| Comma separated list of any currently active tasks upon entry| Text, no whitespace or special chars  
task_entry_count| Yes| Number of times caller has entered this task (including current)| Digits  
task_custom_start| No| an optional string for containing any pertinent information not listed above| Text, no special chars  
  
**  
**

## 3.2        TaskEnd Object (end of task)

At the end of each task, the following information should be logged by the application:

 

**Field**| **Required**| **Description**| **Allowed Values**  
---|---|---|---  
task_name| Yes| Name of task| Text, no whitespace or special chars  
task_end_time| Yes| Time at which the call ended| YYYYMMDD.HH:MM:SS.mmm  
task_duration| Yes| Total duration for the task| Time in seconds rounded to tenths (e.g. 23.5)  
task_success| Yes| Did the task complete successfully?| Boolean: "true" or "false"  
task_exit_reason| Yes| Reason for Task exit| 

  * "AgentRequestTransfer"
  * "BusinessRuleTransfer"
  * "CallerHangup"
  * "SystemHangup"
  * "MaxNoMatch"
  * "MaxNoInput"
  * "SystemError" (e.g. syntax error, missing url, backend error)
  * "TaskCompleted"
  * "TaskExited"
  * "MaxDisconfirms" (caller disconfirmed, consecutively, maximum allowed times)
  * "MaxMainMenu" (caller consecutive "main menu" requests reached allowed maximum)
  * "MaxRepeats" (caller consecutive "repeat" requests reached allowed maximum)
  * "MaxMenuVisits" (caller menu visits reached allowed maximum for a given menu)
  *  "MaxHelp" (caller consecutive "help" requests reached allowed maximum)

  
task_last_state| Yes| The final active state from which the task ended (dialog, decision, or backend). If there is a generic transfer handler in the VXML code, we would probably want to be able to skip this state, picking the previous one.| Dialog State Name  
task_custom_end| No| an optional string for containing any pertinent information not listed above| Text, no special chars.

  * Task specific failure message (e.g. "insufficientFunds")
  * Task specific success message (e.g. "paymentConfirmed")

  
task_event_trace| No| An array of event names to be tracked in a call| An array of text  
  
** **

## 3.3        Sample Task Log Entry:

"Tasks": [

    {

      "TaskStart": {

          "task_name": "Entry",

          "task_start_time": "20150305.14:52:49.605",

          "task_active_list": [],

          "task_entry_count": "1",

          "task_custom_start": ""

        }

    },

    {

       "TaskEnd": {

           "task_name": "Entry",

           "task_end_time": "20150305.14:52:49.605",

           "task_duration": "0",

           "task_success": "true",

           "task_exit_reason": "TaskCompleted",

           "task_last_state": "AIL0000",

           "task_custom_end": "",

           "task_event_trace": ["item1", "item2"]

       }
    
    
        }
    
    
     ]

 

** **

# 4                    Interactions "Call Path" Logging Requirements

This section describes the basic logging requirements proposed for enabling call path tracking within the Speech Tuner tool. For basic path logging, there should be a **Interactions** JSON object set within the VXML code (or handler) and logged by the platform. These log entries would be fired at the finish of each call. The fields for each call path event are listed, below.

## 4.1        Interactions Object

At the end of each call, the following information should be logged:

 

**Field**| **Required**| **Description**| **Allowed Values**  
---|---|---|---  
 _dialog_state_|  Yes| The name of the current DM, backend state, play prompt state, subdialog call, or decision state.| text, underscores, and digits.  No special  chars allowed: [a-zA-Z0-9_-]  
_interaction_code_|  Yes| Code specific to state/interaction type| See table 4.2  
 _interaction_field_|  Yes| Detailed information pertaining to interaction of type interaction_code.| See table 4.2  
 _comment_|  No| An optional comment| text restricted to [a-zA-Z0-9_-= !]  
_decision_label_|  No| A label used for specifying a possible decision path within an interaction.| text restricted to [a-zA-Z0-9_-= !]  
_time_|  Yes| time stamp at which interaction occured| date/time stamp of format:  YYYYMMDD.HH:MM:SS.msec  
  
 

## 4.2        Interaction Codes & Fields:

Each interaction of the IVR system (recognition, prompt playback, decision state, or backend lookup) will be logged within the Interaction JSON object.  The following table lists the allowed codes for a given interaction.  Note: avoid using ":" or double quotes within any value strings within the JSON object.  This includes comments, labels, recognition results, and backend fields.

 

**interaction_code**| **interaction_field**  
---|---  
B| Backend access with ID initiated.  May include optional backend call inputs specified in section.  Occurs for "DB" states, only.  ID is optional. See sec 4.2.2 for examples.{                "ID":id,                "inputs":{                    "input1":"value1",                    "input2":"value2",                    "input3":"value3" }Note: secure/masked data should result in "**masked**" filling the _value_ fields.  In the case of encryption, the encrypted data string would fill the _value_ fields.  
BF| Backend access with ID failed.  Occurs for "DB" states, only. ID is optional. ID is optional. See sec 4.2.2 for examples.{                "ID":id,                "outputs":{                    "input1":"value1",                    "input2":"value2",                    "input3":"value3" }Note: secure/masked data should result in "**masked**" filling the _value_ fields.  In the case of encryption, the encrypted data string would fill the _value_ fields.  
BS| Backend access with ID successful.  May include optional backend call outputs specified in section.  Occurs for "DB" states, only. ID is optional. ID is optional. See sec 4.2.2 for examples.{                "ID":id,                "outputs":{                    "input1":"value1",                    "input2":"value2",                    "input3":"value3" }Note: secure/masked data should result in "**masked**" filling the _value_ fields.  In the case of encryption, the encrypted data string would fill the _value_ fields.  
DS| Decision state with label for satisfied condition.  Occurs for "BC" states, only.  The "decisionLabel" filed is optional.  See Sec. 4.2.3 for examples.interaction_field:""  
E| An application / platform error of type ID occurred.  Occurs for any state.{      "ID":id}   
H| Help was requested.  Occurs for "DM" states, only.interaction_field:""  
MD| Exit state due to max disconfirms.  Occurs for "DM" states, only.interaction_field:""  
ME| Exit state due to max NoMatch.  Occurs for "DM" states, only.interaction_field:""  
MH| Exit state due to max help requests.  Occurs for "DM" states, only.interaction_field:""  
MM| Exit state due to max "main menu" requests.  Occurs for "DM" states, only.interaction_field:""  
MO| Exit state due to max "operator" requests.  Occurs for "DM" states, only.interaction_field:""  
MR| Exit state due to max "repeat" requests.  Occurs for "DM" states, only.  
MT| Exit state due to max NoInput.  Occurs for "DM" states, only.interaction_field:""  
MV| Exit state due to max allowed visits for a given menu.  Occurs for "DM" states, only.interaction_field:""  
N| NoMatch.  Occurs for "DM" states, only.interaction_field:""  
P| Prompt played with ID.  Occurs for "DM" and "PP" states, only. In the case of multiple prompts URIs, use commas to separate within the parentheses.{                "prompts":                                [                                                "prompt1",                                                "prompt2",                                                "prompt3"                                ]} Note: secure/masked data should result in "**masked**" filling the _prompt_ fields.  In the case of encryption, the encrypted data string would fill the _prompt_ fields.   
R| Successful voice recognition.  The format of <RecResult> is specified in section.  Occurs for "DM" states, only. In the case of multiple slot returns (key/value pairs), use commas to separate within the interpretation field (see 4.2.1 for example).{                "mode":mode,                "confidence":confidence,                "lliteral":"the recognized caller utterance",                "slots":{                    "slot 1":"value 1",                    "slot 2":"value 2",                    "slot 3":"value 3"} Note: secure/masked data should result in "**masked**" filling the _value_ fields.  In the case of encryption, the encrypted data string would fill the _value_ fields.  
S| Entering a dialog state.  The format of the <GrammarURIs> is specified in sec.  Occurs for "DM" states, only. In the case of multiple grammar URIs, use commas to separate within the parentheses.  See Sec. 4.2.5 for examples.{                "grammars":                                [                                                "grammar1",                                                "grammar2",                                                "grammar3"                                ]}   
SD| Subdialog calling state.  interaction_field specifies destination URI as well as parameters passed in via the namelist.  See Sec. 4.2.4 for examples.{                "uri":"<http://blah.com/blah>"                "inputs":{                    "input1":"value1",                    "input2":"value2",                    "input3":"value3" }Note: secure/masked data should result in "**masked**" filling the _value_ fields.  In the case of encryption, the encrypted data string would fill the _value_ fields.   
SR| Return from subdialog.  The namelist, comma separated, in key/value pairs.  See Sec. 4.2.4 for examples.{                "outputs":{                    "key1":"value1",                    "key2":"value2",                    "key3":"value3"                }} Note: secure/masked data should result in "**masked**" filling the _value_ fields.  In the case of encryption, the encrypted data string would fill the _value_ fields.  
T| NoInput.  Occurs for "DM" states, only.interaction_field:""  
XA| Application hang-up.  Occurs for any state. This is an end of call code.interaction_field:""  
XC| Transfer to CSR.  Occurs for any state. This is an end of call code.interaction_field:""  
XH| Caller hang-up.  Occurs for any state. This is an end of call code.interaction_field:""  
XT| Transfer to 3rd party (can be IVR or 3rd party call center).  Occurs for any state. This is an end of call code.interaction_field:""  
ED| Exiting a dialog state.  Occurs for "DM" states, only. Comma separated, in key/value pairs, See Sec. 4.2.6 for examples.interaction_field {          "input_mode": Mode,          "confidence": Confidence,          "literal": The recognized caller utterance,          "result": slot,          "dialog_state_error_counter": The overall dialog state error counter,          "confirmation_error_counter": The confirmation error counter,          "disconfirmation_counter": The disconfirmation counter,          "repeat_counter": The repeat counter,          "no_input_counter": The no input counter,          "no_match_counter": The no match counter,          "confirmation_mode": The confirmation mode,          "confirmation_confidence": The confirmation confidence,          "confirmation_literal": The confirmation recognized caller utterance,          "confirmation_result": The confirmation slot}   
  
 

The Interactions will take the form of a JSON string containing separated events of the form:

**         {**

**" dialog_state":state_name,**

**" interaction_code":interaction_code,**

**                 "interaction_field":interaction_field,          **

**" decision_label":decision_label,**

**" comment":comment,**

**" time":YYYYMMDD.HH:MM:SS.msec**

**         },**

** **

Confirmation nodes for DM states are indicated by appending "_confirm" to the DM state name:

**         {**

**" dialog_state":state_name + "_confirm",**

**" interaction_code":interaction_code,**

**                 "interaction_field":interaction_field,          **

**" decision_label":decision_label,**

**" comment":comment,**

**" time":YYYYMMDD.HH:MM:SS.msec**

**         },**

### 4.2.1      Recognition Result Format

Speech recognition results should be logged in the following format:

  * **mode:** Input mode must have a value of 'dtmf' or 'voice'.  
  * **confidence:** The confidence score must be reported within the range of 0-1 with two significant digits (e.g. "0.55")
  * **literal:** the literal field must contain the text of the recognized utterance or dtmf input returned by the recognizer.   For masked DMs, the value should  be "****".
  * **slots:** an array object containing key/value pairs of slot name and slot value returned by the recognizer.



 

Examples of a recognition result event for a dialog state:

 

        {

            "dialog_state":"AA00100_MainMenu_DM",

"interaction_code":"R",

            "interaction_field":{

                        "mode":"dtmf",

                        "confidence":"1.00",

                        "literal":"3",

                        "slots":{

                                    "out":"pay_bill"

                        }

            }

"comment":"",

"decision_label":"",           

            "time":"20141209.07:46:32.832"           

        },

 

        {

            "dialog_state":"AA00200_PayBill_DM",

"interaction_code":"R",

            "interaction_field":{

                        "mode":"speech",

                        "confidence":"0.55",

                        "literal":"pay fifty dollars to visa",

                        "slots":{

                                    "out.amount":"50.00",

                                    "out.payee":"visa"

                        }

            }

"comment":"",

"decision_label":"amount_and_payee_provided",           

            "time":"20141209.07:46:32.832"           

        },

### 4.2.2      Format for Backend Inputs and Outputs

The backend inputs and outputs can optionally be supplied for backend events via key/value pairs within the interaction_field.

 

        {

            "dialog_state":"AA00300_SubmitPayment_DB",

"interaction_code":"B",

            "interaction_field":{

                "ID":"12345",

                "inputs":{

                    "account_num":"****",

                    "amount":"50.00",

                    "payee":"visa"

                }

            }

"comment":"",

"decision_label":"",           

            "time":"20141209.07:46:32.832"           

        },

 

        {

            "dialog_state":"AA00300_SubmitPayment_DB",

"interaction_code":"BS",

            "interaction_field":{

                "ID":"12345",

                "outputs":{

                        "confirmation_num":"000-921-4361",

                        "status":"success",

                        "payment_date":"20150203",

                }

            }

"comment":"",

"decision_label":"status = success",           

            "time":"20141209.07:46:32.832"           

        },

 

Note, backend return values should not contain colon ":" or double quote chars.

### 4.2.3      Format for Decision State Outputs

The decision state outputs can optionally be supplied via labels indicating the outcome. 

 

Example of decision state event (where a payment amount exceeds the minimum due condition):

 

        {

            "dialog_state":"AA00400_MinimumDueCheck_DS",

"interaction_code":"DS",

            "interaction_field":""

"comment":"",

"decision_label":"payment_amount >= minimum_due",           

            "time":"20141209.07:46:32.832"           

        },

 

Note, decision state labels should not contain double quotes or colons ":".

### 4.2.4      Format for Subroutine Return State Outputs

The subroutine state inputs and outputs can optionally be supplied via key/value pairs within the _interaction_filed_.

 

Example of decision state event:

 

        {

            "dialog_state":"AA00600_Authentication_SD",

            "interaction_code":"SD",

            "interaction_field":{

                "uri":"<http://blah.com/blah>"

                "inputs":{

                    "ani":"3456751123",

                    "caller_type":"consumer",

                }

            }

            "comment":"",

"decision_label":"",

            "time":"20141209.07:46:32.832",

        },

       

       {

            "dialog_state":"AA00600_Authentication_SD",

            "interaction_code":"SR",

            "interaction_field":{

                "outputs":{

                    "authenticated":"true",

                    "account_number":"****",

                }

            }

            "comment":"",

"decision_label":"authenticated = true",

            "time":"20141209.07:46:32.832",

        },

 

Note, decision state events should not contain colon ":" or double quote chars.

 

### 4.2.5      DM Entries and the Grammar Set Format

The grammar set is specified by a comma delimited list of grammar URIs, including any query params, upon entering a dialog module (DM).

 

Example of a dialog state entry event for a state with a dynamic grammar set:

 

        {

            "dialog_state":"AA00100_MainMenu_DM",

            "interaction_code":"S",

            "interaction_field":{

"grammars":[

                                    "http:\\\some_server\grammars\en-us\AA00100_MainMenu_DM.grxml?state=IL",

                                    "http:\\\some_server\grammars\en-us\AA00100_MainMenu_DM_dtmf.grxml",

                                    "http:\\\some_server\grammars\en-us\AA00000_GlobalCommands.grxml"

                        ]

            }

"comment":"",

"decision_label":"",

"time":"20141209.07:46:32.832"

        },

 

### 4.2.6      DM Exit Format

Dialog Module results should be logged in the following format:

  * **statusCode** : exit overall status for the DM execution, possible values are: SUCCESS, SYSTEM_ERROR, HANGUP, MAX_MENU_VISITS, GLOBAL_COMMAND, MAX_REPEATS, NOMATCH, MAX_NOMATCHES, NOINPUT, MAX_NOINPUTS, MAX_DISCONFIRMS.
  * **mode:** Input mode must have a value of 'dtmf' or 'voice'. 
  * **confidence:** The confidence score must be reported within the range of 0-1 with two significant digits (e.g. "0.55")
  * **literal:** the literal field must contain the text of the recognized utterance or dtmf input returned by the recognizer.   For masked DMs, the value should  be "****".
  * **result:** an array object containing key/value pairs of slot name and slot value returned by the recognizer.
  * **dialog_state_error_counter:** counter of the DM iterations.
  *  



 

Examples of a recognition result event for a dialog state:

 

    {

            "interaction_code": "ED",

            "dialog_state": "ILBP00040_ILBillingAndPaymentsMenu_DM",

            "decision_label": "make_payment",

            "time": "20160127.22:11:37.711",

            "statusCode": "SUCCESS",

            "interaction_field": {

                    "input_mode ": "dtmf",

                    "confidence ": "1",

                    "literal ": "2",

                    "result ": "make_payment ",

                    "dialog_state_error_counter": "1",

                    "confirmation_error_counter": "0",

                    "disconfirmation_counter": "0",

                    "repeat_counter": "0",

                    "no_input_counter": "0",

                    "no_match_counter ": "0",

                    "confirmation_mode ": "",

                    "confirmation_confidence ": "",

                    "confirmation_literal ": "",

                    "confirmation_result ": ""

      }

    },

### 4.2.7      Sample Exit (operator request)

see sample, above.  Note, for some applications, you may have CSR transfer states occuring prior to all transfers.  It is not always desirable to track these as the final state.  Code should allow the option to skip such states when setting the "last_state" field for the call.

 

        {

            "dialog_state":"AA00100_MainMenu_DM",

            "interaction_code":"S",

            "interaction_field":{

"grammars":[

                                    "http:\\\some_server\grammars\en-us\AA00100_MainMenu_DM.grxml",

                                    "http:\\\some_server\grammars\en-us\AA00100_MainMenu_DM_dtmf.grxml",

                                    "http:\\\some_server\grammars\en-us\AA00000_GlobalCommands.grxml"

                        ]

            }

"comment":"",

"decision_label":"",

"time":"20141209.07:46:32.832"

        },

        {

            "dialog_state":"AA00100_MainMenu_DM",

"interaction_code":"P",

            "interaction_field":{

                        "prompts":[

"http:\\\some_server\prompts\en-us\AA00100_MainMenu_DM_I_01.wav"

]

            }

"comment":"",

"decision_label":"",           

            "time":"20141209.07:46:32.832"           

        },

 

        {

            "dialog_state":"AA00100_MainMenu_DM",

"interaction_code":"R",

            "interaction_field":{

                        "mode":"dtmf",

                        "confidence":"1.00",

                        "result":"0",

                        "slots":{

                                    "out":"operator"

                        }

            }

"comment":"",

"decision_label":"",           

            "time":"20141209.07:46:32.832"           

        },

        {

            "dialog_state":"AA00100_MainMenu_DM",

"interaction_code":"MO",

            "interaction_field":"", 

"comment":"",

"decision_label":"",           

            "time":"20141209.07:46:32.832"           

        },

        {

            "dialog_state":"AA00100_MainMenu_DM",

"interaction_code":"XC",

            "interaction_field":"", 

"comment":"",

"decision_label":"",           

            "time":"20141209.07:46:32.832"           

        },

        {

            "interaction_code": "ED",

            "dialog_state": "AA00100_MainMenu_DM",

            "decision_label": "operator",

            "time": "20160127.22:11:37.711",

            "statusCode": "GLOBAL_COMMAND",

            "interaction_field": {

                    "input_mode ": "dtmf",

                    "confidence ": "1",

                    "literal ": "0",

                    "result ": "operator",

                    "dialog_state_error_counter": "1",

                    "confirmation_error_counter": "0",

                    "disconfirmation_counter": "0",

                    "repeat_counter": "0",

                    "no_input_counter": "0",

                    "no_match_counter ": "0",

                    "confirmation_mode ": "",

                    "confirmation_confidence ": "",

                    "confirmation_literal ": "",

                    "confirmation_result ": ""

          }

        },

### 4.2.8      Sample Exit (Business Rule Transfer)

       

       {

            "dialog_state":"AA02000_DelinquentCheck_BC",

"interaction_code":"DS",

            "interaction_field":"",

"comment":"",

"decision_label":"delinquentCaller = TRUE",           

            "time":"20141209.07:46:32.832"           

        },

       {

            "dialog_state":"AA10000_CSRTransfer_BC",

"interaction_code":"DS",

            "interaction_field":"",

"comment":"",

"decision_label":"",           

            "time":"20141209.07:46:32.832"           

        },

 

        {

            "dialog_state":"AA10000_CSRTransfer_BC",

"interaction_code":"XC",

            "interaction_field":"", 

"comment":"",

"decision_label":"delinquentCaller = TRUE",           

            "time":"20141209.07:46:32.832"           

        },

 

### 4.2.9      Sample Exit (Max Rejects)

 

        {

            "dialog_state":"AA00100_MainMenu_DM",

            "interaction_code":"S",

            "interaction_field":{

"grammars":[

                                    "http:\\\some_server\grammars\en-us\AA00100_MainMenu_DM.grxml",

                                    "http:\\\some_server\grammars\en-us\AA00100_MainMenu_DM_dtmf.grxml",

                                    "http:\\\some_server\grammars\en-us\AA00000_GlobalCommands.grxml"

                        ]

            }

"comment":"",

"decision_label":"",

"time":"20141209.07:46:32.832"

        },

 

        {

            "dialog_state":"AA00100_MainMenu_DM",

"interaction_code":"P",

            "interaction_field":{

                        "prompts":[

"http:\\\some_server\prompts\en-us\AA00100_MainMenu_DM_I_01.wav"

]

            }

"comment":"",

"decision_label":"",           

            "time":"20141209.07:46:32.832"           

        },

 

        {

            "dialog_state":"AA00100_MainMenu_DM",

"interaction_code":"N",

            "interaction_field":{}

"comment":"",

"decision_label":"",           

            "time":"20141209.07:46:32.832"           

        },

        {

            "dialog_state":"AA00100_MainMenu_DM",

"interaction_code":"N",

            "interaction_field":{}

"comment":"",

"decision_label":"",           

            "time":"20141209.07:46:32.832"           

        },

        {

            "dialog_state":"AA00100_MainMenu_DM",

"interaction_code":"ME",

            "interaction_field":"", 

"comment":"",

"decision_label":"",           

            "time":"20141209.07:46:32.832"           

        },

        {

            "interaction_code": "ED",

            "dialog_state": "AA00100_MainMenu_DM",

            "decision_label": "maxNoMatches",

            "time": "20160127.22:11:37.711",

            "statusCode": "MAX_NOMATCHES",

            "interaction_field": {

                    "input_mode ": "",

                    "confidence ": "",

                    "literal ": "",

                    "result ": "",

                    "dialog_state_error_counter": "3",

                    "confirmation_error_counter": "0",

                    "disconfirmation_counter": "0",

                    "repeat_counter": "0",

                    "no_input_counter": "0",

                    "no_match_counter ": "0",

                    "confirmation_mode ": "",

                    "confirmation_confidence ": "",

                    "confirmation_literal ": "",

                    "confirmation_result ": ""

          }

        },

 

### 4.2.10  Sample Exit (Max Timeouts)

        {

            "dialog_state":"AA00100_MainMenu_DM",

            "interaction_code":"S",

            "interaction_field":{

"grammars":[

                                    "http:\\\some_server\grammars\en-us\AA00100_MainMenu_DM.grxml",

                                    "http:\\\some_server\grammars\en-us\AA00100_MainMenu_DM_dtmf.grxml",

                                    "http:\\\some_server\grammars\en-us\AA00000_GlobalCommands.grxml"

                        ]

            }

"comment":"",

"decision_label":"",

"time":"20141209.07:46:32.832"

        },

 

        {

            "dialog_state":"AA00100_MainMenu_DM",

"interaction_code":"P",

            "interaction_field":{

                        "prompts":[

"http:\\\some_server\prompts\en-us\AA00100_MainMenu_DM_I_01.wav"

]

            }

"comment":"",

"decision_label":"",           

            "time":"20141209.07:46:32.832"           

        },

 

        {

            "dialog_state":"AA00100_MainMenu_DM",

"interaction_code":"T",

            "interaction_field":{}

"comment":"",

"decision_label":"",           

            "time":"20141209.07:46:32.832"           

        },

        {

            "dialog_state":"AA00100_MainMenu_DM",

"interaction_code":"T",

            "interaction_field":{}

"comment":"",

"decision_label":"",           

            "time":"20141209.07:46:32.832"           

        },

        {

            "dialog_state":"AA00100_MainMenu_DM",

"interaction_code":"MT",

            "interaction_field":"", 

"comment":"",

"decision_label":"",           

            "time":"20141209.07:46:32.832"           

        }

        {

            "dialog_state":"AA00100_MainMenu_DM",

"interaction_code":"XC",

            "interaction_field":"", 

"comment":"",

"decision_label":"",           

            "time":"20141209.07:46:32.832"           

        }

        {

            "interaction_code": "ED",

            "dialog_state": "AA00100_MainMenu_DM",

            "decision_label": "maxNoInputs",

            "time": "20160127.22:11:37.711",

            "statusCode": "MAX_NOINPUTS",

            "interaction_field": {

                    "input_mode ": "",

                    "confidence ": "",

                    "literal ": "",

                    "result ": "",

                    "dialog_state_error_counter": "2",

                    "confirmation_error_counter": "0",

                    "disconfirmation_counter": "0",

                    "repeat_counter": "0",

                    "no_input_counter": "0",

                    "no_match_counter ": "0",

                    "confirmation_mode ": "",

                    "confirmation_confidence ": "",

                    "confirmation_literal ": "",

                    "confirmation_result ": ""

          }

        },

 

 

## 4.3        Overall Sequencing Information

With Interaction logging, it is critical to keep event sequencing in proper order.  For example, when entering a recognition state (Dialog Module), the state entry event "S" should appear first in the log, followed by the prompt play, recognition, or error events belonging to that state.   Furthermore, no event from a following state or DM should appear prior to the completion of the current state.  The P, R, and error related events should only appear following the associated DM's entry and prior to entry into the next state.  For example,

 

        {

            "dialog_state":"AA00100_MainMenu_DM",

            "interaction_code":"S",

            "interaction_field":{

"grammars":[

                                    "http:\\\some_server\grammars\en-us\AA00100_MainMenu_DM.grxml?state=IL",

                                    "http:\\\some_server\grammars\en-us\AA00100_MainMenu_DM_dtmf.grxml",

                                    "http:\\\some_server\grammars\en-us\AA00000_GlobalCommands.grxml"

                        ]

            }

"comment":"",

"decision_label":"",

"time":"20141209.07:46:32.832"

        },

 

        {

            "dialog_state":"AA00100_MainMenu_DM",

"interaction_code":"P",

            "interaction_field":{

                        "prompts":[

"http:\\\some_server\prompts\en-us\AA00100_MainMenu_DM_I_01.wav"

]

            }

"comment":"",

"decision_label":"",           

            "time":"20141209.07:46:32.832"           

        },

 

        {

            "dialog_state":"AA00100_MainMenu_DM",

"interaction_code":"R",

            "interaction_field":{

                        "mode":"dtmf",

                        "confidence":"1.00",

                        "result":"3",

                        "slots":{

                                    "out":"pay_bill"

                        }

            }

"comment":"",

"decision_label":"",           

            "time":"20141209.07:46:32.832"           

        },

        {

            "interaction_code": "ED",

            "dialog_state": "AA00100_MainMenu_DM",

            "decision_label": "pay_bill",

            "time": "20160127.22:11:37.711",

            "statusCode": "SUCCESS",

            "interaction_field": {

                    "input_mode ": "dtmf",

                    "confidence ": "1",

                    "literal ": "3",

                    "result ": "pay_bill",

                    "dialog_state_error_counter": "1",

                    "confirmation_error_counter": "0",

                    "disconfirmation_counter": "0",

                    "repeat_counter": "0",

                    "no_input_counter": "0",

                    "no_match_counter ": "0",

                    "confirmation_mode ": "",

                    "confirmation_confidence ": "",

                    "confirmation_literal ": "",

                    "confirmation_result ": ""

          }

        },

 

** **

Lastly, each call's Interaction string should end with one of the following four allowed termination events: XA, XH, XT, or XC (see example in Sec 4.4).

 

 

 

## 4.4        Sample JSON Log Entry:

 

{

  "Call": {

     "call_id": "11111111111",

     "site_id": "localhost",

     "customer_name": "Ameren",

     "application_name": "AILRES",

     "ani": "1234567890",

     "dnis": "54321",

     "app_server_url": "somehost",

     "caller_type": "Res",

     "call_start_time": "20150305.14:52:49.605",

     "call_end_time": "20150305.14:52:49.606",

     "call_duration": "0.0",

     "call_exit_type": "transfer",

     "call_exit_reason": "AgentRequestTransfer",

     "call_self_served": "false",

     "call_authenticated": "false",

     "call_last_state": "AU02000_SomeState_DM",

     "call_audio_file": "none.wav",

     "call_custom_start": "test start",

     "call_custom_end": "",

      "call_custom_1": "",

      "call_custom_2": "",

      "call_custom_3": "",

      "call_custom_4": "",

      "call_custom_5 ": "",

       "call_event_trace": [

       "item1",

       "item2"

     ]

  },

  "Tasks": [

    {

      "TaskStart": {

        "task_name": "MainMenu",

        "task_start_time": "20141209.07:46:32.832",

        "task_active_list": [],

        "task_entry_count": "1",

        "task_custom_start": ""

      }

    },

    {

      "TaskEnd": {

        "task_name": "MainMenu",

        "task_end_time": "20141209.07:46:40.529",

        "task_duration": "7.4",

        "task_success": "true",

        "task_exit_reason": "TaskCompleted",

        "task_last_state": "AIL0000",

        "task_custom_end": "",

        "task_event_trace": []

      }
    
    
        }
    
    
      ],

  "Interactions":[

        {

            "dialog_state":"AA00010_Welcome_PP",

"interaction_code":"P",

            "interaction_field":{

                        "prompts":[

"http:\\\some_server\prompts\en-us\AA00010_Welcome_PP_01.wav"

]

            }

"comment":"",

"decision_label":"",           

            "time":"20141209.07:46:32.832"           

        },

 

        {

            "dialog_state":"AA00050_LanguageSelection_DM",

            "interaction_code":"S",

            "interaction_field":{

"grammars":[

                           "http:\\\some_server\grammars\en-us\AA00050_LanguageSelection_DM.grxml",

                           "http:\\\some_server\grammars\en-us\AA00050_LanguageSelection_DM_dtmf.grxml",

                        ]

            }

"comment":"",

"decision_label":"",

"time":"20141209.07:46:32.832"

        },

 

        {

            "dialog_state":"AA00050_LanguageSelection_DM",

"interaction_code":"P",

            "interaction_field":{

                        "prompts":[

"http:\\\some_server\prompts\en-us\AA00050_LanguageSelection_DM_I_01.wav"

]

            }

"comment":"",

"decision_label":"",           

            "time":"20141209.07:46:32.832"           

        },

 

        {

            "dialog_state":"AA00050_LanguageSelection_DM",

"interaction_code":"T",

            "interaction_field":"", 

"comment":"",

"decision_label":"english selected",           

            "time":"20141209.07:46:32.832"           

        },

        {

            "dialog_state":"AA00100_MainMenu_DM",

            "interaction_code":"S",

            "interaction_field":{

"grammars":[

                                    "http:\\\some_server\grammars\en-us\AA00100_MainMenu_DM.grxml",

                                    "http:\\\some_server\grammars\en-us\AA00100_MainMenu_DM_dtmf.grxml",

                                    "http:\\\some_server\grammars\en-us\AA00000_GlobalCommands.grxml"

                        ]

            }

"comment":"",

"decision_label":"",

"time":"20141209.07:46:32.832"

        },

 

        {

            "dialog_state":"AA00100_MainMenu_DM",

"interaction_code":"P",

            "interaction_field":{

                        "prompts":[

"http:\\\some_server\prompts\en-us\AA00100_MainMenu_DM_I_01.wav"

]

            }

"comment":"",

"decision_label":"",           

            "time":"20141209.07:46:32.832"           

        },

 

        {

            "dialog_state":"AA00100_MainMenu_DM",

"interaction_code":"R",

            "interaction_field":{

                        "mode":"dtmf",

                        "confidence":"1.00",

                        "result":"0",

                        "slots":{

                                    "out":"operator"

                        }

            }

"comment":"",

"decision_label":"",           

            "time":"20141209.07:46:32.832"           

        },

        {

            "dialog_state":"AA00100_MainMenu_DM",

"interaction_code":"MO",

            "interaction_field":"", 

"comment":"",

"decision_label":"",           

            "time":"20141209.07:46:32.832"           

        },

        {

            "interaction_code": "ED",

            "dialog_state": "AA00100_MainMenu_DM",

            "decision_label": "operator",

            "time": "20160127.22:11:37.711",

            "statusCode": "GLOBAL_COMMAND",

            "interaction_field": {

                    "input_mode ": "dtmf",

                    "confidence ": "1",

                    "literal ": "0",

                    "result ": "operator",

                    "dialog_state_error_counter": "1",

                    "confirmation_error_counter": "0",

                    "disconfirmation_counter": "0",

                    "repeat_counter": "0",

                    "no_input_counter": "0",

                    "no_match_counter ": "0",

                    "confirmation_mode ": "",

                    "confirmation_confidence ": "",

                    "confirmation_literal ": "",

                    "confirmation_result ": ""

         }

       },

       {

            "dialog_state":"AA10000_CSRTransfer_BC",

"interaction_code":"DS",

            "interaction_field":"",

"comment":"",

"decision_label":"",           

            "time":"20141209.07:46:32.832"           

        },

        {

            "dialog_state":"AA10000_CSRTransfer_BC",

"interaction_code":"XC",

            "interaction_field":"", 

"comment":"",

"decision_label":"",           

            "time":"20141209.07:46:32.832"           

        }

 

]

 

 

 

 
