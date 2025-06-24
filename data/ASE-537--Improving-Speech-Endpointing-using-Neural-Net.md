## NN Testing Results Page: 

## Early Experiments:

  * Srinath tried training a CNN
    * Feature input is the spectrogram and level of the signal
    * Softmax.  Speech . vs Nonspeech
    * Dataset is small subset of VAD integration test
    * Accuracy was about 78%



## Requirements/Constraints:

  * Must detect the beginning of speech within 150-200 ms
    * This can be a less accurate low confidence detection which would be used to lower the volume of a prompt being played.  If it was not a true barge-in (due to noise or background speech), the user can still hear the prompt
    * Accurate VAD hypothesis must signal it wasn't speech so the volume can return to normal in the case of a false barge-in
  * For CA, the accurate beginning of speech should be signaled within 500? ms
    * Can retroactively mark frames as speech once we are confident of where it began.
  * Must signal the accurate begin and end of speech within 150-200 ms of end of speech
    * A low latency response of speech end is critical for a good voicebot or IVR experience (no noticeable delay in prompt response)
    * Save $ using transcription engines so we aren't paying for streaming silence (google charges per audio seconds, not speech seconds or words transcribed)
    * Lex doesn't return a transcription until you stop sending audio (not a streaming service)
  * Resilient to noise or background speech
  * Accurate with short words (Si or short tones in Chinese).  These can be troublesome for a VAD
  * Prefer a global language-agnostic model
  * Classes: Speech, Silence, Noise (possibly more classes for specific types of noise)
  * Loquentia Lex Integration Constraints?



### Comments/Suggestions:

  * Use MFCCs for VAD, not spectrogram.  MFCCs are good with normalizing all speakers for training
  * Developer of OPUS codec, designed a speech-based DNN (speech coding entropy) open source library
    * Look at the architecture to see if we can use a subset of it to detect speech vs non-speech: <https://people.xiph.org/~jm/opus/opus-1.3/>
  * Use Kaggle 
    * Mix short words with noise for training
    * Clean audio
  * Test with other languages
  * Confidence is difficult to set as a threshold.  Who sets this threshold?
  * Rather have classes: Babble Noise, Typing, Speech
    * Is it better to have many noise classes or cluster/generalize them?  
  * Sequence to sequence (whole audio sequence) modeling encoding might have too high latency
  * Use a latent space to hypothesize, sliding window
  * Felix hunch would be to use:  HCN Hierarchical Convolutional Neural Network, cheaper and faster than LSTM
  * Research at what's out there first.  It's been a while since we've looked at VADs research.
  * Use energy in clean recordings to endpoint audio and add noise to clean recordings for noisy examples
  * Use features that aren't language dependent
  * Like ISR, 1st stage, to hypothesize classes, 2nd stage to generate confidence (softmax)
  * Do we need 2 VADs: fast vs accurate?



  


## Meeting Notes/Action Items:

  * 1/22/2020
    * Srinath: See performance of current VAD vs
      * SILK, CELT(NN), and All Opus Layers
      * Up-sample 8k to test if needed
    * Tan: Research new VAD technologies
    * Adam: Set up meeting with Loquentia team to discuss their requirements.
    * Attaching opus related papers250250
  * 2/5/2020
    * Srinath shared Opus test results.  Best results came from AND-ing the 2 VADs (SILK and CELT). Opus is more sensitive.  Should we plot ROC curves for sensitivity on dsd vad?
    * Opus features, rate of change of tone, BARK filter banks features, noisiness
    * Should we do tonality analysis in the DSD vad?
    * Train with different set of features to see which features have high correlation.   Test with integration test data. 
    * What training data are we going to use?  Need a large annotated data set that has noisy examples or large clean set that we can add noises to.  Training data needs to be well defined so each training experiment can be compared easily.
    * Srinath: Plot curve for different sensitivities [0-1] .1 increments
    * Rivarol: Look at tonality code next week to see if there's obvious features that can be added to dsd vad easily.
    * Tan: Look at what data we have to see what we can do about creating a training data set.
      * Do we have a clean data set folder?
      * Listen quickly to each example to know if it has noise or not (divvy up to the team)



2/10/2020

  * Initially integrate current speech team vad for Lex
  * Need to rewrite code to integrate with Loquentia
    * Loquentia is in java
    * Implement in javascript
  * VAD shouldn't be in it's own microservice
    * crossing VPCs, is it worth it
    * for streaming, you have to chunk it
    * could increase latency
    * Run requirements by Glen
  * Interface from JVM to C++ might be slow, do a prototype to test/benchmark first.
  * Are there math libraries to do matrix operation in javascript?
  * Initial api include early speech indication to lower the volume of the prompt
  * Early hypothesis, noise events.  Buffer of audio before speech.  .5 sec
  * 150 ms barge in.  Configurable end of speech timeout.  .8-1 sec.  
    * Confirmations should have short timeouts, credit card timeout should be longer
  * computationally efficient
  * Matt Jahns has speech transcription engine framework to test the vads
  * Implement it in C++/python to run, and also in javascript to compare
    * efficient matrix library in java
    * purecloud java chatroom to ask about efficient math libraries
  * charter talk about the different user stories



2/12/2020

  * Srinath: run all categories for plots (1 day)
  * Tan: look at plotting in integ test
  * Srinath: take a look at benchmarking java to c++ interop with dsd vad.  Need to measure latency.
  * Adam: Get ASE set up for project.



2/19/2020

  * Srinath & Tan: Install Java and test Java native Interface (JNI). Run JNI with dsd VAD.
  * Srinath: wrap up the performance of OPUS
  * Relative performance of opus vad vs dsd vad is summarized here:
  * : comparison file with dsd vad
  * : Accuracy  vs False Alarm for opus 
  * : Accuracy  vs False Alarm for dsd vad
  * Further details found in \\\i3filesarchive\SpeechAnalyticsData\opus_vs_dsd_vads



5/19/2020

  * Types of Noise:
    * Must: Babble, Throat Clearing, Driving(car)
    * Should: Transient(keyboard, coughing)
    * Could: Airport, Background Noise(Whitenoise)
  * Unvoiced sounds: dsd vad uses energy in high frequency, periodic signals.  Should these be features?
  * Action Items:
    * Take a look at high performers in Kaggle competition. Architecture, layers, features, etc.   (Srinath)
      * Comments: Structure may be too complicated or too focused on one dataset to use as is.
    * Take a quick look to see if there's good existing open source speech endpointer networks (Srinath)
      * Comment: Most are old, not that many available
    * Finish cleaning up the integration test set data (Tan)
      * Should integration set results have the Must/Should categories: Babble, Driving, Throat Clearing, Transient


  * Next Time: How to add noise to training set data.



## Testing speech detector inside opus

  * opus speech detector flag triggers even during periods of very quite audio and false alarm rates are higher in these regions. Accuracy results were mixed with some categories showing huge improvement. Performance with noisy audio caused high false alarm rates. Some sample integration test results can be found here. 1. default setting (16khz audio) 2\. setting using only silk vad and a threshold of 100  (16khz audio)    3\. default silk setting (8khz audio)  4\. silk threshold of 100 (8khz audio). Best behavior is for short speech.  VAD in opus is not publicly exposed so internal behavior was inferred.
  * Wideband and higher band audio ( 16khz  or higher resampled to 16khz)   first goes through a pretrained RNN speech/music detector. The activity of this network is then passed on to a SNR based VAD. RNN used BARK features and some novel features like tonality, tonality slope, frame noisiness. 
  * Narrowband audio (8khz) is not processed by the RNN but by SILK VAD for further decisions concerning encoding etc.



  

