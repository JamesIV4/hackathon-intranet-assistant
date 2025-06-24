#### Quarter Goals

Priority goals for the team that we are confident we can meet for the quarter.

Goal  |  % Complete  |  Notes   
---|---|---  
Media Server: Implement license changes and check for duplicate IC licenses  |  95%  |  GA: IC-85602, IC-85605, SU1: IC-85601  
Media Server: Prevent DTMF tones from being recorded for PCI compliance  |  10%  |  IONMEDIA-159, IC-82034 (waiting on TS for system level testing)   
Media Server: Prevent DTMF digits from being logged in trace log for PCI compliance  |  100%  |  DP-137 (waiting on TS for system level testing)  
Media Server: Add support for line-in and broadcast endpoint to audio source  |  100%  |  For external hold music support (with media streaming server) IC-48616  
Media Server: Design of media server conference peering  |  100%  |    
Media Server: Initial peering support in media server  |  100%  |  Based on peering design, make sure media server conference object has facilities to support initial peering (for testing by TS team members)   
Protocols: MRCP ASR Server code complete  |  100%  |  Potentially have something for testing to start playing around with   
Protocols: Complete IPv6 support into  |  75%  |    
Protocols: Add line-in support to  |  100%  |  DP-275  
This will allow controlling the external music source through MRCP. That way the impact on the TS and media server infrastructure is reduced (re-use infrastructure already present for TTS).   
Protocols: Complete i3snmp protocol implementation for SNMP v1 and v2  |  100%  |    
Protocols: Complete i3smi management objects implementation  |  100%  |    
Protocols: Complete design for SNMP v3 support  |  20%  |    
Protocols: Complete i3speech ABNF parser  |  100%  |    
Protocols: Complete i3speech AST composer  |  100%  |    
Protocols: Complete i3speech PLS parser  |  70%  |    
Protocols: Complete implementation for i3sip digest authentication  |  100%  |  Needs to be promoted and tested via tasip   
Protocols: Start implementation of SNMP MIB parser and serializer  |  100%  |    
Protocols: Start design of play support phase 2 |  60%  |    
Speech Analytics: I3ChatCorpus  |  100%  |  Complete concept labeling of speech data and cleanup of the chat text data for concepts.   
  
Speech Analytics: Research Festival based speech synthesis -   
|  100  |  Continue work from Q2 and create voice based on our preferred voice talent   
Understand the areas that need work for improved voice quality   
Compare HTK and I3 based phoneme alignment performance   
Migrate festvox, Festival and Flite to run under Cygwin   
Integrate Lexicon/STP if necessary   
  
Speech Analytics: Prototype basic infrastructure for i3ASR   
|  100%  |  Ability to perform reco on SRGS specified grammars   
Identify areas that need optimization   
9/29: Main areas left are support for external grammar/rule references and PLS support   
  
Speech Analytics: Research Concept Discovery   
|  0%  |  Phector based concept discovery using algorithms identified so far including LSI   
9/29 - Postponed to next Q. DVS beta and need for some labeled data took time away from experimentation,   
  
Speech Analytics: Research Phoneme Recognition   
|  100%  |  Improve performance of Julius based phoneme recognition   
LM improvements to handle I3ChatCorpus   
9/29 - Best phoneme accuracy of about 68% on WSJ corpus. Still some areas for improvement being pursued.   
  
Speech Analytics: Canadian French Support   
|  30%   
|  Depends on when we acquire speech data   
9/29 - Postponed to next Q because of delay in data procurement.   
  
Media Conference Signal Conditioning - Echo Canceller   
|  100%  |  Code complete for new echo canceller including template for Matlab code   
9/29 - C++ port works better than Matlab code in most cases except when echo level is low or during double talk. 5-6 MIPS on average.   
  
Media Conference Signal Conditioning - Echo Canceller Test cases   
|  50%  |  Test case creation and processing for G16X standards - postponed to next Q. Will continue work based on C++ implementation.   
  
MSCA - Research new algorithms or improvements to babble and music detection  |  40%  |  Continue work similar to tone-detection post processing to identify music detection issues and babble noise related issues from support cases   
9/29 - Some interesting features being researched. Beat detection features being researched.   
  
MSCA - DTMF   
|  100%  |  Complete implementation and testing   
9/29 - Working on gap resiliency and further tests based on non-Bellcore datasets.   
  
Spotability Patent - Initial Work   
|  100%  |  9/29 - Basic discussions with attorney complete. Identified/studied/reviewed several  relevant patents/prior art cases.   
  
  
#### Overflow Goals

Lower priority goals that would be nice to work on if the goals above are accomplished.

Overflow Goal  |  % Complete  |  Notes   
---|---|---  
Protocols: Complete i3http NTLM direct server support  |  0%  |    
Protocols: IONCORE-311 \- Provide a way for i3inet to cancel a transaction  |  100%  |  
