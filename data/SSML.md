The VoiceXML server is currently not passing the entire SSML document it receives from  
BladewareVXML to the TTS engine. The interpreter parses the SSML and only passes the  
text within a speak element to TTS. This was originally put into place to get  
non-SSML compliant engines (such as Microsoft Sam) to work. What is lost is the ability to  
support SSML with engines (i.e. RealSpeak) that do support SSML.  What is also  
lost is the encoding attribute which affects the rendering of TTS.

This mini-project (a couple weeks' effort) is to address that.

The design document is attached ().

The SCR for these changes is IC-42239.
