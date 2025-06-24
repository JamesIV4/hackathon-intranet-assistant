 

 

Status| GreySTOPPED  
---|---  
Stakeholders| , ,   
Outcome| use of Kaldi not feasible at the moment  
Due date| June 30, 2014  
Owner|    
  
* * *

## Contents

3

* * *

## Background

This page will be used to document results generated from various acoustic models, and help us pick the best.

* * *

## Experimental Data

Two sets of data will be used for experiments

  * Diagnostics from indyreco. - \\\i3filesarchive\SpeechAnalyticsData\asr\indyreco\2014\05May\w5 & 06June\w1
  * Benchmark tests (company directory, phone, mobile-office, yesno) - \\\speechanalytics\benchmark\asr



* * *

## Experiments

All models are stored here: \\\devspeech2\D_devspeech2\Public\i3asr-model

 

* * *

### kaldi_1_sil3_nosp

System : Kaldi  
Data : WSJ, Fishers  
Frontend : continuous CMVN  
Tag : kaldi_1_sil3_nosp

#### Indyreco tests

#recordings| 1288|  |  |  |  |  |  |  |  |  |  |    
---|---|---|---|---|---|---|---|---|---|---|---|---  
 | nuance|  |  |  | i3asr|  |  |  | i3asr-kaldi_1_sil3_nosp|    
 | #| %| #C| %C| #| %| #C| %C| #| %| #C| %C  
accept| 581| 45.1%| 576| 99.1%| 566| 43.9%| 508| 89.8%| 760| 59.0%| 582| 76.6%  
confirm| 95| 7.4%| 82| 86.3%| 247| 19.2%| 100| 40.5%| 218| 16.9%| 48| 22.0%  
reject| 612| 47.5%| 487| 79.6%| 475| 36.9%| 432| 90.9%| 310| 24.1%| 297| 95.8%  
> 0.5| 676| 52.5%| 658| 97.3%| 813| 63.1%| 608| 74.8%| 978| 75.9%| 630| 64.4%  
  
* * *

### kaldi_2_datacoll

System : Kaldi  
Data : WSJ, Fishers, i3datacollection  
Frontend : continuous CMVN  
Tag : kaldi_2_datacoll

#### Indyreco tests

#recordings| 1288|  |  |  |  |  |  |  |  |  |  |    
---|---|---|---|---|---|---|---|---|---|---|---|---  
 | nuance|  |  |  | i3asr|  |  |  | i3asr-kaldi|  |    
 | #| %| #C| %C| #| %| #C| %C| #| %| #C| %C  
accept| 581| 45.1%| 576| 99.1%| 566| 43.9%| 508| 89.8%| 661| 51.3%| 496| 75.0%  
confirm| 95| 7.4%| 82| 86.3%| 247| 19.2%| 100| 40.5%| 254| 19.7%| 89| 35.0%  
reject| 612| 47.5%| 487| 79.6%| 475| 36.9%| 432| 90.9%| 373| 29.0%| 343| 92.0%  
> 0.5| 676| 52.5%| 658| 97.3%| 813| 63.1%| 608| 74.8%| 915| 71.0%| 585| 63.9%  
  
* * *

### lvtk_1_resetcmvn

System : LVTK  
Data : WSJ, Fishers, i3datacollection  
Frontend : reset CMVN  
Tag : lvtk_1_resetcmvn

#### Indyreco tests

#recordings| 1305|  |  |  |  |  |  |  |  |  |  |    
---|---|---|---|---|---|---|---|---|---|---|---|---  
 | nuance|  |  |  | i3asr|  |  |  | i3asr-lvtk_resetcmvn|    
 | #| %| #C| %C| #| %| #C| %C| #| %| #C| %C  
accept| 582| 44.6%| 577| 99.1%| 566| 43.4%| 508| 89.8%| 202| 15.5%| 177| 87.6%  
confirm| 95| 7.3%| 82| 86.3%| 248| 19.0%| 100| 40.3%| 308| 23.6%| 189| 61.4%  
reject| 628| 48.1%| 503| 80.1%| 491| 37.6%| 447| 91.0%| 795| 60.9%| 652| 82.0%  
> 0.5| 677| 51.9%| 659| 97.3%| 814| 62.4%| 608| 74.7%| 510| 39.1%| 366| 71.8%  
  
* * *

### kaldi_sil_3_nosp_i3data_nisil_in_transcript

System : Kaldi  
Data : WSJ, Fishers, i3datacollection  
Frontend : continuous CMVN  
Tag : kaldi_2_datacoll  
extra : sil removed in training transcript but exist in dictionary

#### Indyreco tests

#recordings| 1287|  |  |  |  |  |  |  |  |  |  |    
---|---|---|---|---|---|---|---|---|---|---|---|---  
 | nuance|  |  |  | i3asr|  |  |  | i3asr-new|  |    
 | #| %| #C| %C| #| %| #C| %C| #| %| #C| %C  
accept| 581| 0.451437| 576| 0.991394| 566| 0.439782| 508| 0.897527| 824| 0.640249| 597| 0.724515  
confirm| 95| 0.073815| 82| 0.863158| 247| 0.191919| 100| 0.404858| 200| 0.1554| 37| 0.185  
reject| 611| 0.474747| 486| 0.795417| 474| 0.368298| 431| 0.909283| 263| 0.204351| 259| 0.984791  
> 0.5| 676| 0.525253| 658| 0.973373| 813| 0.631702| 608| 0.747847| 1024| 0.795649| 634| 0.619141  
  
* * *

### kaldi_lda5context

System : Kaldi  
Data : WSJ, Fishers, i3datacollection  
Frontend : continuous CMVN  
Tag : kaldi_lda_5context  
Notes : kaldi LDA model with 5 context frames

#### Indyreco tests

#recordings| 1305|  |  |  |  |  |  |  |  |  |  |    
---|---|---|---|---|---|---|---|---|---|---|---|---  
 | nuance|  |  |  | i3asr|  |  |  | i3asr-new|  |    
 | #| %| #C| %C| #| %| #C| %C| #| %| #C| %C  
accept| 582| 0.445977| 577| 0.991409| 566| 0.433716| 508| 0.897527| 867| 0.664368| 603| 0.695502  
confirm| 95| 0.072797| 82| 0.863158| 248| 0.190038| 100| 0.403226| 182| 0.139464| 32| 0.175824  
reject| 628| 0.481226| 503| 0.800955| 491| 0.376245| 447| 0.910387| 256| 0.196169| 251| 0.980469  
> 0.5| 677| 0.518774| 659| 0.973412| 814| 0.623755| 608| 0.746929| 1049| 0.803831| 635| 0.605338  
  
* * *

## Benchmark tests

confidence threshold: 0.0

All chars, lower the better.

% ErrorWord Error Ratevertical300700barbefore Word Error Rates| lvtk_1_reset| main_systest| kaldi_1_sil3_nosp| kaldi-lda5context| kaldi_sil_3_nosp_i3data_nisil_in_transcript  
---|---|---|---|---|---  
mobileoffice| 33.9| 23.3| 22.6| 21.8| 21.8  
phase1-1| 29.2| 14.7| 17.9| 18| 18  
phase1-2| 27.8| 13.5| 16.6| 17.4| 17.4  
phase1-3| 28.9| 15.4| 17.3| 17.7| 17.7  
phase1-4| 28.9| 14.1| 17.7| 17.3| 17.3  
phase1-5| 28.7| 14.4| 17.7| 18.2| 18.2  
phase1-6| 27.7| 14.1| 16.8| 17.1| 17.1  
phase1-7| 28.3| 14.3| 17.4| 17.7| 17.7  
phone| 40.7| 29| 30.1| 29.1| 29.1  
yesno| 12.9| 4.1| 5.2| 5.5| 5.5  
  
 

* * *

 

% ErrorSentence Error Ratevertical300700barbefore Sentence Error Rates | lvtk_1_reset| main_systest| kaldi_1_sil3_nosp| kaldi-lda5context| kaldi_sil_3_nosp_i3data_nisil_in_transcript  
---|---|---|---|---|---  
mobileoffice| 70.4| 57.6| 60.2| 58.2| 58.2  
phase1-1| 30.6| 16| 19.3| 19.4| 19.4  
phase1-2| 29.3| 14.4| 17.6| 18.3| 18.3  
phase1-3| 30.3| 16.6| 18.2| 18.7| 18.7  
phase1-4| 30.4| 15.3| 18.7| 18.5| 18.5  
phase1-5| 30.4| 15.6| 19.3| 19.6| 19.6  
phase1-6| 29.2| 15.5| 18| 18.3| 18.3  
phase1-7| 29.7| 15.4| 18.6| 19.1| 19.1  
phone| 85.4| 63.5| 68.4| 67.9| 67.9  
yesno| 19.4| 6.2| 8.5| 8.9| 8.9  
  
 

* * *

 

Avg MHzAverage MHzvertical300700barbefore Average Search Mhz| lvtk_1_reset| main_systest| kaldi_1_sil3_nosp| kaldi-lda5context| kaldi_sil_3_nosp_i3data_nisil_in_transcript  
---|---|---|---|---|---  
mobileoffice| 371.239| 115.965| 168.958| 178.681| 176.156  
phase1-1| 318.851| 123.986| 139.419| 150.099| 136.766  
phase1-2| 342.181| 119.217| 139.655| 149.487| 141.601  
phase1-3| 348.293| 109.439| 139.275| 153.18| 145.679  
phase1-4| 343.631| 108.897| 139.333| 151.342| 145.051  
phase1-5| 339.947| 123.703| 140.589| 153.965| 146.116  
phase1-6| 305.116| 114.117| 140.64| 154.284| 145.817  
phase1-7| 349.996| 120.476| 142.638| 151.337| 157.661  
phone| 82.6414| 36.1452| 47.0901| 50.2387| 50.1616  
yesno| 24.154| 14.4898| 12.2864| 15.3348| 17.0032
