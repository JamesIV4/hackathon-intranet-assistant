false

## Overview and Requirements

The project calls for adding regionalization information to Automatic Speech Recognition (ASR) servers (i.e. location) in order to more intelligently select an ASR server to use to service a call. Currently the ASR selection process uses a least load selection algorithm to determine which server to use. This is not optimal in situations where a customer has ASR servers across multiple regions as a server can be picked that has a high latency link to the media server processing the audio for that call. This results in poor audio quality that affects the recognition accuracy and speed, as well as using unnecessary WAN bandwidth.  To resolve this a location attribute will be added to each ASR server configured for a CIC server. That location will be considered in the selection process before load is taken into consideration. The location will be evaluated against an ASR server selection rule defined for each region similar to selection rules defined for selecting media servers.

 

**The following are proposed requirements for ASR regionalization:**

BLOCKNumber| Description| Detail| *Priority  
---|---|---|---  
R1| Modify RecoSubsystem server selection process to use location information and selection rules|  | Must have  
R2| Modify TS to return back the location information of a media server selected for an ASR call|  | Must have  
R3| Add ability to configure a location for each ASR server in IA|  | Must have  
R4| Add ability to configure a selection rule for selecting ASR servers for each region|  | Must have  
  
  
*Priority Descriptions

,,style="background:yellow; font-size:8pt;"BLOCKPriority| Description  
---|---  
Must have| The initial release MUST have the feature.  
Should have| The initial release SHOULD have the feature but can defer it to the next iteration.  
Nice to have| The initial release MAY have the feature but its priority is low.  
Future revision| The initial release will NOT include the feature and will be evaluated in the future.  
  
 

## SCRs

BLOCKFeature (Plan)| Percent   
complete| SCR| Developer| Description  
---|---|---|---|---  
Project|  | DP-816|  |    
Reco Framework|  | IC-70298| |    
Interaction Administrator|  | IC-111711| |    
 |  |  |  |    
  
 

## Design

### ASR Server Configuration

A new property is needed for each ASR server's location.  The attribute 'Location' will be stored in the DS entry $SERVER\Recognition\ASR Engines\_< EIM Name>_\Servers\_< Server Name>_\\.  If the 'Location' property isn't set for a server, the server is assumed to be in the default location.  Note that the ASR server must connect to the IC server (with its certificate trusted) before an entry for the server gets created and its configuration can be set.

Users will be able to select the server's location from a drop down of location names.  This configuration tab can be merged with the Web Configuration tab, similar to the mockup below.

ASR Server Config tab

Existing reco properties (including recocfg: properties) will continue to be set on the Properties tab.  (Creating special controls on a new tab for recocfg: properties is complicated because users may still try to add recocfg properties to the Properties tab, and the current inheritance mechanism where default recocfg properties can be set for all Servers is lost.  Addressing those issues poses trade-offs for users.  Since users aren't complaining about the current property configuration for ASR servers, we'll leave the existing properties mechanism for simplicity and to avoid confusion about how property inheritance works.)

### Location ASR Selection Rule Configuration

Each location in IA will need to have a configurable selection rule for ASR servers.  In DS, each location stored at $SERVER\Locations\_< Location Name>_ can now have an 'ASR Server Selection Rule' attribute, whose value maps to an entry in $SERVER\Selection Rules\\.  Locations without an 'ASR Server Selection Rule' attribute are assumed to use the selection rule '<Default ASR Selection Rule>'.  If that selection rule doesn't exist, the RecoSubsystem will use a hard-coded selection rule:

  1. <ThisLocation> (i.e. the location where echo cancellation is taking place)
  2. <ICServerLocation>
  3. <Any> 



A new drop down for "ASR Server" needs to be added inside the Selection Rules group for the Locations Configuration dialog:

### Reco Subsystem ASR Selection Process

The old selection process picked servers as follows:

  1. Smallest priority number (set by the property recocfg:ServerProxyPriority)
  2. Least load (among servers with the same priority)
  3. Is active, accepting sessions, below the maximum session count, and supports the session's language.



The new selection process adds an additional location criterion before any of the previous criteria are applied for picking a server.

  1. More preferred region according to the ASR selection rules for the location where echo cancellation is being performed.
  2. Selected according to the previous selection process (among servers in an equally preferred region) - i.e. priority, load, and acceptable



### Internal Reco API changes

In order to accommodate this change to the server selection process, the RecoSubsystem initializes sessions differently.  The old process:

  * Fully initialized an ASR session (including selecting which ASR server to use), then
  * Created a RecoSession (which sends a TSAPI::ASRBeginSession request to TS).



Since the response to the TSAPI::ASRBeginSession request indicates the location where echo cancellation will be taking place, that part of the initialization needed to be performed before the ASR server selection is performed.  However, a RecoSession can't be created without the ASR session object (which indicates which EIM is being used), so the ASR session is now initialized in two steps:

  * Partially initialize an ASR session (including selecting which EIM to use)
  * Create a RecoSession (and get a response to TSAPI::ASRBeginSession to learn which location echo cancellation is being performed)
  * Finish initialization of the ASR Session with a new Initialize function (so the ASR session knows where echo cancellation is being performed for selecting the best ASR server)



## Links

  * 


 
