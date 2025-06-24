# Sequencing plays with MRCP

The following page documents how plays using an MRCP synthesizer are sequenced. This information is based on the [Draft 17 of MRCP spec](http://tools.ietf.org/id/draft-ietf-speechsc-mrcpv2-17.txt).

## Synthesizer State Machine

The synthesizer maintains a state machine to process MRCPv2 requests from the client. The state transitions shown below describe the states of the synthesizer and reflect the state of the request at the head of the synthesizer resource queue.

## SPEAK Method

The SPEAK method initiates a speech synthesis and streaming. The SPEAK method can carry voice and prosody headers that alter the behavior of the voice being synthesized, as well as a typed media message body containing the actual marked-up text to be spoken.

When applying voice parameters there are 3 levels of precedence: 

  1. The highest precedence are those specified within the speech markup text.  
2\. Followed by those specified in the headers of the SPEAK request (hence apply for that SPEAK request only).  
3\. Followed by the session default values which can be set using the SET-PARAMS request and apply for subsequent methods invoked during the session.



If the resource was idle at the time the SPEAK request arrived at the server and the SPEAK method is being actively processed, the resource responds immediately with a success status code and a request-state of IN-PROGRESS.

If the resource is in the speaking or paused state when the SPEAK method arrives at the server, i.e. it is in the middle of processing a previous SPEAK request, the status returns success with a request-state of PENDING. The server places the SPEAK request in the synthesizer resource request queue. The request queue operates **strictly FIFO** : requests are processed serially in order of receipt.
