### Introduction

The MRCP protocol is designed to allow a client device to control media processing resources on the network. Some of these media processing resources include speech recognition engines, speech synthesis engines, speaker verification and speaker identification engines.

### About MRCP

  * MRCP uses SIP
  * [MRCP v2 draft specification, version 24](http://tools.ietf.org/html/draft-ietf-speechsc-mrcpv2-24.txt)
  * MRCP uses SDP with the offer/answer model described in [RFC 3264](http://www.ietf.org/rfc/rfc3264.txt) to setup control channels.
  * Sequencing plays with MRCP



#### Design

  * [Technical Overview](http://perforce:8080/depot/systest/eic/main/products/eic/resources/mrcp/docs/MRCP Support in xIC.doc)
  * [Configurations](http://perforce:8080/depot/systest/eic/main/products/eic/resources/mrcp/docs/MRCP Configurations.doc)
  * [Installer Requirements](http://perforce:8080/depot/systest/eic/main/products/eic/resources/mrcp/docs/MRCP Installer.doc)
  * Client Interfaces
  * New Features in 4.0



### Documentation

  * [IA MRCP container documentation](http://wiki.inin.com/bin/view/ClientTeam/MRCPContainer)
  * Installing MRCP
  * MRCP Technical Reference
  * 


### Testing

  * [MRCP Test Plan](http://perforce:8080/depot/systest/EIC/main/products/eic/resources/mrcp/docs/MrcpMajorRelease30SU2.doc)



### Schedule

Feature  |  Component  |  Updated  |  SCR  |  % Complete  |  Days  |  Finish Date  |  Developer   
---|---|---|---|---|---|---|---  
MRCP Client API  |  Define Client Interfaces  |   |  48473 |  100%  |  5  |  1/1/2008  |  Rod Francisco   
  
|  Integrate IONs AIO  |   |   |  100%  |  3  |  1/1/2008  |  Rod Francisco   
  
|  Message Classes  |   |   |  100%  |  2  |  1/1/2008  |  Rod Francisco   
  
|  Header/Message Parsers  |   |   |  100%  |  3  |  1/1/2008  |  Rod Francisco   
  
|  Synthesizer  |   |   |  100%  |  5  |  2/1/2008  |  Rod Francisco   
  
|  SIP Connectors  |   |   |  100%  |  5  |  1/1/2008  |  Rod Francisco   
  
|  Boost Tests  |   |   |  100%  |  5  |  1/1/2008  |  Rod Francisco   
  
|  MRCP Test Server  |   |   |  70%  |  5  |   |  Rod Francisco   
MRCP Subsystem  |  Service  |   |   |  100%  |  3  |  1/1/2008  |  Rod Francisco   
  
|  Configuration  |   |   |  100%  |  5  |  2/1/2008  |  Rod Francisco   
  
|  Notifier API  |   |   |  100%  |  3  |  1/1/2008  |  Rod Francisco   
  
|  Session Management  |   |   |  100%  |  5  |  2/1/2008  |  Rod Francisco   
  
|  Server Management  |   |   |  100%  |  5  |  2/1/2008  |  Rod Francisco   
  
|  SIP Integration  |   |   |  100%  |  4  |  2/1/2008  |  Rod Francisco   
SIP Engine  |  Add support for MRCP  |   |  49257 |  100%  |  3  |  1/1/2008  |  Rod Francisco   
Audio Lib RTP Source  |  RTP Source  |   |  48474 |  100%  |  5  |  2/1/2008  |  Rod Francisco   
  
|  Integration Tests  |   |   |  100%  |  3  |  2/1/2008  |  Rod Francisco   
TS Integration  |  Support for MRCP Plays  |   |  48475 |  100%  |  10  |  2/1/2008  |  Rod Francisco   
  
|  Support for RTP Source  |   |   |  100%  |  2  |  2/1/2008  |  Rod Francisco   
  
|  Integration Tests  |   |   |  100%  |  1  |  2/15/2008  |  Rod Francisco   
IA configuration  |  Add MRCP server(s) config in IA  |   |  49345 |  100%  |  1  |  2/22/2008  |  Stefan Okrongli   
Install  |  Add MRCP client to install  |   |  58326 |  100%  |  1  |   |  Mark Stumpf   
Integration Tests  |  Test against Loquendo Speech Suite  |   |   |  100%  |  2  |  2/15/2008  |  Rod Francisco   
  
|  Test against Nuance Media Server  |   |   |  100%  |  2  |  2/15/2008  |  Rod Francisco   
Documentation  |   |   |  48473 |   |   |   |  Bj Sumner   
  
### Tools

#### mrcp_synthesizerU.exe

#### rtp_receiverU.exe
