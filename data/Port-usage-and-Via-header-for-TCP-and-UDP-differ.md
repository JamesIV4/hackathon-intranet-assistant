There is an inconsistency between which port i3sip uses to send messages for UDP and TCP. The Via header is impacted by that decision because it includes the port where requests get sent from. It's not clear whether either UDP or TCP does it a "wrong" way, and neither may need to be changed. The SIP RFC 3261 says this about [Via headers](http://tools.ietf.org/html/rfc3261#section-8.1.1.7):

> The Via header field indicates the transport used for the transaction and identifies the location where the response is to be sent. A Via header field value is added only after the transport that will be used to reach the next hop has been selected (which may involve the usage of the procedures in [4](http://tools.ietf.org/html/rfc3261#ref-4)).

It seems that this requirement is being satisfied for both TCP and UDP (though RFC 3263 could say something different). For example, when we send an INVITE from port 4096 using TCP, we expect that the OK response be sent back to port 4096, even though a listener may be on port 6060.

The possible issue is that TCP SIP dialogs may use multiple ports to send messages, and Nuance Speech Server seems to be having trouble with this. We are waiting to hear from Nuance support about whether they plan to change their SIP stack or whether they can point out why ours is wrong.

## Overview of port usage

If transceiver_udp_listenAddress or transceiver_tcp_listenAddress parameter specifies a port "P", then i3sip uses the port as follows:

  
|  Listen Port  |  Send from  |  Via Header   
---|---|---|---  
**UDP** |  P  |  P  |  P   
**TCP** |  P  |  Ephemeral  |  Ephemeral   
  
SIPEngine worked differently. UDP wasn't tested for this page yet, but it works as shown below for TCP. This arguably doesn't agree with the SIP protocol, because the Via header doesn't indicate the transport used for the transaction.

  |  Listen Port  |  Send from  |  Via Header   
---|---|---|---  
**TCP** |  P  |  Ephemeral  |  P   
  
If transceiver_udp_listenAddress or transceiver_tcp_listenAddress parameter does NOT specify a port, i3sip will choose a port "P". Then i3sip uses the port as follows:

  |  Listen Port  |  Send from  |  Via Header   
---|---|---|---  
**UDP** |  P  |  P  |  P   
**TCP** |  P  |  Ephemeral  |  Ephemeral   
  
For example, if transceiver_udp_listenAddress specifies a port, the UDP listener is created on the specified port.  All messages are sent from that port, and the Via header also uses that port.

Note that an ephemeral port is a different port than port "P" for all these tables.
