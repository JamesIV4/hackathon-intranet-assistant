This article describes how to get [Nuance's VocalPassword](http://www.nuance.com/for-business/customer-service-solutions/voice-biometrics/vocalpassword/index.htm) to work with CIC.  Vocal Password is a product that allows customer's to perform voiceprint verification with voice applications such as an IVR or mobile application.  Voiceprint authentication is getting more popular with customers as they seek to improve the security of their applications but do so with less hassle to their users by simply allowing them to use their voice as their password.  This article focuses on using VocalPassword in IVR applications for CIC written in VoiceXML.

# Step-by-step guide

## 1. Install VocalPassword

Start by installing VocalPassword on server.  For testing purposes I installed VocalPassword on my VoiceXML server which may not be the recommended deployment for a production environment.  To install VocalPassword follow the install guide which can be found here: . The install guide is very thorough but here are a few items to keep in mind as you run through it:

### a. Make sure to install all prerequisites before installing VocalPassword

There is an extensive list of prerequisite steps listed in the install guide even before the VocalPassword install is run. Make sure these steps are followed or the install will not complete successfully.  Also make sure you have licenses ready as the install will ask for it.

### b. Nuance Recognizer is optional

Note that Nuance Recognizer is not required for use with VocalPassword. It is required if text validation is needed. Text validation is used for instances where VocalPassword needs to authenticate not only a user's voice, but a pass-phrase as well.  Text validation is optional when calling VocalPassword's verification APIs.

### c. After the install make sure VocalPassword's Quick Test application runs successfully

A QuickTest application will be available in the VocalPassword folder after install.  Run this application and make sure it passes all test as this will save a lot integration issues when developing the application.

### d. Change authentication of VocalPassword web application

CIC's VoiceXML interpreter does not support any form of authentication when calling into a web service. It is important that anonymous authentication is configured for the VocalPassword web application in order for it to work correctly with VoiceXML.  To do this select VocalPassword application under the default web site in IIS Manager.  Double click on Authentication under IIS.  Make sure Anonymous Authentication is enabled and configured with a user - edit the credentials as needed to select a user.

## 2\. Develop a VoiceXML Application that uses VocalPassword

A typical VocalPassword application goes through an enrollment stage and a verification stage.  The enrollment stage is where a user trains the system to recognize their voice. The usually involves having the customer call in an recite a few pass-phrases a few times.  The verification stage is where the same customer calls in and the system will authenticate their voice based on the samples collected during the enrollment stage. There are a few sample VoiceXML files that is installed as part of VocalPassword which can be used as a starting point for developing the application. This files are typically found under \program files\Nuance VocalPassword\SDK\VocalPasswordSamples.zip:

 

The sample VXML and javascript files will not work right out of the box. There are modifications that have to be made for it to be compatible with the CIC VoiceXML interpreter

The rest of the instructions will describe the application as laid out in the sample VoiceXML application and go over any caveats getting it to work.

### Starting a Session

Before starting enrollment or verification a new session has to be created. In order to do so the _**StartSession** _API has to be called passing it a configuration set name and an external session ID. A session Id get's returned as part of the API call that can be used for subsequent API calls. The following is an example of how the _**StartSession** _is called in a subdialog using the <data> element:

StartSession.xmlFadeToGreytruexmltrue

### Ending a Session

After enrollment or verification a session can be torn down using the _**EndSession** _API call. The following is an example of how the _**EndSession**  _is called in a subdialog using the <data> element. Note that the API does not return anything so it does not need a name:

EndSession.xmlFadeToGreytruexmltrue

### Enrolling a Speaker

Enrollment collects samples of a user's voice and uses them to train a voiceprint for the user.  Enrollment is done using _**Enroll** _API call which takes the following parameters:

Param| Description  
---|---  
sessionId| Session identifier returned by the _**StartSession**_ API  
separkerId| Identifier of the speaker. If this is a new identifier the system will automatically create an entry for the user.  
voiceprintTag| Identifies the sepaker's voiceprint. If the tag is new a new voiceprint is created during training. If the tag already exists, the system adapts the voiceprint template during training.  
audio| One of the following depending on how audio is fed to the system:

  * filename
  * Base64 buffer of audio
  * Audio segment ID (used in the example below)
  * URL referring to location of audio

  
text| Optional text used for text validation  
configSetName| Name of configuration set  
  
As the API indicates there are several ways to get the speaker's audio into VocalPassword for training.  With CIC VoiceXML the preferred methods are the use Base64 buffer or upload the audio using the _**UploadAudioFile**_   API and then specifying the audio segment ID returned from the call as the audio parameter of _**Enroll**_.  The _**Enroll**_ API may have to be called a few times depending on whether the system has enough audio to create a reliable voiceprint for the speaker.  Once complete the speaker can now be authenticated in future sessions. The following example illustrates how to use the _**UploadAudioFile** _and _**Enroll** _API in VoiceXML:

Enroll.xmlFadeToGreytruexmltrue

Note that this example does not take advantage of any text verification. To make the enrollment more secure the speakers should be prompted for a passphrase that is recognized and matched against a shared secret for that speaker.

### Verifying a Speaker

Verification collects samples of a user's voice and uses them to authenticate or identify a user based on their previously trained voiceprint. Verification is done using **_Verify  _**API call which takes the following parameters:

Param| Description  
---|---  
sessionId| Session identifier returned by the _**StartSession**_ API  
separkerId| Identifier of the speaker. If the user is not found a error will be returned.  
voiceprintTag| Identifies the speaker's voiceprint to authenticate against.  
audio| One of the following depending on how audio is fed to the system:

  * filename
  * Base64 buffer of audio
  * Audio segment ID (used in the example below)
  * URL referring to location of audio

  
text| Optional text used for text validation  
configSetName| Name of configuration set  
  
Verification supports the same means to upload an audio file.  The following example illustrates how to use the _**UploadAudioFile**  _and **_Verify  _**API in VoiceXML: 

Verify.xmlFadeToGreytruexmltrue

# Related articles

<http://www.nuance.com/for-business/customer-service-solutions/voice-biometrics/vocalpassword/index.htm>

 
