## 

# Smarter STP

Leader: Scott

Abstract: A research presentation & discussion regarding how we can improve the quality of words which go through stp.  Includes justification for where the improvements need to happen, feasibility/cost analysis to implement.

Attendees: Ling.  <Should components be invited?>

# Demo: Displaying vowel charts graphically

Presenter: Linda

Abstract: Creating distinctive feature lists for vowels currently requires lots of data massaging.  Having the ability to convert a text-list of vowels into an IPA-style visual vowel chart will help linguists see at a glance what groupings have been selected.

Attendees: Just for ling team.

# Part-Of-Speech Tagging

Leader: Rich

Abstract: Reporting experiment results for how we might train a part-of-speech tagger for some of our languages.  Overview of 1) how we might use leverage a pos-tagger in our run-time system (justification), and 2) brainstorming how a pos-tagger might be incorporated into the ITTS architecture (feasibility, cost, risk, etc)

May also discuss adding getPOS functionality within CAD.

Attendees: Ling.  <Should components be invited?>

# Improved Data Management for TrainingData (labels, alignments)

Leader: Emma

Abstract: Passing data from prompts/dictionary to asr alignments to full-context-labels to SDE annotations requires several formats, conversion scripts, and one-off annotation scripts.  This talk will highlight the biggest issues, and propose some changes that can help consolidate data, reduce data conversion errors, and make script adaptation quicker.

Attendees: Ling. Adam/Ananth. Veera/Aravind.

# 'Commas' that don't correspond to pauses

Leader: Scott

Abstract: Training Prompts may include commas, where the voice talent doesn't actually pause very long before continuing.  asr-alignments may not detect an acoustic pause in this scenario.  Our full-context-labels do not support a phrase boundary that does not also contain a pause.  Can/should we make a change to support this?

  * How big of an issue is this? (justification)
  * Potential solutions:
    * Re-use the tone fields (current, previous, next) to mark whether the current word is at a comma, or maybe the current word's distance from a comma. This could help the model reproduce intonation and length characteristics, whether or not there's actual silence. Re-using tone fields would rule out this strategy for zh-CN, though.



Attendees: Ling. Adam/Ananth. Veera/Aravind.

# Ensure TTS can handle long SSML docs

Leader: Adam

Abstract: Is reviewing CAD regexes enough? What about really big SSML docs of a single character with no word breaks?  Strategizing about how to protect our system from data that could crash it.  May involve forced splitting text before we enter CAD.

Attendees: Adam/Ananth/Ling/?
