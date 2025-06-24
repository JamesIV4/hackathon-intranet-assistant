**UNDER CONSTRUCTION**

**The following information is incomplete and currently under discussion.**

# Overview

Music On Hold (MOH) is a new feature for Clay (SU target TBD). A common customer request has been to stream audio from an external source (radio, iPod, etc) to be used as hold music. It's typical for a given IC server to use many media servers distributed in different locations. This makes direct connection of a live audio source to each media server impractical. Fortunately we already have the Media Streaming Server (MSS) which is designed to stream content such as voicemail and audio. We should be able to add an audio input as just another MSS source that can then feed multiple media servers.

MusicOnHold ComponentsL MusicOnHoldResourceConnectionsL

## SCRs

[DP-238](http://devjira-prod.i3domain.inin.com/browse/DP-238) \- Media Streaming Server  
[DP-275](http://devjira-prod.i3domain.inin.com/browse/DP-275) \- Support for external audio source/ line-in on media server  
[IC-87217](http://devjira-prod.i3domain.inin.com/browse/IC-87217) \- Umbrella: Support for external audio source/line-in on media server  
[IC-86914](http://devjira-prod.i3domain.inin.com/browse/IC-86914) \- TS Changes  
[IONMEDIA-204](http://devjira-prod.i3domain.inin.com/browse/IONMEDIA-204) \- icmediaserveraudio support system audio source in AudioSource  
[IC-48616](http://devjira-prod.i3domain.inin.com/browse/IC-48616) \- Add support for global looping audio sources and line-in in the media server  
[IONMEDIA-203 ](http://devjira-prod.i3domain.inin.com/browse/IONMEDIA-203) \- HPAA system audio element: Allow multiple input element instances for same source  
[IC-86920 ](http://devjira-prod.i3domain.inin.com) \- Media Streaming Server Support for playing from a local audio resource.  
[IC-86919 ](http://devjira-prod.i3domain.inin.com) \- MRCP Subsystem Support for Media Streaming Server based Line-In Audio/Music on Hold  
[IC-86918 ](http://devjira-prod.i3domain.inin.com) \- IA Configuration of Media Streaming Server based Line-In Audio/Music on Hold

## Perforce / Team Builds

Changes to icmediaserveraudio (ION) are taking place in the mediastreamingserver team branch. The MSS is also being developed from a team branch named mediastreamingserver in the XIC perforce repository.

The team build for the MSS has been changed to depend on the ION mediastreamingserver team branch.

## Definitions

  * MOH - Music On Hold
  * MSS - Media Streaming Server
  * Audio Stream Resource- A sound card hardware resource on the MSS that has been given a name like (e.g. ipod-src) through the MSS web interface.



# Design

## Call Sequence

In the typical use case a handle will trigger a PlayWav call to TS. The passed source will be either an IA audio source (audio:hold-music-indy) or a MSS live audio stream in the form of a URI (x-inin-audiostream:localaudio/ipod-src). If the IA audio source maps to a MSS audio stream it will be translated to the x-inin-audiostream format. The play requests cause async play requests to be sent to TSMedia which are organized into command batches. TS will then call StartTx to initiate the execution of the command batches.

For audio streams TS media needs a target IP/port on the media server. A modify is sent to the Media Server audio source to request the endpoint to receive the stream. When TSMedia receives this information it then crates the media player resource through the MRCP subsystem passing the x-inin-audiostream:/<name>. This will trigger a SIP invite to the MSS so that the output stream can be connected to the Media Server receiver that is already there. The MSS uses the icmediaserveraudio API to create this output resource via the audio source resource (same type of resource used on the Media Server). Once this all completes TSMedia will activate the stream by sending the MSS a MRCP "speak" command. Audio will start to flow to the Media Server soon after this completes.

MusicOnHoldSequence1L

## IA

### System Configuration -> MRCP Servers -> Servers

#### Supported Resources

Add a check box for "Audio Stream Resource" to the "Supported Resources" tab. This will enable/disable a MRCP server for use with a Audio Stream Resource.

#### Audio Stream Resources

A new tab needs to be added to configure which audio stream resources on the MSS are available for use. Note that more than one MSS can have a audio stream resource with the same name. The names (e.g. ipod-src, fm-radio, pandora) are configured through the web interface of the individual MSS and these same names are called out in IA to either be available or selected. The MSS maps the name to the actual sound card resource since the connection is machine specific but the name is potentially universal.

TBD: If we can pull these names from the connected MSS to make the pick list that would probably be ideal. This allows the user to move each named resource between an available and selected list. If that isn't possible we should probably just allow the user to add the name without validation.

### <Machine Name> -> Audio Sources

Add the ability to pick a MSS audio stream resource. Currently only local wav files are supported.

### People -> Workgroups -> Files

This is used currently to configure "On Hold Music". Augment to allow specification of a MSS audio stream resource. Add a radio button on the "Configure..." dialog for "MSS Audio Stream Resource". Note that if more than one MSS has a audio stream resource with this name either is a potential source. Ideally the user would be presented with a pick list aggregated from all available MSS. If the resource is removed from the mapping a default source name should be used that is understood by the MSS. This default is always understood by all MSS out of the box. How the MSS maps the default source is TBD. Note that the user will also be able to pick the MSS audio stream resource by selecting an IA audio source that is mapped to the MSS.

## TS

TS examines each play command it receives to decide what operations need to be performed through each interface. In the case of MOH it will be asked to play a audio stream resource of a given name (x-inin-audiostream:localaudio/<name>). The list of MSS that are capable of playing that named stream is configured through IA. If TS can't find a capable MSS for the stream it will pick a MSS to play the default stream (i.e. x-inin-audiostream:localaudio/default) which all MSS should have mapped to either a local wav file or audio input.

A media server resource must exist to receive the stream. This receiving resource is the same type used to receive TTS plays. The returned IP/port information is used to send the MSS a SIP invite. After the invite the MSS play (MRCP "speak" command) may be requested and the streaming with start.

## Media Streaming Server

### SIP Invites

The icmediaserveraudio interface is used by the MSS to setup the MOH streams based on a combination of SIP invites and MRCP "speak" commands it receives. The audio source icmediaserveraudio resource is the way these local live audio plays will be constructed. The MSS commands a modify to the audio source in response to the SIP invite it receives passing the SDP of the invite via the "modifyRtpSink" parameter in the modify. In response the icmediaserveraudio interface to return the results of the invite in the "rtpSinkAnswer" parameter. The answer includes a sink ID that allows management of multiple output "sinks" associate with the audio source. This can be used later to reinvite the endpoint.

### Local Audio Device Mapping

The MSS will enumerate the list of available audio devices and resources using the icmediaserveraudio query_info interface. A given server may be equipped with a number of sound cards. Each sound card may in turn have a number of available audio resources such as line-in, microphone, mixed audio output, etc. These resources are presented in the web interface so that they can be associated with a name (e.g. wfbq-fm, ipod-src, indy-hold-music, default-hold-music, etc). The user should also have the ability to configure a default source that is either a local wav file or audio resource that can be played in the event the request resource isn't available or the requester asks for x-inin-audiostream:localaudio/default. See the icmediaserveraudio section for how this information is passed down.

### MRCP Speaks

When the MSS receives a speak command of the form x-inin-audiostream:localaudio/<resource name> where <resource name> is a valid mapped resource name it will request the audio source to play that source. The MSS must translate the passed name (e.g. ipod-src) to the mapped device name. Assuming the icmediaserveraudio interface has already been used to map the resource name to an audio resource the audio will be played out through the previously invited RTP sink resource in the audio source. If the RTP sink doesn't exist or the audio resource is not mapped the command will fail and it will be up to the MSS to determine what action to take.

## MRCP Subsystem

Generally we expect the MOH request to translate to a MRCP speak command. The details are TBD.

## icmediaserveraudio interface

### Enumerating Local (Line-In) Audio Resources

The existing query_info interface can be used to fetch a list of audio resources. The call returns the "localAudioResources" parameter which contains the list in XML format. Each listed device will have a direction attribute that will be either "input" or "output". The device will also have a state attribute that will indicate "disabled", "enabled", or "unplugged". The MSS web interface should allow mapping of all devices that are either "unplugged" or "enabled". If a device is later disabled and referenced it should still be resolved by the MSS however it will fail. Devices that are unplugged will also result in a failure when they are played. We need these devices to remain visible to the web interface.

### Media Server Local (WASAPI) Audio

The source of the MOH will be a WASAPI endpoint. The MSS will enumerate the available sources and allow the user to name each with an associated x-inin-audiostream:localaudio naming scheme (x-inin-audiostream:localaudio/<resource name>)

So for example if the machine contains three USB audio adapters and a built-in AC97 sound card you might see something configured like this:

SoundBlaster Line In ==> x-inin-audiostream:localaudio/wfbq-fm-radio  
SoundBlaster Mixed Audio ==> x-inin-audiostream:localaudio/pandora-source  
Internal Sound AC97 Line In ==> x-inin-audiostream:localaudio/ipod-source

### Audio Source Resource

The audio source is used by both the Media Server and the Media Streaming Server. The MSS uses the audio source to configure the play side of the audio to stream the sound resource via RTP. The Media Server uses the audio source to receive the RTP audio stream from the MSS and pass it to the downstream RTP endpoint. The "sourceUri" parameter is used by the MSS to pick the audio resource to stream. Just like other prompt sources within audio source graph, the caller may specify any number of audio resources to stream.

audio_source_with_system_audio_sourceM

## Media Server

The media server already supports the prompt play call necessary. Since the resource is identified via URI and is used similar to TTS there shouldn't be a need for change in the Media Server beyond the changes being made to the icmediaserveraudio library.

# Testing

TBD

# Documentation TODO
