#F0F0F0solid#808080

#  _For Discussion...  
_

in two-week increments

[Language Status page](https://confluence.inin.com/pages/viewpage.action?pageId=67016845) - update for Wednesday TTS mtg

 

## CURRENT Discussion Items

  1. Moving our team to work in staging.speech branch instead of ling branch.
     1. No more push/pull.
     2. We're already comfortable using p4 (don't need "safety net" of our own separate branch anymore)
     3. Ling branch history will always be available via depot
     4. Sound ok?  If so, best if we all make the switch at once.  Immediately after a push, all our outstanding work gets shelved in ling, and unshelved in staging.speech, and we continue from there.
  2. Anyone want to volunteer to get rid of old stuff on this page?  



 

 

\-------OLDER NOTES--------------

  * Languages
    * Portuguese
    * Japanese
    * Dutch
    * Mandarin - next steps
    * British English
    * Italian
    * EuroSpanish
  * Updates from Speech Analytics leadership meeting
  * format="verbose" for say-as telephone? "The phone number area code three one seven..." sounds kind of odd.
  * Fractions - Interactive Intelligencea6f784b9-ef5d-3d60-bca5-6d0a3771dd27IONMEDIA-2978
    * First draft of proposed logic on .
  * Removing one step for a ling member reporting a TTS issue - just create the SCR.
  * Pauses in TTS vs predicted in ASR alignments
    * Summary: We will introduce a third category of "trusted pause", using colon ":" to mark manually-verified intonational pauses.  We may adjust notation.
      * training phrase predictor: ensure ':' is interpreted as Intn=List
      * mlf.mergeAsrAndTTS: add logic to shove in new timings for ':', but do not mark it for review (i.e. just leave as ":" rather than ",?"
    * praat gridSearch: Instead of resolving [,?] to ',' or ';', it should now resolve to ':' or ';'
      *         * Is that intuitive enough? eh.
  * Dictionary ordering conventions?
  * walk-through of setting parameters for merging prompts and alignments in labelGen library.



Todo:

en-XX changes (Scott will do)

  * Interactive Intelligencea6f784b9-ef5d-3d60-bca5-6d0a3771dd27IONMEDIA-2496
  * Interactive Intelligencea6f784b9-ef5d-3d60-bca5-6d0a3771dd27IONMEDIA-2506
  * Interactive Intelligencea6f784b9-ef5d-3d60-bca5-6d0a3771dd27IONMEDIA-2423 Phase I



 

Working Discussions

  1. Decide on 
  2. Additional i3tts architecture
     * Is getPOS sufficient for changes we'll need in the future, or is it a piece-meal addition?
     * What about compound analysis?
       * also needs dictionary lookup to determine prons
       * for Germanic languages, Russian, Finnish, etc.
     * Word-break & spaces
       * compound languages
       * even mandarin!
     * Justifications for "getPOS"
       * Possible now, but getPOS would make it easier  

         * de-DE abbreviated ordinals (other adjectives also possible but uncommon)
         * pt-BR (??), es-US detection of adjectival cardinals
         * pt-BR (??), es-US, fr-CA gender prediction of feminine adjectival cardinals
         * homonym disambiguation, leveraging surrounding pos tags
       * Impossible now
         * de-DE distinguish cardinal number at end of sentence (before period), or ordinal with period marker in middle of sentence. (look for certain closed classes following)
  3. 'Commas' that don't correspond to pauses.        <help fill this out!>
     *        * How big of an issue is this? (justification)
       * Potential solutions:
       * Will schedule a meeting for this when Scott/Rich here.
  4. We decided that the point person for a language will create/maintain a Confluence page of major decisions for that language (linked to the tts language status page a la ja-JP) as we settle on the decisions.



 

_On hold :_

  * PoS tags (Rich)
  * Ensuring -abbr doesn't go to STP  

    * If abbreviations are unambiguous, expand them via a translation table within CAD directly.
    * For de-DE numbers and other adjectives, if we want to have a check, best is to do so in a rake script.
  * en-XX make lg-specific generation via rake?
  * German Compounds - Components backlog
  * Elimination of PLS version of dictionary (ruby scripts; branch setup) - Components backlog. Combine this with a project to develop a single ASR/TTS dictionary for each language?
  * ASR error detection (Ling approaches - on hold until given error data to explore)
  * Phoneme Dictionary - defining broad phone classes for Tan's interpolation research. May not need to do

#F0F0F0solid#808080

# In Progress Issues

type,priority,key,summary,assignee,updatedInteractive Intelligencea6f784b9-ef5d-3d60-bca5-6d0a3771dd27assignee in ("scott.randal", "emma.ehrhardt", "rich.campbell", "linda.lanz") AND status in ("In Progress", "Integration Testing") AND issuetype not in ("Dev Sub-task") ORDER BY updated DESC 20

 

 

#F0F0F0solid#808080

# More Issues...

  * [Language Research Issues in "Accepted" or "Waiting for Review"](https://devjira.inin.com/issues/?jql=assignee%20in%20%28%22scott.randal%22%2C%20%22emma.ehrhardt%22%2C%20%22rich.campbell%22%2C%20%22linda.lanz%22%29%20AND%20status%20in%20%28Accepted%2C%20%22Waiting%20for%20Review%22%29%20AND%20issuetype%20not%20in%20%28%22Dev%20Sub-task%22%29%20ORDER%20BY%20updated%20DESC%2C%20issuetype%20ASC)
  * [Issues assigned to Components Team (Adam or Ananth) that directly involve us](https://devjira.inin.com/issues/?jql=assignee%20in%20%28%22adam.paugh%22%2C%20%22ananth.iyer%22%29%20AND%20status%20not%20in%20%28Resolved%2C%20Closed%29%20AND%20issuetype%20not%20in%20%28%22Dev%20Sub-task%22%29%20AND%20component%20%3D%20i3tts%20ORDER%20BY%20status%20ASC)


