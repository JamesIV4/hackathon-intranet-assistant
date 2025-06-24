### Purpose

This page is used by development to maintain the life-cycle of [feature toggles](https://confluence.inin.com/display/PureCloud/Feature+Toggles).

The first feature flag that was created was for ASE-126 and can be used as an example for future features: Interactive Intelligencea6f784b9-ef5d-3d60-bca5-6d0a3771dd27IONMEDIA-4000

The PureCloud feature toggle name in GrandCentral should have the prefix "edgeMedia", such as "edgeMediaShortSpeechDetection", which is then converted on the media side (icservermediaaudio) to "featureFlagShortSpeechDetection".  Note that edgeMedia* maps to featureFlag* for consumption, for example, by call analysis in i3ca.  This work was done in Interactive Intelligencea6f784b9-ef5d-3d60-bca5-6d0a3771dd27IONEDGE-4659.

How do I know when the feature flag is actively being used after initially enabled?

The media layer (whether on the MMS, media microservice, in AWS or on a local Edge if its an LDM Edge, local deployment model) receives a parameter modify event from Edge (control) and traces the following (within a few minutes of the feature flag being enabled for a specific org, for example).  A trace at the same level that comes next, will show all of the old values and the new values (trace starting with "icmediaserveraudio::Server::set_properties() : Properties changed:").

Snippet \2019-04-03\ininedgemedia.ininlog

Message| Timestamp (UTC)| Topic| Thread| Level  
---|---|---|---|---  
icmediaserveraudio::Server::modify() : Modify parameters:   
'mediaprovider.properties' => [AttributeMap:   
{  
'OrgId' => [String: {"11348069-109f-4b21-a26e-7f76cc6b79a9"}]  
'featureFlagShortSpeechDetection' => [Boolean: {true}]  
'MaxAudioEngineCount' => [Integer: {-1}]  
'HyperThreadedAudioEngines' => [Boolean: {true}]  
'FaxBaseUriLocal' => [URI: {[file:///c:/edge/resources/tenants/[UUID_removed]/faxes/received/](file:///c:/edge/resources/tenants/11348069-109f-4b21-a26e-7f76cc6b79a9/faxes/received/)}]  
'TraceLogBaseUriRemote' => [URI: {<file:///c:/edge/inin_tracing/>}]  
'MinSchedulerLatency' => [Integer: {4}]  
'CallRecordingBaseUriLocal' => [URI: {[file:///c:/edge/resources/tenants/](file:///c:/edge/resources/tenants/11348069-109f-4b21-a26e-7f76cc6b79a9/recordings/calls/)[UUID_removed][/recordings/calls/](file:///c:/edge/resources/tenants/11348069-109f-4b21-a26e-7f76cc6b79a9/recordings/calls/)}]  
'ProcessCpuLoadLimit' => [Double: {0.9}]  
'MinThreadPoolThreads' => [Integer: {8}]  
'QosFactoryCreateOption' => [String: {"Auto"}]  
'AudioEngineUdpSenderLoopback' => [String: {"ForceForLocalAddresses"}]  
'MaxActiveDiagnosticCaptures' => [Integer: {32}]  
'CreateMemoryDumpOnEngineFault' => [String: {"Full"}]  
'AudioEngineThreadPriority' => [String: {"TimeCritical"}]  
'AudioEngineCpuMask' => [Null]  
'ProcessPriorityClass' => [String: {"Realtime"}]  
'AudioEngineSelectionAlgorithm' => [String: {"Dynamic"}]  
'AudioEngineLoadLimit' => [Double: {0.8}]  
'VoicemailRecordingBaseUriLocal' => [URI: {[file:///c:/edge/resources/tenants/](file:///c:/edge/resources/tenants/11348069-109f-4b21-a26e-7f76cc6b79a9/recordings/voicemail/)[UUID_removed][/recordings/voicemail/](file:///c:/edge/resources/tenants/11348069-109f-4b21-a26e-7f76cc6b79a9/recordings/voicemail/)}]  
'featureFlagMicroService' => [Boolean: {true}]  
}]| 15:20:00.8562306_0015| icmediaserveraudio.Server| 0x85c| 41  
  
 

If this parameter modify notification didn't come in during the expected time (within a few hours on the same day), assuming the feature has been successfully saved (GrandCentral), then you could also confirm whether the feature toggle service returns true for the new feature toggle for a given organization.  Details can be found on , specifically:

"Non-Spring services can use the feature-toggle service REST API (e.g. <http://feature-toggles.us-east-1.inindca.com/feature-toggles/>) to query the value of feature toggles for the environment and specific organization."

That REST API should redirect you to the documentation (e.g., <http://feature-toggles.us-east-1.inindca.com/feature-toggles/swagger-ui.html>), where you can browse to the right endpoint to place a test call (e.g., [/v1/organizations/{organizationId}/feature-toggles/{featureName}](http://feature-toggles.us-east-1.inindca.com/feature-toggles/swagger-ui.html#!/organization-feature-toggles/getSpecificFeatureToggleForOrgUsingGET)).

**Media Referenced** \- Media (C++) code still exists that references this toggle.

**Org(s) Enabled Date(s)** \- Specific organizations that had it enabled to test.  Submit a [Change Management](https://inindca.atlassian.net/servicedesk/customer/portal/7) ticket when enablingsingle orgs ([example](https://inindca.atlassian.net/projects/PURECM/queues/issue/PURECM-72172)).

**Globally Enabled Date** \- Date that toggle was enabled globally. Almost all toggles should eventually reach this point, otherwise the toggle is most likely being misused.  Before enabling, submit a [Change Management ticket](https://inindca.atlassian.net/servicedesk/customer/portal/7).  


**May Be Deleted** \- Time to eliminate this toggle by starting the removal of code references.

**Ready for Deletion** - Code references have been removed and toggle is no longer wanted.

### Speech Technology Feature Toggles

Name| Media Referenced| Org(s) Enabled Date(s)| Globally Enabled Date| May Be Deleted| Ready for Deletion| Notes  
---|---|---|---|---|---|---  
      
    
    edgeMediaShortSpeechDetection

|  1 complete Yes | prod (us-east-1):

  * 2019-xx-xx:   EXL-YRC (7a972322-5d85-4bcc-9efc-514f2a2c6043)
  * 2019-04-01: [flex-viacrediassembleias](https://inindca.atlassian.net/browse/PURECM-72171) (279a4959-9a1d-4590-bd3d-7da6d76d7307)
  * 2019-04-01: [Flex-paranabanco](https://inindca.atlassian.net/browse/PURECM-72171) (56d841f6-1b40-4316-8a26-8b91908e84b2)
  * 2019-04-01: [flex-camerite](https://inindca.atlassian.net/browse/PURECM-72171) (ab0d7ffe-ea39-4336-b01f-a8af76e9acca)
  * 2019-04-01: [flex-prbarthurbernardes](https://inindca.atlassian.net/browse/PURECM-72171) (c22ab4a5-0a47-4944-86ad-d96525f91f14)
  * 2019-04-01: [flex-prbjoaobettega](https://inindca.atlassian.net/browse/PURECM-72171) (eece151e-2e93-46bb-a732-5b83f19520f1)
  * 2019-04-01: [flex-viacredi](https://inindca.atlassian.net/browse/PURECM-72171) (fab42e17-e059-43c2-801d-1df36cd89b9d)
  * This list has exploded from Care, so please check [GrandCentral](https://grandcentral-ui.ininica.com/#/feature-toggles/feature-toggle/edgeMediaShortSpeechDetection?ecosystem=pc) for the latest enabled Orgs (32 as of April 2019)

prod-apse2 (ap-southeast-2)

  * 2019-04-03: [BizCover](https://inindca.atlassian.net/projects/PURECM/queues/issue/PURECM-72172) (11348069-109f-4b21-a26e-7f76cc6b79a9)

 |  |  3 incomplete Yes |  4 incomplete Yes | Interactive Intelligencea6f784b9-ef5d-3d60-bca5-6d0a3771dd27IONMEDIA-4000Interactive Intelligencea6f784b9-ef5d-3d60-bca5-6d0a3771dd27IONMEDIA-4058Interactive Intelligencea6f784b9-ef5d-3d60-bca5-6d0a3771dd27IONEDGE-53342019-06-14: So far only positive impact for customers.  When missed short greetings are reported, this feature fixes it, without causing any additional known/reported issues (regressions).  See JIRAb3972da3-ea76-350d-b02c-d56219184865SERVOPS-6653 where over 25 orgs had it enabled (for a partner, April 23, 2019) sine the issue was resolved in the initially reported org
