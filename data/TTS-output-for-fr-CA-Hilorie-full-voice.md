## HTS output

Exp.No| Experiment name| Experiment description| Remarks| Samples location  
---|---|---|---|---  
1| wav_hilorie_16khz_4272_mdl_st2hts_st_mgc_f0_32_lpf_gv| 

  * Model built using 4272 files
  * HVite/eHMM alignments are used
  * Used following parameters for tree construction
    1. Dur: 0.9, F0: 0.8 MGC: 0.8

| 

  * Prosody is good
  * Observed alignment issues
  * Major issues in fricatives, plosives

| \\\speechanalytics\Public\VeeraRaghavendra\  
2| wav_hilorie_16khz_4272_asr_align_mdl_st2hts_st_mgc_f0_32_lpf_gv| 

  * Alignments are obtained from fr-CA ASR output

| 

  * Significant improvement observed in voice quality
  * Poor prosody observed

| \\\speechanalytics\Public\VeeraRaghavendra\  
3| wav_hilorie_16khz_4272_asr_align_mdl_st2hts_st_mgc_48_f0_32_lpf_gv| 

  * Combined above two models
  * F0 models are used from 48KHz models of experiment 1
  * Duration and MGC models are used from experiment 2

| 

  * Observed prosody improvement from experiment 2.
  * Due to f0 dipping creakiness observed at few places

| \\\speechanalytics\Public\VeeraRaghavendra\  
4| wav_hilorie_16khz_2606_mdl_st2hts_st_mgc_48_f0_32_lpf_gv| 

  * Model built using 2606 files
  * Alignments are used from fr-CA ASR output
  * Used following parameters for tree construction
    1. Dur: 0.9, F0: 0.8 MGC: 0.8

| 

  * Did not give any improvements
  * Exp 3 is sounded better

| \\\speechanalytics\Public\VeeraRaghavendra\  
5| wav_hilorie_16khz_4272_asr_align_mdl_st2hts_st_mgc_48_f0_32_lpf_mgcgv| 

  * GV is off for F0

| 

  * Observed creakiness reduction and introduced few other issues

| \\\speechanalytics\Public\VeeraRaghavendra\  
6| wav_hilorie_16khz_4272_asr_align_mdl_st2hts_st_mgc_48_f0_32_lpf_gv_with_es-US_gv-LogF0| 

  * Variance component of LogF0 GV is very high.
  * Hilorie LogF0 GV is replaced with Jayde LogF0 GV

| 

  * Observed reduction of creakiness

| \\\speechanalytics\Public\VeeraRaghavendra\  
7| wav_hilorie_16khz_4272_asr_align_glottf0_mdl_st2hts_st_mgc_48_f0_32_lpf_gv| 

  * F0's are extracted using GlottF0 method
  * F0 model used from 48KHz models
  * Used following parameters for tree construction
    1. Dur: 0.9, F0: 0.8 MGC: 0.8

| 

  * Reduced creakiness and breath sounds
    * Observed wobbling effect at few places

| \\\speechanalytics\Public\VeeraRaghavendra\  
  
## Eigen output

Exp.No| Experiment name| Experiment description| Remarks| Samples location  
---|---|---|---|---  
1| eigenwav_hilorie_16khz_4272_asr_align_mdl_st2hts_st_mgc_48_f0_32_lpf_gv| 

  * Eigen templates were built using 500,000 vectors
  * Followed experiment 3 setup in HTS output for f0,dur and mgc models

| 

  * sounds better and close to Hilorie voice.

| \\\speechanalytics\Public\VeeraRaghavendra\  
  
## i3tts output

Exp.No| Experiment name| Experiment description| Remarks| Samples location  
---|---|---|---|---  
1| i3tts_fr-CA| 

  * i3tts models were generated using Exp.6 of HTS-Output

| 

  * Found lower energy

| \\\speechanalytics\Public\VeeraRaghavendra\fr-CA\full-hilorie  
2| i3tts_wav_fr-CA_after_normalization| 

  * i3tts models were generated using Exp.6 of HTS-Output
  * Eigen vector was normalized using Matlab code provided by Ananth

| 

  * Working inline with earlier voices

| \\\speechanalytics\Public\VeeraRaghavendra\fr-CA\full-hilorie
