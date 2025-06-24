**Projects**| **scrs**| **members**| **22-Jul**| **5-Aug**| ~~**19-Aug  **~~ **26-Aug**| **9-Sep**| **23-Sep**| **30-Sep**  
---|---|---|---|---|---|---|---|---  
ITTS: User defined dictionaries | IONMEDIA-1083| Adrian| ~~complete code~~ reviews & submit| ~~address issues found in review~~ & submit|  | Fix bug reported in code-review|  | ~~Code review with new SsmlEntry (icmediaserver) and needed i3tts changes~~  
ITTS: Voice volume balancing| IONMEDIA-2743| Srinath|  |  | ~~Identify a strategy, methods that need to be changed and start code changes.~~| ~~Complete review~~ and submit code changes|  |    
ITTS: Prototype concatenative voice model|  | Adam| ~~conduct design discussion & document~~| ~~hash out concatenative model design~~[LINK](https://confluence.inin.com/display/~Adam.Paugh/Concatenative+ITTS+voice)| ~~begin implemenation of concatenative model~~|  Complete basic concatenative model builder| ~~Complete basic concatenative model builder~~| ~~Add features to concatenative model builder~~  
ITTS: zh-CN|  | Adam| ~~implement word tokenization for zh-CN ITTS~~| ~~zh-CN tokenizer support~~| ~~zh-CN tokenizer support~~| ~~zh-CN tokenizer support~~| ~~zh-CN tokenizer support~~| ~~zh-CN tokenizer support~~  
ITTS: es-ES|  | Emma| ~~finalize corpus/dictionary~~|   |  | CAD syntax upgrades| ~~CAD syntax upgrades~~|     
ITTS: it-IT|  | Emma|  |  |  |  |  |    
ITTS: interpolation|  | Tan|  | analysis of interpolation issue: how the MCEPs affect the spectrum|  |  |  |    
 |  |  |  |  |  |  |  |    
ISR: Grammar parameters support| IONMEDIA-2432| Adrian|  | ~~analyze the requirements and clarify the scope~~~~evaluate the code changes that need to be done~~| ~~Identify a list of parameters and grammars where this feature will be supported~~|   |  |    
ISR: Improve confidence estimation|  | Ananth| ~~evaluate new NN & compare results~~| ~~Work with Srinath/Ram on coding up new features and creating dataset for training~~|   | ~~Complete & submit code changes in review~~|  | ~~Study features' behavior under simple v/s complex grammar conditions~~  
 |  | Srinath| ~~summarize other methods in literature~~| ~~Implement 2 features identifed: NoMatchProb & HypothesisStability~~|  |  |  |    
 |  | Roger|  | ~~Train an optimized NN for confidence estimation~~| ~~Identify the best feature set and redo the parameter optimization~~|  Continue to support model building if the dataset is available|  |    
 |  | Ram|  | ~~Continue work on the background decoder~~|   |  |  |    
ISR: Improved VAD implementation| IONMEDIA-1607| Rivarol| ~~Finish New VAD Implementation - Report Initial Result~~| ~~Re-implement sensitivity for CepstrumVAD~~| ~~Investigate Keras for DNN based VAD~~  | Address comments in code-review & submit~~Error analysis of NN-VAD with transient noises~~|   |    
ISR: es-ES|  | Emma| finalize testdata|  |  |  |  |    
ISR: it-IT|  | Emma|  |  |  |  |  |    
ISR: zh-CN|  | Tan|  | Test character-based grammarTest asr benchmarks w character-based model| ~~asr grammar testing~~|  asr benchmarks|  |    
ISR:fr-FR|  | Ram|  |  |  | asr benchmarks| asr benchmarks|    
 |  |  |  |  |  |  |  |    
DataAnalysis: Delta Dental (DD-1)|  | Ram| ~~determine baseline accuracy & presentation~~|  |  |  | Ram: Error Category Analysis|    
 |  | Tan| ~~report ISR performance with parameter tuning~~|  Evaluate performance by grammar category| ~~Evaluate performance by grammar category~~|   | Emma: Error Category Analysis|    
DataAnalysis: Delta Dental (DD-2)|  | Emma| ~~get new data (DD-2) organized to be sent for transcription~~ (ongoing)| Kick off transcription with LionBridge| Kick off transcription with LionBridge|  |  |    
DataAnalysis: ISR@ININ|  | Emma| ~~Ananth to get data collection turned on~~| ~~Ongoing data collection;~~  
~~Kick off transcription with SDE's~~| ~~Ram: prelim analysis on days 1-2 (ISR~~ & Nuance)| Tan: initial results page (once transcriptions complete)| Tan: initial results pageRam: compare results against Nuance|    
DataAnalysis: Techniques|  | Ram|  | Literature survey on choosing training data when no transcription;~~Draft initial suite of scripts for prepping initial data/results~~| ~~Signal to Noise Ratio Tool~~  | ~~Ram: check in tools~~|   |    
 |  | Tan|  |  | ~~Timeout 'silence' Detector Tool~~|   | check in timeout 'silence' detector tool|    
 |  |  |  |  |  |  |  |    
MSCA: Continued support|  | Jason| ~~Continued case support (Japan, France)~~| ~~Continued case support (US, Japan, France)~~| ~~Continued case support (France, Japan, Brazil, LATAM PC)~~| ~~Continued case support, research[IONMEDIA-2796](https://devjira.inin.com/browse/IONMEDIA-2796)~~| ~~Continued case support,~~ implementation of [IONMEDIA-2796](https://devjira.inin.com/browse/IONMEDIA-2796) (pushed to Q4 since it's more complex and has many existing issues)| ~~Continued case support~~  
MSCA: [Audio Pattern Detection](https://confluence.inin.com/display/~Jason.McDowell/Audio+Pattern+Detection)|  | Jason| ~~Research: reduce the top fingerprint candidate matches to unique set.~~| ~~Determine how to weed out poor (auto-generated) fingerprint candidates~~| ~~Code heuristics to weed out poor fingerprints and validate confidence results~~|  Methodology documentation and ~~review implementation options~~|   | (implementation for Q4)  
 |  |  |  |  |  |  |  |    
Research: Speaker change detection|  | Roger| ~~demo of prototype algorithm~~| ~~Tabulate SCD accuracy on TIMIT using NNSC-based patented method~~| ~~Switch the similar methodology of NNSC-based SCD from TIMIT to YOHO and get baseline accuracy~~| ~~Get best speaker classifier using YOHO and prepare the real meeting data~~| ~~Identify the major difference between ideal and real-world dataset~~|  Demo SCD on meeting data  
Research: FB+DNN|  | Ananth| make feature calculator parameters model driven~~create app to write our FB features~~|   | Work with Naresh/Rivarol on building a model model based on FB features.(Found discrepancy in Ananth & Naresh's builds)| ~~Sort out differences~~ and get an initial model trained.Prep for testing in i3asr.| prep for testing in i3asr(Not yet needed, we've not been able to build a better model)  
|    
Research: STP language modeling|  | Roger|  | Summarize existing methods in literature| Initialize the grapheme-to-phoneme conversion using LSTM RNN| summarize existing methods in literature|  |    
 |  |  |  |  |  |  |  |    
i3cm: Integrate with hpaa|  | Suresh| Look at HPAA changes required for i3cm and initial design ( only husk- HPAA Element/Proxy).| ~~Look at HPAA changes required for i3cm and initial design ( only husk- HPAA Element/Proxy).~~| ~~ConversationAnalyzer element/proxy implementation.~~| ~~Address any changes required from code review and complete them. Follow up media server team about hooking them to icmediaserveraudio library.~~|   | ~~Code is in review.~~  
IPP: Investigate alternate implementations|  | Suresh| ~~IPP 9.3 upgrade; provide list of IPP methods used~~~~Unit Test all the changes related to ipp team branches again as  underlying library changed~~Review ipp changes(audit list) with FelixW/KevinO and our Team.| Review ipp changes(audit list) with FelixW/KevinO and our Team.~~Verify all the codecs are working in IPPSPeechcoding~~| ~~List all ipp methods used in G.729, GSM, G.726, G.169 ALC.~~| ~~Evaluate G.729 open source implementation with IPPSpeechCoding.~~~~Follow up with Adam Hardy and prepare for push.~~~~Remove unused code from IPPSpeechCoding.~~~~Review IPP methods list used in codecs with group.~~|   | ~~Team branches upgraded to IPP 9.0 update 3 and passed regression testing and performance testing. Team branch push is in code review.~~~~Evaluated and proposed alternate source code for GSM, G.726, and G.729 codec. Integrated those code with our build system and they are shared.~~      
Newly added projects|  |  |  |  |  |  |  |    
Voice biometrics|  | Ananth|  |  |  | ~~Get project kicked off. Identify algorithms and components needed. Document.~~~~Completed the interfacing and testing code~~| ~~Compare front-ends and formalize our version~~| ~~Test system - across larger speakers, datasets, languages~~  
 |  | Srinath|  |  |  | ~~Get familiarized with Keras~~|  Get a 100 speaker (TIMIT) classification network trained|  
