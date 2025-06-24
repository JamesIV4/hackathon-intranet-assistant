# Media Streaming Server  
  
false

## Overview and Requirements

Originally called the "Voicemail Playback Server", the Media Streaming Server (MSS) is an MRCP server that will be capable of audio playback (audio files and voicemails) and speech synthesis. The current support for playing audio files and voicemail with the Media Server is somewhat inefficient because it requires that the audio file be accessible by the Prompt Server (on the IC server) and then fetched by the Media Server when played. With prompts this mechanism is fine because prompts don't change very often and can be cached on the Media Server. With voicemail this is undesirable because it requires that the voicemail be first downloaded from the mail server onto the IC server and then streamed via HTTP to the Media Server. Voicemails also don't benefit from being cached on the Media Server because they are transient and are usually only played a few times. MSS solves this problem by streaming voicemails to the media server on demand from a mail server.

MSS can also be used for playback of audio files that don't need to be cached on the media server and will eventually support TTS (speech synthesis). MSS, along with the Media Server, contributes to the overall goal of removing all audio processing and flow from the IC server.

**The following are proposed requirements for MSS:**  


Number  |  Description  |  Detail  |  *Priority   
---|---|---|---  
R1  |  Support MRCP v2 protocol  |  MSS will be an MRCP server access via SIP and MRCP  |  Must have   
R2  |  Support streaming voicemails  |  MSS will receive a voicemail moniker which it will use to access voicemail to stream via RTP  |  Must have   
R3  |  Support speech synthesis  |  MSS will support "speechsynth" resource and do TTS initially via SAPI  |  Should have   
R4  |  Allow config via a web interface  |  Similar to other server, MSS will have a web config front end  |  Must have   
  
*Priority Descriptions  


,,style="background:yellow; font-size:8pt;" Priority  |  Description   
---|---  
Must have  |  The initial release MUST have the feature.   
Should have  |  The initial release SHOULD have the feature but can defer it to the next iteration.   
Nice to have  |  The initial release MAY have the feature but its priority is low.   
Future revision  |  The initial release will NOT include the feature and will be evaluated in the future.   
  
## Design

Development:Media Streaming Server Design

## Breakdown

This project is broken down into a number of pieces as described in this section.

(**Bold** items are done.)

  * Media Streaming Library 
    * Communicating with xIC 
      * **Interface to i3sip stack**
        * **MssManage** class
        * **SipApiHostImpl** class
        * **SipConnection** class
        * **TransceiverHandler** class 
          * **INVITE** method
          * **ACK** method
          * **CANCEL** method
          * **OPTIONS** method
        * **SessionHandler** class 
          * **INVITE** method
          * **ACK** method
          * **CANCEL** method
          * **BYE** method
          * **OPTIONS** method
      * Interface to i3mrcp stack 
        * **MrcpManager** class
        * **MrcpSession** class
        * **MrcpHandler** class 
          * **SPEAK** method
          * **STOP** method
          * **SET-PARAMS** method
          * **GET-PARAMS** method
          * PAUSE method
          * RESUME method
          * **BARGE-IN-OCCURRED** method
          * **CONTROL** method
          * **SPEECH-MARKER** event
          * **SPEAK-COMPLETE** event
    * **Communicating with the mail server**
      * **MailServer** class
      * **MailFileResource** class
      * **MailFileResourceProvider** class
    * Communicating with the audio library 
      * **Player** class 
        * **control_current_play** command
        * **play** command
        * **stop** command
      * **VoicemailPlayer** class 
        * **control_current_play** command
        * **play** command
        * **stop** command
      * SpeechSynth class 
        * control_current_play command
        * play command
        * stop command
      * **ResourceNotifyHandler** class
      * **ServerNotifyHandler** class
      * **LibraryNotifyHandler** class


  * **Media Streaming Server**
    * **Web configuration pages**
      * **WebConfigPages_Parameters** class
      * **WebConfigPages_Audio** class
      * **WebConfigPages_Mail** class
      * **ConfigServer** class
      * **ConfigManager** class
    * **Server initialization**



(**Bold** items are done.)

Work on this project is currently proceeding in the "mediastreamingserver" team branch in Clay.

## Schedule

Feature (Plan)  |  Percent   
complete  |  SCR  |  Developer  |  Description   
---|---|---|---|---  
Project SCRs  |   |  DP-238, DP-275 |    
Design/Umbrella  |  100% |  IC-62447 |  |    
Media Streaming Server  |  100% |  IC-66971 |  |  Implement new Media Streaming Server   
Media Streaming Server  |  100% |  IC-89320 |  |  MSS web config enhancements   
Media Streaming Server  |  100% |  IC-89322 |  |  Support SIP Options   
Media Streaming Server  |  0% |  IC-89323 |  |  Add support for exchange web services connector.   
**Moved to future SU as it requires quite a bit of work**  
TS Server  |  100% |  IC-70141 |  |  Support using MSS for voicemail playback   
MRCP Subsystem  |  100% |  IC-70149 |  |  Support MSS server and "mediaplayer" resource   
MRCP Subsystem  |  100% |  IC-70300 |  |  Add support for selecting an MRCP server based on region   
Session Manager/Client  |  100% |  IC-70140 |  |  Pass voicemail moniker to TS when playing voicemails   
Handlers  |  100% |  IC-70128 |  |  Pass voicemail moniker to TS when playing voicemails   
Attendant  |  100% |  IC-90008 |  |  Support external audio source for Queue Audio plays   
Handlers  |  100% |  IC-90225 |  |  Add support for playing from an external audio sources in Queue Audio node in Attendant   
IA  |  100% |  IC-89195 |  |  Add media player resource in MRCP server configuration   
Install  |  100% |  IC-69891 |  |  Create an install for MSS   
  
## Configuration

The media streaming server will be configured like any other MRCP server in the MRCP container in IA. For an IC server to use a media streaming server it would have to be configured like any other MRCP server. The difference between the media streaming server and other MRCP servers we have supported in the past is that the MSS server will be able to support a couple new capabilities: External Audio Source and Voicemail. This will be configured in the Capabilities tab of the MRCP server configuration (previous called 'Supported Resources' tab):

newmrcpservernewmrcpserver1 mrcpserverconfigmrcpserverconfig2

**Capabilities**

  * **Text To Speech** : The MRCP server supports speech synthesis using various text to speech voices.
  * **External Audio Source** : The MRCP server supports playing from an external audio source such as line in or speakers. Only supported by the media streaming server.
  * **Voicemail** : The MRCP server supports playing voicemail from email attachments. Only supported by the media streaming server.



**Interaction Administrator Changes For Capabilities**  
IA currently currently lists all the supported MRCP resource types in the **_Supported Resources_** tab for a server configuration:

Since xIC's MRCP integration only supports the _Speech Synthesizer_ resource it did not make sense displaying all the resources in this tab. Instead the tab will be changed to the tab displayed above. With the new configuration IA will only write 2 types of resources in the DS Entry **_$SERVER\MRCP\Servers\ <Server Name>\Resources Supported_**. If **_Text To Speech_** capability is selected, IA will add the **'speechsynth'** to the list of resources supported. If **_External Audio Source_** or **_Voicemail_** is selected, IA will add the **'mediaplayer'** to the list of resources supported.

For the **'mediaplayer'** resource the Media Streaming Server has the ability to turn off voicemail and external audio support independently. Similarly, IA will give the administrator the ability to turn on and off support for each of these mediaplayer features. To accomplish this there are a couple attributes under the entry **_$SERVER\MRCP\Servers\ <Server Name>\MediaPlayer_** that IA has to set to '1' or '0' depending on whether each feature is enabled. The attributes are as follows:

Attribute Name  |  Values  |  Default  |  Description   
---|---|---|---  
ExtAudioSupported  |  1: enabled   
0: disabled  |  0  |  Indicates that **_External Audio Source_** playback is supported on this MRCP server   
VoicemailSupported |  1: enabled   
0: disabled  |  0  |  Indicates that **_Voicemail_** playback is supported on this MRCP server   
  
A user also has the option for the IC server to retrieve the capabilities of the media streaming server automatically using the SIP OPTIONS request. To turn this feature on/off IA has to set the following attribute in the **_$SERVER\MRCP\Servers\ <Server Name>_** entry:

Attribute Name  |  Values  |  Default  |  Description   
---|---|---|---  
UseOptionsForCapabilities  |  1: enabled   
0: disabled  |  0  |  Indicates that IC server should use OPTIONS to determine the capabilities of the media streaming server   
OptionsInterval  |  Options Interval in seconds. min: 5s   
max: 1200s   
0s disables options messages  |  10s  |  Indicates that IC server should use OPTIONS to determine the capabilities of the media streaming server   
MRCP Configuration

For details on DS Configuration for MRCP go to: [MRCP Configuration Specification](http://perforce:8080/depot/systest/eic/main/products/eic/resources/mrcp/docs/MRCP%20Configurations.doc).

### External Audio Sources

**Media Streaming Server Config > External Audio**  
External audio sources (a.k.a. Line-In) are configured in a couple places. The first is on the Media Streaming Server we config page where local devices are mapped to external audio names. This is configured in the external audio tab:

MSS External Audio ConfigMSS External Audio Config6

  * **Device Mapping** : Users will be able map local audio devices on the media streaming server to a name which would be use to reference that devices when using this media streaming server. All the available devices for a system will be displayed on the page and in order for a user to be able to use a device they have to give it an **external audio name** in the corresponding text field. If a name is not provided that device will not be used. If a user deletes a name its mapping is removed. If a device is labelled *****device not enabled***** it indicates a device that is now disabled but still has an external audio name assigned to it.
  * **Fallback Audio File** : This will be a read only field that points to an audio file that will be used if an external audio source fails to play or if a device cannot be found.

External Audio Names

The external audio names that are given to a device are **case sensitive**. This means the name _IPod_ is not the same as _ipod_ and the MSS will return an error if a name mismatch is found. External audio names will be retrieved by the IC Server using OPTIONS request so mismatching of names should be infrequent.

**IA System Configuration > MRCP Servers > Servers > External Audio Sources**  
External audio sources also have to be configured in the MRCP container in IA so that the appropriate MSS server will be picked when selecting an external audio source. The list will be found under the _External Audio Sources_ tab in the MRCP server configuration.

MSS IA Server Config External AudioMSS IA Server Config External Audio3

  * **Available Sources** : List of available external audio sources configured on the media streaming server.
  * **Refresh** : Fetches the most current external audio sources mapping from the media streaming server.



**Interaction Administrator Changes For External Audio**  
IA will pick up the list of supported external audio sources for a server from the following DS Entry: **_$SERVER\MRCP\Servers\ <Server Name>\MediaPlayer\ExternalAudio_**. Similar to DS entries for synthesizer voices there will be a subkey under this entry for each external audio name supported by this server. The name of the key will contain the name of the external audio as follows **_$SERVER\MRCP\Servers\ <Server Name>\MediaPlayer\ExternalAudio\<ExternalAudioName>_** and will have the following attributes:

Attribute Name  |  Values  |  Default  |  Description   
---|---|---|---  
Description  |  String  |   |  Description of the External Audio Source as displayed on the media streaming server web config   
  
When an administrator hits **_Refresh_** , IA will send a request to the MRCP Subsystem to refresh that list for a specific server (eMrcpApiMsg_RefreshServer) and then repopulate the list based on the items in the (refreshed) DS entry.

**Using External Audio Sources**  
External audio sources are treated like any other play request but with a special URI. The URI for the play will follow the URI format: _**x-inin-audiosrc:systemaudio/ <external audio source name>**_ where the **< external audio source name>** will be the name mapped in the MSS web configuration page. For example, referencing the sources mapped above, to play from the IPod source a user would specify the following URI: _**x-inin-audiosrc:systemaudio/IPod**_. The External Audio Source URI will also support optional parameters that control how the external audio is played:

Parameter Name  |  Values  |  Default  |  Description   
---|---|---|---  
timeout  |  int (in seconds)  |   |  Amount of time to play the audio source before timing out   
  
There are 3 places this URI can be used in xIC:  
1\. **IA People > Workgroups**

The workgroup configuration allows a user to select what to use for _**On Hold Music**_ for that queue. Right now a user can configure using a random or specific wave file or an audio source. Another option will be to allow a user to select using an external audio source as well:

MSS Workgroup Audio ConfigurationMSS Workgroup Audio Configuration2

  * **Use external audio source** : Allows the user to pick from the list of all available external audio source names to use for music on hold. Internally this will be translated to an external audio source URI when send to TS for playing.
  * **Only play this external audio for x seconds** : Configures the maximum time the hold music is played for.



To make populating the list of available external audio sources easier for IA, the MRCP subsystem will gather all the external audio source names from all the servers and populate the following attribute under the DS Entry: **_$SERVER\MRCP_** :

Attribute Name  |  Values  |  Default  |  Description   
---|---|---|---  
ExternalAudioSources  |  Multi-valued String  |   |  List of all available External Audio Sources across all servers   
  
2\. **Handlers > Play Audio File**  
Users can use the **_Play Audio File_** toolstep to play from an external audio source by specifying the URI in the **_Audio File Name_** field:

3\. **Attendant > Profile > Schedule > Play Audio**  
In Attendant users have the ability to play audio from a file or audio source to a user in the IVR. This node is added by selecting _Insert > New Operation > Play Audio_ on the Interaction Attendant context menu. An options to play from an external audio source has to be added to this node as well:

AudioPlayback External AudioAudioPlayback External Audio1

  * **External audio source** : If selected will use an external audio source for playback.
  * **Name** : Name of external audio source to use. This will be auto populated with a list from DS.
  * **Timeout** : How many seconds to play from the external audio source until moving onto the next node.



4\. **Attendant > Profile > Schedule > Group Transfer > Queue Audio**  
In Attendant users have the ability to transfer a call into a queue. Once transferred a user can configure Attendant to play a message to the caller using the **Queue Audio** node. This node is added by selecting _Insert > New Operation > Queue Operations > Play a Message to the caller_ on the Interaction Attendant context menu. An options to play from an external audio source has to be added to this node as well:

Attendant External Audio Source PlayAttendant External Audio Source Play1

  * **External audio source** : If selected will use an external audio source for queue audio.
  * **Name** : Name of external audio source to use. This will be auto populated with a list from DS.
  * **Timeout** : How many seconds to play from the external audio source until moving onto the next node.



### Voicemail

At the moment all voicemails are downloaded from the mail server to the IC server before being played back using the media server. To change this so that the MSS can stream the voicemail directly from the mail server to the media server a user would have to configured xIC to use MSS for voicemails:

MSS MRCP Servers ConfigurationMSS MRCP Servers Configuration2

**Interaction Administrator Changes For Voicemail**  
IA will pick up whether Media Streaming Server will be used for Voicemail playback from the following DS Entry: **_$SERVER\MRCP\Config\UseMRCPForVoicemail_**.

#### Open Items

The following items still have to be discussed and may go into a future release:

  1. Playlist support
  2. Only have a single RTP source from MSS to each media server and not one per play
  3. Open concern for the number of boxes needed for our solution
  4. If all MSS servers are down should we default TS to play hold music file from the IC server?



Media Server:

  1. Add support to continuously play a file from where it last left off vs. at a random location
  2. Add parameters for play items (random, timeout, loops).



## Testing

  * 

