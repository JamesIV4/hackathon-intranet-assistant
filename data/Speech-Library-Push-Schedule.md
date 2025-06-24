### The purpose of this page is to maintain a schedule and a checklist for code pushes from //media/main_team_staging.speech ('staging') to //media/main_systest ('systest')

Please note that any submissions made to staging after 'push-create-date' will not be included.

## 

## Schedule

SpeechPushSchedule06/19/2017push-submit-date| 06/28/2017 Wednesday|    
---|---|---  
push-create-date| 06/19/2017 Monday|    
scrs resolved| | IONMEDIA-3185| ISR Confidence Model - Use DNN multiclass modeling - Ph I  
---|---  
IONMEDIA-3217| en-US: Use multi-class confidence model for ISR  
IONMEDIA-3225| ja-JP: Use DNN multi-class confidence model for ISR  
IONMEDIA-3186| fr-CA: Improve confidence model for ISR  
IONMEDIA-3260| fr-CA: fix confidence modeling wrt phone #s  
IONMEDIA-3218| de-DE: Use multi-class confidence model for ISR  
IONMEDIA-3223| en-AU: Use DNN multi-class confidence model for ISR  
IONMEDIA-3227| es-ES: Use DNN multi-class confidence model for ISR  
IONMEDIA-3226| it-IT: Use DNN multi-class confidence model for ISR  
IONMEDIA-3188| nl-NL: Use DNN multi-class confidence model for ISR  
IONMEDIA-3187| pt-BR: Use DNN multi-class confidence model for ISR  
IONMEDIA-3219| es-US: Use multi-class confidence model for ISR  
IONMEDIA-3352| update ja-JP dict & grammars for better performance  
IC-145782| ISR model updates  
 |    
IC-145783| ISR builtin grammar generates incorrect interpretation  
IONMEDIA-3263| ISR de-DE builtin phone grammar generates incorrect interpretation  
IONMEDIA-3258| ISR zh-CN builtin time & currency grammars generates incorrect interpretation  
 |    
IONMEDIA-3088| German TTS Voice Model Retraining based on new alignments & added phone  
 |    
IONMEDIA-2978| en-XX Improve TTS readout of dates vs fractions  
IONMEDIA-3216| i3tts en-US say-as address refinement  
IONMEDIA-3019| en-XX TTS read years as years in certain contexts  
IONMEDIA-3020| en-XX TTS plural years/decades should be read as such  
IONMEDIA-3154| enhance xx-XX say-as alphanumeric   
 |    
IONMEDIA-2447| Make TtsVoice and Acoustic Models backwards/forwards compatible with Lexicon models  
  
 

 

 

 

 

 

 

   
pusher| |    
checklist|  70 incomplete Make sure staging has a successful build 71 incomplete Make sure you have no open changes in staging 72 incomplete Perform `buildupdate` and `p sync` to update your workspace 73 incomplete Do `p push` and resolve any conflicts in systest 74 incomplete Build systest locally 75 incomplete Run unit tests 76 incomplete Run integration tests (MSCA, Analyzer, ISR, ITTS) 77 incomplete Edit the changelist to include SCRs 78 incomplete Start a code-review, potentially multiple reviews if the push is large 79 incomplete Submit - `p submit` 80 incomplete Watch for BUILD_COMPLETE email 81 incomplete Do a `p pull` in staging and if any languages are removed in the model builder rakefiles, check the files out and add the language back in. It's safe to revert the rest of the files and just check in the edited rakefiles. 82 incomplete Create new card (in this page) for next push | During Push Review 512 complete Confirm all relevant SCR's are attached 527 complete Push page complete & linked Post-Push 528 complete Mark OTs as Done & DPs as pushed.  Add push date info. 166 incomplete Email SpeechNews with summary of changes (STG, SEG, EdgeMgmt, PC PM, CIC PM)  
notes| Push Page link: |    
  
 

 

05/15/2017push-submit-date| 05/15/2017 Wednesday|    
---|---|---  
push-create-date| 05/24/2017 Thursday|    
scrs resolved| Interactive Intelligencea6f784b9-ef5d-3d60-bca5-6d0a3771dd27IONMEDIA-2512Interactive Intelligencea6f784b9-ef5d-3d60-bca5-6d0a3771dd27IONMEDIA-2513Interactive Intelligencea6f784b9-ef5d-3d60-bca5-6d0a3771dd27IONMEDIA-2343Interactive Intelligencea6f784b9-ef5d-3d60-bca5-6d0a3771dd27IONMEDIA-3110Interactive Intelligencea6f784b9-ef5d-3d60-bca5-6d0a3771dd27IONMEDIA-2339Interactive Intelligencea6f784b9-ef5d-3d60-bca5-6d0a3771dd27IONMEDIA-3186Interactive Intelligencea6f784b9-ef5d-3d60-bca5-6d0a3771dd27IONMEDIA-3211\--- 5/20:  Please remove this SCR from the push.  We're not ready to release (& code is disabled). Interactive Intelligencea6f784b9-ef5d-3d60-bca5-6d0a3771dd27IONMEDIA-3120|    
pusher| |    
checklist|  142 complete Make sure staging has a successful build 143 complete Make sure you have no open changes in staging 144 complete Perform `buildupdate` and `p sync` to update your workspace 145 complete Do `p push` and resolve any conflicts in systest 146 complete Build systest locally 147 complete Run unit tests 148 complete Run integration tests (MSCA, Analyzer, ISR, ITTS) 149 complete Edit the changelist to include SCRs 150 complete Start a code-review, potentially multiple reviews if the push is large 151 complete Submit - `p submit` 152 complete Watch for BUILD_COMPLETE email 153 complete Do a `p pull` in staging and if any languages are removed in the model builder rakefiles, check the files out and add the language back in. It's safe to revert the rest of the files and just check in the edited rakefiles. 154 complete Create new card (in this page) for next push | During Push Review 155 complete SCR's 156 complete Confirm all relevant SCR's are attached 157 complete Title, Description, Effects, Links, Documentation, Resolved Status 158 complete Install & Licensing  
159 complete Any Install SCR's needed? (CIC)  160 complete Any licenses needed? (CIC)  161 complete Link to PURE epic? (PC) 162 complete Documentation 163 complete CIC: Doc SCR or attach to Install SCR 164 complete PC: Doc Notes & PureCloud Doc label Post-Push 165 complete Email SpeechNews with summary of changes (STG, SEG, EdgeMgmt, PC PM, CIC PM)  
notes|  |    
04/20/2017push-submit-date| 04/26/2017 Wednesday|    
---|---|---  
push-create-date| 04/20/2017 Thursday|    
scrs resolved| | [IONMEDIA-3029](https://devjira.inin.com/browse/IONMEDIA-3029)| [Expand STP training dictionaries for several languages](https://devjira.inin.com/browse/IONMEDIA-3029)  
---|---  
[IONMEDIA-3079](https://devjira.inin.com/browse/IONMEDIA-3079)| [fr-XX number processing error: "X-one thousand" wrong](https://devjira.inin.com/browse/IONMEDIA-3079)  
[IONMEDIA-2045](https://devjira.inin.com/browse/IONMEDIA-2045)| [ISR should support pronunciation lexicon files](https://devjira.inin.com/browse/IONMEDIA-2045)  
[IONMEDIA-1083](https://devjira.inin.com/browse/IONMEDIA-1083)| [i3tts: Add support to accept and use user-defined PLS dictionaries.](https://devjira.inin.com/browse/IONMEDIA-1083)  
[IONMEDIA-3091](https://devjira.inin.com/browse/IONMEDIA-3091)| [Engine optimization using caching and hmm index prefetch](https://devjira.inin.com/browse/IONMEDIA-3091)  
[IONMEDIA-1922](https://devjira.inin.com/browse/IONMEDIA-1922)| [Improve detection of Int'l Phone #s](https://devjira.inin.com/browse/IONMEDIA-1922)  
[IONMEDIA-3016](https://devjira.inin.com/browse/IONMEDIA-3016)| [TTS names with initials have unnaturally long pauses](https://devjira.inin.com/browse/IONMEDIA-3016)  
[IONMEDIA-3083](https://devjira.inin.com/browse/IONMEDIA-3083)| [Fix stress on en-GB numbers](https://devjira.inin.com/browse/IONMEDIA-3083)  
[IONMEDIA-3171](https://devjira.inin.com/browse/IONMEDIA-3171)| [Text Processing Improvements for en-XX](https://devjira.inin.com/browse/IONMEDIA-3171)  
   
pusher| |    
checklist|  94 complete Make sure staging has a successful build 95 complete Make sure you have no open changes in staging 96 complete Perform `buildupdate` and `p sync` to update your workspace 97 complete Do `p push` and resolve any conflicts in systest 98 complete Build systest locally 99 complete Run unit tests 100 complete Run integration tests (MSCA, Analyzer, ISR, ITTS) 101 complete Edit the changelist to include SCRs 102 complete Start a code-review, potentially multiple reviews if the push is large 103 complete Submit - `p submit` 104 complete Watch for BUILD_COMPLETE email 105 complete Do a `p pull` in staging and if any languages are removed in the model builder rakefiles, check the files out and add the language back in. It's safe to revert the rest of the files and just check in the edited rakefiles. 106 complete Create new card (in this page) for next push | During Push Review 107 complete SCR's 108 complete Confirm all relevant SCR's are attached 109 complete Title, Description, Effects, Links, Documentation, Resolved Status 110 complete Install & Licensing  
111 complete Any Install SCR's needed? (CIC)  112 complete Any licenses needed? (CIC)  113 complete Link to PURE epic? (PC) 114 complete Documentation 115 complete CIC: Doc SCR or attach to Install SCR 116 complete PC: Doc Notes & PureCloud Doc label Post-Push 117 complete Email SpeechNews with summary of changes (STG, SEG, EdgeMgmt, PC PM, CIC PM)  
notes|  |    
02/15/2017push-submit-date| 02/17/2017 Friday|    
---|---|---  
push-create-date| 02/15/2017 Wednesday|    
scrs resolved| Interactive Intelligencea6f784b9-ef5d-3d60-bca5-6d0a3771dd27IONMEDIA-3032Interactive Intelligencea6f784b9-ef5d-3d60-bca5-6d0a3771dd27IONMEDIA-2976Interactive Intelligencea6f784b9-ef5d-3d60-bca5-6d0a3771dd27IONMEDIA-3021Interactive Intelligencea6f784b9-ef5d-3d60-bca5-6d0a3771dd27IONMEDIA-3022Interactive Intelligencea6f784b9-ef5d-3d60-bca5-6d0a3771dd27IONMEDIA-2934Interactive Intelligencea6f784b9-ef5d-3d60-bca5-6d0a3771dd27IONMEDIA-3027|    
pusher| |    
checklist|  55 complete Make sure staging has a successful build 56 complete Make sure you have no open changes in staging 57 complete Perform `buildupdate` and `p sync` to update your workspace 58 complete Do `p push` and resolve any conflicts in systest 59 incomplete Build systest locally 60 incomplete Run unit tests 61 incomplete Run integration tests (MSCA, Analyzer, ISR, ITTS) 62 incomplete Edit the changelist to include SCRs 63 incomplete Start a code-review, potentially multiple reviews if the push is large 64 incomplete Submit - `p submit` 65 incomplete Watch for BUILD_COMPLETE email 66 incomplete Do a `p pull` in staging and if any languages are removed in the model builder rakefiles, check the files out and add the language back in. It's safe to revert the rest of the files and just check in the edited rakefiles. 67 incomplete Create new card (in this page) for next push | During Push Review 83 complete SCR's 84 complete Confirm all relevant SCR's are attached 85 complete Title, Description, Effects, Links, Documentation, Resolved Status 86 complete Install & Licensing  
87 complete Any Install SCR's needed? (CIC)  88 complete Any licenses needed? (CIC)  89 complete Link to PURE epic? (PC)  
90 complete Documentation 91 complete CIC: Doc SCR or attach to Install SCR 92 complete PC: Doc Notes & PureCloud Doc label Post-Push 93 complete Email SpeechNews with summary of changes (STG, SEG, EdgeMgmt, PC PM, CIC PM)  
  
  
notes|  |    
1/13/2017push-submit-date| 1/23/2017 Friday  
---|---  
push-create-date| 1/11/2011 Wednesday  
scrs resolved| | [IONMEDIA-2950](https://devjira.inin.com/browse/IONMEDIA-2950)| de-DE TTS "Spielrein"  
---|---  
[IONMEDIA-2939](https://devjira.inin.com/browse/IONMEDIA-2939)| fr-CA update ASR dictionary  
[IONMEDIA-2938](https://devjira.inin.com/browse/IONMEDIA-2938)| fr-FR ASR dictionary updates  
[IONMEDIA-2937](https://devjira.inin.com/browse/IONMEDIA-2937)| fr-FR TTS dictionary fixes  
[IONMEDIA-2936](https://devjira.inin.com/browse/IONMEDIA-2936)| fr-FR dictionary fixes  
[IONMEDIA-2932](https://devjira.inin.com/browse/IONMEDIA-2932)| confirm en-US prons for merger  
[IONMEDIA-2865](https://devjira.inin.com/browse/IONMEDIA-2865)| IONMEDIA-2723 it-IT test: ivr prompts  
[IONMEDIA-2864](https://devjira.inin.com/browse/IONMEDIA-2864)| IONMEDIA-2723 it-IT test: common words  
[IONMEDIA-2853](https://devjira.inin.com/browse/IONMEDIA-2853)| IONMEDIA-2588 es-ES STP & StressPredictor  
[IONMEDIA-2850](https://devjira.inin.com/browse/IONMEDIA-2850)| IONMEDIA-2589 create all training data  
[IONMEDIA-2831](https://devjira.inin.com/browse/IONMEDIA-2831)| Basic Say-As for zh-CN  
[IONMEDIA-2745](https://devjira.inin.com/browse/IONMEDIA-2745)| IONMEDIA-2588 dictionary  
[IONMEDIA-2621](https://devjira.inin.com/browse/IONMEDIA-2621)| es-ES (Euro Spanish) support in i3asr  
[IONMEDIA-2601](https://devjira.inin.com/browse/IONMEDIA-2601)| add full textNormalization and say-as support for zh-CN  
[IONMEDIA-2536](https://devjira.inin.com/browse/IONMEDIA-2536)| es-ES TestVoice  
[IONMEDIA-2126](https://devjira.inin.com/browse/IONMEDIA-2126)| i3tts nlNL CAD: Stress Predictor validation  
[IONMEDIA-1885](https://devjira.inin.com/browse/IONMEDIA-1885)| IONMEDIA-1884 port en-XX CAD changes to es-US  
[IONMEDIA-2806](https://devjira.inin.com/browse/IONMEDIA-2806)| Improve i3speech parsing support for SSML 1.0 and 1.1  
[IONMEDIA-2326](https://devjira.inin.com/browse/IONMEDIA-2326)| Parsing SSML with lang element fails  
[IONMEDIA-1106](https://devjira.inin.com/browse/IONMEDIA-1106)| Percentage not being accepted for prosody pitch  
[IONMEDIA-1097](https://devjira.inin.com/browse/IONMEDIA-1097)| SSML tags with invalid attributes are ignored  
pusher|   
checklist|  5 complete Make sure staging has a successful build 6 complete Make sure you have no open changes in staging 7 complete Perform `buildupdate` and `p sync` to update your workspace 8 complete Do `p push` and resolve any conflicts in systest 9 complete Build systest locally 10 complete Run unit tests 11 complete Run integration tests (MSCA, Analyzer, ISR, ITTS) 12 complete Edit the changelist to include SCRs 13 complete Start a code-review, potentially multiple reviews if the push is large 14 complete Submit - `p submit` 41 complete Watch for BUILD_COMPLETE email 15 incomplete Do a `p pull` in staging and if any languages are removed in the model builder rakefiles, check the files out and add the language back in. It's safe to revert the rest of the files and just check in the edited rakefiles. 16 complete Create new card (in this page) for next push  
notes|    
09/09/2016push-submit-date| 9/09/2016 Friday (originally was targeting 08/05/2016)  
---|---  
push-create-date| 9/07/2016 Wednesday  
scrs resolved|    
pusher|   
checklist|  42 complete Make sure staging has a successful build 43 complete Make sure you have no open changes in staging 44 complete Perform `buildupdate` and `p sync` to update your workspace 45 complete Do `p push` and resolve any conflicts in systest 46 complete Build systest locally 47 complete Run unit tests 48 complete Run integration tests (MSCA, Analyzer, ISR, ITTS) 49 complete Edit the changelist to include SCRs 50 complete Start a code-review, potentially multiple reviews if the push is large 51 complete Submit - `p submit` 52 complete Watch for BUILD_COMPLETE email 53 complete Do a `p pull` in staging and if any languages are removed in the model builder rakefiles, check the files out and add the language back in. It's safe to revert the rest of the files and just check in the edited rakefiles. 54 complete Create new card (in this page) for next push  
notes|    
07/15/2016push-submit-date| 7/15/2016 Friday  
---|---  
push-create-date| 7/13/2016 Wednesday  
scrs resolved| IONMEDIA-1917  
pusher|   
checklist|  29 complete Make sure staging has a successful build 30 complete Make sure you have no open changes in staging 31 complete Perform `buildupdate` and `p sync` to update your workspace 32 complete Do `p push` and resolve any conflicts in systest 33 complete Build systest locally 34 complete Run unit tests 35 complete Run integration tests (MSCA, Analyzer, ISR, ITTS) 36 complete Edit the changelist to include SCRs 37 complete Start a code-review, potentially multiple reviews if the push is large 38 complete Submit - `p submit` 39 incomplete Watch for BUILD_COMPLETE email 40 complete Create new card (in this page) for next push  
notes| 

  * Say-as Address for en-US

  
06/03/2016push-submit-date| 6/3/2016 Friday  
---|---  
push-create-date| 6/1/2016 Wednesday  
scrs resolved| IONMEDIA-1286IONMEDIA-2501IONMEDIA-2502IONMEDIA-2518IONMEDIA-2523  
pusher|   
checklist|  1031 complete Make sure staging has a successful build and tests have passed 1032 complete Make sure you have no open changes in staging 1034 complete Perform `buildupdate` and `p sync` to update your workspace 1035 complete Do `p push` and resolve any conflicts in systest 1036 complete Build systest locally 1037 complete Run unit tests 1038 complete Run integration tests (MSCA, Analyzer, ISR, ITTS) 1039 complete Edit the changelist to include SCRs 1040 complete Start a code-review, potentially multiple reviews if the push is large 1041 complete Submit - `p submit` 1042 complete Watch for BUILD_COMPLETE email 3 complete Create new card (in this page) for next push  
notes|    
05/03/2016push-submit-date| 5/3/2016 Tuesday  
---|---  
push-create-date| 5/3/2016 Tuesday  
scrs resolved| [IONMEDIA-1241](https://devjira.inin.com/browse/IONMEDIA-1241 "Browse to Issue IONMEDIA-1241")[IONMEDIA-2341](https://devjira.inin.com/browse/IONMEDIA-2341 "Browse to Issue IONMEDIA-2341")[ ](https://devjira.inin.com/browse/IONMEDIA-1241 "Browse to Issue IONMEDIA-1241")[IONMEDIA-2342](https://devjira.inin.com/browse/IONMEDIA-2342 "Browse to Issue IONMEDIA-2342") [IONMEDIA-2344](https://devjira.inin.com/browse/IONMEDIA-2344 "Browse to Issue IONMEDIA-2344") [IONMEDIA-2395](https://devjira.inin.com/browse/IONMEDIA-2395 "Browse to Issue IONMEDIA-2395") [IONMEDIA-2511](https://devjira.inin.com/browse/IONMEDIA-2511 "Browse to Issue IONMEDIA-2511") [IONMEDIA-2569](https://devjira.inin.com/browse/IONMEDIA-2569 "Browse to Issue IONMEDIA-2569") [IONMEDIA-2593](https://devjira.inin.com/browse/IONMEDIA-2593 "Browse to Issue IONMEDIA-2593")  
pusher|   
checklist|  1019 complete Make sure staging has a successful build 1020 complete Make sure you have no open changes in staging 1021 complete Perform `buildupdate` and `p sync` to update your workspace 1023 complete Do `p push` and resolve any conflicts in systest 1024 complete Build systest locally 1025 complete Run unit tests 1026 complete Run integration tests (MSCA, Analyzer, ISR, ITTS) 1027 complete Edit the changelist to include SCRs 1028 complete Start a code-review, potentially multiple reviews if the push is large 1029 complete Submit - `p submit` 1030 complete Watch for BUILD_COMPLETE email 4 complete Create new card (in this page) for next push  
notes|   
  
* * *

## Related articles

Related articles appear here based on the labels you select. Click to edit the macro and add or change labels.

false5com.atlassian.confluence.content.render.xhtml.model.resource.identifiers.SpaceResourceIdentifier@e91ec11bmodifiedfalsetruepageANDkb-how-to-articlelabel = "kb-how-to-article" and type = "page" and space = "MediaGroup"
