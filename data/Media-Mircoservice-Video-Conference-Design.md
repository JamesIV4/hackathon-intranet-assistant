# Overview

Design page for Charter - Video Conference for Media Microservices

The overall goal is to start using Media Microservices for video conferences in PureCloud. 

# Architecture

Edge Media Video4

# Components

Media Service Video Conference ComponentsMedia Service Video Conference Components12

## Sidecar / Media Service

The video media service instances service all video conferencing media requests. The same binary that runs the edge media services that already exists and are used by our telephony services in PureCloud. The primary differences between the two micro-services are:

  * The sidecar rest API is used for video conferencing instances. The port (8443) used by the REST API advertised via Adrestia in places of the edge IPC port.

  * The port advertised by edge media service instances as the IPC communication port is not available for video conferencing capable instances.




API documentation for media sidecar can be found here: Media Sidecar API

### Video Media Service Port Rules

**Port Type**| **Protocol**| **Port Range**| **Source**| **Description**  
---|---|---|---|---  
Inbound| UDP| 16384 - 32767| 0.0.0.0/0| RTP/RTCP  
Inbound| TCP| 8443| VPN Security Group| VPN  
Inbound| TCP| 8443| Media Controller Instance Security Group| Media Controller  
Inbound| TCP| 8443| video-media-service ELB Security Group| ELB Health Checks  
Outbound| UDP| 1024 - 65535| 0.0.0.0/0| RTP/RTCP  
Outbound| ALL| ALL| 10.42.0.0/16| Adrestia, Media VPC  
  
## Media Controller

Common interface to video providers in the PureCloud ecosystem. For this solution we'll have a specific video controller that talks to media services via the sidecar interface.

# Call Flows

## Create a Video Conference

**Use Case** : A user is in a chat room and decided to start a video converstation

MacroBodyPlantUML

## Disconnect a Video Conference

**Use Case** : A user is in a video conference and decided to disconnect

MacroBodyPlantUML

# Project Tracking

Pure Epic: PURE-1662b3972da3-ea76-350d-b02c-d56219184865ININDCA JIRA

Dev Jira Epic: Interactive Intelligencea6f784b9-ef5d-3d60-bca5-6d0a3771dd27MMS-70

Kanban Board:  <https://devjira.inin.com/secure/RapidBoard.jspa?rapidView=746>

# Questions

  * Do we want to use a new media type for video conversations or use existing "Multimedia Session/VideoComm"? **Yes**  





# References

  * PureCloud Video Conferencing

  * Video Conferencing v.2

  * Media Server Video Conferencing

  * [Media Server SFU Video Conferencing Support](https://genesys-confluence.atlassian.net/wiki/pages/createpage.action?spaceKey=~KevinO&title=Media%20Server%20SFU%20Video%20Conferencing%20Support)

  * [HPAA Video Conferencing Selective Forwarding Unit Design Document](https://genesys-confluence.atlassian.net/wiki/pages/createpage.action?spaceKey=~KevinO&title=HPAA%20Video%20Conferencing%20Selective%20Forwarding%20Unit%20Design%20Document)

  * Media Micro-service Design

  * User Stories

  * High Level Video Conference Bridge Design Diagram




* * *

1
