# Automatic Speech Recognition Audio Support in Media Server

## Overview

Phase 4 of the Media Server calls for supporting ASR audio through the Media Server. This includes providing echo cancellation if not already provided for by the gateway. Currently, echo cancellation is done using HMP with CSP/Speech Recognition resources.

## Team Branch Locations

All ION work can be found in the mediaserverasr team branch.

## Architecture

### Overview

ASR support on the Media Server can be accessed via the audio source graph construct.   

The following diagram illustrates a typical use case for ASR.

MediaServerASRSequence1L

### Media Server API

#### Audio Source Input Parameters

IC Media Server Parameter Name   
|  Parameter Name String   
|  Parameter Value Description   
  
---|---|---  
g_paramName_asrSourceControl   
|  asrSourceControl   
|  Indicates the desired ASR session state.   


  * "start" \- This causes the ASR session to reset the detection of speech.  Reference audio is passed through and not ASR endpoint packets are transmitted until speech is detected.  Once speech is detected the reference audio is blocked (bargein) and the ASR endpointed audio is passed until a "stop" or "start" is issued.
  * "stop" \- Puts the ASR endpointing element into a pass-through mode.  Reference audio is passed directly to the output and the speech detector is turned off. Detection can be restarted by issuing a "start".

  
g_paramName_targetUri  |  targetUri  |  Specifies remote endpoint details.   
g_paramName_modifyAsrSourceRtpSink  |  modifyAsrSourceRtpSink  |  Contains SDP description the ASR media parameters.   
  
g_paramName_asrBargeinOnSpeech  |  asrBargeinOnSpeech  |  If set to true the endpointer will perform local barge-in.  If not set or set to false then only the barge-in event will be fired.   
  
  
#### Audio Source Output Parameters

**IC Media Server****Parameter Name** |  **Parameter Name String** |  **Parameter Value Description**  
---|---|---  
g_paramName_address  |  address  |  Local IP address for RTP sockets.   
  
|    
|    
  
  
#### Audio Source Event Notifications

**Event Name String** |  **Parameter Value Description**  
---|---  
audiosource.asr.bargein  |  This event is sent when the speech discriminator of the audio source detects a speech event.  This will cause the audio source to start sending the buffered audio from the remote endpoint to the ASR server endpoint.The sample time of the bargein is sent with the event (asrSourceSampleTime=>'i3core::RelativeTime::as_string()')   
  
  
### Media Server Elements

This section describes the media server elements that may be used to construct ASR sessions.   


#### ASR Source Endpointer   


This element hosts the speech detector and circular buffering for the remote endpoint.  It also switches reference audio to perform barge-in locally.    Currently the ippspeechcoding VAD class is used for speech detection. When the element is created it enters the initialized state.  In this state audio is passed through the reference input to the output.  The endpointed output will output silence in this state.  When a start is issued the vad detector is reset.  The reference audio is still passed through.  The endpointed audio is circular buffered until the vad detects speech.  At the detection point a barge-in event is sent and the reference audio output is silenced.  The time delayed version of the endpointed audio is sent out. 

MediaServerASRStateDiag1L

### Bargein

We will also be consolidating handling bargein throughout the system as part of the work to support ASR on the media server. This means creating a unified way of handling barge in between tools, VoiceXML, RecoSubsystem, TsAPI, TsServer, TsVendor/TsMedia, and Media Server. Handling of bargein will for the most part mimic the way the [VoiceXML spec](http://www.w3.org/TR/2002/WD-voicexml20-20020424/#dml4.1.5) defines how to handle bargein with the **only notable difference being** that the properties cannot be defined on a prompt per prompt basis but instead is defined on a dialog basis (i.e. per RecoInput/GetInputEx). The following sections defines how each bargein property is defined in each of the subsystems.

#### Tools

Bargein is controlled using properties in "Reco Input" toolstep. The properties are defined as follows:

Property  |  Values  |  Description   
---|---|---  
reco:ASRBargeinDisabled  |  **" false"** (default): bargein is enabled   
**" true"**: bargein is disabled  |  Controls whether bargein is disabled   
reco:BargeinType  |  **" speech"** (default): Any speech detected will bargein on the prompt   
**" hotword"**: First match in a grammar will bargein on the prompt  |  Controls the type of bargein   
  
#### Reco API

Bargein will be controlled using the same properties as specified in the Tools above. The properties are passed a property set in the Reco Input request.

#### VoiceXML

VoiceXML supports properties for Bargein and BargeinType. Look at the [VoiceXML reference](http://www.w3.org/TR/2002/WD-voicexml20-20020424/#dml4.1.5) for more details.

#### TSAPI/TS Server

Bargein is controlled as parameters of GetInputEx_req. The bargein parameters will control bargein for all plays serialized as part of the request.

Parameter  |  Type  |  Values  |  Description   
---|---|---|---  
Bargein  |  boolean  |  **" true"** (default): bargein is enabled   
**" false"**: bargein is disabled  |  Controls whether bargein is enabled   
BargeinType  |  string  |  **" speech"** (default): Any speech detected will bargein on the prompt   
**" hotword"**: First match in a grammar will bargein on the prompt  |  Controls the type of bargein   
  
#### Media Server

Bargein on the media server is controlled using Audio Source input parameters as described above. Only switching bargein on/off is supported and not specifying a bargein type which is always assumed to be "speech".

Parameter  |  Type  |  Values  |  Description   
---|---|---|---  
asrBargeinOnSpeech  |  string  |  **" true"** (default): bargein is enabled   
**" false"**: bargein is disabled  |  Controls whether bargein is enabled   
  
### Notes

  * We have to support local barge-in (on/off) switching between plays.  For plays sequenced on the Media Server one way to handle this would be an additional parameter being passed per play. This avoids some chatter between TS and the MS because without this plays would have to be sequenced on barge-in state boundaries.   For remotely sourced plays (e.g. TTS) the audio source should expect a modify with each barge-in state change.  Synchronization would be the responsibility of TS.  Even if the audio source has torn down the ASR instance the local barge-in state for ASR should be maintained to make this work.  This portion of the design is still under discussion.


