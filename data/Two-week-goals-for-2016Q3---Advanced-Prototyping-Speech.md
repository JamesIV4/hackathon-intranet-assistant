**Priority** : Range 1 to 5. 5 is high priority and 1 is low priority  
  
Team Member| 22-July| SCR| Priority| Completeness| 5-Aug| Priority| Completeness| Remarks| 28-Aug| Priority| Completeness| Remarks  
---|---|---|---|---|---|---|---|---|---|---|---|---  
Rajesh| Address r-flap issue for ja-JP in Matlab|  | 3| 80%| Implementation of r-flap in i3tts| 4| 0%| Dependency on error analysis| Work with Linda and get the r-flap issues and fix them in Matlab if possible| 4| 0%| Decided to go with current approach.  
Rajesh| Tune en-GB and nl-NL based on Tan's observation|  | 3| 0%| Generate Eigen and two-band templates for es-ES| 5| 100%|  | Analyze two-band output for nl-NL and ja-JP with new models and address the issues.| 5| 100%|    
Rajesh| Italian test voices|  | 4| 100%| Analyze two-band templates output for nl-NL and ja-JP with new models| 5| 50%|  | Understand Sinusoidal modeling| 4| 20%| Rivarol is looking into initial approach.  
Rajesh| Identify issue between i3tts and matlab frequency domain|  | 5| 100%| Understand Vocain vocoder approach.| 5| 100%|  | Continue training Duration, F0 and MCEP using DNN's| 4| 50%| Current model gave slight improvement. Need to address F0 issue.  
Rajesh| Improve two-band and spectral quality for en-US using DNN model|  | 4| 60%| Address F0 and MCEP issues in RNN modeling with different network representations| 4| 30%| Not converging well|  |  |  |    
Pavan| Explore tree building from DNN final layer output features

  * Build a tree using SGMM model
  * Train a context-dependent DNN using senons
  * Take output from Final layer
  * Re-train the tree using DNN final layer features

|  | 4| 100%| Replacing SGMM trees with K-Means approach and self-organizing maps| 4| 40%| Kaldi doesn't support shared tree| Replacing SGMM trees with clustering

  * Build center phone based clusters
  * Get the cluster count from SGMM tree if required.

| 4| 100%| Results are similar to standard approach. But, saw good improvement with digits.Assuming that unseen triphones are the issue.  
Pavan|  Re-train Mandarin model

  *     * Use character to inin phone dictionary
    * Generate HTK alignments
    * Map inin phone dictionary to pinyin
    * Compare new pinyin transcription with existing transcription and pass it to Rich for analysis

Re-train the model with new transcription|  | 5| 100%| 

  * Test character based models in Kaldi and i3asr
  * Analyze errors between character and pinyin

| 5 | 40%| Facing issue in porting model in i3asrDependency for grammars| 

  * Port Mandarin model in i3asr
  * Verify benchmark results in i3asr using character based grammars

| 5| 80%| Dependency on grammars for boolean, phone, etc..  
Pavan| Complete model building with Deltal dental and existing database from scratch|  | 3| 100%| Explore dumping senones from i3asr and re-build DNN model - work with Ram and Ananth| 4| 0%| Need to start| Explore dumping senones from i3asr and re-build DNN model - work with Ram and Ananth| 5| 10%| Dependency on testapp for dumping senone.  
Pavan| Train a model with senons from original transcription

  *     * Extract acoustic features and senones from delta dental original transcription
    * Add this data along with existing database features and senones
    * Train a PDNN model

|  | 3| 100%| Train en-US model for TTS objective evaluation| 4| 100%|  |  |  |  |    
Naresh| Explore Rivarol's features and come up with normalization approach for DNN's|  | 4| 100%| Continue exploring Rivarol's features with Global mean and variance for normalization| 4| 100%| Did not see improvement over original features| Speaker adaptation

  * Linear input network adaptation
  * Linear output network adaptation

Testing approach

  * Validate with original model
  * Validate with adapted model
  * Validated with fake adapted model

 | 5| 40%| Issue in adaptation  
Naresh| Identify DNN adaptation techniques |  | 3| 25%| Train a model with i3asr Filter bank features - work with Ananth| 4| 0%| Dependency on test app| Vitual box setup for Keras| 3| 20%| Completed only virual box installation  
Naresh| Error analysis for es-ES and en-GB using path analysis|  | 5| 50%| Error analysis for en-GB| 5| 100%| Path analysis show that and/the are not present acoustically| Train a model with i3asr Filter bank features - work with Ananth| 4| 40%| There is discrepency in the code between Ananth's output and Naresh's output.  
Naresh|  |  |  |  | Present possible approaches for adaptation| 5| 100%|  | Start review for es-ES grammar files.| 5| 90%| Waiting for approval from authors  
Tejas| Create a gold standard network with different network structures

  *     * Explore different neural network structure like 1024-512-1024, 2048-1024-2048, etc..
    * Come up with best accuracy network.
    * Create a gold standard for model compression

|  | 4| 10%| Continue building model with large data set for en-US

  *     * Explore different neural network structure like 1024-512-1024, 2048-1024-2048, etc..
    * Come up with best accuracy network.
    * Create a gold standard for model compression

| 5| 50%| Training completed until tri2a. Currently running with Keras using tri2a alignments.| Continue large model training| 5| 100%|    
Tejas| Error analysis for it-IT on insertion/deletion of "E"|  | 5| 100%| Generating PDNN alignments for Dutch TTS voice| 5| 100% |  | Model training for MediaEval| 4| 70%|    
Tejas| Plan of action for MediaEval|  | 3| 50%|  |  |  |  |  |  |  |    
Veera| Model building for two test-voices of it-IT|  | 4| 100%| Generate models for es-ES 1000 sentence voice| 5| 100%|   | Objective evaluation

  * Analyse results for speaker dependent model
  * Try with actual ASR model

| 4| 100%|    
Veera| Explore methods for objective evaluations on synthesis quality|  | 4| 100%| re-generate Japanese model using PDNN and HTK labels| 5| 100%|  | Error analysis for nl-NL and ja-JP| 5| 100%|    
Veera| Re-train ja-JP model using updated transcriptions|  | 5| 50%| re-generate Dutch model using PDNN and apply outlier approach| 5| 100%|  | Building es-ES model for full data| 4| 50%| Dependency on full context labels  
Veera| Explore delta dental data for use|  | 3| 100%| Explore KL divergence approach for TTS objective evaluation| 4| 100%|  | Explore fixing discontinues for DNN f0 output| 4| 20%| Dependency on latest F0 model  
 |  |  |  |  | Prepare usable script for PDNN and HTK alignment generation - work with Naresh| 4| 50%| Completed for HTK alignments.|  |  |  |  
