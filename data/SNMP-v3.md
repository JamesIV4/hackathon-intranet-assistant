# Overview

SNMPv3 was designed to correct the security deficiencies of previous SNMP releases. It includes 3 important services: authentication, privacy, and access control and is described over a few RFCs documented below. This project will add SNMPv3 support to our  stack. The main motivation for doing so is that we do not lose our JITC certification which SNMPv3 will be a . 

The main SNMPv3 RFCs are as follows:

RFC Number| Title  
---|---  
[RFC 2271](https://tools.ietf.org/html/rfc2271)| An Architecture for Describing SNMP Management Frameworks  
[RFC 2272](https://tools.ietf.org/html/rfc2272)| Message Processing and Dispatching for the Simple Network Management Protocol  
[RFC 2273](https://tools.ietf.org/html/rfc2273)| SNMPv3 Applications  
[RFC 2274](https://tools.ietf.org/html/rfc2274)| User-Based Security Model for SNMPv3  
[RFC 2275](https://tools.ietf.org/html/rfc2275)| View-Based Access Control Model (VACM) for SNMP  
  
# Requirements

The requirements of this project is entirely driven by what is needed to pass JITC certification. The following are the JITC requirements:

 

Number| Description| JITC Requirement| Priority  
---|---|---|---  
R1| i3snmp shall generated and handle SNMPv3 messages| | 
    
    
    Number

| 
    
    
    Product

| 
    
    
    Description  
  
---|---|---  
      
    
    AUX-006540

| 
    
    
    Required: CP Server, CP MG, CP SBC

| 
    
    
    The CP Server, CP MG, and CP SBC shall support generation and transmission   
    of Simple Network Management Protocol (SNMP) version 3 (SNMPv3) alarms for remote monitoring  
      
    
    IA-077000

| 
    
    
    Required: SS, SC, MG, SBC, RSF, R,   
    LS, SD

| 
    
    
    The product shall be capable of using SNMPv3 for all SNMP sessions.  
       
    NOTE: If the product is using Version 1 or Version 2 (instead of SNMPv3) with all of   
    the appropriate patches to mitigate the known security vulnerabilities, then any findings   
    associated with this requirement may be downgraded. In addition, if the product has   
    developed a migration plan to implement Version 3, then any findings associated with   
    this requirement may be further downgraded.  
  
**Must Have**  
R2| i3snmp shall check SNMPv3 messages for integrity| | 
    
    
    Number

| 
    
    
    Product

| 
    
    
    Description  
  
---|---|---  
      
    
    IA-066000

| 
    
    
    Required: SS, SC, MG, SBC, RSF, R,   
    LS, SD

| 
    
    
    The entire SNMPv3 message shall be checked for integrity and shall use the HMAC SHA196   
    with 160 bit key length by default  
  
**Must Have**  
R3| i3snmp shall support privacy of SNMPv3 messages| | 
    
    
    Number

| 
    
    
    Product

| 
    
    
    Description  
  
---|---|---  
      
    
    IA-077010

| 
    
    
    Required: SS, SC, MG, SBC, RSF, R,   
    LS, SD

| 
    
    
    The security level for SNMPv3 in the DoD VVoIP environment shall be authentication with   
    privacy -snmpSecurityLevel=authPriv. The product shall set snmpSecurityLevel=authPriv   
    as the default security level used during initial configuration.  
      
    
    IA-077020

| 
    
    
    Required: SS, SC, MG, RSF, R, LS,   
    SBC, SD

| 
    
    
    The SNMPv3 implementation shall be capable of allowing an appropriate administrator to   
    manually configure the snmpEngineID from the operator console. A default unique   
    snmpEngineID may be assigned to avoid unnecessary administrative overhead, but this   
    must be changeable.  
      
    
    IA-077070

| 
    
    
    Required: SS, SC, MG, SBC, RSF, R,   
    LS, SD

| 
    
    
    For backwards compatibility, the product shall support the capability to use Data   
    Encryption Standard-Cipher Block Chaining (DES-CBC) (usmDESPrivProtocol) with a 16   
    octet (128 bit) input key, as specified in RFC 3414, as an encryption cipher for SNMPv3.  
      
    
    IA-077080

| 
    
    
    Required: SS, SC, MG, SBC, RSF, R,   
    LS, SD

| 
    
    
    The product shall support the capability to use the CFB-AES128 encryption cipher   
    usmAesCfb128PrivProtocol for SNMPv3 as defined in RFC 3826 and specify this as   
    the default encryption cipher for SNMPv3.  
      
    
    IA-07706

| 
    
    
    Required: SS, SC, MG, SBC, RSF, R,   
    LS, SD

| 
    
    
    The message processing model shall be SNMPv3 - snmpMessageProcessingModel=3.  
      
    
    IA-077140

| 
    
    
    Required: SS, SC, MG, SBC, RSF, R,   
    LS, SD

| 
    
    
    The product using SNMPv3 shall implement the key-localization mechanism.  
  
**Must Have**  
R4| i3snmp shall enforce timeliness of message| | 
    
    
    Number

| 
    
    
    Product

| 
    
    
    Description  
  
---|---|---  
      
    
    IA-077040

| 
    
    
    Conditional: SS, SC, MG, SBC, RSF, R,   
    LS, SD

| 
    
    
    If the product receives SNMPv3 response messages, then the product shall conduct   
    a timeliness check on the SNMPv3 message.  
      
    
    IA-077050

| 
    
    
    Required: SS, SC, MG, SBC, RSF, R,   
    LS, SD

| 
    
    
    An SNMPv3 engine shall perform time synchronization using authenticated messages.  
      
    
    IA-077110

| 
    
    
    Required: SS, SC, MG, SBC, RSF, R, 
    
    
    LS, SD

| 
    
    
    When using msgID for correlating Response messages to outstanding  
    Request messages, the SNMPv3 engine shall use different msgIDs in   
    all such Request messages that it sends out during a 150 second Time Window  
      
    
    IA-077120

| 
    
    
    Required: SS, SC, MG, SBC, RSF, R,   
    LS, SD

| 
    
    
    An SNMPv3 Command Generator or Notification Originator Application shall use   
    different request-ids in all Request PDUs that it sends out during a Time Window  
  
****Must Have**  
**  
R5| i3snmp shall validate responses it receives based on outstanding requests| | 
    
    
    Number

| 
    
    
    Product

| 
    
    
    Description  
  
---|---|---  
      
    
    IA-077090

| 
    
    
    Conditional: SS, SC, MG, SBC, RSF,   
    R, LS, SD

| 
    
    
    If the product receives SNMPv3 response messages, then the SNMPv3 engine shall   
    discard SNMP response messages that do not correspond to any current outstanding   
    Request messages.  
      
    
    IA-077100

| 
    
    
    Conditional: SS, SC, MG, SBC, RSF,   
    R, LS, SD

| 
    
    
    If the product receives SNMPv3 responses, then the SNMPv3 Command Generator   
    Application shall discard any Response Class Protocol Data Unit (PDU) for   
    which there is no outstanding Confirmed Class PDU.  
  
**Should Have**  
 |  |  |    
  
 

# Punchlist

Indicate percentage complete and status simultaneously using color badges in "% Complete" column.

{green:XX%}| 0%| Active work being performed  
---|---|---  
{red:XX%}| 0%| No work currently being performed  
{yellow:XX%}| 0%| Having issues  
{on-hold:XX%}| 0%| Waiting on something  
{grey:Complete}| 0%| Complete  
  
  


2015 R3 Release

Task| SCR| Component| Description| Percent Complete| Notes| Developer  
---|---|---|---|---|---|---  
Dev Project| [DP-1272](http://devjira.i3domain.inin.com/browse/DP-1272)|  | Support SNMPv3| Green50%|  |     
Umbrella SCR| [IONCORE-663](http://devjira.i3domain.inin.com/browse/IONCORE-663)|  | Umbrella SCR| Green100%|  |    
i3snmp: USM support| [IONCORE-754](http://devjira.i3domain.inin.com/browse/IONCORE-754)|  | Add user-based Security Model to i3snmp ([RFC 3414](https://tools.ietf.org/html/rfc3414))| Green100%|  |   
i3snmp: Integrate USM and protocol changes| [IONCORE-755](http://devjira.i3domain.inin.com/browse/IONCORE-755)|  |  | Green100%|  |    
i3snmp: Transactional support| [IONCORE-752](http://devjira.i3domain.inin.com/browse/IONCORE-752)|  |  | Green100%|  |    
i3snmp: Configuration| [IONCORE-753](http://devjira.i3domain.inin.com/browse/IONCORE-753)|  |  | Green100%|  |    
Remoco: Integrate i3snmp| [IC-116357](http://devjira.i3domain.inin.com/browse/IC-116357)|  |  | Green100%|  |   
Install: Install and Configure SNMPv3| [IC-127555](http://devjira.i3domain.inin.com/browse/IC-127555)|  |  | Green100%|  |   
  
 

 
