#### Quarter Goals

Priority goals for the team that we are confident we can meet for the quarter.

Goal  |  % Complete  |  Notes   
---|---|---  
Media Server: Design and initial implementation of framework for i3asr grammar management  |  30%  |  Spent most of the time on the i3asr side.  Media server part is still in infancy.   
  
Media Server: Verify QoS (DSCP tagging) on inbound RTP streams   
|  100%   
|  ﻿DP-583  
Media Server: Support for tone generation in GatewayChannel resource  |  0%  |  IONMEDIA-279 - Higher priority IPv6 related issue preempted this.   
Media Server: Support RTCP-XR (﻿3611)  |  20%  |  ﻿﻿IONMEDIA-293  
Migrate FAX server to use i3config for Coffee  |  99%  |  86768 (in code review)   
  
Protocols: Finish porting DTMF Acceptor into ION  |  50%  |    
Protocols: Implement RecognitionResult in i3speech  |  90%  |    
Protocols: Address any SCRs for MRCP ASR in preparation for SU2 release  |  100%  |    
Protocols: Finish implementation of SNMP Agent Registry  |  80%  |    
Protocols: Investigate adding CPU/thread profiler in QoS Driver  |  100%  |  Investigation complete and 85% implemented.   
Protocols: Start result framework enhancements for inclusion with core-1.4 (coffee)  |  100%  |    
Protocols: Resolve open i3sip/i3sdp/i3inet SCRs  |  ~90%  |    
Protocols: Performance testing and profiling i3inet/i3http  |  10%  |    
Protocols: Resolve SCRs found during testing of Media Streaming Server  |  99%  |  In code review   
Protocols: Add event logging to VoiceXML server  |  100%  |    
Protocols: Finish design of play support phase 2 |  80%  |  Object model in place - creating *.h files for review.   
Protocols: Create i3json library in ION core tier  |  90%  |  The library will be a pull parser similar to the i3xml   
In code review   
Analytics: Packet Loss Handling   
|  20%   
|  Postponed to next Q because of support related work we had to do in Analyzer this Q   
  
Analytics: Design model structures for Unit DB to support TTS   
|  NA  |  4/01 -Postponed to future Q - until we address new algorithms for systhesis that Rivarol is pursuing   
  
Analytics: Research LDA and other signal conditional algorithms for AM improvements   
|  100%  |  2/27 Need to explore variance normalization   
4/01 Tests show consistent improvement on several languages and tasks. Will move to implementation for next Q.   
  
Analytics: Streamline process for converting LVTK Disc. AM's to i3ca AMs   
|    
|  Have already confirmed measurable improvement in accuracy - need to get AMs for all languages done   
2/27 Missing piece was triphone mapping which seems have been addressed now.   
3/14: Tested LDAs efficacy with en-US and fr-CA. Consistently get >30% improvement in FA rejection   
  
Analytics: Research areas for Echo Canceller optimization   
|  30%  |  3/14: Srinath just starting to look into this   
4/1:   
  
Analytics: Complete parallelization work for AM training   
|  90%  |  2/27 Most work is complete - Need optimization. Will test entire process on es-US training   
3/14 Getting i3inet level errors on some clients. Exploring for solution   
4/1: File delete errors nagging the issue   
  
Analytics: Implement new Music Detection algorithms in MSCA   
|  90%  |  2/27 Speed optimization - Most time went into getting PLP in C++ to match up with matlab implementation   
3/14 Preliminary implementation done. Performing large scale testing.   
4/1: Will submit for code reviews this Q and push for completion of testing in ION   
  
Analytics: Research acoustic information based prominence detection   
|  50%  |  4/1: Spectral tilt and duration analysis seems promising - Will continue exploration including test dataset creating.   
  
Analytics: Research algorithms for reducing join issues in unit selection TTS   
|  50%  |  2/27 Explored triangular filter based join cost computation instead of simple MFCC Mahalanobis measure   
       Currently exploring Sinusoidal analysis based synthesis capable of changing prosody without artifacts   
3/14 Sinusoidal analysis based method seems to be in good shape as far as basic synthesis is concerned. Need to explore how it does with join discontinuities and pitch variations,   
4/1: Have not been able to drive this to a reasonable conclusion. Exploring interpolation at joins along several lines (amplitude, spectrum, formants)   
  
Analytics: Complete research for context based FA reduction   
|  100%  |  2/27 All work complete   
  
Analytics: Implement chosen algorithm in ION KWS framework   
|  60%  |  2/27 Created team branch and integrated I2 mfcc front-end to test app   
        Vlack will head rest of design   
4/1 Test harness available in ION using IPP functionality - design will take place next Q   
  
Analytics: New Analyzer languages - Dutch, Australian English, German   
|  90%  |  2/27 - Dutch is in quagmire - model seems OK but accuracy is lacking - Exploring serveral avenues including folding all   
          training data to process. Previously only used 25% to avoid using data with dysfluencies.   
          Australian English - almost done. FOM Model missing   
3/14 Beginning German now. Have all pieces for training model. Working on STP now.   
       Completed updating model for es-US as well.   
4/1: All languages complete except Dutch (waiting on data provider to cleanup some issues)   
  
Analytics: Research stress prediction and symbolic prosody for TTS   
|  90%  |  3/14 Identified papers that we can explore. Based on mfcc analysis.   
4/1  Will explore integrating this with STP next Q   
  
Analytics: Complete testing of i3ASR SRGS support   
|  100%  |  2/27 Completed creation of test set using Samsung data - identified some bugs that are being addressed   
         Attempt collection for data for Mobile Office   
3/14 Continuing to work on speed optimization and bug resolution   
4/1   Some bugs remain - will address next Q - icmeadiaserveraudia level integration work in progress   
  
Analytics: Patent work for FOM   
|  100%  |  2/27 Our work done - change in patent liaison slowed down the good progress   
  
Analytics: Patent work for posterior based KWS   
|  100%  |  4/1 Claims writeup done   
  
Analytics: Patent work for context based FA rejection   
|  90%  |  2/27 Very good progress on this front - need to add some more claims related to future work   
3/14 All info in place. Need to wordsmith the writeup   
4/1 Claims writeup almost complete   
  
Analytics: Patent work for other ancillary ideas in KWS   
|  50%  |  Get material ready for provision on filler based KWS and class based MARS discriminative training   
3/14 Work started on posterior based KWS   
4/1 Claims writeup for MARS complete   
  
Analytics: Patent work for frequency domain based EC   
|  100%  |  2/27 Srinath took first cut at this. Need more progress before we can send it off to attorneys.   
3/14 Have a concrete plan in place to have something ready by middle of next week for Margaret to go over   
4/1 Claims writeup complete   
  
  
#### Overflow Goals

Lower priority goals that would be nice to work on if the goals above are accomplished.

Overflow Goal  |  % Complete  |  Notes   
---|---|---  
Protocols: IC-91228 - Investigate VoiceXML Interpreter Server that stops responding after 100k+ calls  |  0%  |    
Protocols: IC-90599 - Clarify which Parameters require restart to change  |  0%  |    
Protocols: Complete investigation of NDM Spelling and Email modules  |  0%  |    
Protocols: Investigate supporting LumenVox as 3rd party ASR engine  |  100%  |  We decided not to support their current ASR engine until they have a few issues resolved - expected in Q2 
