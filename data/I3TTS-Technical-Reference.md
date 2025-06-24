## Introduction

The media server now supports text to speech synthesis without the use of any third party software. Previously, the xIC platform only supported TTS using 3rd party vendors like Nuance which it communicates with using standards such as SAPI or MRCP. Having our own TTS engine embedded in the media server has the following advantages over our current TTS integration:

  * No 3rd party dependencies. If something breaks we can fix it plus we are not dependent on 3rd party release cycles, pricing, and bug fixes.
  * Less servers to configure and deploy. Dealing with 3rd party installations and configurations has always been challenging. Monitoring and keeping the servers updated is also updated cost. Having this as part of the media server reduces the cost of deployment and maintenance.
  * Lower costs to the customer. Our TTS licenses will be cheaper than Nuance since this will be bundled in our overall media server licensing.
  * Takes advantage of media server topology and architecture. Load balancing, regionalization, failover etc. is already handled by the media server so we would not need to configure another subsystem or 3rd party server to handle that.



## Using I3TTS in xIC

The xIC platform will automatically use the media server for all its text-to-speech plays if configured to do so in IA. This configuration is done in the system configuration for text-to-speech:

Media Server Configuration TTSLeft3

The following table describes the configuration setting for this dialog:

Configuration| Description| Default| Notes  
---|---|---|---  
Default TTS Provider| Configures the default TTS provider for the system. Valid values are:Media Server  
MRCP  
SAPI |  |    
  
 

### Interaction Designer Tools

To use media server for TTS the text to speech prompt tools (telephony palette) are available. If a system is configured to use media server as its default TTS provider these tools will automatically use the media server for speech synthesis.

However, a system can be configured to use SAPI or MRCP by default and still be able to use I3TTS. This is done by using the "Extended" version of the prompt tools and in the optional parameters simply enter in "I3TTS" as the first parameter:

Several other parameters can be specified in the optional parameters field to control the speech synthesis for that tool step when using the media server. These parameters are space delimited and if a parameter requires a value, its name/value pair is separated by a colon (i.e. "com.inin.lang:en-US"). The following table lists what each of the parameters are:

Parameter| Description| Values| Notes  
---|---|---|---  
i3tts.content.language| Uses the specified language to synthesize the text to speech| Identifiers as specified in RFC 3066 (language-country)|    
I3TTS| Controls whether media server should be used for TTS|  | **IMPORTANT** : If this parameter is specified it has to be first parameter in the optional parameter field.  
i3tts.content.type| The content type of the text being synthesized| text/plain (default)  
application/ssml+xml|    
i3tts.voice.name| Uses the specified i3tts voice to synthesize the text to speech| i3tts voice name as specified in IA.|    
i3tts.voice.rate| SSML prosody rate of a voice| The value can be a number in Hz  
**or**  
The following predefined values which indicate a relative change:  
x-slow  
slow  
medium  
fast  
x-fast  
default|    
i3tts.voice.volume| SSML prosody volume| The value can be +/- number in dB  
**or**  
One of the following predefined values which indicate a relative change:  
silent  
x-soft  
soft  
medium  
loud  
x-loud  
default|    
i3tts.voice.pitch| SSML prosody pitch| The value can be number in Hz  
**or**  
One of the following predefined values which indicate a relative change:  
x-low  
low  
medium  
high  
x-high  
default|    
  
 

### SSML Support

TBD

### Licensing

Media Server TTS will be licensed as a feature for CIC. There will also be a feature license per language supported. The licenses will be enforced similar to the way the analyzer feature and language licenses are enforced. The following are the license keys used:

License Key| Description| Voice Name  
---|---|---  
I3_FEATURE_MEDIA_SERVER_TTS| Feature License|    
I3_FEATURE_MEDIA_SERVER_TTS_LANGUAGE_EN| North American English| Jill  
I3_FEATURE_MEDIA_SERVER_TTS_LANGUAGE_ES| North American Spanish| Isabel  
I3_FEATURE_MEDIA_SERVER_TTS_LANGUAGE_ES_ES| Spanish|    
I3_FEATURE_MEDIA_SERVER_TTS_LANGUAGE_FR| French|    
I3_FEATURE_MEDIA_SERVER_TTS_LANGUAGE_FR_CA| Canadian French| Hilorie  
I3_FEATURE_MEDIA_SERVER_TTS_LANGUAGE_DE| German| Arabella  
I3_FEATURE_MEDIA_SERVER_TTS_LANGUAGE_EN_AU| Australian English| Kandyce  
I3_FEATURE_MEDIA_SERVER_TTS_LANGUAGE_EN_GB| British English| Ellene  
I3_FEATURE_MEDIA_SERVER_TTS_LANGUAGE_JA| Japanese|    
I3_FEATURE_MEDIA_SERVER_TTS_LANGUAGE_NL| Dutch|    
I3_FEATURE_MEDIA_SERVER_TTS_LANGUAGE_PL| Polish|    
I3_FEATURE_MEDIA_SERVER_TTS_LANGUAGE_PT_BR| Brazilian Portuguese|    
I3_FEATURE_MEDIA_SERVER_TTS_LANGUAGE_TR| Turkish|  
