One team member will be assigned to oversee all of these tasks, with the responsibility rotating quarterly.

  1. Keep 'main_team_ling' branch in sync with 'main_team_staging.speech' with weekly pulls and (weekly or bi-weekly) pushes
     * Instructions for ****
     * Check  [Pulse Server](http://ibuild1:8080/browse/projects/media_main_team_staging.speech/) to confirm staging.speech is in a good state to pull, or check with AdamP.

     * Generally, we want to push everything in ling to staging.speech, unless a specific language is in a bad state.

Outlook rules that may be useful
       * Rule1: "Move Pull_Required Emails to Maintenance Folder"
         * Where my name is in the To box; and sent only to me; and from "Randal, Scott"; and with "FW: [PULL_REQUIRED]" in the subject
         * Move it to the "MaintenanceNotes" folder
       * Rule2: "Move Pull_Required Emails to Maintenance Folder And Mark Read Except on Friday" (client-only)
         * Where my name is in the To box; and sent only to me; and from "Randal, Scott"; and with "FW: [PULL_REQUIRED]" in the subject; and with "'Sat' or 'Sun' or 'Mon' or 'Tue' or 'Wed' or 'Thu'" in the message header
         * Move it to the "MaintenanceNotes" folder; and mark it as read; and stop processing more rules
  2. Triage user-reported TTS errors  
 
  3. Various tasks when pushing from staging.speech to systest
     * update 
     * For the push review, provide a list of any SCR's associated with code on regular pushes from staging.speech to systest

Details...

**Grab list of SCRs**  
1\. In Perforce, look at history for CLs submitted since last push.  Grab SCRs from these CLs.  
2\. In JIRA, look at SCR's resolved recently

(component in (i3tts, i3asr, i3kws, i3speech, i3ca, ippspeechcoding) OR assignee in (emma.ehrhardt, Rivarol.Vergin, Yingyi.Tan, Linda.Lanz, naresh.kumar, scott.randal, adam.paugh, jason.mcdowell, adrian.petrescu, srinath.cheluvaraja, margaret.ortell, ananth.iyer)) and project not in ("OT","DP","xIC","Customer Care") AND issuetype not in ("Dev Sub-task", Sub-task,Task) AND resolutiondate >= "2017/12/01" AND resolution not in ("Rejected")

3\. In JIRA, also look for SCR's that were updated lately but maybe haven't been marked resolved

(component in (i3tts, i3asr, i3kws, i3speech, i3ca, ippspeechcoding) OR assignee in (emma.ehrhardt, Rivarol.Vergin, Yingyi.Tan, Linda.Lanz, naresh.kumar, scott.randal, adam.paugh, jason.mcdowell, adrian.petrescu, srinath.cheluvaraja, margaret.ortell, ananth.iyer)) and project not in ("OT","DP","xIC","Customer Care") AND issuetype not in ("Dev Sub-task", Sub-task,Task) AND status not in (Resolved,Backlog) AND updatedDate >= "2017/12/01"

**Narrow down the list**

1. Exclude SCR's that do not affect this release version.  E.g.

       * archival checkins (e.g. training files)
       * code that is not being pushed (e.g. language components still under development & not yet released)
       * SCRs about changes to webapps or other scripts/tools that aren't built in CIC

2\. Generally, if several tiny task-like SCR's are covered by a larger umbrella SCR, it's ok to just tag the umbrella scr and omit the smaller steps.

 

Hint, use "AND key not in (IONMEDIA-2061...)" use to exclude SCR's not relevant to this push (while you're sorting through the list)



