## Introduction

The SRTP protocol 3711does not specify the means for key exchange between the endpoints to establish the secured streams.  We currently support SDES (Session Description Protocol Security Description) as specified in 4568 to communicate keying material between endpoints.  SDES requires confidentiality of the key transport mechanism as the keys are carried in the signaling protocol (SDP in SIP over TLS).  That means any intermediary that processes the SDP sees the keys.  Instead of using SDES, WebRTC media specification instead mandates DTLS-SRTP (5764).  DTLS (Datagram Transport Layer Security) specifies a protocol to use TLS with unreliable datagram (e.g. UDP) transports.  While DTLS provides encryption and authentication of data in the datagrams, DTLS-SRTP only uses DTLS for key establishment but then uses SRTP for encryption and authentication.  Unlike SDES, DTLS-SRTP does not require confidentiality of the signaling channel as it is not used to exchange secret information.  To prevent man-in-the-middle attacks on the DTLS key exchange, certificate fingerprints are exchanged through the signaling channel instead.  As the fingerprint does not have to be secret, only integrity protection of the signaling channel is required to prevent tampering.

## Current SRTP Support in HPAA

SRTP simply represents a "bump in the stack" between the sockets receiving/sending the UDP packets and the RTP/RTCP receiver and sender.  This is reflected in the HPAA elements SrtpReceiveElement and SrtpSenderElement which can be inserted between the UdpReceiverElement/UdpSenderElement and RtpReceiverElement/RtpSenderElement/RtcpElement elements in an HPAA graph.

 

Endpoint with SRTP

As we until now only supported SDES, the master keys for the SRTP Receiver and SRTP sender are provided out of band and and set by the application HPAA graph.  With SDES the sender and receiver SRTP channels use separate master keys.  Each sender side generates a key and sends to the corresponding receiver as part of the session negotiation.  Note that this is unlike with the regular media payload types where the offerer provides the media types it is willing to receive.  That means the offerer offers the media types it is willing to _receive_ and provides the SRTP master key it will be _sending_ with. 

## Proposed Integration of DTLS-SRTP

With DTLS-SRTP the key exchange occurs in-band and the master keys for both receiver and sender are are derived from one key exchange through TLS Keying Material Exporters (5705).  On the other hand, DTLS-SRTP treats the RTP and RTCP streams as separate sessions _unless_ RTP/RTCP multiplexing (5761) is used.  WebRTC endpoints are required to support for RTP/RTCP multiplexing.  It also requires support to send RTP and RTCP to different destination ports for backwards compatibility (see <http://tools.ietf.org/html/draft-ietf-rtcweb-rtp-usage-06#section-4.5>).  As multiplexing considerably reduces the protocol and resource overhead, may thus only support DTLS-SRTP with multiplexed RTP/RTCP.  The reasoning being that we have to support DTLS-SRTP for communicating with WebRTC endpoints and they are required to support RTP/RTCP multiplexing.  Note that WebRTC also requires symmetric RTP/RTCP (4961)..  The media server already uses symmetric RTP and RTCP. 

The following figure shows a proposed media endpoint topology to implement the features necessary for WebRTC:

DTLS-SRTP Endpoint
    
    
      
    

All packets for RTP, RTPC, DTLS, and STUN will be transferred through the same socket.  We thus need a HPAA element that identifies and demultiplexes the receiverd packets into the four protocols.  Fortunately, this only requires inspecting at most the first two bytes of the packets according to the following rules:

1st Byte| 2nd Byte| Protocol  
---|---|---  
128...191| 0...63, 96...191, 224...255| RTP  
128...191| 64...95, 192...223| RTCP  
18...63| *| DTLS  
0...1| *| STUN  
  
 

Note: If we wanted to support separate ports for RTP and RTCP (i.e. not multiplexed RTP/RTCP), the diagram would have to be as follows.  Clearly the added complexity is only worth it we can't get away with only supporting DTLS-SRTP with multiplexed RTP/RTCP.

DTLS-SRTP Without RTP-RTCP Multiplexing

 

## Relevant RFCs

The following table lists the RFCs relevant to implementing DTLS-SRTP and integrating it for reference:

RFC| Notes  
---|---  
<http://tools.ietf.org/html/draft-ietf-rtcweb-rtp-usage-06>| Media transport over RTP for WebRTC  
5761|  _Multiplexing of RTP/RTCP_  
5246|  _Transport Layer Security (TLS) 1.2_  
4347|  _Datagram Transport Layer Security (DTLS)_  
5705|  _Keying Material Exporters for Transport Layer Security (TLS)_  
5763|  _Framework for DTLS-SRTP_ Overall specification of negotiating DTLS-SRTP with SIP and SDP  
5764|  _SRTP Extension for DTLS_ Establishing SRTP keys through DTLS.  The keys are generated through a keying materials exporter.  
4145|  _TCP Based Media Transport in SDP_ Defines `a=setup` attribute used to indicate which endpoint initiates DTLS handshake. According to 5763the offerer MUST specify `a=setup:actpass`.  The answerer then has the choice respond with `a=setup:active` and immediately initiate DTLS handshake.  Or it can specify `a=setup:passive` indicating that the offerer must initiate the DTLS handshake.  Note: The `a=connection` attribute is not used.  
4572|  _TLS Based Media Transport in SDP_ Extends 4145 to TLS.  Introduces `a=fingerprint` attribute for endpoints to indicate the fingerprint (hash) of their respective certificates.  Note: Certificate fingerprint is hash of DER encoded certificate.  
3279|  _Algorithms and Identifiers for PKI Certificates_ Specifies hash, signature, and public/private key algorithms for certificates.  Referenced by 4572 for hash algorithms.  
4961|  _Symmetric RTP/RTCP_  
5389|  _STUN_  
5245|  _ICE_  
4566|  _SDP_  
  
 

 

 

 
