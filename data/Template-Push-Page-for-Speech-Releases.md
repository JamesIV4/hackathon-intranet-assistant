  1. Purpose of the Feature
     * <fill in table for feature(s) being pushed>

Feature Name| DP/OT/PURE  
---|---  
ITTS for it-IT (Italian)| [DP-2087](https://devjira.inin.com/browse/DP-2087)  
ISR for it-IT (Italian)| [DP-1798](https://devjira.inin.com/browse/DP-1798)  
     * <copy justification from DP/OT/PURE>
     * Additional stand-alone SCR's being pushed (bug fixes, very minor changes)
       * <scr links> or <delete this bullet point if n/a>
  2. Areas of the Product Affected
     * Media Tier
  3. Documentation - Has documentation by the Doc team been completed?  

     * Release Notes: <n/a> or <link to SCRs>
     * Tech Refs: <n/a> or <link to SCRs>
     * read.me: <add link here to JIRA query to show all issues linked to this push. Look at service update-related fields. Use a saved filter as base to affect columns that are visible by default.>  

       * Do a JIRA query showing all issues linked to this push.  Show columns for docLabel, Exclude from ReadMe, Customer Description, & Customer Details.
       * If it should be documented in PureConnect: Must be on an IC-XXXX, usually under Media Server component.  Fill out Customer Description and Customer Details.  Link that IC to the DP/OT/PURE and/or to the main umbrella IONMEDIA scr.  For examples, see <https://my.inin.com/products/Pages/Downloads.aspx> under CIC Summary.  Why an IC?  Currently IONMEDIA (& other ION projects) do not use the service-update field, wish they did. :/
       * If it should be documented in PureCloud: Must be on an IONMEDIA.  Fill out Customer Description Only & apply DocLabel "PureCloud"
       * Assuming team members added service notes on IONMEDIA during normal check-ins, then for push just need to review wording & make adjustments that are platform specific as stated above.  For instance, a single IC-XXXX may be created that covers related changes for multiple languages.**  
**
  4. Product Release Management
     * All associated SCR's linked appropriately & resolved?  
     * DP/OT/PURE all filled out?   

  5. Usability
     * UI/UX changes? <n/a>
     * Install process? <n/a> or <details below>  

       * If adding a new language to KWS/ISR/TTS, install work is same as for previous lgs.  (submitted to an eic team branch, push simultaneous with pushing media team branch)
  6. Patents
     * Any new technology or methods in this push?
       * If yes, have patentability discussion with legal counsel (Margaret Baumgartner) occurred?
  7. Design
     * <No change to UI/UX or architecture.> (If routine update with no architecture changes) or <describe or link to info pg> (if architecture changes to i3tts or media)
  8. Licensing
     * <No new licensing or pricing work necessary, since this was improvement to existing models.> (only if push is an update to existing licensed product/language combo, and no pricing changes needed) OR
     * feature key(s) created & in code:
     * added to price sheet?
     * "Are the part numbers already created and has the license been added to the production license generator?"
     * "Has a license from [license-int](http://license-int.inin.com/LicenseManagement) been tested?"
     * "Is the feature billable by CaaS?"
  9. Outstanding issues
     * <list any known quality issues or room for improvement>
     * <any remaining known bugs at speech-media level>
  10. 3rd Party Verification
     * <n/a. Only native speech products affected by this push.> OR
     * <details> (if changes affect Nuance, e.g. echo canceller, confirm appropriate tests run)
  11. Manual & Automation Testing, Speech Library
     * code & model unit tests & [integration tests](https://confluence.inin.com/display/MediaGroup/Speech+Components+Integration+Test) passing?
     * <keep appropriate descriptions below>
     * Quality tests for ISR: <attach here> precision/recall & per-grammar results attached (runs [automatically on each build](http://devspeechtests.inin.com:8080/job/media_team_staging_speech/ws/html_reports/junit/i3asr/index.html))
     * Quality tests for KWS: <attach here> detection rate and false alarm rate results attached (runs [automatically on each build](http://devspeechtests.inin.com:8080/job/media_team_staging_speech/ws/html_reports/junit/i3asr/index.html))
     * Quality tests for TTS: unit tests for common pronunciations (500) & text normalization (500+).  Manual "listening tests" to approve quality changes.
     * New Tests: <describe new tests added>  

  12. Functionality Testing, Media Server & PureConnect (or Edge/PureCloud)
     * <Right now these are owned by other teams, but we need to review what tests are available to run, & if they are needed for a specific push.>  

 
  13. Scale Testing, Media Server & PureConnect (or Edge/PureCloud)  

     1. <Will fill in details from Margaret as we start running these.>
  14. Misc Testing
     1. CaaS?
     2. Anything else not covered?  

  15. Compatibility
     * Automated testing covers backwards compatibility with previous models/engines.
     * <NB: If any other compatibility testing needed, note here.>
  16. Migration
     * n/a
  17. Memory Profiling
     * "Profile to make sure there are no memory leaks.  Server side and client side"
     * <No new code in this push, only models.  So don't expect issues with respect to memory leaks, etc.>
     * <We have run size-in-memory numbers, and these are on par with other released languages.>
     * <need better wording to address this>
  18. Localization

     * n/a. We are the localization. :)
  19. Recommendations

     * Push into systest, push into systest contingent on a fix, or do not push? <Explain push contingencies or why a project should not push.>




 
