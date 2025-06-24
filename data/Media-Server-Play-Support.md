# Media Server Play Support

false

## Overview (from [MediaServerPromptSupport.doc](http://perforce:8080/depot/systest/EIC/main/products/eic/resources/mediaserver/docs/MediaServerPromptSupport.doc))

In the current configuration where the audio processing for plays is hosted on the IC server, access to prompt files and WAV files created by handlers is as simple as accessing a local file. With media servers, we have to somehow provide remote access to these resources. Access through file shares is not a viable option as it requires domain membership. Instead, we propose a prompt server that exposes the play resources through HTTP. This has the added advantage that it automatically works with third party MRCP servers and embedded <audio> tags. 

## Major Features and Requirements

  * Supports IVP and wave files.
  * Supports versioning and caching.
  * Configurable virtual directories and file extension support.
  * Uses ION i3http/i3inet.



## Design

  * [Media Server Play Support Design](http://perforce:8080/depot/systest/EIC/main/products/eic/resources/mediaserver/docs/MediaServerPromptSupport.doc)
  * [Prompt Server Configurations](http://perforce:8080/depot/systest/EIC/main/products/eic/resources/promptserver/Prompt%20Server%20Configurations.doc)
  * [IA Prompt Server Configuration Design](http://wiki.inin.com/bin/view/ClientTeam/IAPromptServer)



## Schedule

Feature | Description | Updated | SCR | % Complete | Days | Finish Date | Developer  
---|---|---|---|---|---|---|---  
Prompt Server  |   |   |  61272 |  100%  |   |   |   
Prompt Server Client  |  Define Client Interfaces  |   |   |  100%  |   |   |   
TS Integration  |   |   |   |  100%  |   |   |   
Media Server Integration  |   |   |  60796 |  100%  |   |   |   
IA configuration  |  Add Prompt Server config in IA  |   |  61263, 63528 |  100%  |   |   |   
Install  |  Add Prompt Server to install  |   |  61261 |  100%  |   |   |    
Integration Tests  |  Test against Loquendo Speech Suite  |   |   |  100%  |   |   |   
  |  Test against Nuance Media Server  |   |   |  100%  |   |   |   
Documentation  |   |   |   |  100%  |   |   |  Kevin Kuhns  
  
## Testing

  * Testing Page



## Design Considerations

Several components are affected by play operations. The following section documents which components are being researched and documents any changes that have to be made.

### IP and Tool Changes

There are quite a few tools devoted to doing plays:

  * Play Audio File
  * Play Digits
  * Play Prompt
  * Play Prompt Extended
  * Play Recording
  * Play String
  * Play String Extended
  * Play Text File
  * Play Text File Extended
  * Play Tone



All of these tools will not change. The only added feature is that the Play Audio File will also support http URIs for the input audio filename if a media server is being used for the play.

**Future (Clay)** : In Clay voicemail plays can be optimized to use the . At the moment the default system and TUI handlers will first download a voicemail attachment to the work folder and issue a play to TS to play that file. In Clay handlers will be able to pass that voicemail moniker directly to TS which will pass it to the Media Streaming server which in turn will stream the voicemail directly to the Media Server. For details look at 78687. 

### Client/ICELib/Session Manager

The .NET client supports playing voicemail via one of three method: play to speakers, handset, or a remote number. The client accomplishes playing voicemails to a handset or a remote number using ICELib which sends a request to SessionManager containing the moniker of the voicemail attachment to play. SessionManager will download the voicemail to the user's client setting folders and issue a play request to TS Server to play that file. 

To support this with plays on the media server the client settings folder has to be mapped in prompt server as a virtual directory. Session Manager also has to change to download the file with a *.wav extension as opposed to a *.tmp. For details look at 65064.

**Future (Clay)** : There are potential optimizations that can be put into place once the  is available. The Media Streaming server will be able to take a voicemail moniker directly and stream the audio to the media server. This will save having to download the file first into the client settings folder only to have it be fetched by the media server. For details look at 78698.
