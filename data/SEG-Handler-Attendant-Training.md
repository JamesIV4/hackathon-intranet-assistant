**The video for this training can be found here:  \\\i3files\SSDG\SSDG Internal Team Files\Handler and Attendant Training**

Before beginning this, you should have gone through the Introduction to Handlers and Interaction Attendant training (this can be found here: [Handler Training](https://confluence.inin.com/display/SupInt/Handler+Training))

# Handlers

* * *

## Playing Audio Prompts

The best toolstep for playing an audio file is called simply "Play Audio File":

The Inputs tab has a number of options, but you will rarely care about anything except the Audio File Name and Immediate Mode.  The audio file name should be a fully qualified path OR the file specified should be located in the path set in the "Resource Path" server parameter in Interaction Administrator:

Immediate mode is a boolean value that determines whether the queued audio is played immediately or not.  This can be used to queue up multiple prompts before playing them.

@PlayAudioFile**F1 Help for Play Audio File**

* * *

 

@PlayAudioFile

**Play Audio File**  
This Telephony tool plays a .WAV file for a caller, and allows the caller to adjust volume and rewind or fast forward the file. This step does not play a prompt or CIC audio recording.

Note: For best performance, all .WAV files should be in the format 8 kHz mono mu-law PCM. On-the-fly conversion is performed when the format of the audio in the .WAV file is anything other than 8 kHz mono mu-law PCM. If a .WAV file is going to be played often, the 8 kHz mono mu-law PCM format allows CIC to bypass Microsoft Audio Conversion Manager and play the audio with much less overhead.

Note: This tool does not support .MP3 audio files.

**Inputs**  
**Call Identifier**  
The unique identifier for a call.

**Audio File Name**  
The unique name of the .WAV file. If you specify a path, make sure it is a fully qualified path indicating the server or drive letter. If you do not type a path, this tool uses the path stored in the Resource Path server parameter.

**Key(s) to Increase Volume**  
The keypad keys a caller can press to increase volume.

**Key(s) to Decrease Volume**  
The keypad keys a caller can press to decrease volume.

**Key(s) to Skip Forward**  
The keypad keys a caller can press to advance the recording the number of seconds specified in Skip Amount.

**Key(s) to Skip Backward**  
The keypad keys a caller can press to rewind the recording the number of seconds specified in Skip Amount.

**Skip Amount (seconds)**  
The number of seconds to advance and rewind when a caller presses a Skip Forward or Skip Backward key.

**Key(s) to Increase Playback Speed**  
The keypad keys a caller can press to speed up playback of the audio file.

**Key(s) to Decrease Playback Speed**  
The keypad keys a caller can press to slow down playback of the audio file.

**Immediate Mode**  
Set to True if you want the digits to be played when this step executes. Set to False if you want the digits to be queued with other digits played before and after so that several prompts are seamlessly played one after another.

**Exit Paths**  
**Next**  
This step always takes the Next exit path.

## Playing TTS Prompts

There are nine toolsteps that can call a TTS session:

  1. Play String
  2. Play String Extended
  3. Play Text File
  4. Play Text File Extended
  5. Record String
  6. Record String Extended
  7. Record Text File
  8. Record Text File Extended
  9. Play Prompt Phrase



Generally you will be using the Play String Extended since it just takes text and plays it back to the caller.  For information on the others, see the F1 help in Interaction Designer.

The Extended versions of each toolstep add the ability to specify Voice Name, Volume, Speed, and Load Controller Timeout. They also provide the Optional Parameters field which can be used to pass MRCP options to the MRCP server. You will almost always want to use the extended versions of these toolsteps.

Here is the Play String Extended toolstep:

The inputs we care about are Text, Voice Name, Immediate Mode, and Optional Parameters.  These are all pretty self-explanatory, but it should be noted that all MRCP parameters should be specified in the optional parameters field.  When the voice is set in both the "Voice Name" field and in the MRCP optional parameters field, the MRCP parameter will take precedence.  It is recommended to always set the voice using an optional parameter and not the "Voice Name" field when using MRCP.

For a list of the MRCP optional parameters, see the MRCP Technical Reference: <https://extranet.inin.com/products/cic/Documentation/mergedProjects/wh_tr/bin/mrcp_tr.pdf>

@PlayStringExtended**F1 Help for Play String Extended**

* * *

 

@PlayStringExtended

**Play String Extended**  
This Telephony tool reads the contents of a string to a caller using the text-to-speech (TTS) engine that you specify in the parameters. This tool extends the options available over the Play String tool in that you can specify Speech Mode, Language ID, Gender, Pitch, Speed, and Load Controller Timeout. You should not use the Language ID parameter if you are running the Centigram TruVoice TTS engine.

Note: For EIC SR-C, only international versions of EIC currently ship with a TTS engine that supports multiple language modules (L&H TTS3000). North American EIC uses the Centigram TruVoice, and only the English language module. See the International Release notes for information on installing the L&H TTS3000.

**Inputs**  
**Call Identifier**  
The identifier for the call to which the string will be played.

**Text**  
A text value or string variable containing the text to be played.

Note: The Text input can contain tags to specify the Language ID. To determine the format for the tags, refer to the documentation for your TTS engine.

**Voice Name**  
The name given to a voice defined in Interaction Administrator. This is the voice that will be used to play the string.

Note: You can specify a language in Interaction Administrator when defining a voice. For more information, refer to the Interaction Administrator online help.

**Volume**  
An integer from zero to 100 representing the percentage of the maximum permitted volume at which the string will be played. That is, a value of 100 will play the recording at the maximum volume, whereas a value of 25 will play the recording at 25% of the maximum level.

**Speed**  
This optional value indicates the rate of the voice. The value ranges from -10 (the slowest rate) to 10 (the fastest rate). The default rate is 0.

Do not use this input parameter with MRCP. Use the mrcp.audio.voice.rate parameter instead.

**Immediate Mode**  
Select this option if you want the text to be played when this step executes. Clear this option if you want the text to be queued with other prompts played before and after so that several prompts are played seamlessly, one after another.

**Load Controller Timeout (milliseconds)**  
If the TTS IC Server subsystem is too busy and doesn't have the resources to play the message, it will time out after the number of seconds you specify here and take the Rejected exit path.

**Optional Parameters**  
Use this field to set any optional parameters to TTSServer.

One of the optional parameters you can specify is "NOXML." If the NOXML parameter is specified, the TTS engine ignores the < sign and does not attempt to process the text as a SAPI tag. If the NOXML parameter is not specified, the TTS engine attempts to process the < sign as the beginning of a SAPI tag.

You can also specify a name value pair to control advanced MRCP properties, as specified in Using MRCP Tools.

**Exit Paths**  
**Next**  
This step takes the Next exit path if the speech is played.

**Rejected**  
This step takes the rejected exit path if the TTS subsystem does not have the resources to play the speech. See the Load Controller Timeout parameter above for more information.

## Speech Recognition in Handlers

Here is the official documentation for using speech recognition in handlers: <https://extranet.inin.com/products/cic/Documentation/mergedProjects/wh_tr/bin/speech_recognition_overview_tr.pdf>

There are 39 toolsteps in the Reco category in Interaction designer.  We will not be going over all of these, but we'll talk about some of the more important ones.

### Reco Initialize

This toolstep is used to initialize a recognition session with the ASR server.  No speech recognition can be performed on a call until this step has been executed.

The only important input here is the Input Modes field, which you will typically set to "voice dtmf".  If you require a specific engine when there are multiple configured on the CIC server, you can set the ASR Engine Name as well.

The Properties tab contains name/value pairs to apply to this specific session. For example, you can set a property called "sensitivity" and set the value to 0-1.0 to control the sensitivity for that session. This is the default value for that session, but if the property is explicitly stated elsewhere down the line (such as on the RecoInput toolstep), the default value will be overruled.

@RecoInitialize**F1 Help for Reco Initialize**

* * *

 

@RecoInitialize

**Reco Initialize**

This Reco tool explicitly initializes an ASR session for an interaction. It allows specifying the engine to use. If no engine is given, the recognition subsystem will pick an engine based on the language identifier of the interaction, the requested features, and the configuration order of the engines.

The Reuse Compatible Session checkbox controls whether an existing ASR session must be re-initialized or can simply be reused. If all parameters are left unspecified and Reuse Compatible Session is checked, an ASR session with default parameters will be created if the interaction does not have a session. If the current session is compatible, the session is used as is. If the checkbox is unchecked, a new ASR session will be created irrespectively of whether the interaction already has an active session, even if the specified parameters match the exiting session.

Common error codes returned by this tool:

Error code| Description  
---|---  
error.com.inin.reco.asr.engine| Specified ASR engine is unknown or not installed  
error.unsupported.language| Engine doesn't support the specified language  
error.com.inin.interaction.type| The specified interaction type is not supported by the recognition subsystem.  
error.com.inin.inputmodes| Not all of the specified 'Input Modes' are supported ('No Fallback' = true) or none of the specified 'Input Modes' are supported ('No Fallback' = false).  
error.noresource| Unable to initialize the recognition session because there are too many sessions already active and the number of available ports is limited (e.g. licenses or total load of all ASR servers exceeded limit).  
error.com.inin.reco.feature| The requested capabilities are not supported by the specified engine (or any engine that may be selected based on the language etc.).  
error.com.inin.reco.session.tied| The session configuration cannot be changed, as the ASR engine of the currently active session doesn't support this (once the engine is initialized, it has to stay with the call). The engine may still support changing the recognition language.  
error.com.inin.ownership| The invoking handler is not the owner of the interaction or it lost the ownership.  
  
 

Note: Irrespective of whether a new session is created or an old session reused, invoking this tool will always un-register all grammars and reset the session.

IMPORTANT: If the Language attribute of an interaction is changed after this tool has been invoked, the language of the ASR session will not change until the session is re-initialized by calling this tool.

**  
**

**Inputs**

**Interaction**

Identifier of the interaction (call)

**ASR Engine Name**

Optional. Name of the ASR engine configuration to use. If not defined, consider any engine that matches the Language ID argument or the Language interaction attribute and the required features.

**Server Groups**

Optional. Space separated list of server groups on which the ASR session must be created. This can be used to group sessions that use the same grammars on certain ASR servers to optimize grammar caching. If this parameter is not defined, the session may reside on any server.

**Language ID**

Optional. ISO language ID of the language to be recognized. If this parameter is not defined, then by default the value of "Language" interaction attribute will be used.

Note: Some engines support multiple languages and/or use the language specified in the grammar. This parameter may thus just be used to ensure that the engine supports the language (but is still may allow using grammars of other languages).

**Required Features**

Optional. String containing a space separated list of features that the ASR engine must support. Default is an empty string.

**Input Modes**

Optional. Space-separated list of input modes to use for this session. If this parameter is not defined, the value of the the 'Eic_RecoInputModes' interaction attribute is used by default.

**Max. Wait for Resource**

If allocating an ASR port fails because all of them are in use, the Reco subsystem may wait up to the number of seconds specified by this parameter for a port to become available. If no port is available within this time, the tool fails with 'Resource Limit'. The default value for this parameter is 0.0s

**Reuse Compatible Session**

This checkbox specifies behavior if the interaction already has an associated ASR session. This box is checked by default, and so the session won't be re-initialized and the engine won't be unloaded if this interaction already has an existing ASR session that matches the specified parameters. All grammars will be deactivated, however.

Clear this box if you want the session to always reset and the engine to reload.

**Lazy ASR Port Allocation**

This checkbox specifies whether a physical ASR port should only be allocated the first time an ASR operation is actually performed. This box is unchecked by default.

Check this box if you want the tool to decide which engine to use, but not actually allocate the port. If this box is unchecked and all ports are in use, the tool will take the Failure exit path.

**No 'Input Modes' Fallback**

This checkbox specifies whether the specified input modes must be supported or an automatic fallback is OK. This only applies if 'Input Modes' argument is defined (does not apply to default). This box is checked by default and the tool will take the Failure exit path if any input modes specified as "Input Modes" arguments cannot be used.

Clear this box if you do not want this tool to fail if only some of the input modes specified as "Input Modes" are unavailable. If all such modes are unavailable, the tool will still take the Failure exit path.

**Properties**

Inline properties (name/value pairs) to apply to session. These properties can be used to control the engine selection, pass engine specific data to the engine integration, or set default values for certain parameters.

**  
**

**Outputs**

**Error Code**

This output parameter contains the error code if the tool failed in the form of a VoiceXML style event.

**Error Text**

Text accompanying the error code.

**Exit Paths**

**Success**

This path is taken if the recognition session was successfully initialized.

**Failure**

This path is taken if an error has occurred. The Error Code and Error Text parameters contain details about the failure.

From now on I will forgo adding the F1 help for each of the toolsteps. The above examples show how useful it is, and I highly recommend using it whenever possible.

### Reco Session Active

Reco Session Active is a very basic function that checks to see whether the current call already has an active recognition session or not.  The only input is the Interaction.  This will often be used simply to check whether we need to call Reco Initialize or not:

### Reco Register Grammar

Once we have established a recognition session and are ready to do a recognition, we must first register the necessary grammars with the ASR engine:

The only necessary inputs here are the Grammar URI and the Grammar Mode.  Grammar Mode can be set to either "voice" or "dtmf" (depending on what type of grammar it is).  The URI can be set to either a local file location (in which case it must have the form shown above) or an HTTP location.  To register multiple grammars for one particular input, you can place multiple Reco Register Grammar toolsteps in a row, each with its own grammar.

### Reco Input

Now that our session is active and the necessary grammars are registered, we are ready to listen to a prompt and provide input.  Here is what our flow looks like thus far:

It should be noted that you will want to place the prompt play right before the Reco Input toolstep.  Reco Input has a built-in flush audio that provides the ability to barge in.

On the Input tab, you will need to make sure to specify the grammars that should be used.  This is a space delimited list of the grammar IDs which are the output of the Reco Register Grammar toolstep(s), so if you have multiple grammars it would need to look like this:

sGrammarID1 & " " & sGrammarID2 & " " & sGrammarID3

 

You might also be interested in setting the Confidence Level to determine the minimum confidence level that will result in the toolstep taking the Success path.

The Timing tab also has settings of interest:

Here you can set the normal recognition timeouts such as the input timeout, incomplete timeout, complete timeout, and max speech timeout.

 

As you can see, there are multiple output paths.  The ones we are most interested in are Success, No Input, and No Match.  Success means an utterance was provided and it was above the minimum confidence level.  No Input and No Match are self-explanatory.  When a recognition is successful, the output will be XML that looks like this:

### Reco Analyze Result

Now that we have received the results from the recognition engine, we can analyze them to proceed forward with whatever logic we decide.  The XML recognition result from Reco Input (shown above) will be passed in as an input to Reco Analyze Result, along with the Acceptance Confidence and Confirmation Confidence:

 

In our results above we only had one hypothesis, and it had a confidence of 0.89 (which is above the Acceptance Confidence).  For this reason, the Accept Single path would have been taken.  The outputs include Top Hypothesis, Hypotheses, and Hypothesis Count:

Let's say I've lowered the Confidence Level on Reco Input to 0.01.  Now the Recognition Result should be populated with any hypotheses above this confidence.  Now it looks like this:

When Reco Analyze Result is reached, here are the outputs:

**Top Hypothesis**

**Hypotheses**

**Hypothesis Count**

So you can see that since the confidence of our second hypothesis was below the Confirmation Confidence of 0.2, it is discarded.

 

Five of the output paths will be important to us:

  1. Accept Single - This path is taken if a single hypothesis is above the accept threshold.
  2. Accept Multiple - This path is taken if multiple hypotheses are above the accept threshold.
  3. Confirm Single - This path is taken if a single hypothesis is below the accept threshold but above the confirm threshold. This hypothesis should be confirmed with the caller.
  4. Confirm Multiple - This path is taken if multiple hypotheses are below the accept threshold but above the confirm threshold. These hypotheses have to be confirmed.
  5. Rejected - This path is taken if there are hypotheses in the recognition result, but they are all below the Confirm Confidence.



### Reco Get Slot Value

Now that we have the top hypothesis, we want to extract meaningful information from the XML result.  To do this, we need to retrieve specific slot values.  This can be achieved with either Reco Get Slot Value (to retrieve one specific slot value) or Reco Bind Slot Values, to assign each returned slot to a specific variable for further logic.  First we'll talk about Reco Get Slot Value.

The main input field (Hypothesis or Slot) allows any of the XML formats of a hypothesis, slot, or a recognition result.  Since this can take a recognition result, we could simply link Reco Input to Reco Get Slot Value and provide no input for Index, Name, or Min. Confidence, and Get Slot Value will retrieve the top slot from the top hypothesis in the Recognition result (which should be the result with the highest confidence).  Here is what that would look like:

xmlRecognitionResult is the original output we got from Reco Input.  Instead of running it through Reco Analyze Result to get the top hypothesis, we'll just have Reco Get Slot Value grab the the top result.

The problem with this method is that you aren't checking to see if the confidence is in confirmation range or acceptance range. So basically even if the engine returns a result that has 0.01 confidence, you will be moving forward with that as the top hypothesis instead of rightly taking the Rejected path in Reco Analyze Result.

 

Using the xmlRecognitionResult was simply to show that any of the XML formats are fine to use in Reco Get Slot Value.  You would be better off using the Top Hypothesis variable from Reco Analyze Result, this way you know it has a high enough confidence to potentially be valid.  Here is a better example:

Now we are using only the top hypothesis which was in acceptance range according to Reco Analyze Result.  We are looking for the value of the slot named "SWI_meaning".  The important outputs of this toolstep are the Slot Value, the Slot Name, and the Slot Confidence:

 

Going by our latest example, this would set each of the following:

sRecoSlotValue = emergency

sRecoSlotName = SWI_meaning

nRecoSlotConfidence = 0.81

### Reco Bind Slot Values

If you're looking to retrieve multiple values from a returned hypothesis, you can use Reco Bind Slot Values to get them all at once:

This step takes an input of an XML hypothesis, and you can specify the name of each slot and what variable its value will be assigned to.  In our example, the variables would contain the following:

s_value = emergency

s_swi_literal = it is

s_swi_meaning = emergency

### Reco Release

Once you have the necessary information from the recognition engine, whatever logic you desire can be performed upon it.  Once we reach the end of the call, we'll want to call a Reco Release which will end our speech recognition session:

This toolstep needs no additional explanation, you simply give it an input of the Interaction and it will end the ASR session.

When a call is disconnected, a Reco Release will be automatically executed. It should also be noted that there is no reason to call a Reco Release if a call will be using speech recognition again, as this will just add additional overhead when we need to re-initialize the session.

 

There are other toolsteps that can be used, but the ones covered here should be sufficient for most speech recognition scenarios in handlers.  Now we can build a fully functioning test handler to try these out.

## Initiating a VXML session from handlers

The only way to start a VXML session is through handlers.  Generally an Attendant profile will be configured that contains a subroutine initiator which launches the handler containing the VoiceXML initiation logic.  The Attendant profile might only look like this:

The first node is a Set Attribute which sets a call attribute containing the initial VXML document's name.  The second node is a subroutine initiator to call the VoiceXML handler.  The handler itself could be as simple as this:

Step 1 is a Get Attribute to retrieve the name of the VoiceXML document and assign it to a variable (in this case, sDocName).  The main step that matters here is the VoiceXML Initiate:

The Document URI field is from the perspective of the VXML Interpreter server. In this example, I have "http://localhost/vxmlfiles/". This is pointing to the web server on my interpreter server since the interpreter will be the one using this URI to access the document. Likewise, if you are using a local URI (like file://c:/vxmlfiles/test.vxml), this will be the path on the Interpreter and not the CIC server.

 

Once VoiceXML Initiate is called, call control is passed to the VXML Interpreter and nothing more will happen in IP/Handlers until the call is returned.

### Inputs

There are two additional inputs that are useful: Argument Names and Argument Values.  Each is a list of string containing variable names and values that can be passed in to the application.  For example, your Argument Names parameter might contain the following:

And your Argument Values parameter might contain this:

Once you reach the VXML application, you can access these by using just the Argument Name or by using session.ArgumentName:

### Outputs

When returning from VXML, you sometimes want to return information to CIC.  This can be done in the <exit> element.  You can return either one variable or a list of variables.

Returning one variable with expr:

Returning multiple variables with namelist:

This information will be assigned to the Result Data output of VoiceXML Initiate (by default named xmlVoiceXmlResultData):

# Attendant

* * *

## Playing Audio Prompts

There are two main nodes for explicitly playing audio prompts, Play Audio (or Audio Playback) and Play Info.

### Play Audio

Play Audio is used when you want a node that plays audio and does nothing else:

You should set a label for the node, the Audio type, the Audio Name, and the Action When Finished.  We'll focus on the Audio type and Audio Name.

When choosing your source, you can select from the following:

  1. Audio file - standard wav file in the InteractionAttendantWaves directory
  2. Audio source - an audio source defined in IA
  3. Audio file specified by the following interaction attribute - a passed in call attribute pointing to a file in the InteractionAttendantWaves directory
  4. External audio source - an external audio source available to the CIC server (such as an audio source configured by Media Streaming Server)



Normally you will just be choosing a wav file, but feel free to peruse the F1 help if you're interested in the other types.

The Audio Name field will change based on which Audio Type you select.  Audio file will show a dropdown of all the wav files in the InteractionAttendantWaves directory, Audio source will show all available audio sources, Audio file specified... will show a text box in which to enter the call attribute, and External audio source will show all available external audio sources.

### Play Info

Play Info can be used to string together audio prompts and TTS playback of call attributes:

In the example I have here, it will play back the audio file specified (40A_ASR_....) followed immediately by a TTS synthesis of the Eic_CallID call attribute.

You cannot set MRCP optional parameters when using Play Info, so it is very limited in what it can do unless the TTS server only has one voice installed.

## Playing TTS

### Other Tools - Play TTS

To properly play TTS in Attendant, you'll need to add an Other Tools node, then set the Tool to "Play TTS":

As shown in the description, this requires that the input text be previously set in the ATTR_TTS_INPUT call attribute.  You can also set MRCP optional parameters by setting the ATTR_TTS_OPT call attribute.  See this KB for more information on MRCP TTS in Attendant: <https://extranet.inin.com/products/pages/kb-details.aspx?entryid=q137088638401674>

### Play Info

As described in the Play Audio section, Play Info can be used to play TTS as well, however its usage is limited when using MRCP instead of SAPI.

## Speech Recognition

### Speech-enabled Attendant

Speech recognition can be done in Attendant with built-in options.  Most nodes will have a button that says "Configure Speech Recognition...":

Here is what the options look like on a profile:

This basically just lets you set whether speech recognition will be done in Attendant for menus in this profile and/or whether it will be used for company directory.  You can also set the specific speech engine to be used if more than one is enabled.

Here is a schedule:

As you can see, you can set the minimum confidence level, complete timeout, incomplete timeout, and max speech timeout.  You also have the ability to specify the retry prompts.

Lastly you will have all of the other nodes which contain this:

This allows the user to specify the utterances that will cause this Attendant node to be hit next.  The grammar for this is created on-the-fly during runtime.

Speech-enabled Attendant is not good for SSDG projects. All of the recognition is done in base handlers, so implementing KPI calls would require base handler customization (which is generally not recommended, and not allowed at all for CaaS customers). We also have no control over the grammar creation, other than throwing more phrases at it (or taking them out). Overall, we want to avoid this like the plague.

### Calling speech recognition handlers

The proper way to do speech recognition when working with Attendant is to build a re-usable handler that can be called with different parameters any time a recognition needs to be done.  PSO has created a handler and implemented it for a number of customers called PSO_Custom_DynamicRecoEntry.  When using this handler, we can insert all of our CallPath_Interactions subroutines at the correct places to make sure KPI logging is done correctly as well.

# Key Performance Indicators (KPI) Logging

* * *

For more information about implementing KPI in handlers, see the KPI Logging Implementation Guide in P4 (\speechsolutions_main_systest\pub\resources\docs\Tuning\Key_Performance_Indicators\KPI_Logging_ImplementationGuide.docx)

## Overview

Implementing KPI logging for a handler/Attendant integration can get a little complicated.  We are not actively creating new projects using handlers, so any tuning project we get will involve taking an established IVR and fitting in KPI as best we can.  If the project was originally done by PSO, the customer likely has the PSO reco handler, which allows us to more easily track the dialog state and perform recognition-related CallPath_Interactions logging.  If the project was done by the customer or by a partner, it will require some effort to figure out the best way to log everything based on the implementation.

## Handlers

There are ten total KPI handlers that need to be published, however we will only directly interface with five of them.  We will also need to alter some customization point handlers, the recognition handler, and possibly other handlers to deal with DB states or other places where CallPath_Interactions must be executed.  Here are the different handlers:

  1. Base KPI handlers
     1. Interface handlers
        1. SSDG_StartCall_KPI_Logging
        2. SSDG_EndCall_KPI_Logging
        3. SSDG_StartTask_KPI_Logging
        4. SSDG_EndTask_KPI_Logging
        5. SSDG_CallPath_Interactions_KPI_Logging
     2. Supporting subroutines
        1. SSDG_ConvertUTCforUniqueID
        2. SSDG_ConvertUTCtoDateTime2_SQLServer
        3. SSDG_ConvertUTCtoKPITime
        4. SSDG_Create_CallPath_Header
        5. SSDG_Format_RecoResult
  2. CustomSubroutineInitiatorRouter
  3. CustomCallDisconnect
  4. The speech recognition handler (implementation-specific)
  5. Backend lookup handler(s)/Other handlers with prompt plays, branch conditions, etc. (implementation-specific)



 

Unless a scenario requires changes to the base functionality, you shouldn't have to make any alterations to the SSDG_* handlers.  You will however be making changes to the others.

### CustomSubroutineInitiatorRouter

This will already be customized, so you will need to work with whatever is currently present.  The only requirements are the following:

  1. The selection step contains calls for "StartCall", "EndCall", "StartTask", "EndTask", and "CallPath_Interactions"
  2. A Parse String toolstep is present before the selection step to parse out the different arguments that will be passed in from Attendant (we'll go over this more later)
  3. If speech recognition is being used in applications that won't need KPI logging, we'll need to make a copy of the recognition handler (and prefix it with SSDG_) and add a selection option for that



At a minimum, CSIR will look something like this:

 

The Parse String at the beginning of the handler basically takes the p_sSubroutineName variable and puts it into a list of strings. p_sSubroutineName is the value of the "Subroutine" field in a subroutine initiator node in Attendant:

What we will be doing is submitting subroutine names that also contain arguments delimited by a pipe (|). This allows us to pass in information a little more easily than setting a ton of call attributes. When referencing any of these arguments, you can use: GetAt(listVariable, index). So based on the handler shown above, I would retrieve the subroutine name by using:

And I would retrieve the shape by using:

 

### CustomCallDisconnect

This is a customization point that should already be published on the CIC server.  When any call is disconnected from CIC, a handler called ObjectDisconnectMonitor is executed.  ObjectDisconnectMonitor includes a call to CustomCallDisconnect, which is blank by default.  So typically nothing will happen in this handler, however we need to log hangups so we need some logic here to do this.  Here is what happens at a high level:

If the customer already has customizations in CustomCallDisconnect, we will need to work around/with them to make sure both KPI functionality and the original functionality remain intact.

### The Speech Recognition Handler

Depending on the complexity of the handler, this one can get tricky.  I will go over an example with a modified version of PSO's recognition handler.  Essentially this handler gets all of its data from an IP table.  IP tables can be found here in Interaction Administrator:

The IP table contains rows for each specific DM state.  The row might look like this:

This contains the prompt wav file names, grammar file names, DM name, timeout settings, confidence settings, etc.  When a recognition is initiated from Attendant, a lookup is done on this table to retrieve this information.  Since we have a standardized "function", we only need to place CallPath_Interactions toolsteps in a few places and that will cover most of the scenarios for the whole call flow (related to DM states at least).

Since each implementation is different, I will just list the places at which subroutines needed to be inserted in this example:

  1. CallPath_Interactions - right before grammar registration (Interaction Code: S)
  2. Format_RecoResult - right after input is received
  3. CallPath_Interactions - right after Format_RecoResult for the prompt play (Interaction Code: P)
  4. CallPath_Interactions - right after the prompt play CallPath_Interactions (Interaction Code: R)
  5. CallPath_Interactions - right after the input, when there is no input (Interaction Code: T)
  6. CallPath_Interactions - right after the input, when there is no match (Interaction Code: N)
  7. CallPath_Interactions - right after no input, when the max NoInput limit has been reached (Interaction Code: MT)
  8. CallPath_Interactions - right after no match, when the max NoMatch limit has been reached (Interaction Code: ME)



Based on the 3D for a specific project, there may be a need for other subroutine calls as well.

### Backend Lookup Handlers

This will be unique to each project, you must simply find the correct places to run CallPath_Interactions for the Backend Lookup Initiated, Backend Lookup Success, and Backend Lookup Failure.

## Attendant

Depending on the length and complexity of the IVR, most development time will be spent here.  This is where we will:

  1. Track Tasks
  2. Track Calls
  3. Track Authentication
  4. Track Self Service
  5. Track Event Traces
  6. Etc.



 

We'll go over the start of a sample call.  Here we will do the StartCall, and we'll start and end two tasks before moving on to the main IVR.

### StartCall

Currently StartCall is very basic.  You don't need to pass in any arguments, you just call "StartCall":

If there are multiple applications, you will need to pass in an argument with the application name as well and make sure the subroutine call in CustomSubroutineInitiatorRouter is looking for that argument.

### StartTask

StartTask is also pretty simple, you just need to pass in the task name:

### EndTask

EndTask has more arguments, it will usually look like this: 

Those parameters in order are: EndTask, task name, task success (true or false), exit reason, last state, and custom end.

### EndCall

EndCall also has a number of arguments:

The parameters are: EndCall, exit type, exit reason, last state, and custom end.

EndTask and EndCall are the functions you will be dealing with the most in Attendant since there are usually many places where the task and/or the call need to be ended and logged.

In the latest versions of the EndCall handler, the last state will be looked up in the SSDG_LastState call attribute. This call attribute is kept up to date by the CallPath_Interactions handler, which sets SSDG_LastState every time it is called with a valid dialog state.

 

### CallPath_Interactions

The main use of CallPath_Interactions in Attendant will be for prompt plays outside of DM states.  Here is an example:

Parameters: CallPath_Interactions, dialog state, interaction code, recognition result, prompt name, grammar set, backend ID, backend input, backend output, error ID, decision label

The list of arguments can be changed by simply changing the subroutine in CustomSubroutineInitiatorRouter to look for an additional argument. It's good to figure this out ahead of time before you start adding these in Attendant, or you will have to go back and make sure the format of each subroutine call is correct for each node.

### Miscellaneous Attributes

There are some call attributes that might need to be set in Attendant to keep track of something, here are some examples:

  1. SSDG_CallerHangup - if there is a turning-point where a hangup is considered a CallerHangupNormal instead of a CallerHangupEarly, you will want to set this attribute to CallerHangupNormal at that point in the flow
  2. SSDG_SelfServed - once the requirements for a call being SelfServed are met, set this call attribute to True
  3. SSDG_Authenticated - once the requirements for a call being Authenticated are met, set this call attribute to True
  4. SSDG_CallCustomEnd- there are certain places where you might re-use an EndCall node in Attendant, but for one specific path you need to have a custom end on the call.  Leave the argument blank when calling the subroutine and set this attribute to the custom end description and it will be retrieved by the EndCall handler
  5. SSDG_TaskCustomEnd - same with SSDG_CallCustomEnd, except for tasks.
  6. SSDG_LastState - if you are entering a PP state, you'll want to set this beforehand in case the caller hangs up during the prompt.  This will preserve the integrity of the actual last state.
  7. SSDG_Task_Event_Trace - if a task has an event trace, set this call attribute with it
  8. SSDG_Call_Event_Trace - same as Task_Event_Trace, although you will often have multiple of these.  They can be concatenated by setting the call attribute to something like this in Attendant: 

By doing this, you will add the event trace onto the end of the existing event traces.  This will also work for task event traces.  
  




