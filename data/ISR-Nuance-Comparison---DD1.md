Nuance Recognizer and ISR recognizer were compared to better understand what the differences are and where we need to improve

## Nuance Reco Tool (acc_test)

For Nuance run, acc_test tool which is part of Nuance package was used. Couple of points about it below

  1. This is a batch recognition tool and can run on multiple utterances given the grammar
  2. It does OOV identification
  3. There are some nice reports to plot ROC etc
  4. I am not yet clear on how it does VAD



## Initial Results

The whole DD1 set was run using acc_test. Since the way OOV is calculated is different from acc_test and our own i3asr_sim tool, IG utterances as reported by acc_test were used for run using ISR. This had 12104 utterances. These IG utterances were run on test_wave_files (vadless app). 

**Num Utterances**| **Num Nuance Correct (%)**| **Num ISR Correct (%)**| **Comments**  
---|---|---|---  
** **|   |  |    
**12104**|  11301 (93.36%)| 10137 (83.74%)|    
**12104**|  11301 (93.36%)| 10191 (84.19%)| Replaced certain date words like 'sixth' to 'six' etc. in reference to match isr hyp  
**12104**|  11301 (93.36%)| 10714 (88.51%)| Replaced 'yes' with 'yeah' and 'no' with 'nope' to match isr hyp  
  
 

  * Vadless app was run with confidence setting zero and beam width to 200
  * Comparison was done on raw transcriptions and not on semantic outputs
  * For example, 'yes' and 'yeah' are considered different results and so are "speak to a representative" and "speak to representative". If we had considered, semantic results, these would have been the same result  
  




Some observations:

  * Since VAD is not done, a stretch of long trailing silence causes insertions (like 'provider office' instead of 'provider'). This would mostly be correctly segmented by our VAD
  * Dates incorrect utterances are mainly due to subsitutions like "January six" instead of "January sixth" etc.
  * Missing articles like 'a', 'an' like 'speak to representative' instead of 'speak to a representative'
  * Most of the errors are in utterances where speech begins right at the start of the file or when there is a long trailing silence



## Further Analysis

Further analysis needs to be done to identify issue as modeling issue, search issue, vad issue etc. Some ideas were discussed and presented below

  * Run using a better model like 1024:512:1024 instead of 512:256:512
  * Open up beam width, token capacity to see if it yield better results
  * Find utterances that have insertions towards the end and see if trimming end silence helps
  * Force align utterances which give totally different results and analyze path scores  
  




As we complete the tasks, the results will be updated in this page
