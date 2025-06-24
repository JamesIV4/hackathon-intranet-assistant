# Single Party Recording support in Media Server  
  
## Overview (from [MediaServerVoicemailSupport](http://perforce:8080/depot/systest/EIC/main/products/eic/resources/mediaserver/docs/MediaServerVoicemailSupport.doc))

Phase 4 of the Media Server includes using the Media Server for single party (i.e. voicemail) recordings. Single party recordings have traditionally been done using voice resources on HMP. As part of the initiative to eliminate HMP and to support prompt plays on the Media Server, single party recordings will now be offloaded to Media Server.

## Major Features and Requirements

  * Use Media Server for single party recordings.
  * Support on-demand fetching of recordings from the Media Server using HTTP/HTTPS.
  * Support  record and timing properties.
  * Support different audio formats for the recording (Will allow bypassing compression on the IC server).
  * Support media features: Silence suppression, Automatic Level Control, Noise Reduction, Emotion detection.



## Design

  * [Media Server Single Party Recording Support](http://perforce:8080/depot/systest/EIC/main/products/eic/resources/mediaserver/docs/MediaServerVoicemailSupport.doc)



## Schedule

Feature  |  Component  |  Updated  |  SCR  |  % Complete  |  Days  |  Start Date  |  Finish Date  |  Developer   
---|---|---|---|---|---|---|---|---  
HTTP/HTTPS recording retrieval  |  Media Server  |   |  65124 |  100  |  5  |  1/1/09  |  1/16/09  |  Rod Francisco   
New RecordSingleParty API  |  TS API  |   |   |  100  |  2  |  1/1/09  |  1/16/09  |  Rod Francisco   
New Notifier Message API  |  TS API  |   |   |  100  |  2  |  1/1/09  |  1/16/09  |  Rod Francisco   
TS Server Changes  |  TS Server  |   |   |  100   
|  10  |  3/1/09  |    
|  Bogdan Munteanu   
Modify Audio Source resource  |  Media Server  |   |   |  100   
|  4  |  3/16/09  |    
|  Felix Wyss   
Modify Record tools  |  Telephony and Record tools  |   |  67154 |  100  |  3  |  1/1/09  |  2/22/09  |  Rod Francisco   
New Record tools  |  Telephony and Record tools  |   |  68748 |  100  |  5  |    
|    
|    
IC server installer changes  |  IC install  |   |   |  0  |  3  |    
|    
|    
Media server installer changes  |  Media Server install  |   |   |  0  |  3  |    
|  4/1/09  |    
HTTP client/CWorkfile changes  |  Tools  |   |   |  100  |  3  |  1/1/09  |  1/16/09  |  Rod Francisco   
Post Office Server changes  |  Post Office Server  |   |  68941 69264 |   |   |   |   |  Troy Tricker   
VoiceMail handler changes  |  Handlers  |   |  69215 |   |   |   |   |  Mark Mellencamp   
VoiceXML changes  |  VoiceXML Server  |   |  69225 |   |   |   |   |  Bill Baird   
Interaction Admin  |  IA  |   |  70051 |   |   |   |   |    
Documentation  |  All  |   |   |  0  |  5  |    
|    
|    
  |   |   |   |   |   |   |   |    
Overall  |   |   |  64607 |  75  |    
|    
|  4/1/09  |    
  
## Design Considerations

Several components/subsystems in IC may have to change to accommodate the new Single Party record functionality in the media server. This section will document which components are being researched and any changes that may have to be done to it.

### TS API Changes

A new TSAPI call has been added for Single Party Recordings. The new API is a port from the current API. It has been improved with the following features:

  * , , and  have each been encapsulated in its own class. This will allow extensibility for future changes to the API.
  * The ION serializer is used for sending the request to . This will allow for forward and backward compatibility for new versions of this API call.
  * New Single Party recording parameters have been added for MIME types, Automatic Level Control and Noise Reduction.
  * For Media Server recordings an HTTP URI will be returned with the results that can be used to access that recording on the Media Server.



The new API call is as follows:

### IP and Tool Changes

#### Record Audio

The Record Audio tool will be changed to used the new TSAPI:: API. This change includes being able to download the file from the Media Server if an HTTP URI is being returned for the recording URI. To help with this the  class in iputility will be modified to allow for downloading contents from an HTTP resource.

##### Migration to New Version

The Record Audio tool will be migrated to a 3.0 version with the following new fields:

  * **Final Silence (seconds)** : The number of silence at the end of an utterance that will terminate the recording. Default is 10s.
  * **Mime Type** (Media Server only): The audio format to record the audio to. Default is empty which defaults to the format specified on the media server.
  * **Automatic Level Control** (Media Server only): Whether ALC should be applied to the audio. Default is false.

  
|    
  
---|---  
  
**NOTES:**

  * Silence suppression (silence compression in the tool) is supported by the Media Server and defaults to 2s.
  * A final silence of 0 means that the IA system line setting for voicemail silence detection is used.
  * A final silence < 0 means that it is disabled.



#### Record File

The Record File tool is similar to the Record Audio tool but allows the user to specify a wave file to record to. The wave file can be an existing file or one that will be created. The tool also allows a user to specify whether an existing file should be overwritten or simply appended to. When appending to an existing file the user can specify a tone to append between recordings. The primary user of appending to existing files and inserting a tone are handlers that forward a voicemail and allow users to attach a recording comment to the original voicemail.

##### Migration to New Version

The Record File tool will be migrated to a 3.0 version with the following new fields:

  * **Final Silence (seconds)** : The number of silence at the end of an utterance that will terminate the recording. Default is 10s.
  * **Mime Type** (Media Server only): The audio format to record the audio to. Default is empty which defaults to the format specified on the media server.
  * **Automatic Level Control** (Media Server only): Whether ALC should be applied to the audio. Default is false.

  
|    
  
---|---  
  
**NOTES:**

  * It was determined that forwarding voicemail messages (!TUIForwardMessage) **DOES NOT** use the append features of Record File. Instead it uses the Forward Voicemail tool and pass it the original email (with voicemail attachment) and the recording id of newly recorded comment to append. Forward Voicemail will send the request to 



server which does the concatenation of recording but **DOES NOT** append a tone. Look at Forward Voicemail tool description below for more details.

  * MIC forwards voicemails the same way CIC does.
  * Append to an existing file will be supported and inserting a tone when appending **will** be supported but only in the Record File toolstep. It will not be supported in the TSAPI:: method.



#### File To Recording

File to recording is used to synthesize a recording object from a file. The recording id of the object is what is passed to various tool steps for processing. This tool has to be changed to support HTTP URIs for recordings created on the Media Server. File To Recording also uses the 

and will use it to download from a HTTP source.

#### Work File

The CWorkFile class is a iputility class that provides support for the creation of temporary files that can be shared between processes. One such example of this is use is for voicemail recordings that have to be shared between different subsystems. To support voicemail recordings created on the Media Server 

has to support downloading it's contents from an HTTP source. To support this a new !CopyFrom() method will be added to the 

class.

A new field will also be added CWorkFile to indicate its source. This source field will allow applications to indicate what had originally create the file. In the case of a media server recording the applications will mark the recording source as "mediaserver". This will allow applications processing recordings from the Media Server different from recordings made on the IC server.

**NOTES:**

  * A new property has been added to  to indicated the source of the file. This is used to optimized recordings created by the Media Server. Since recordings done on the Media Server are already transcoded there is not need to do a post op compression on it (as Post Office server does for voicemail). To handle this recordings via the ] that have sources marked as "mediaserver" will indicate that was created by the media server and do not need to be re-compressed.



#### Send Voicemail

At the moment no changes are needed for the tool. It has to be determine whether the tool can be optimized to not do any compression (even if the compression is a no-op) if the Media Server has already transcoded the audio to the format required. The following diagram depicts how a voicemail is currently sent in IP:

**NOTES:**

  * Voicemail recordings are written into  so that the can be shared between processes. The  id is the recording handle that is passed around tools/processes. The id is a sequential id generated by Notifier.
  * If a voicemail is less than 2 seconds the .ihd handler will not send the voicemail (via the Send Voicemail tool). Since the voicemail is a  it will automatically be deleted if no process has incremented its reference count.
  * The Send Voicemail tool has a format attribute which can be used to specify what audio format to transcode the voicemail to before sending it. If this parameter is not filled  will use the formats specified in IA (System Configuration->Mail->Configuration->Prefixes and Voice Mail). In IA a user can specify a different (long and short) compression based on the length of the recording.



#### Forward Voicemail

At the moment no changes are needed for the tool. The tool allows users to forward a voicemail message to another user and optionally append another recording (usually a comment) to the original voicemail attachment. For documentation purposes the following depicts how a voicemail is forwarded with a comment in IP:

#### Play Recording

At the moment no changes are needed for the tool. It has to be determine whether a play can be optimized so that the recording does not have to be downloaded from the Media Server only to be played out again by the same Media Server.

#### Handlers

The following are a list of our stock handlers that use the tools mentioned above.

Record Audio:

  *   *   *   *   *   * 


Record File:

  * CSSurvey_
  *   *   * System_
  * System_
  *   *   *   * 


Send Voicemail:

  *   *   *   *   * 


Forward Message:

  *   * 


File To Recording:

  *   * 


Play Recording:

  *   *   *   *   * 


## Media Server Design Considerations

### Config File Changes

#### Network Config Changes

The following configurations have been added for HTTP Recording Retrieval support:

  * ****: Port that HTTP Recording Retrieval will listen on (default 8102).
  * ****: Network adapter to listen on.
  * ****: Number of concurrent HTTP requests (default 100).
  * ****: Thread priority of the HTTP Recording Retrieval proactor thread (default ' ')
  * ****: The authority format to use for recording URIs (default "FQDN"). Possible values: 
    * "FQDN": Use the fully qualified domain name.
    * "IPAddress": Use the IP address.
    * "": Use the machine name.
    * "Custom": Use a custom authority as specified in the  field.
  * ****: The authority to use if "Custom" is specified for .
  * ****: Security policy to use for accessing Recordings folder via HTTP. Possible values:
    * "Disabled": Do not allow access.
    * "": Only allow access via HTTPS.
    * "": Permit all access on any connection.
  * ****: Security policy to use for listing contents of the Recordings folder.
  * ****: Security policy to use for accessing Fax folder via HTTP.
  * ****: Security policy to use for listing contents of the Fax folder.
  * ****: Security policy to use for accessing Trace folder via HTTP.
  * ****: Security policy to use for listing contents of the Trace folder.



#### HTTP Recording Retrieval Folders

The config file had to be changed to accommodate http access to call recordings, voicemail recordings, and faxes. To support this a new  property has been added that will serve as the base local path to all resources. The upgrade process is as follows:

  1. Look for the  property. If it does not exist then an upgrade is needed.  
2\. Read the  location. Typically this is the recordings folder so navigate up one folder and set the new  to that folder.  
3\. Create the resource folders from the local base: 'recordings/call', 'recordings/voicemail', 'faxes'.  
4\. Get the recording retrieval server authority based on the configuration settings.  
5\. Set the  to the authority appended with "/recordings/call" path.  
6\. Set the  to the authority appended with "/recordings/voicemail" path.  
7\. Set the  to the authority appended with "/faxes" path.  
8\. Remove .



**NOTES:**

  * The  property will kept to temporarily support UNCs while the Media Server is being upgraded. The  property take higher precedence than the new . To start using HTTP access a user would simple have to delete the  or set it to 'http' on the IC server.
  * The  properties will be displayed in the web config as **read only** fields which cannot be modified.



## Voice Mail handler and Post Office Server Design Considerations

Voicemail in IC recorded by .ihd handler will take advantage of the new Media Server features (69215). This includes being able to set the mime type and ALC parameter in the Record Audio toolstep. For this the handler will read Email settings in IA (System Configuration->Mail->Configuration->Prefix and Voice Mail). It will use the "Long Message Compression" to indicate what mime type to use to the recording and the "Normalize Voice Mails" option to determine if ALC has to be enabled. Record Audio toolstep will automatically mark the source of the recording as coming from the Media Server.

When Post Office server gets a voicemail recording that it has to process it will check the source of that recording. If the recording was created by the Media Server it will **not** do a post op compression or normalization (via compression manager). This will decrease the processing time and load on the IC server.

NOTE: The "Short Message Compression" in the Mail Configurations in IA will not be used in a in an environment that uses the Media Server for voicemail recording (70051). Since recordings are done in real time it is difficult to switch codecs during a recording after a certain threshold.   

