To run any of the following, it is necessary to cb into the appropriate branch.

### Generate Audio - 3 options

  * Web app: <http://adampaughpc.us.int.genesyslab.com:3000/#/texttts>
  * src\i3tts\test_apps\test_tts\gen\release\w32\bin\i3tts_test_tts-w32r-<VERSION>.exe (takes plain text input)
  * src\i3tts\test_apps\i3tts_sim\gen\release\w32\bin\i3tts_sim-w32r-<VERSION>.exe (takes ssml input)



### Generate Context Labels Using the Run-Time System

  * src\i3tts\test_apps\test_label_generator\gen\release\w64\bin\test_label_generator-w64r-<VERSION>.exe  
The command-line arguments we use are: -l <langID> -i <input text> -r <resource_dir>  
Input text is just a file containing lines of text to be spoken.    
resource_dir is the source of the models to use, e.g. '-r I:\builds\media_main_team_staging.speech\pub\gen\resources'.  
If the output dir isn't specified with -o, the labels will appear in a new dir under the working dir, called tts_labels.



### Generate Context Labels For Training

  * src\i3tts\model_builder_apps\tts_label_builder\gen\release\w64\bin\i3tts_label_builder-<VERSION>.exe  
The command-line arguments we use are: -b <_absolute path_ to the langID dir> -i <input text> -d "" -p utteranceData.txt  
Input text is a prepared training corpus with pre-normalized text, and an utterance ID in parens at the end of each line.  
If the output dir isn't specified with -o, the labels will appear in a new dir under the working dir, called tts_labels,  
The -d argument followed by empty double quotes prevents the default "i3tts_" prefix on the filename for each label.



Notes:

If you get an error about an entry point and a dll, try rebuilding the utility by raking in src\i3tts\model_builder_apps\tts_label_builder.

See  for a description of the full process of generating context labels for training.

### Generate STP Prons

  * **i3kws** : src\i3kws\test_apps\test_lexicon\gen\release\w32\bin\test_lexicon-w32r-<VERSION>.exe
  * **i3tts** : src\i3tts\test_apps\test_tts_lexicon\gen\release\w32\bin\test_tts_lexicon-w32r-<VERSION>.exe



(Note that the output will contain underscores.)

(Note also that en-US TTS uses the i3kws STP model and utility.)

Batch files to run both pron generators are checked into the staging.speech branch under resources\utilities\stp:

  * testSTPLexTTS.bat
  * testSTPLexKWS.bat



Both batch files must be run from one level below the int directory, and they both also call checkPronAccuracy.pl, which uses the language's STP reference prons, if it exists, to measure accuracy.

If you want to generate prons from the dictionary and only go to STP for OOV words like the system does at runtime, edit the batch file to temporarily remove the -s argument (for STP-only).

### Run Text Through a Single CAD File

Unlike rake, this generates all the output at once without requiring expected output to compare it against. Note that running each module's output through the next module will not exactly mimic runtime output (e.g. if the phrase predictor splits the utterance, the text normalizer input will be both phrases together).

  * src\i3kws\test_apps\test_text_normalizer\gen\release\w32\bin\test_text_normalizer-w32r-<VERSION>.exe
  * For example, to run from src level:

    * i3kws\test_apps\test_text_normalizer\gen\release\w32\bin\test_text_normalizer-w32r-<VERSION>.exe -t <PATH_TO_CAD_FILE_YOU_WANT_TO_USE>.xml -i <PATH>input.txt -o <PATH>output.txt




### How to rake an individual TTS language model

  * src\i3tts\model_builder_apps\tts_lexicon_builder> rake windows_release['pt-BR --update']



### How to rake an individual ASR language model

  * src\i3kws\model_builder_apps\lexicon_builder> rake windows_release['pt-BR --update']



### How to run language-independent integration tests individually (Echo Canceler)

Echo Canceler: Relatively quick (a few minutes)   


  * set ININBUILD_INTEGTEST=1 && set ININBUILD_NORUN_INTEGTEST= && set DISABLE_LONG_INTEGTEST=1
  * src\ippspeechcoding\test_apps\test_signal_conditioner> rake && rake test



See  for more information.   


### How to run language-related integration tests individually (TTS, ASR and KWS)

TTS: Relatively quick (a few minutes) 

  * set ININBUILD_INTEGTEST=1 && set ININBUILD_NORUN_INTEGTEST= && set DISABLE_LONG_INTEGTEST=1
  * src\i3tts\test_apps\i3tts_sim> rake && rake test



ASR: Takes longer (about 3 hours for rake test alone)   

  * set ININBUILD_INTEGTEST=1 && set ININBUILD_NORUN_INTEGTEST= && set DISABLE_LONG_INTEGTEST=
  * src\i3asr\test_apps\i3asr_sim> rake && rake test



KWS: Takes longest (about 3 hours for rake test)   

  * set ININBUILD_INTEGTEST=1 && set ININBUILD_NORUN_INTEGTEST= && set DISABLE_LONG_INTEGTEST=
  * src\i3ca\test_apps\test_word_spotter> rake && rake test



**To run integration tests for _just one_ language**, pass the language ID as a second argument to test (e.g. > rake test[,es-ES]).****

**Note:** Running tests for one language takes almost as long as running tests for all languages. If you need to run a single-language test more than once, copy the audio files from //i3filesarchive/SpeechAnalyticsData/languagePerformanceEvaluationData and temporarily change the paths in es-ES_ref.mlf and es-ES_wave.txt to run the test locally. Copying will take a couple of hours, but that should reduce the test time from 3 hours to about 30 minutes.  


Note: The initial rake step isn't necessary if the test app has already been built.

If successful, each of these tests will open a browser tab to display the results.

See  if there's an acceptable change.

### How to generate a list of valid sentences from a grammar

  * src\i3asr\test_apps\sentence_generator\gen\release\w64\bin\i3asr_sentence_generator-w64r-<VERSION>.exe --input <grammar> \--method <exhaust|sample> \--maxSentences <num>



* * *

  


## Frequently Asked Questions

### Q: How can I get a list of OOV words from a set of prompts (TTS)?

A: Create a lexicon_test file from the prompts & add it to the tts_lexicon_definition for the language. Rake the language with -d flag. Open trace logs and filter on "resolved using STP". Copy the lines that are related to your lexicon_test file (i.e. not from other active lexicon_tests) to a textfile, and regex/replace to extract the words only.  Sort & deduplicate. 

(Remember to revert the tts_lexicon_definition and the lexicon_test file when you're done.)

Alternately, if your words are already normalized, use the GenerateProns script (allow for dictLookup as well as stp), and the words which went to stp will have underscores.

### Q: How do I build a voice from a code review?

  1. Make sure your build environment is up to date. (buildupdate, p sync, rake)
  2. Download the files from the code review & install them in our local directory.  (Make sure to check out or mark these files for add)
  3. Build the voice model (this is parallel to building a TTS language model).  src\i3tts\model_builder_apps\tts_voice_builder> rake windows_release['Manon --update']
  4. If you want to generate output audio, see the options earlier in the page.



### Q: How do I rake without my machine's resources being maxed out by the rake process?

Use the --jobs 1 argument. E.g.:

  * int\src> rake --jobs 1
  * int\src\i3tts\model_builder_apps\tts_lexicon_builder> rake windows_release['--update --jobs 1']



### Q: How and why do I update model validation files?

Since May 2016, model validation files must be updated whenever a (voice/language/acoustic/etc) model is modified. If the model has changed and you don't use the '--update' argument with rake, the rake will fail. If you do update the model validation files, they will automatically be checked out and added to your default changelist. See  for more info.

Important info from the Speech Model Validation page: To be sure your check-in won't break the build, follow this procedure:

  * int\src> buildupdate --latest && p sync && rake && rake test



That takes longer, because it's a general rake, but it will catch any model validation issues you weren't aware of.

A change to the tts_lexicon requires a new tts_voice_model. You can build both in one command one level above both directories like this:

  * int\src\i3tts\model_builder_apps> rake windows_release['-update it-IT Luisa']



Note: Building the lexicon, then running buildupdate, then building the voice won't work, because buildupdate gets the checked-in compiled lexicon. So the voice will be built using that instead of your newly-built lexicon.

### Q: How do I push changes directly to a specific release as a patch?

First, get approval for the patch. Check this page for detailed instructions:

### Q: How do I change settings for my Windows Command Prompt so that I can make sense of rake messages that include special characters (diacritics, etc.)?

Make sure your font is set to Lucida Console (right-click>Properties>Font), then use the chcp utility to change your code page:

  * > chcp 65001



As far as we know, this only works for Roman-based fonts. We haven't found a code page that works for Japanese in the command console, but Japanese script does appear correctly in the trace files.

### Q: How do I modify the contents of the TTS web app? (3/10/2022: The webapp can no longer be updated)

  * ~~Grab the webapps stream from Perforce:~~  
~~> cb //webapps/tts.latest_systest~~  
~~> buildupdate~~
  * ~~Make your changes, probably to these two files:~~  
~~    \- int\src\tts\apps\tts\templates\textInput.html~~  
~~    \- int\src\tts\apps\tts\controllers\textInputController.js~~
  * ~~Rake in int\src\ with these rake arguments:~~  
~~> rake clean && rake deploy_windows_x86_64_release~~
  * ~~Open a new windows shell**with admin privileges** and CB into webapps again, then rake with these special arguments:~~  
~~> rake teardown && rake setup && rake build~~
  * ~~Using the credentials listed on to access ssdgweb_ii, copy int\pub\gen\distrib\release\tts_web_app.zip from your local drive to a temporary directory on the c drive of ssdgweb_ii.~~
  * ~~Remote-desktop into ssdgweb_ii using the same credentials.~~
  * ~~On ssdgweb_ii, unzip tts_web_app.zip to d:\i3tts_webapp\build\web\, replacing everything except the 'audio' directory.~~
  * ~~If you have made changes that affect files in pub\gen\bin\ or resources, use the same procedure to update them in their locations under d:\i3tts_webapp\build\ on ssdgweb_ii.~~
  * ~~To restart the modified TTS Demo, either find 'Launch TTS Web App' in Task Scheduler and run it (double-click on it under 'Active Tasks', then right-click and 'Run') or reboot ssdgweb_ii.~~  
~~**Note** : ssdgweb_ii is auto-updated every night, so any changes you make to it directly may disappear until they're also checked into the webapps stream.~~


