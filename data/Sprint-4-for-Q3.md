Team member| Task| Priority| Completion| Remarks  
---|---|---|---|---  
Rajesh| Apply smoothing on F0 and MCEPs RNN output

  * Model smoothed f0 using DNN model

| 5| 100%| Need too address smoothing in the model.  
Rajesh| Build duration model| 5| 100%| Currrently, durations are 15-20% shorter compared to GMM prediction  
Rajesh| Sinusoidal modeling based on Rivarol feedback| 4| 0%| Rivarol is pursuing this approach  
Rajesh wi| Re-visiting multiple template based Eigen approach| 4| 50%| Initial copy synthesis is done. Observed windiness in the output.  
Pavan| Address unseen triphones

  * Use nearest phones to replace unseen triphone

| 4| 100%| Tested on WSJ database. Results were below expectations.  
Pavan| Re-visit character based mandarin model

  * Include noise-tag data for model building
  * Perturb audio data

| 5| 80%| Results on Digits and Names showed ~2% improvement in SGMM output.  
Pavan| Test fr-FR test data using fr-CA model| 4| 0%| Ram Sundaram is pursuing  
Pavan| Dump i3asr features and model using PDNN| 3| 0%| Dependency on Ananth  
Naresh| Speaker adaptation

  * Linear input network adaptation
  * Linear output network adaptation

Testing approach

  * Validate with original model
  * Validate with adapted model
  * Validated with fake adapted model

| 5| 50%| Initial results on male speaker adaptation is not encouraging.Tested only with Linear Input Network.  
Naresh| Vitual box setup for Keras| 3| 0%| Not required anymore as we are using WinPython  
Naresh| Train a model with i3asr Filter bank features - work with Ananth| 4| 20%| Discrepency is resolved. Need to generate features and train the model  
Tejas| Retrain large model with fixed transcription

  * WSJ, SWB, i3asrdatacollection, tidigits, aurora, timit

| 5| 100%| Results are not encouraging.  
Tejas| Re-train dnn model with previous model alignments

  * Generate alignments from checked-in model

| 5| 100%| Results are not encouraging.  
Tejas| Continue MediaEval experiments| 4| 80%| Not much improvement from previous sprint  
Tejas| Start preparation for work shop travel arrangements| 4| 100%|    
Veera| Build LVCSR model for voicemail transcription| 5| 70%| Seems there is issue with test data. Need to figure out.  
Veera| Outlier analysis for long vowels in ja-JP| 5| 100%| Found root of the issue. Mixed models and able to fix /owl/ issue.  
Veera| Start DNN modelling for TTS using Keras| 4| 60%| Code preparation is in progress  
Veera| Explore latest language modeling techniques| 4| 0%|    
Veera| Continue objective evaluation for one more language| 3| 0%|  
