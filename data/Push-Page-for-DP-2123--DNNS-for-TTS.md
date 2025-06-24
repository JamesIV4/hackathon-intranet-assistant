  1. Purpose of the Feature
     * Feature Name| DP/OT/PURE| Purpose/Description  
---|---|---  
DNNs for TTS (Phase I)| Interactive Intelligencea6f784b9-ef5d-3d60-bca5-6d0a3771dd27DP-2123| Interaction Text to Speech now supports enhanced models, providing more natural sounding voices for a better caller experience. These models trained with Deep Neural Networks are available for en-AU (English, Australia), en-US (English, United States), es-US (Spanish, United States, nl-NL (Dutch, Netherlands), and ja-JP (Japanese, Japan), and are enabled via an opt-in server parameter.We have used DNNs to produce more natural sounding TTS voices than was possible using earlier modeling techniques. We want to take these good results from the lab and translate them to product for improved customer and caller experiences.  Phase I includes 6 languages: en-US, es-US, en-AU, nl-NL, ja-JP, de-DE.     
  2. Areas of the Product Affected     

     * PureConnect: Media Server, ITTS
     * PureCloud: n/a.  DNN models are isolated into a separate folder under a different naming convention.  Edge code is not aware of these & so will not be affected.  PURE-1965 will implement these models for PureCloud platform.
  3. Documentation   

     * Release Notes: cf Roadmap Description field in DP
     * Tech Refs: Documented server parameter in Administrator Help under Optional General Server Parameters. Created a Release Note pointing to this.
       * Interactive Intelligencea6f784b9-ef5d-3d60-bca5-6d0a3771dd27IC-147328   

  4. Product Release Management
     * DP/OT/PURE all filled out? Yes  
     * All associated SCR's linked appropriately & resolved? Yes. The few unresolved are listed in "outstanding issues" section.    

     * Link for release notes:<https://help.genesys.com/cic/mergedprojects/wh_rn/desktop/new_features_in_2018_r2.htm> 
  5. Usability
     * No UI changes.
     * Install & Config - Utilizes a new opt-in server parameter to select loading of the new DNN models.  Not setting the parameter or setting it to false means GMM models continue to be loaded.  Intended progression is 2018R2 = Opt-in, 2018R3 = Opt-out, 2018R4 = remove parameter & only use DNN models.
  6. Patents and/or Papers and/or Tech Talks  

     * Application of DNNs to TTS was a novel application for us. 
     * Patents: Planned submission for work on "F0 transfer learning"
     * Papers:  
     * Tech Talks: DevOps Days 2017 & PureConnect Dev Showcase June 2017
  7. Privacy
     * No impact. Code touches speech models & engine, but not tracing behavior, etc.    

  8. Design
     * Yes, design discussions for how to support the 2 model types during the transition period.
  9. Licensing
     * No changes needed; all tts already licensed in code.  NB: Pushing nl-NL & ja-JP means we do need to get those on the price sheet now for PureConnect though.
  10. Outstanding issues   

     *   Media Server Sizing Document - Need to complete load testing & update calculations document.  Will work with to figure out how to actually get from our testing numbers to the points system of the sizing document.  Is considered a release blocker because customers need this info & PureConnect Cloud requests it too.   
  

     *   Interactive Intelligencea6f784b9-ef5d-3d60-bca5-6d0a3771dd27IC-147339 NB: Added this SCR during Push Meeting. Change server parameter from opt-in to opt-out.  Makes things easier for PureConnect Cloud, and our resource utilization numbers show using opt-in was probably more conservative than necessary.  
     * Interactive Intelligencea6f784b9-ef5d-3d60-bca5-6d0a3771dd27IONMEDIA-3277 \- Cf notes on PureConnect Cloud below.  

     * Interactive Intelligencea6f784b9-ef5d-3d60-bca5-6d0a3771dd27IONMEDIA-3197 - Passed the final listening tests, so we added it to the DP.  

     * Interactive Intelligencea6f784b9-ef5d-3d60-bca5-6d0a3771dd27IONMEDIA-3399 \- Didn't pass the final listening tests. Holding out language for next push.  

     * key,summary,type,created,updated,due,assignee,reporter,priority,status,resolutionInteractive Intelligencea6f784b9-ef5d-3d60-bca5-6d0a3771dd27IC-147331 \- Not a push blocker; pre-existing issue found during load testing.   

  11. 3rd Party Verification
     * n/a. Only native speech products affected by this push.
  12. Manual & Automation Testing, Speech Library   

     * Code and Models' unit tests & integration tests are passing. .  Various unit tests were added around the i3tts engine changes (refactor, optimization, etc).  

     * Manual listening tests for TTS quality:  

       * Ran internal listening tests to confirm that the DNN models sound better to us (linguists & signal processors)
       * Ran native-speaker listening tests to determine preference between DNN and GMM ([ methods & results described here ](https://confluence.inin.com/display/MediaGroup/Info+Page%3A+DNNs+for+ITTS#InfoPage%3ADNNsforITTS-languages))
  13. Functionality Testing, Media Server & PureConnect (or Edge/PureCloud)
     * Functionality testing for Media Server parameter & model selection was run manually.  No formal test cases were added to tcdb b/c parameter will go away after 2-3 release cycles when all have migrated to DNN models.  Testing description [documented here](https://devjira.inin.com/browse/IC-145535):
       * 1\. A VM with media server and IC server installed with the latest build of eic_main_team_i3ttsdnn and IVR configured to exercise TTS.  
2\. We verified in the logs that at startup without the server parameter added, the GMM legacy models were loaded in the media server. A call was placed to verify TTS output synthesized audio successfully.  
3\. Then the server parameter was added and set to true. After rebooting the media server, we verified in the logs that the parameter was set in DS, and the new DNN models were loaded into the media server. A call was placed to verify TTS output synthesized audio successfully.  
4\. Then the server parameter was added and set to false. After rebooting the media server, we verified in the logs that the parameter was set in DS, and the legacy GMM models were loaded into the media server. A call was placed to verify TTS output synthesized audio successfully.  
5\. Then the server parameter was added and set to true. The DNN models were deleted from the IC server manually. After rebooting the media server, we verified in the logs that the parameter was set in DS, and the IC server fell back to the GMM models since the DNN models did not exist. A call was placed to verify TTS output synthesized audio successfully.    

  14. Scale Testing, Media Server & PureConnect (or Edge/PureCloud)   

     1. _Testing done by the Scalability Testing team.   [Ortell, Margaret](https://confluence.inin.com/display/~Margaret.Ortell) conducted scale testing for the main_team_i3ttsdnn team branch.  Final results verified on main_systest build #_2017-10-10-CL1849980-84 with Team build files from Adam Paugh dated 11/20/2017.  We avoided updating to the latest builds through a traditional install due to TS issues in main.
        * _Media server memory for ISR + TTS in main for only 366 system calls was 2.8 GB.   We took out ISR and just ran our tests with TTS to be able to increment our test up as needed without memory being an issue._
            1. <https://devjira.inin.com/browse/IC-147331>
            2. This issue already exists in main and should have no impact on us pushing
        * The following list is our planned list of testing goals for DP-2123.
          * _Media Server Sizing document testing_
        1.            1.               1. BIS\WesTest Concurrent Calls ONLY - maximum number of calls until the packaged media server hits 70% utilization
                 1. main_systest build key,summary,type,created,updated,due,assignee,reporter,priority,status,resolutionInteractive Intelligencea6f784b9-ef5d-3d60-bca5-6d0a3771dd27IC-146422
                 2. DP-2123 team build key,summary,type,created,updated,due,assignee,reporter,priority,status,resolutionInteractive Intelligencea6f784b9-ef5d-3d60-bca5-6d0a3771dd27IC-146429
              2. BIS\WesTest Keyword Spotting
                 1. keyword set with 10 kws, on 100% of calls - maximum number of calls until the packaged media server hits 70% utilization
                    1. main_systest build key,summary,type,created,updated,due,assignee,reporter,priority,status,resolutionInteractive Intelligencea6f784b9-ef5d-3d60-bca5-6d0a3771dd27IC-146422
                    2. DP-2123 team build key,summary,type,created,updated,due,assignee,reporter,priority,status,resolutionInteractive Intelligencea6f784b9-ef5d-3d60-bca5-6d0a3771dd27IC-146433
                 2. keyword set with 100 kws, on 100% of calls - maximum number of calls until the packaged media server hits 70% utilization  

                    1. main_systest build key,summary,type,created,updated,due,assignee,reporter,priority,status,resolutionInteractive Intelligencea6f784b9-ef5d-3d60-bca5-6d0a3771dd27IC-146423
                    2. DP-2123 team build key,summary,type,created,updated,due,assignee,reporter,priority,status,resolutionInteractive Intelligencea6f784b9-ef5d-3d60-bca5-6d0a3771dd27IC-146433
              3. BIS\WesTest ISR + TTS - maximum number of calls until the packaged media server hits 70% utilization
                 1.                     1. main_systest build key,summary,type,created,updated,due,assignee,reporter,priority,status,resolutionInteractive Intelligencea6f784b9-ef5d-3d60-bca5-6d0a3771dd27IC-146428
                    2. DP-2123 team build key,summary,type,created,updated,due,assignee,reporter,priority,status,resolutionInteractive Intelligencea6f784b9-ef5d-3d60-bca5-6d0a3771dd27IC-146432
              4. BIS\WesTest ISR with prompt recordings - maximum number of calls until the packaged media server hits 70% utilization
                 1.                     1. main_systest build key,summary,type,created,updated,due,assignee,reporter,priority,status,resolutionInteractive Intelligencea6f784b9-ef5d-3d60-bca5-6d0a3771dd27IC-146426
                    2. DP-2123 team build key,summary,type,created,updated,due,assignee,reporter,priority,status,resolutionInteractive Intelligencea6f784b9-ef5d-3d60-bca5-6d0a3771dd27IC-146433
              5. BIS\WesTest Combined scenario - some calls, some w/ KWS and some IVR\TTS until the packaged media server hits 70% utilization
                 1.                     1. main_systest build key,summary,type,created,updated,due,assignee,reporter,priority,status,resolutionInteractive Intelligencea6f784b9-ef5d-3d60-bca5-6d0a3771dd27IC-146428
                    2. DP-2123 team build key,summary,type,created,updated,due,assignee,reporter,priority,status,resolutionInteractive Intelligencea6f784b9-ef5d-3d60-bca5-6d0a3771dd27IC-146434
        * We added these test
          * key,summary,type,created,updated,due,assignee,reporter,priority,status,resolutionInteractive Intelligencea6f784b9-ef5d-3d60-bca5-6d0a3771dd27IC-147332
            * Results 

Callset| Rate of each callset| Time Started| Media Server Average Working Set| Media Server Audio Engine Load| Media Server Privileged Time| Media Server Processor Time| Media Server User Time| Media Server DPC Time| Media Server Disk Idle Time| Concurrent system calls  
---|---|---|---|---|---|---|---|---|---|---  
1st| 3 calls every second| 13:30| 1.61 GB| 21%| 121.33%| 1,746%| 1,625%| 2.65%| 99.95%| 868  
2nd| 4 calls every second| 13:30| 1.61 GB| 21%| 121.33%| 1,746%| 1,625%| 2.65%| 99.95%| 868  
3rd| 4 calls every second| 13:40| 2.37 GB| 25%| 186.78%| 2,118%| 1,948%| 3.95%| 100.38%| 1,412  
4th| 4 calls every second| 14:30| 3.23 GB| 35%| 218.86%| 2,227%| 2,009%| 5.89%| 100.78%| 1,846  
5th| 4 calls every second| 16:30| 3.96 GB| 45%| 242.02%| 2,193%| 1,951%| 7.26%| 100.26%| 2,342  
          * key,summary,type,created,updated,due,assignee,reporter,priority,status,resolutionInteractive Intelligencea6f784b9-ef5d-3d60-bca5-6d0a3771dd27IC-147333
            * Results 

Callset| Rate of each callset| Time Started| Media Server Average Working Set| Media Server Audio Engine Load| Media Server Privileged Time| Media Server Processor Time| Media Server User Time| Media Server DPC Time| Media Server Disk Idle Time| Concurrent system calls  
---|---|---|---|---|---|---|---|---|---|---  
1st| 3 calls every second| 10:55| 1.53 GB| 19%| 115.64%| 569.3%| 453.66%| 2.36%| 98.28%| 868  
2nd| 4 calls every second| 10:55| 1.53 GB| 19%| 115.64%| 569.3%| 453.66%| 2.36%| 98.28%| 868  
3rd| 4 calls every second| 13:00| 1.91 GB| 32%| 183.76%| 937.52%| 753.76%| 4.03%| 98.73%| 1,356  
4th| 4 calls every second| 15:00| 2.30 GB| 47%| 264.52%| 1,445.48%| 1,180.95%| 6.04%| 99.93%| 1,848  
5th| 4 calls every second| 16:30| 2.71 GB| 65%| 339.57%| 1,952.52%| 1,612.95%| 8.31%| 99.81%| 2,345  
        * [DP-2123 Scale testing project page](https://confluence.inin.com/display/Testing/DP-2123+Scale+Testing+for+Implementing+DNNs+%28Deep+Neural+Networks%29+for+ITTS)
  15. Misc Testing & Concerns  

     1. PureConnect Cloud
        1. Per , plan is to enable this parameter for all customers, & add Media Servers as needed, avoiding the issue of having 2 customers sharing a media server but requesting different model types.  Confirming that the parameter is sufficient for their management processes. NB: Addressed this at push meeting.  Course of action: 1)change parameter to opt-out.  Makes it easier to administer b/c only 1 IC server must have parameter enabled for all to pick up the DNNs. 2)Will retain gmm models current label as "higher version number models", so that if rollback is needed no media restart is required.  

  16. Compatibility
     * Automated testing covers backwards compatibility with previous models/engines.
  17. Migration
     * n/a
  18. Memory & CPU Profiling
     * New TTS models, under worst-case scenario (only interactions are IVR calls, IVR consists only of TTS+DTMF, with no recordings, run at load), show ~15% higher cpu and ~40% higher memory.  Since TTS is actually a quite small part of most interactions, few customers should notice the hit.

 | Concurrent system calls| Media Server Average Working Set| Media Server Audio Engine Load| Media Server Processor Time  
---|---|---|---|---  
Team Build. EnhancedTTS = True (DNNs)| 2,342| 3.96 GB| 45%| 2193%  
Team Build. EnhancedTTS = False (existing GMMs)| 2,345| 2.71 GB| 65%| 1952.52%  
Systest Build. (existing GMMs)| 2,345| 2.70 GB| 67%| 1898.28%  
  19. Localization

     * n/a. We are the localization. :)
  20. Security
     * No new concerns, since we're just making a new version of models available.
  21. Recommendations

     * Push into systest; but must finish up documentation, & Media Server Sizing Document as release blocker.




 
