Page Contents

# Creating an SCR**  
**

**Issue Type**

****

  1. New Feature
     1. Most of our work is considered a 'New Feature', or enhancement. New language, general model improvements, pron fixes, text norm enhancements, etc.  

  2. Bug   
     1. Only use in response to a customer support case or a potential support case (i.e. the issue was severe enough to warrant complaining).  For example:  

        1. Making a significant improvement to a deficiency along the lines of fixing a voice that wasn't intelligible enough, fixing a confidence model that was skewed, etc.  

        2. Correcting wrong behavior: fixing code that was incorrectly reading out "0060" as "1060"  

     2. Or when fixing some incorrectly supported SSML standard  




**  
**

**Summary**

****

Name your work succinctly. Treat the rest of the Speech Group as your audience, and make sure they would get the gist at a glance.

**  
**

**Component**

****

Most often this is 'i3tts', 'i3asr', 'i3kws', or 'i3ca'.

  


**Description**

****

Document the high-level details of what this work entails.   Enough for your manager or teammate to know what type of changes to expect in your changelist.  Note any significant technology or algorithm changes.

  


**Priority**

****

If you're not sure, leave this for your manager to set.

 

  


**Found In Version/s   (**Bugs Only**)  
**

Set to 'main'.  We only set specific releases if this bug requires patching.  


 

  


**Found In Branch   (**Bugs Only**)**

"Production" = Bug exists in a released version of CIC or a deployed Edge build  
"Systest" = Bug exists in  //media/main_systest  
"Team" = Bug only exists in  staging.speech, ling, etc.  


  


**Development Labels**

****

If applicable, specify the language(s) affected (e.g. "en-US", "fr-CA").

  


**Team Labels**

****

Optional.   Useful for tagging with team branch name if you're working in one of those.  


**  
**

**Links**

After creating an SCR, link ("More" > "Link") any relevant SCR's.  Particularly if this is a multi-part change.

  


# Tracking your work in an SCR

NB: We're not strict about Backlog vs Accepted vs In Progress at the moment, but want to move this direction.  Doing so will help us keep the scope of our workload less sprawled.  


**Backlog**  

  * Work we may get to someday



**Accepted**   

  * No active progress, but this is planned work  




**In Progress**  

  * Active progress being made (e.g. in current sprint)



**Integration Testing**  

  * Use this status while you're: 
    * Testing on your own machine,   

    * Doing code review, and   

    * Waiting for your submitted code to successfully build
  * Add comments to the SCR
    * Describe any changes in performance for the end-user.  E.g. performance improvements noted & the integration test results posted, description of size requirements (memory, mips, etc)  




**Resolved**

  * Once your code has been submitted and succesfully built on a build machine, mark your SCR as resolved.



**  
**

# FAQ

**When should I add Customer-facing information?**

  * "Documentation"
    * New feature added to existing language
      * E.g. "Added Say-As support for "address" in en-US"
      * E.g. "Added new phoneme for de-DE KWS/ISR. (name & give example word/pron)"
    * New language added  

      * E.g. "Added pt-BR (Brazilian Portuguese) for TTS"
      * NB: Be sure to note any restrictions on input or behavior (i.e. for ja-JP and zh-CN)
  * "Readme" (Information customers should know, about changes in particular versions)  

    * Specifically include for: 1) Bug fixes, 2) Significant changes in handling behavior (highlighting the effect of the change)
    * NB: Since this wording is including directly in the release notes, make sure to look at a few examples if you haven't done these before. Some additional guidelines.
  * Service Update



 

  *     * This is if we want to give our customers notice that behavior has changed.  On PureCloud we document every behavior change. On PureConnect, we document behavior changes that customers need to know about because it's a bug fix, or because it's an enhancement that makes the product more sellable.  (i.e. there's a somewhat higher bar for documenting changes in pureconnect).
    * PureCloud 


  1.      1.         1. Exclude from Readme = Unchecked
        2. Add "PureCloud" to the Documentation Label field in the SCR
        3.  Add "Customer Description" field.


  *     * PureConnect


  1.      1.         1. Exclude from Readme = Unchecked
        2. Add "Customer Description" field.
        3. Add "Customer Details" field.
        4. Create an xIC SCR with the same title as the IONMEDIA SCR, and link them together.
        5. Repeat step 1-3 on the xIC SCR, copying from the IONMEDIA one.
        6. NB: when submitting this IONMEDIA SCR to systest or another release stream, you need to let that build, then immediately submit the xIC SCR with a dummy code change in eic so they're tied together in code as well.  See Adam or Emma if you need to do this.  Yes this duplicate SCR & dummy submission thing is a pain, but it doesn't have an easy workaround, and so for now it's how things are. 
        7. The following link contains examples of the type of "Customer Description" and "Customer Details" that are often included.  Check out some IONMEDIAs to see how we've been doing those, mostly related to modeling changes.  Check out other ION ones to see good examples for code & bug-related changes. <https://devjira.inin.com/issues/?jql=updatedDate%20%3E%3D%20%222016%2F01%2F01%22%20AND%20%22Customer%20Description%22%20is%20not%20EMPTY%20AND%20%22Documentation%20Labels%22%20in%20(PureCloud)%20AND%20component%20not%20in%20(i3ca)%20ORDER%20BY%20key%20ASC>


  * Documentation Impact 
    1. Select "yes" if a Technical Reference document should be updated.  If you're not sure, ask a teammate if this type of change qualifies as something that should be documented there.  These are generally for big changes in functionality and performance.
    2. Otherwise set to "no".
    3. If you accidentally selected 'yes', and a DocLink scr is created, don't just leave it.  Go "Reject" that scr and comment that it was not needed.



 

 

**When it is most important to fully document SCRs?  
** Short answer: When it affects end-users.

Longer answer via examples:  


  * Umbrella SCR for new languages
  * Bug fixes to any languages in systest
  * 'say-as' changes to any languages in systest
  * Enhancements that a customer should be informed of:  

    * gmm > dnn
    * pronunciation and/or text normalization improvements
    * acoustic model improvement
    * accuracy improvements, etc



**What is considered a "bug" in TTS (vs "new feature")?**

We say we follow SSML standards, so anything that is mandated there and incorrectly supported in our system is a bug. Let's call these bugs "True bugs".  Everything else can likely be considered a "new feature".  For example, if an issue was discovered with our acronym detection algorithm, fixing/improving that could still be considered a new feature, not a bug, from a customer perspective.  That said, we do mark these as bugs sometimes.  Let's call this second time "internal-facing bugs".

_If a "True Bug" is found in TTS, how do I fill out "Found Version"?_

(The following assumes the bug is not isolated to a teamBranch. If it's an "internal-facing bug"; usually no need to track down all the versions.)

  * Mark Main.
  * Mark CIC unreleased versions that are affected, but have not yet been released.
  * Mark all CIC release versions that are affected, up to when TTS was first released (2016 R2).



_If a "True Bug" is found in TTS, how do I fill out "Fix Version"?_

You don't. This field is automatically updated as builds complete.

_If a "True Bug" is found in TTS, do I do anything with "Patches"?_

We generally do not patch Speech Models unless:

  *     * There is a major egregious error
    * There is a customer support case



**NB: Do get "True Bug" fixes into main ASAP.  Don't be content to let them slowly trickle up the team branches with normal code.**

 
