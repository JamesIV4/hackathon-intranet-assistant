# Security Practices

This page captures the basic security measures to be taken in order to mask sensitive data within a CIC deployment.

## CIC Log Masking

The CIC provides the com.inin.securedata parameter to allow masking of the CIC/Media Server/VoiceXML logs and recordings.  The parameter is settable within the VXML code and is set to empty by default.  To turn masking on, set the parameter value to "mask".  For more information, see .

## Nuance ASR Log Masking

In order to mask sensitive data within Nuance ASR logs, set the following parameters within a given recognition's associated GRXML:

## KPI Logs (callpath)

 Here is an example of logs:-

JSON SnippetJSON Fulltrue

## Detailed Dialog Design (3D)

### Implementing the masking within the 3D

By default the masking will be set to false for ALL input and output fields defined within a Database Module. To set it differently one must define the following parameters within the Developer Notes section. Each value **MUST** be delimited using a semi-colon or it will not be captured properly during code generation. This is because the <params> block is delimited using a comma. Also, the true / false values are NOT case sensitive but lower case is preferred. As with all parameters they must be defined within a <params></params> block and be delimited by a comma. 

## Interaction Administrator Changes

To use the Secure Data parameter within CIC the following items or configurations must be in place.

  * Secure Input License within the CIC License  

  * Secure Input must be enabled within the Telephony Parameters found in Server Configuration.  

  * If it is NOT enabled the following error message will be found in the VoiceXMLServer log  


TSAPI::SecureSessionBegin : TSAPI::SecureSessionBegin returned an error:   
ErrorCode: error.tsserver.internalError  
Description: Call <1001470722> **attempted secure input operation. Secure Input is licensed but NOT enabled**. rejected.  
vxisvc::VXIRecognitionImpl::Recognize : SecureSessionBegin() tErr=eTsError=0xf0(Internal Error) RecoImplTopic




## Logging.js :-

Latest Code: //speechsolutions/main_team_4q15/pub/resources/javascript/Logging.js  


 The code changes in js modified the below fucntions with adding secureData as parameter. The values of secureData within our properties file can be mask, encrypt, or none. These values will cause the following to happen within the dialog_state.jsp

Then the vxml generator will set the following right before the last line of the dialog module to reset those values as follows;

 

### LogRecognition

For Example :-

For the below function calls I have passed in an extra parameter maskArray which should have the same number of values that we pass to the DB calls.

### LogComplex :-

This function will validate the input names with maskArray values which needs to be masked.

The following functions call LogComplex with the appropriate additional parameters as necessary based upon the calling function, i.e. logBackEndFailure passes in 'BF' as the value for the 'code' parameter.

  * LogBackEndInitiate
  * LogBackEndFailure
  * LogBackEndSuccess



 For Example :-

### Vxml DB Call :-

Here is an example of how we log backend initiate:-

### Dialog_state.vxml ;-

We use this file to get the param value passed from vxml DM like secureData and we pass this value in LogRecognition function to get the literal value to be masked.

For Example :-

 

**  
**

 

  

