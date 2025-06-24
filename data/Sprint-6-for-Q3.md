Team member| Task| Priority| Completion| Remarks  
---|---|---|---|---  
Rajesh| Copy synthesis using aperiodicity| 5| 80%| Needs noise level adjustments  
Rajesh| Modelling three-bands using DNN| 5| 20%| Still model training is in progress. Improved copy synthesis  
Pavan| Analyze k-means clustering unseen triphone prediction

  * Look at nearest triphone that is predicted for the unseen triphone.
  * Do analysis, is the nearest triphone makes sense or not
  * How close these nearest triphones with respect to SGMM tree nearest triphones

| 4| 80%| Decided to model at statelevel. Improved accuracy for development set. But not test set.Increased minimum number of clusters per state as 3. Did not give accuracy improvement.  
Pavan| Error analysis for Mandarin output

  * Find differences between i3asr and Kaldi

| 5| 100%| Analyuzed average sysllable duration for training and testing.Found that 200 msec for S-0, 250msec S-1, and 300 msec for digits data.  
Pavan| Build zh-CN DNN model with speed perturbation| 4| 100%| No improvement  
Naresh| Verify speaker adaptation for female data| 4| 100%| Observed similar behaviour as with male data.  
Naresh| Build baseline model with dropout| 4| 100%| Model not improved.  
Naresh| Train filterbank features with CMVN and delta-delta's from Kaldi| 5| 100%| Observed slight improvement over direct features. Still accuracy is lower than standard features.  
Tejas| Work with Veera and train compressed DNN for TTS/ASR| 5| 70%| Model training is in progress.  
Tejas| Read and prepare a summary of techniques on DNN compression published in ICML, ICLR, NIPS, etc.in the recent past.| 2| 50%|    
Veera| Explore articulatory features for TTS DNN modeling| 4| 100%| Observed improvement voiced phones.  
Veera| Train a DNN with WORLD features and synthesize using it.| 3| 100%| Not big improvement  
Veera| Re-build model for Dutch using updated questions| 5| 100%| Did not see any change in the model output.
