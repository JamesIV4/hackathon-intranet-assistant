The Echo Canceler test set is a set of 17 recordings checked in here:  
pub\resources\integ_tests\configs\ippspeechcoding\echo_canceller

Each recording to be tested is accompanied by three additional files, so for example, the received-signal agro1 recording we test is named 'agro1-rx.wav', and it comes with these three files:

  * agro1-tx.wav (the transmitted signal)
  * agro1-out.wav (the baseline output from the previous version)
  * agro1LabelTrack.txt (the annotated file that indicates which segments are speech, echo, or silence



The 'agro' set is made up of samples where the Echo Canceler was attenuating legitimate speech during 2017, causing a reduction in recognition performance.

The 'roomEcho' set includes samples where echo was so loud that it was perceived as speech.

The fe_03 set contains audio that is 10-12 minutes long, from recorded phone conversations by volunteers.
