## Overview

Playing Text-To-Speech (TTS) in Attendant requires using the **_Other Tools_** operation and specifying the Tool as "Play TTS". The operation uses **_Play String Extended_** tool under the covers and requires the following call attributes to be set to fill the tool's input fields:

**$ATTR_TTS_INPUT** : Text text to play.  
**$ATTR_TTS_VOICE** : Voice to use for TTS.  
**$ATTR_TTS_VOLUME** : Volume of TTS voice.  
**$ATTR_TTS_SPEED** : Rate of TTS voice.  
**$ATTR_TTS_OPT** : Optional parameters.

By default this operation will result in a SAPI TTS play being executed unless the **_Use MRCP for TTS Plays_** global option in the MRCP container has been selected. This can be overridden by using the optional parameters above as detailed by the rest of this document.

## Procedure To Use MRCP in Attendant

1\. Add a **_Multi-Action_** Container and add sub operations/actions to it:

2\. Add a **_Set Attribute_** operation that sets "ATTR_TTS_INPUT" attribute. This will set the text that gets played. **Important** : Make sure the action when finished is set to jump to the next node.

3\. Add a **_Set Attribute_** operation that sets "ATTR_TTS_OPT" attribute. This will set the optional properties in the Play String Ex tool as specified on: . Make sure the first attribute is "MRCP". In my example I am setting the content type to SSML:

4\. Add an **_Other Tools_** operation and set the Tool to "Play TTS":

You use various other MRCP parameters in step 3 above such as setting language, prosody, gender etc.
