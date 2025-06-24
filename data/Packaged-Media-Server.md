# Packaged Media Server (with embedded OS)

## Overview

This page is intended to keep track of features in the Media Server that are needed for a packaged solution.

## Links

[Channel Ready Solutions](http://wiki.inin.com/bin/view/Services/CRIMS)

## Requirements

Requirement  |  Description  |  Notes   
---|---|---  
Switch Between Server and Appliance Modes  |  A mechanism is need to switch between server mode and appliance mode  |  Some configurations are not needed in server mode (Network, NTP, SU)   
Initial IP Configuration  |  A mechanism is need to configure the Media Server's IP address if DHCP is not being used  |  This could be something similar to the network utility used for Interaction Gateway   
Network settings in Web Config  |  A mechanism is need to configure the Media Server's IP address using the web config  |    
NTP Configuration in Web Config  |  A mechanism is need to configure the Media Server's NTP  |    
Service Updates in Web Config  |  A mechanism is need to load service updates, set restore points, and reboot  |    
EWF Control in Web Config  |   |  EWI dlls that might have to added for this   
Appliance Monitor  |   |  New executable that need to be added to the install   
Mark which settings need a restart  |  It is important that setting that need a restart are marked in the web config  |  SCR:68962   
Changing trace levels  |  Be able to change the log levels via the web config  |    
List recordings in the Web UI  |  Implement listing recordings for orphaned recording retrieval  |    
Support HTTPS  |  For security reasons we need to support HTTPS for recording retrievals  |    
  
## IGateway, Media Server, SIP Proxy Combination Appliance

An interim solution to supporting a complete embedded media server. The interim solution includes having the media server be installed on IGateway hardware appliance as an add on. The IGateway will take care of a lot of management tasks of the appliance server itself. The media server will manage its own application settings via the web config. The following list indicates the work required to get this configuration supported on the media server:

Requirement  |  Component  |  Notes  |  SCR   
---|---|---|---  
Umbrella SCR  |   |  Support media server as an add on the IGateway  |  IGW-757  
Install Media Server to run under system account  |  Install: Media Server  |   |  IC-80415  
Remove .NET framework from media server install  |  Install: Media Server  |   |  IC-80665  
Create installer for new i3QoS driver  |  Install: QoS Driver  |   |  IC-73519  
Add ability to adjust tracing levels on the web configuration page  |  Media Server  |   |  IC-80959  
Clarify which Parameters require restart to change  |  Media Server  |   |  IC-62432  
  
### Open Issues




## Testing
