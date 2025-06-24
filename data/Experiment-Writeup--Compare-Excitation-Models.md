## Summary

In September of 2014 we conducted a listening experiment, asking ININ employees to compare 3 versions of our synthesized voices (HTS, Drugman, and EigenVoice).  Our current research voice, EigenVoice, was dispreferred, even after attempting to make some adjustments on our end.  We believe this voice has better intonation than the earlier models, but participants rated it lower overall, citing that it had an overall 'tinny' sound to it.  This led our research team to look further into what adjustments can be made so eigen is perceived better.

## Introduction

There are various methods of evaluating synthetic voices, and for this experiment we specifically wanted to look at how listeners rated our current research voice (EigenVoice) compared to other methods we had tried in the past.  Do do this we made use of two different types of experiments, A/B testing and Mean-Opinion Score.  A/B testing pits two versions of the same prompt against one another, and requires the listener to select which sample they prefer.  This yields a ranking of voice preferences.  Mean-Opinion Score does not force ranking, but rather has listeners rate a prompt on a scale based on how natural,intelligible, etc. the prompt is.  Historically this test was used to ascertain the quality of telephone connections (e.g. were they clear enough to understand the speaker at the other end), but within Speech Synthesis it is used to rate how closely the synthetic voice mimics a natural speaker.

Because the voice-building process is somewhat different for each language, we completed the experiment for both our American English (en-US) and American Spanish (es-US) synthetic voices.

## Methodology

### Subject recruitment, demographics

Indianapolis-based ININ employees were invited by email to volunteer for the experiment.   They were directed to sign-up on a google form, which collected demographic data.  For American English we selected a subset of volunteers to actually participate, balancing by age and gender demographics as much as possible, and requiring all were native speakers of American English. [1] One group of volunteers participated in the A/B experiment, while a separate group was assigned to the Mean-Opinion Score group.

For the American Spanish experiments, due to a lack of available speakers, we tested all subjects who had some level of proficiency in the language.  These subjects completed _both_ the A/B and MOS experiments.

Note: The experiment was conducted over two days.  After day 1 when we realized EigenVoice was not well-liked by participants, we tried to make some compensatory adjustments to the American English (en-US) prompts that were used for day 2.

 

#### American English (en-US)

A/B Thurs|  |  |  |  |  |    
---|---|---|---|---|---|---  
 | <25| 25-34| 35-44| 45-54| 55+|    
Female| 1| 2| 0| 2| 1| 6  
Male| 0| 2| 1| 1| 1| 5  
 | 1| 4| 1| 3| 2| 11  
MOS Thurs|  |  |  |  |  |    
 | <25| 25-34| 35-44| 45-54| 55+|    
Female| 0| 0| 2| 1| 0| 3  
Male| 2| 1| 1| 1| 1| 6  
 | 2| 1| 3| 2| 1| 9  
A/B Fri|  |  |  |  |  |    
---|---|---|---|---|---|---  
 | <25| 25-34| 35-44| 45-54| 55+|    
Female| 1| 2| 2| 1| 1| 7  
Male| 1| 1| 1| 3| 1| 7  
 | 2| 3| 3| 4| 2| 14  
MOS Fri|  |  |  |  |  |    
 | <25| 25-34| 35-44| 45-54| 55+|    
Female| 1| 2| 2| 1| 1| 7  
Male| 0| 1| 1| 3| 1| 6  
 | 1| 3| 3| 4| 2| 13  
  
 

#### American Spanish (es-US)

A/B & MOS|  |  |  |  |  |    
---|---|---|---|---|---|---  
 | <25| 25-34| 35-44| 45-54| 55+|    
Female| 0| 1| 0| 2| 0| 3  
Male| 0| 6| 6| 2| 0| 14  
 | 0| 7| 6| 4| 0| 17  
  
 

### Experiment setup

For the Mean-Opinion Score Testing we had subjects rate our voice on a sale of 1-5 on how natural it sounded.  Averaging within and across users gives a Mean-Opinion Score for the voice.  Each participant heard 10 different prompts for each of the three voices.

For our A/B Testing we presented participants with recordings of two voices saying the same prompt, and asked them to choose which version they preferred.  In addition to running comparisons between the three synthesis voices, we also included some parings with original recordings the synthesized voices were based on, and with intentionally badly-produced synthesized samples.  The judgments from these pairings served to identify any subjects who perhaps weren't paying close attention, or who had hearing difficulties they didn't readily admit.  Each participant heard 10 different prompts for each of three voices, plus 5 additional prompts comparing the standards with the experimental voices.

#### Data Selection

Prompts were selected which covered our target use cases: personal names, IVR prompts, and reading email text.  Maximum prompt length was 6-7 seconds.  10 distinct prompts each were used for A/B testing and MOS testing.  MOS testing used an additional 5 prompts for comparing the the experimental voices with actual recordings and with poorly synthesized audio.

#### Software

The experiment was administered with custom-built experimentation software, using a web-based framework.  HTML pages used javascript to select and display the appropriate experiment stimuli to the subject, and recorded their response, posting it to a google form.  The google forms captured all relevant participant data, and made for easy downloading and analysis across research team members.

The software used a participant ID entered by each subject to determine which version of the experiment to display.  For each experiment task, instructions were displayed, then a sample stimuli was provided.  Once the subject proceded to the actual task, the stimuli were presented in a randomized fashion to prevent an ordering bias.

#### Environment

In order to remove potential sources of bias from the data collection, we heavily controlled the physical environment in which the experiment was conducted.  A quiet computer lab was configured with clean machines containing the minimal software needed for the experiment.  High-quality headphones were used to ensure subjects could clearly hear the various audio prompts.  Subjects were required to complete the experiment in person, after being given specific verbal instructions[1] from the coordinator.

## Results

 

### Statistical Analysis

**AB Test Analysis:**

Fig1:Analysis for Day1 AB English test, showing relative preference for Eigen voice as compared to HTS and Drugman across different listeners.

 

Fig2: Analysis for Day2 AB English test, showing relative preference for Eigen voice as compared to HTS and Drugman across different listeners.

 

Fig3: Analysis for AB Spanish test, showing relative preference for Eigen voice as compared to HTS and Drugman across different listeners.

 

**MOS Test Analysis:**

Fig4: Comparison of means and variances of MOS scores for Day1 English listeners

 

Fig5: Comparison of means and variances of MOS scores for Day2 English listeners

 

Fig6: Comparison of means and variances of MOS scores for Spanish listeners

### Feedback from Participants

Although we did not request feedback, some participants offered their thoughts anyway:

  * "Some of the 'names' prompts were hard to make a decision on, since they weren't very long."
  * "Sometimes I liked the entire prompt except the last word which sounded bad. So I would end up choosing the other prompt that wasn't as good of quality but didn't have that noticeable problem." (from Thurs)
  * "Some were hard to distinguish and I wanted to rate them the same" (on A/B)
  * "one of the versions had really good intonation but was tinny" (from Friday, regarding eigen).
  * "the ones I didn't prefer were the ones that had a "tinny" sound. (from Friday)
  * 2 others: "I couldn't get past the buzzy/metallic one" (referring to eigen). After the experiment we discussed this a bit further, and they said they didn't really look into the voice itself, since the metallic quality was more prominent.
  * _" I was really surprised how good and natural all the voices sounded._  I'm impressed that these are so good." (referring to all the synthesis versions)



## Conclusion

This experiment seemed to show that while improvements to excitation modeling have an important effect, but we must also consider other areas listeners take issue with at this time.

## Future Considerations

  * Labels and instructions probably have a strong priming effect on scoring.  Do we mean "natural", "pleasant", "preference", "intelligible", "overall voice quality", "acceptable" etc.
  * Do we want to do other types of tests as well (intelligibility, etc)?
  * Shorter vs. longer prompts have an effect of how people view them.
  * Is it a safe assumption that listening to 16k audio on good headsets in a quiet enfironment will yield the same user preferences as we would get with 8k on a phone in typical use scenarios?



 

 

 

 

 

  


* * *

[[1]](https://confluence.inin.com/#_ftnref1) Age groups were binned as <25, 25-34, 35-44, 45-54, and 55+.

  


* * *

[[1]](https://confluence.inin.com/#_ftnref1) It proved helpful to give background about why we were doing the research, and to remind them of how the TTS would be used, and explain a bit about what we meant by 'natural'.
