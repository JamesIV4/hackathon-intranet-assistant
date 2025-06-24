# Debugging approach

S. No| Acoustic Model| Testing data| Language model| Remarks  
---|---|---|---|---  
1| Full model| All testing benchmarks| Generated using grammar files|    
2| Full model| sub-set of training database| Generated using training sentences| WER should be very minimal, less than 3% otherwise model is broken  
3| Full model| Digits benchmark| Loop grammar| If current approach WER and #2 WER smaller, there is issue with LM.  
4| Full model| Training digits data| Loop grammar| If current approach WER is higher model is broken.  
  
# Error analysis

  1. Generate alignments for testing data.
  2. Extract all possible chunks for a word (eg: one/two/three) from test audio files
  3. Concatenate them together and analyze possible errors
  4. If there are any unusual sounds (eg: /sh/, /th/, /f/) or some other word pronunciations, then model is broken
  5. If all the chunks has valid words, then model is well trained.
  6. If #5 is true, analyse errors using hypothesis text on testing data.



# Handling noise tags

  1. NON: For non-human noises (<non> tag in the transcription)
  2. SPK: For speaker noises and fillers (<spk> and <fil> tags in the transcription)
  3. Ignore <sta> and <nps> as they occur very rarely.
  4. Ergodic for SPK phone
  5. Non-ergodic for NON phone 


