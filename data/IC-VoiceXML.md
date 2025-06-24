 

VoiceXML, the Voice Extensible Markup Language, is an XML-based language used to  
create audio dialogs. These audio dialogs feature synthesized speech (TTS) or digitized  
audio (pre-recorded audio) to prompt the user, and they accept spoken words or DTMF  
key input. The VoiceXML application - or script - contains the logic that controls the flow  
of the dialog, and it's what prompts the caller, accepts the caller's input, and determines  
the next step for the caller.

2.1 - <http://www.w3.org/TR/voicexml21/>

2.0 - <http://www.w3.org/TR/voicexml20/>

 

**Software Support:**

The Interaction Center's VoiceXML feature consists of two main components:

  * VoiceXML Host Server
  * VoiceXML Interpreter Server



**Interesting information:**

In xIC 2.4, our VoiceXML interpreter utilizes the OpenVXI 3.4 library.  This library supports the  
VoiceXML 2.0 specification, and some elements of the VoiceXML 2.1 specification.

In xIC 3.0, our VoiceXML interpreter utilizes the Commetrex BladewareVXML library.  This library  
supports both the VoiceXML 2.0 and the VoiceXML 2.1 specifications.
