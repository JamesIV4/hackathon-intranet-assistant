#### Quarter Goals  
  
Priority goals for the team that we are confident we can meet for the quarter.

Goal| % Complete| Notes  
---|---|---  
Media Server: Implement media buffer support for synchronization points| Green100%|    
Media Server: Add support for video in RTP Receiver| Grey0%|    
Media Server: Complete design for ASR diagnostics| Green30%|    
Media Server: Complete en-AU builtin grammars| Green100%|    
Media Server: Complete design for MxN for VoiceXML| Grey0%| DP-1524  
Media Server: Implement billing and payment VoiceXML module for Amren| Green100%|    
Media Server: Complete SNMPv3 implementation and push into systest| Green100%|   
Media Server: Get media tier test applications running on Linux| Grey0%|    
Media Server: Complete implementation of media server REST API| Green90%|   
Media Server: Complete design documentation on ICE integration| Green75%|   
Media Server: Complete ICE integration in UDP endpoint| Green75%|    
Media Server: Add RTCP XR support| Grey0%| <https://tools.ietf.org/html/rfc3611>  
Media Server: Integrate latest SpiderMonkey engine into edge| Grey0%|    
Media Server: Add support for SASF video recordings| Green50%|   
Media Server: Add WebSocket server support| Green100%|    
Media Server: Add barge-in support in Edge| Green100%| IONMEDIA-1576  
Media Server: Implement VoiceXML scripts for Voicemail Phase 2 in Edge| Grey0%|    
Research: TTS old languages to be fine tuned| Green80%| fr-CA - liaison prediction improvement (done)en-AU - quality improvement (will be finished week of 4/6). Dictionary expansion is in progress.en-GB - fixed phone discrepancy in modelde-DE - wrapped up loose ends. General compound handling is being developed for use across languagesProject Team: Language Research, Advanced Prototyping  
Research: TTS Error Analysis| Green100%| Set up a process to categorize and address issues:-Lexicon  
-Text normalization  
-Model issues  
-i3tts issuesWorked through the first round in de-DE, fr-CA, and en-AU.Project team: Veera, Aravind, Rajesh  
Research: TTS new languages| Green70%| pt-BR - push towards alpha versionja-JP - start initial progressProject Team: Language ResearchProject progressing for both languages.  
Research: Data Archival| Yellow40%| Attempt model building related data pulls for a language via perforce  
Project Team: Aravind, Veera and Ananth3/15 - Consolidate folder has been in use this Q. We are filling up holes as we encounter them. Will schedule call to discuss adding to perforce soon  
Research: DNN based acoustic models for i3ASR| Green60%| Attempt DNN models using i3ASRdatacollection for i3ASR use - see if MIPS usage is under controlProject Team: Roger, Ananth3/31 - DNN models in good shape. Phoneme accuracies in 80% range. Need to feed those to i3ASR and see what the word accuracies will be. MIPS usage is about 400. Twice that of what we see with GMMs. Will continue work next Q.  
Research: Voicemail Datacollection| Green100%| New round VM data collection so we can use for better LM building as well as testingProject team: Linda, Emma, Aravind, Konstantin, RohithExpect the final 5 sets of V3 to be done by the week of 4/6. NE tagging will overflow to next Q.  
Research: Voicemail Transcription - LM data| Green70%| Explore new data sources for generic LMProject team: Veera, Aravind, Konstantin, Rohith3/15 - SWB+Fisher and Cantab being explored  
Research: Voicemail Transcription - LM Research| Green70%| LM model research - Explore better interpolation and RNN based LMsProject team: Aravind, Konstantin, Rohith3/15 - Rohith has done experiments where RNNs seem to help with number recognition but are suffering with dysfluencies.  
Research: Voicemail Transcription - Named Entity| Green90%| complete CRF/rule based work to identify names and numbersProject team: Darshan, Konstantin, Rohith3/15 - After a lot of experimentation we have decided to give this a break as underlying word accuracy needs to be improved first to close to 70% before NE extraction can be more reliable.  
Research: TTS Research - Outlier Detection| Green80%| Fine tune approach and possibly file for patentProject team: Veera, Aravind3/15 - Have a good setup to do this as a hybrid method. Will have a writeup ready to present to Margaret by end of the Q  
Research - TTS Quality improvement| Green70%| Enhancement of spectral features using DNN/sinusoidal modelling.Eigen voice training with new approaches for template generationProject Team: Rajesh, Rivarol, Veera3/15 - DNN exploration in progress but no tangible output yet. Eigen templates are better now. Found V/UV decisions and plosive noise profile to have a big impact more so than the eigen template. Also exploring several equalization methods on a per language basis.  
Research - VAD for ASR| Green80%| Complete algorithm prototype and verify MIPS usage for NNMF based VAD and adjust algorithm if necessaryProject team: Rivarol3/15 - Have implemented and tested the algorithm on a lot of data. Is a definite improvement over spectral flux method. Waiting on some tuning parameters to be exposed so users can control sensitivity.  
Research: TTS enhance Say-As Support| Green40%| [SCR IONMEDIA-1698](http://devjira.i3domain.inin.com/browse/IONMEDIA-1698)Project Team: Language Researches-US complete; fr-CA (in review); en-US (in progress).  (en-GB, en-AU, de-DE will roll over to Q2.)  
Research: TTS Text Processing Improvements| Yellow70%| Project Team: Language ResearchPorting en-XX CAD-module changes to other lgs (fr-CA in review, es-US and de-DE in progress)Enhanced tts_lexicon_test to use multi-level tests (en-XX done, fr-CA in review, es-US and de-DE in progress)(Will continue next Q. Pushed back b/c of new lg development.)  
Components: i3tts - Add support for user defined dictionaries| Yellow25%| Prep work on i3tts is completed. Working on changes needed on MediaServer.  
Components: i3tts - Support language development| Green100%| General support to Linguists, IPA changes, Lexicon tests ...  
Components: i3asr - Complete code refactoring for DNN support| Yellow50%| Paused development as computational cost of DNN is too high.  
Components: i3asr - RecognitionSearch optimization| Yellow50%| Accuracy improvements - dynamic beamwidth, estimating beamwidth based on grammar, changing token discard strategy, merging overlapping paths.All accuracy improvements came with higher MIPS. This is still a work in progress.  
Components: i3asr - Add diagnostics, create utilities as needed| Red10%|    
Components: i3asr - Improve digit recognition with new models/graph layouts| Yellow80%| Several digit specific models, MFCC v/s LDA.Increase beamwidth and make silences optional.  
Components: i3ca - MSCA support and improvements.| Green100%| First time we have no new cases. 7 different regions all in EMEA/APAC.Began working on a large automated regression test.  
Components: Design REST API and a basic interface for voicemail transcription| Yellow80%| Exception handling and UI improvements.  
Components: Add new features to analysis tab of speech tuner| Yellow90%| Analyze, Recorder, Test changes are complete.  
Components: Opus codec optimization| Yellow10%| Optimized CELT, but we need SILK. Also, we may not need to optimize as other teams are working on it.  
Components: Support/bug fixes (i3tts/i3asr/i3kws)| Green100%|    
  
 

#### Technical Debt

SCRs that we need to address as part of ongoing maintenance of our released products.

SCR| % Complete| Description| Notes  
---|---|---|---  
IC-126026|  |  |    
IC-113566|  |  |    
  
#### Overflow Goals

Lower priority goals that would be nice to work on if the goals above are accomplished.

Overflow Goal| % Complete| Notes  
---|---|---  
Media Server: Integrate latest GCC compiler| Green100%|    
 |  |    
 |  |    
  
 

 
