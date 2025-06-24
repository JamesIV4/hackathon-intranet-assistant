## Overview

Provides ability to use the media engine framework to provide fax send and receive resources that take the place of the traditional Dialogic and Acculab resources. See the fax for more information on fax standards, diagnostic tools, and troubleshooting techniques.

## Major Features and Requirements

### Media Server

  * T.30 / T.38 Termination Elements for Media Server
  * Modifications to Commetrex code to support reading multiple TIFF files.
  * Update Media Server API to support fax plays/records



  * Gateway support
  * SIP Support



### Fax Server

  * Rewrite of Fax Server to Support Media Server Resources
  * Integrating ION into refactored fax server code.
  * Remove all of the device management functionality.
  * Add Fax Group management functionality.
  * Refactor fax server commands.
  * Fax file utility for producing media server compatible fax images. Since pages are streamed the pages need to be ordered before being made available to media server among other things.
  * Add Fax File API and Fax File Server for file management.
  * Integrate http service similar to prompt server.
  * Refactor the fax server configuration management. Completely different from old fax server.
  * Queue manager being used for fax session progress and reporting.
  * Fax Server Transport needs re-factoring to add support for media server



### TS

  * Changes inside TS to handle fax call using media server.
  * Must be able to handle both old fax call methods and new media server sessions (not concurrently).
  * All fax session comms to the media server and updates of queue manager call info.
  * TS will now do the fax session setup and call setup unlike old fax server which managed the device setup.



### IA

Overview: ([detailed requirements](http://wiki.inin.com/bin/view/ClientTeam/IAMediaServerFax))

  * Updates to IA to cover configuration differences between HMP and Media Server fax.
  * Fax Group configuration need to be updated to contain only the max limit inbound and outbound fax
  * A default fax group needs to be added
  * Work to allow for switching between HMP and Media Server config (restart required). Which server to start etc.



## Design

The "ION Fax Overview" was presented at an Edge design meeting. It is useful as a introduction to fax concepts but the design section is out of date at this point. The "Media Server Fax Design" document is being kept up to date and should be used as the primary resource for understanding the new implementation. The "TS Media Server Fax Support" document describes the changes that are being made to TS to support Media server faxing.

  *   *   * 


## SCRs

  * [ION Based Fax Services](http://bugzilla/bugzilla/show_bug.cgi?id=66966)
  * [Changes to IA to support Media Server based faxing](http://bugzilla/bugzilla/show_bug.cgi?id=71742)
  * [Add LineGroup Input To QueueFaxForSend Toolstep](http://bugzilla/bugzilla/show_bug.cgi?id=72876)
  * [Install: Media Server based Faxing](http://bugzilla/bugzilla/show_bug.cgi?id=73198)
  * [Need Remoco to check process tree for changes before restarting subsystems](http://bugzilla/bugzilla/show_bug.cgi?id=76274)



## Testing

Test information can be found [here](https://confluence/display/Testing/MediaServerFaxing) .

### QualityLogic FaxLab Compatibility Testing

emulates the behavior of many different fax machines. We use it to test compatibility. The following fax machine types will not consistently work with either the Media Server or HMP implementation.

%EDITTABLE{ header="| **Call** | **Profile** | **I3 Fax** | **Gateway** | **Comments** |"}%

Call| Profile| I3 Fax| Gateway| Comments  
---|---|---|---|---  
Ans: RX 3 Pg Best ECM Best Enc V.34 33.6k Best Res| Konica Minolta !Magicolor 2490MF| Sender| Mediant| Gateway doesn't pass DIS correctly. Unable to test.  
Ans: RX 3 Pg Best ECM Best Enc Best Mod 200x100| Minolta MF-2800| Sender| Mediant| Gateway doesn't pass DIS correctly. Unable to test.  
Ans: RX 3 Pg Best ECM Best Enc Best Mod 200x100| Ricoh 3760-3760nf| Sender| Mediant| Gateway doesn't pass DIS correctly. Unable to test.  
  
## Schedule

%EDITTABLE{ header="| **Feature** | **% Complete** | **Developer** |"}%

Feature| % Complete| Developer  
---|---|---  
G.711 Termination Element| 100%| Sean Conrad  
T.38 Termination Element| 100%| Sean Conrad  
Media Server API| 100%| Sean Conrad  
Commetrex TIFF Queue Support| 100%| Sean Conrad  
TS Modifications| 100%| Harold Owens  
New Fax Server| 80%| Sean Conrad  
IA Changes| 40%| Jon Gray  
System Design Document| 100%| Sean Conrad  
TS-MS Fax Support Design Document| 100%| Harold Owens  
  
- Main.i3domain\Sean.Conrad - 04 Dec 2008
