# Unified Plan for Using SDP with Large Numbers of Media Flows  
  
This page describes relevant sections, and how they relate to our current WebRTC implementation, of the Unified plan for SDP document here: <https://tools.ietf.org/html/draft-roach-mmusic-unified-plan-00>

## SDP Parsing

The unified plan describes a new format for an SDP exchange, where instead of the full offer or answer being sent, this new format allows for only fragments of sdp to be sent when making changes to an established session.

### General concepts

Specifically, such a fragment consists of and only of a single mline and the attributes for that mline. If the fragment is for a previously unknown mline, it's being newly added. If it's previously known, it's being modified or deactivated.

### Implementation details

To support this draft standard, we must ensure that our code:

  * Generates all mlines with the a=mid attribute. This is probably already the case.
  * Detects if the offer / answer received from the remote party contains a=mid attributes. If it doesn't, it probably won't understand sdp fragments.
  * Generates all mlines with the a=ssrc attribute. This is probably already the case.
  * Detects if the offer / answer from the remote party contains a=ssrc attributes for each mline. Multiple a=ssrc attributes per mline are assumed to be alternative sources for the same stream. (senders can switch whenever they want, but must only send one at a time).
  * Supports receiving SDP from the remote peer that indicates a particular mline MUST be bundled on the same port as another mline.
    * Mark a bundle only mline with a=bundle-only, and set the port to 0.
  * Check that all mlines in a given bundle received from the remote peer have identical attributes except those that apply to the media track.
  * Supports receiving partial SDP fragments as described in the unified plan. Each such fragment must start with an mline.
    * Currently it is unknown what mechanism needs to be used to communicate these. Presumably the same transport as the SDP is being sent over now, but how to frame the messages? Unclear.
    * When SDP fragments are received, we simply have to modified the hpaa elements as indicated to support the new session. 
    * A big consideration here is that we're explicitly requiring that all media between the SFU/mediaserver and the browser happen over a single RTP / RTCP / DTLS stream. So any SDP fragments sent/received will just be adding new flows inside the existing stream. No renegotiation of ICE, or other expensive changes required.
  * We must add support for a RFC5285 header extension to correlate rtp streams with each other.



 

## Correlation between mlines and rtp streams

The BUNDLE mechanism allows us to potentially embed arbitrary numbers of video / audio / other streams in a single transport (ipaddress/port pair). The SDP will have an ssrc (or more) per mline to indicate which rtp streams that are bundled together represent which content.

We're going to need to keep track of this mapping and potentially inform the rtp related elements in the graph of which streams map to which on the receive side, and on the send side the ContextResourceWebrtc will need to know of all of the rtp streams that are bundled into a single transport so that they can be sent in the SDP to the remote peer..

 

## Adding and removing streams

It might be possible to receive media with an unknown ssrc when a new stream is being added, but before the sdp exchange has completed. We need to decide if we want to try to build in some guess work logic to handle these situations prior to the sdp exchange completing. This has always been a possibility with SDP exchanges in the past, but it's a bigger problem now that sdp can be exchanged in fragments.

The unified plan describes a new RTP header extension to help correlate RTP streams that we don't have full information for.

It also appears to be the intention of this unified plan to allow all RTP streams for a audio / video conference SFU like what we're planning to build to channel all RTP streams from participants into a single pair of ipaddresses and ports between the SFU host and any given conference participant. 

With that consideration, newly added media streams that are communicated over SDP fragments should be able to just be added to the existing RTP stream as new ssrcs. 

I've confirmed with Xander Dumaine that the existing video conference capability in purecloud does communicate all RTP over a single ipaddress pair.. 

Alternative implementation details

If we prefer not to implement things as described above, then we'll need to send the newly added rtp streams over one or more newly negotiated ICE transports. Doing that might look like:

  1. Adding newly bound ip addresses to the existing UdpEndpoint which is currently transmitting previously negotiated rtp steams. 
  2. Gather local ICE candidates for the new ip addresses
  3. Transmit / receive ICE candidates via SDP / Trickle.
  4. Negotiate ICE
  5. Begin transmitting media.



The existing i3ice implementation should support this with little to no modification. Negotiating multiple media streams in i3ice has been unit tested very carefully, but adding new streams, and removing streams, on the fly is currently not tested and may need some minor implementation work.

Adding / removing ipaddresses to the existing UdpEndpoint is something that I explicitly designed the UdpEndpoint to support, but it would take a couple of weeks of implementation to get that working.

Supporting this would also require one of the following:

  1. Giving the UdpEndpoint the ability to pair the output of an hpaa element, such as the rtp element (or whatever else is connected to it) with a local/remote address pair
  2. Some mechanism to inform the hpaa element that's originating a UdpIoBuffer the local/remote address pair to use.



The reason for this requirement is that currently the WebRTC stack depends on the UdpEndpoint having a "default" local / remote address pair to send and receive on. If a UdpIoBuffer has an address assigned to it, we use that automatically, but if it doesn't then we use the "default" ones. To support adding new media streams that use alternative address pairs than the ones already negotiated would require the newly sent information to have the appropriate address information, or we'll send to/from the wrong addresses.

Alternatively, we could hack all of this together by instantiating a new UdpEndpoint, and associated collection of HPAA elements. It's not as elegant but could work just as well.

 

# Plan B: a proposal for signaling multiple media sources in WebRTC.

 

As an alternative way of handling large numbers of media streams in SDP when setting up WebRTC sessions, a Plan B draft standard was proposed.

The Unified plan provides a new mechanism to send and receive SDP fragments, which allows for asynchronous updates to a session without doing a full restart of the session. The Plan B proposal takes a different approach in merging all media streams of the same type (video, audio, etc) into a single stream of that type, and multiplexing based on the a=ssrc of the various rtp flows. The ultimate goal of both Plan B and the Unified Plan is to reduce the number of mandatory ipaddress/port allocations that a browser and/or SFU needs to do to exchange media with each other. However, after discussions with Xander Dumaine and David Ertel, it seems that the client for the existing PureCloud video conferencing solution is already explicitly requiring a single ipaddress/port pair for all media between the browser and the SFU. This drastically reduces the differences between the two proposed plans down to simple differences in signaling.

If we were in a situation where we needed to maintain the default behavior of SDP, where each mline automatically meant the allocation of an ipaddress/port and potentially further meant the negotiation of ICE, then PlanB would be significantly more attractive, as it defaults to only requiring two ports maximum to support audio and video. Whereas the Unified plan by default still potentially requires up to num peers * 2 transports to support full audio and video from each participant. However, we already require support for BUNDLE, so as to combine the video and audio into a single rtp/rtcp/dtls stream, and the unified plan clearly demonstrates multiplexing multiple video and/or audio streams into a single rtp/rtcp/dtls stream with the SSRC values to demultiplex them and SDP to signal which ssrc corresponds to a particular source.

Taking only those considerations into account, the Unified plan and Plan B are on roughly equal footing as far as on-the-wire behavior. However, the Unified Plan describes a mechanism that Plan B does not, the concept of partial SDP to update an established session, and as such wins out over PlanB thanks to the added flexibility. Further and finally, PlanB details a large number of additional SDP attributes that we would need to write code to handle and keep track of, where the Unified plan does not add anything of significance to the SDP we'll need to handle.

 

### Major new concepts in Plan B (from the perspective of icmediaserveraudio, anyway)

Again, remember that we're going to be sending all of the audio / video over the same rtp/rtcp/dtls transport for either plan.

  * Multiple ssrcs per mline. Each with their own msid.
  * New attribute: a=remote-ssrc:1 recv:on 
    * If the offer has some ssrc:1, the answer back can include this attribute to say "yes, send me that ssrc".
  * New attribute: a=ssrc-group:SIMULCAST 5 51
    * 5 and 51 are ssrcs. Presumable several/unlimited can be provided
    * Describes a group of related ssrcs.
  * New attribute: a=max-*-ssrc
    * Not defined by the paper.
  * New attribute: a=msid-semantic
    * Not defined by the paper.
  * SDP exchange now always requires a 3 way handshake, instead of potentially only a single round trip. This is done because of the answerer simultaneously saying which items from the offerer it wants, and which it can itself send, the offerer needs to respond to the answer with the list of desired items from the answerer.


