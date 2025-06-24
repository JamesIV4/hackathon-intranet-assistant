### Introduction

As explained in this page's parent page, the VoiceXML interpreter has its own caching facilities for the resource files (grammar files and prompt files) that it uses.  This caching was necessary when the Reco Subsystem, the ASR engines and TS were not able to fetch HTTP URI's.  With these subsystems now able to do HTTP fetches, it could be more efficient if VoiceXML simply passed the desired HTTP URI's through to these systems without doing its caching.

An SCR - IC-111640 (Add support for passing HTTP URIs for prompt and grammars directly through VoiceXML) - has been created suggesting that we allow the setting of a couple of new configuration parameters to bypass this caching level.  This pages looks at the effort involved for this, and describes some of the potential problems.

Note that even after these changes, the VoiceXML interpreter will still have to cache resource files (and pass them up to the IC Server) that are local to the interpreter (i.e., they have a file:// URI).

 

### New Configuration Parameters

The following new configuration parameters will be added to the VoiceXML web configuration page.

  *     grammarCaching



This will be a boolean value (true/false) that will determine whether or not grammar files with an HTTP URI are cached by the VoiceXML interpreter or not.  The default will be "true".

  *     promptCaching



This will be a boolean value (true/false) that will determine whether or not prompt files with an HTTP URI are cached by the VoiceXML interpreter or not.  The default will be "true".

 

The following files/routines will need to be changed:

-1 incomplete 23 incomplete ConfigManager.cpp and ConfigManager.h (list of parameter names) 24 complete Need to add bool ConfigManager::getGrammarCaching() 25 incomplete Need to add bool ConfigManager::getPromptCaching() 26 incomplete ConfigServer.cpp/create_web_config_server()

 

### Grammar File Considerations

  * The following methods will need to be changed: 19 complete SessionResourceCache::loadURIGrammar()   




  


This change was made in IC-130183.  As of the time of this writing, no cache control parameters (e.g., the fetchtimeout, maxage, and maxstale attributes) are passed on to the Reco subsystem.  


  


### Prompt File Considerations

  * The following methods will need to be changed: 15 incomplete SessionResourceCache::prefetchPrompt() 18 incomplete PromptResource::setFile()  
16 incomplete SessionResourceCache::queuePromptToSession() 17 incomplete PromptResource::queueToSystemLocalCache()



  


These changes are described in IC-111640.

  


### Documentation

There will have to be user-facing documentation changes.  Tasks:

20 incomplete Describe the new configuration parameters and their effects. 21 incomplete Get a screen shot of the web configuration page with the new parameters. 22 incomplete Describe the procedure for adding the new parameters to an existing installation.

 

  


### Questions/Potential Problems

  1. I don't currently see a mechanism for passing any cache control parameters specified by the VoiceXML application (for use fetching grammar files) down to the Reco Subsystem. (Ex. the fetchtimeout, maxage, and maxstale attributes are not supported by Reco Subsystem.)
  2. I don't currently see a mechanism for passing any cache control parameters specified by the VoiceXML application(for use fetching prompt files) down through TSAPI.
  3. I don't currently see a mechanism for telling TSAPI to prefetch a prompt file.  

  4. This may complicate the handling of "alternate text prompts".  Currently, if VoiceXML can't fetch an HTTP prompt file, it will know this and use the alternate text specified by the application (if any).  But I don't think that working through the TSAPI will give me this level of control.  The VoiceXML interpreter won't know if the HTTP fetch fails.  I don't think that TSAPI gives me the ability to specify the whole <speak> element that the BladewareVXML library passes our VoiceXML interpreter code.



 

 
