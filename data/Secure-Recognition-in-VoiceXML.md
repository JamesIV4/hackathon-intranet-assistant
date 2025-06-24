# Overview

The purpose of this project is to support secure DTMF and speech recognition in VoiceXML. The goal is for customers to able to meet the requirements of the Payment Card Industry Data Security Standard (PCI DSS) when gathering user information in VoiceXML.

# Requirements

BLOCKNumber| Description| Detail| Priority  
---|---|---|---  
R1| VoiceXML shall provide the ability to define a property that will secure all DTMF and speech recognitions within the same scope that property is defined| 

  * The property will use reverse domain name notation to avoid collision as mandated by the VoiceXML 2.0 specification
  * The property will be a boolean that defaults to 'false'

| **Must Have**  
R2| All call recordings during secure recognition shall be paused so that speech and DTMF inputs are not captured in the recording| 

  * This only takes into effect if proactive recording is recording the IVR
  * Similar to the secure pause feature a tone will be inserted in the recording in place of the utterance
  * The duration of the pause has to be at least the duration of the max speech timeout property in VoiceXML

| **Must Have**  
R3| All sensitive information shall be obfuscated/encrypted in logs for the duration of the secure recognition| 

  * This includes logs of every subsystem involved in the recognition session including: VoiceXML, TsServer, Reco, Media Server and IP
  * Sensitive information include recognition requests and results, plays, JavaScript logging in VoiceXML, and DTMF events

| **Must Have**  
R4| All recognition requests and responses (including results) shall be protected| 

  * All APIs that subsystem expose to support secure recognitions will have their payloads obfuscated/encrypted. This includes APIs to Reco, TsServer, and Media Server

| **Must Have**  
R5| Support for secure recognition in IP| 

  * Provide reco tools for secure inputs as well tools to analyze secure results

| **Should Have**  
 |  |  |    
  
# Punch list

Indicate percentage complete and status simultaneously using color badges in "% Complete" column.

{green:XX%}| XX%| Active work being performed  
---|---|---  
{red:XX%}| XX%| No work currently being performed  
{yellow:XX%}| XX%| Having issues  
{on-hold:XX%}| XX%| Waiting on something  
{grey:Complete}| Complete| Complete  
Task| SCR| Component| Owner| Description| Percent Complete| Commitment Date  
---|---|---|---|---|---|---  
Dev Project| Interactive Intelligencea6f784b9-ef5d-3d60-bca5-6d0a3771dd27DP-1450|  |  |  | 50%|    
Umbrella SCR| Interactive Intelligencea6f784b9-ef5d-3d60-bca5-6d0a3771dd27IC-123726|  |  |  | 50%|    
Secure pause support in VoiceXML| Interactive Intelligencea6f784b9-ef5d-3d60-bca5-6d0a3771dd27IC-123555| VoiceXML| |  | Complete|    
Log encryption in VoiceXML| Interactive Intelligencea6f784b9-ef5d-3d60-bca5-6d0a3771dd27IC-123556| VoiceXML|  |  | Complete|    
Secure recognition support in Reco| Interactive Intelligencea6f784b9-ef5d-3d60-bca5-6d0a3771dd27IC-123727| Speech| |  | 0%|    
Secure recognition support in TS| Interactive Intelligencea6f784b9-ef5d-3d60-bca5-6d0a3771dd27IC-123728| TsServer| |  | 0%|    
Remove logging of sensitive information in Reco| IC-123726| Speech| |  | Complete|    
Set reco:RestrictResultTracing in VoiceXML| IC-128822| Speech| |  | Complete|    
  
# Design

VoiceXML: 

# References

  * <https://www.pcisecuritystandards.org/security_standards/> 


