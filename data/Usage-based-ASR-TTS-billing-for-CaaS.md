Before this project, CaaS customers interested in Speech Recognition (ASR) or Text to Speech (TTS) have been required to purchase and own ASR and TTS ports up front.  This requires a large up-front expense for customers, and it doesn't allow us to offer "Speech as a Service", with the ability for customers to ramp up and scale down resources as needed for seasonal businesses.  As a result, many interested customers decide not to purchase any speech capabilities.  In addition, CaaS isn't able to pool speech servers for multiple customers to save on operational expenses.

We haven't offered usage based billing partly because third-party ASR vendors like Nuance have required that the end-customers own the ports they use, and partly because our system doesn't track the per minute usage of ASR or TTS ports (so our own ISR engine couldn't easily be billed by usage either).  Now that Nuance is willing to allow CaaS customers to share ports and pay by usage, we need an accurate way to measure customers' usage of ASR and TTS ports.  This system should also work for our own Interaction Speech Recognition (ISR) and Interaction Text to Speech (ITTS) engines.

# Overview

A CaaS Billing Subsystem runs on CaaS systems.  The billing subsystem receives Notifier requests from various other subsystems and writes data to a CaaS billing database.  At a high level, the Reco Subsystem needs to track ASR usage and send Notifier requests to the CaaS Billing subsystem as each ASR session completes.  Likewise, the TsServer Subsystem needs to track TTS usage and send Notifier requests to the CaaS Billing subsystem as each TTS session completes.  The basic idea is that these notifications will provide details of the port usage, and that information will be recorded in the billing database.

CaaS Speech Usage Notifiation Overview

# Project Status

### ASR Billing in CaaS

SCR| Owner|  %Complete| Notes  
---|---|---|---  
DP-1698| | Green100%| Submitted to 2016 R2  
IC-132209| | Green100% | Umbrella SCR  
IC-131854| | Green100%|    
CAASBILLING-243| | Green100%|    
  
### TTS Billing in CaaS

SCR| Owner|  %Complete| Notes  
---|---|---|---  
DP-1709|  | Green80%|    
key,summary,type,created,updated,due,assignee,reporter,priority,status,resolutionInteractive Intelligencea6f784b9-ef5d-3d60-bca5-6d0a3771dd27IC-133323| | Green80% | Umbrella SCR  
IC-132212| | Green100%|    
IONMEDIA-2223| | Green100%|    
IC-132210| | Green80%|    
IC-132211| | Green80%|    
  
# Billing Data

While a TTS or ASR session is in progress, TS, MRCP Subsystem, and Reco will record information about the session and send a notification to the CaaS Billing subsystem with the following information when the Speech session completes:

Field| Type| Description| Notes   
---|---|---|---  
StartTime| i3core::AbsoluteTime| Start date and time for speech port usage|    
Duration| i3core::RelativeTime| Length of time speech port was used| Multiple events may overlap for same call. For example, TTS and ASR are reported separately  
InteractionId | Integer| Interaction ID of call|    
ApplicationName | String| Custom identifier for application| Used for reporting. Set by speech application as call attribute  
ConcurrentPorts| Integer | Total number of concurrent ports in use when port was created (including new session). Not used for TTS plays.| Reports concurrent port usage for the same resource type (ASR or TTS) across any application on the IC server. Helps allow CaaS to bill customers by peak port usage, or to just report on that statistic.  
VendorName| String | Vendor name for the MRCP server that was used. When field isn't empty, it indicates that the ConcurrentPorts field is only for servers with the same vendorName. | Only used when BaseResource is MrcpPort. This field allows MediaStreamingServer ports to be counted separately from Nuance ports. The vendor field reported is the MRCP server's vendor field configured in Interaction Administrator.  
SpeechServer| String| The speech server that was used| IP address or server name of configured Speech Server. (TS or Reco will report what value it has, which should be consistent across sessions that use the same server.)  
CallLanguage| String | Language call attribute| Informational, and could be empty. May be useful for reporting or as a sanity check against the detected languages.   
BaseResource | String| Type of resource used (ASR/TTS tier)| See table below for codes. Call attribute can be used to specify ASR tier, otherwise tier-agnostic code will be used.  
LanguagesUsed| List<String>| List of language codes used for Speech resource| List of detected languages.  May be 0 to many.  
Grammars| List<String> | List of grammars used | Only used for ASR sessions.  
AddonResources| List<String>| List of Addon resources| See table below for example codes. Set by speech application as call attribute  
  
## BaseResource types

Resource code| Description| Reported by   
---|---|---  
NR| Nuance Recognizer 9, unknown tier | Reco  
ISR| Interaction Speech Recognition, unknown tier | Reco  
MrcpAsr| MRCP ASR session. SpeechServer field from billing data should be used to check which ASR vendor is used.| Reco  
SapiPlay| Reports length of SAPI play| TS  
MrcpPlay| Reports length of MRCP play| TS This type may not be needed. It provides information on the length of MRCP plays, but we may not bill by that. TS may see additional details about what languages were used for a play, but perhaps MRCP subsystem sees the same details.  
MrcpPort| Reports length of MRCP session. SpeechServer field from billing data should be used to check which MRCP vendor is used.| MRCP (TTS or Media Streaming Server session)  
ITTS | Reports length of Interaction TTS play| TS  
  
## AddonResources types

Note: by analyzing the grammars used, CaaS billing can detect these features rather than relying on these self-reported fields. 

Resource code| Description  
---|---  
NDM1| Nuance NDM Level 1  
NDM2| Nuance NDM Level 2  
Tier _N_|  Indicates Tier of ASR (Ex. Tier2)  
  
## Field details

The speech billing data is needed for generating accurate reports of Nuance Speech (ex. Nuance Recognizer/Vocalizer) and Interaction Speech (ISR/ITTS) usage.  Since billing rates vary based on whether customers are using multi-lingual applications or add-on features like NDMs or Nuance Tier 4 ASR, merely knowing the duration of a speech port isn't sufficient for billing purposes.  However, the IC server does not authoritatively know all the languages or features an application uses when using Nuance.  The IC server knows the duration of every session, and it knows when each request is being sent to the speech servers, but the IC server does not always know the contents of every request (i.e. which languages or features are being used).  In order to allow CaaS to assess the proper billing rates, we will report on the information we do have:

  * **StartTime, Duration, InteractionId,  BaseResource**.  Authoritatively reports the duration of a BaseResource being used for InteractionId.
  * **ApplicationName**.  May not be set reliably because call attributes can accidentally be changed by customers, and that must not prevent us from gathering accurate billing data.  In addition, VoiceXML applications will not be able to set an ApplicaitonName attribute while the call is in the VXML interpreter.  Still, this field can be set for some applications, so at minimum it could be a useful field for reports we provide to customers, and it can also be used to double check billing data determined through these other fields.
  * **ConcurrentPorts**.  Authoritatively reports the number of concurrent ports in use.  Irrelevant for customers paying per minute, but helps enable CaaS to bill customers who want to pay based on peak usage per time period (ex. peak usage per month).  Even for per minute customers where it doesn't affect billing rates, they may be interested to see a report that includes their peak usage per hour/day/week/month, etc.
  * **SpeechServer**.  Authoritatively reports the speech server being used.  Can be used by CaaS to double check what features were available to the customer (ex. Tier 3 vs Tier 4 Nuance ASR), or just for auditing.
  * **CallLanguage**.  May not be set reliably because call attributes can accidentally be changed by customers.  May be useful for double checking what languages a customer is using, or may be used for reporting purposes especially if the LanguagesUsed field is blank.
  * **LanguagesUsed**.  Any language reported by this field was authoritatively used, but languages that were used may not be reported since the IC system does not have full visibility into the requests being issued.  In fact, this field may be empty in reports, which means we weren't able to detect anything.  (Empty field does not mean that the speech resource was not used.)
  * **Grammars**.  Authoritatively lists all grammar URIs that were used. (Only used for ASR resources.)  Since we can't guarantee that we can detect all languages used, we report the grammars used because that's the only information we can reliably see in the ASR requests.  CaaS may be able to use the Grammar URIs to determine what languages or features were actually being used during an ASR session.  This can be used to either determine the appropriate billing rate (ex. check whether the caller used a multi-lingual application) or just for reporting purposes.
    * Even if customers have a flat rate (ex. they're not using multiple languages), verifying the grammar URIs can help show whether the application has changed and might include new grammars that could be using different languages.



# Design

TS, MRCP Subsystem, and Reco Subsystems must gather the Billing Data described above.  Specifically:

  1. **Application Name**.  TS, MRCP, and Reco query a call attribute, and report it to CaaS billing.
  2. **Speech Server**. TS, MRCP, and Reco will report which Speech server was used. For example, if application features are segregated by speech server, reporting which server was used could indicate which application was used. (If certain languages are only installed on certain servers, the fact that certain servers were used would indicate that those languages were used.) TS or Reco will report the information it has available (ex. IP address or server name).  The main constraint is to report a consistent value across sessions that use the same server, assuming that the Speech server configuration hasn't changed.
  3. **Resource Usage**. TS, MRCP, and Reco will report whether ISR/ITTS is order or Nuance Recognizer/Nuance Vocalizer was used.  To the extent possible, TS and Reco will report what languages were used as Addon Resources.  However, TS will not be responsible for parsing SSML to detect embedded languages, and Reco is not responsible for inspecting unparsed grammars or external grammar references to detect languages.  Since it's not possible for Reco to detect which features are used (ex. languages in unparsed grammars or external references, tiers, and whether a grammar belongs to NDMs), we will need to list grammar URLs that are used during the session.  This would allow the billing subsystem to do post-processing to validate whether or not certain features (like NDMs or extra languages) were used.  Since reporting all grammar URIs may increase message sizes, require more storage space, and the data may not be useful in all cases, there should be a Reco property that can be set to disable this reporting.
  4. **Concurrent ports and Duration**. TS may report on concurrent port usage if it has the information available, but it probably won't have that information for MRCP plays.  In addition, TS doesn't know the duration that an MRCP port is used, only the duration of individual plays and the duration of calls that can use TTS.  TS will report the play durations that it sees, and MRCP will report the session duration.  These statistics will be reported as separate BaseResource types, and CaaS Billing can use the information it needs.



For ITTS, Media Server will need to report ITTS durations and languages used.

Informational Data| Call Attribute| Value  
---|---|---  
Application Name| Eic_SpeechApplicationName| String  
ASR Features| Eic_SpeechAddonResources| Multi-valued String. Can report ASR tier as well as possible NDM usage.  
Call Language| Eic_Language| String  
  
## Data Format

When sending notifications, to CaaS Billing, the information will be in an AttributeValue with one or more AttributeMaps.  If there are multiple notifications, multiple AttributeMaps will be in the AttributeValue.  Each AttributeMap will have as many of the fields described in the Billing Data section as possible.  For example, TTS notifications will not set the Grammars attribute.

## Server Parameter

In order to mitigate scalability risks, especially for customers who may be using a lot of speech ports in a Premise environment, we will disable notifications if the Server Parameter "Enable CaaS Speech Billing" is not set.  This parameter can be changed dynamically (does not require any restarts).  In the future, we may tune notifications so that multiple notifications are grouped together so that the load on Notifier is limited. 

# Questions

1. How will TS or Reco Subsystem know what ApplicationName and resources to report?

Call attribute is used for Application Name, and is only used for reporting (not billing).  TS and Reco will attempt to detect languages usage, and they'll also report the call's language attribute.  Reco will also report the grammar URLs used during the session, which can help the billing system detect additional feature usage (NDMs, languages, etc.) through a whitelisting or blacklisting system.

2. How do we measure TTS usage?

By the length of time a TTS port is used.  For example, if there is a gap between TTS plays long enough that we release the TTS port, we report when the port is originally released, and report again when the second port is freed.

3\. How does Nuance charge for language usage?  If an application supports three languages, but each caller only uses a single language, what billing rate applies?

Robin stated that a higher rate applies for calls that use a multi-language application, regardless of which language(s) each caller uses, although the exact definitions weren't clear.  Ultimately, we will report on grammar usage so that CaaS can determine which applications were used and which billing rate applies.

4\. Is there a reliable way for call attributes (or something similar) to be set in an application so that we can use the information for billing?  (In other words, is there a way to set call data in one place such that it could be queried later with confidence that a customer couldn't have altered the value?)

No, call attributes are not reliable and cannot be used for billing purposes.  They are only useful for reporting purposes.  Instead, billing information must be obtained programmatically.

5\. What happens if the billing subsystem is down? Would Reco and TS need to buffer these requests? How many events would we be responsible for buffering (ex. would we need to write to disk)? What if a request times out; we wouldn't know whether the billing subsystem processed that request or not.  Should requests have a GUID so that duplicates could be identified and discarded?

We can assume that the billing subsystem is reliable and will not go down. The subsystem is critical for CaaS, and they have a redundant proxy service that mitigates the risk that the subsystem will go down. Also, there are alarms that would go off in the NOC so that any outage would be brief, and likely no more than one of the redundant systems would fail.

6\. How does Nuance charge for NDM usage?  If an application only uses NDMs for half the call, does the entire call have an uplifted rate?

Robin is not clear on the requirement from Nuance, but noted that we do not have any customers who want to purchase NDMs with per usage billing.  It's assumed that applying the uplift to the entire call would suffice, although it may be more expensive than needed.  This issue may need to be revisited later, but it was expressed that providing timing information on per recognition/per grammar activation basis was too detailed.  Instead, we will report session usage, which would not provide visibility in how long certain grammars were used (ex. the NDM application). 

# Links
