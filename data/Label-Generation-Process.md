 "Label Generation" may refer to:

  * : creating the full-context labels using i3tts and the prompts using the test_label_generator or tts_label_builder app
  * : the entire process of handing over the training materials to the voice-building team.



## _ Label Generator App (the specific process) _

### Generate context labels (simulating run-time)

App is located in int\src\i3tts\test_apps\test_label_generator. (For Training labels, you'll use model_builder_apps\tts_label_builder.  are later on this page.)

Running test_label_generator

  * Scott/Emma probably has a .bat file, or you can just create a folder & supply the app's arguments yourself.  
Check  for details on how to run it.



Language Data File Requirements

  * The language must be able to rake successfully for this app to generate labels.



 

## _ Handing Off Training Data (the generic process of label generation) _

### Starting position

  * PromptsForReading.txt
  * stub E2E Language Model, with
    * prototype_phrase_predictor_training.xml (a stripped down version; included in stubs)
    * prototype_pronunciation_dictionary.csv (must cover all vocabulary in prompts)
    * tts_lexicon_training_definition.xml (included in stubs)
  * audio recordings
  * questions file (.hed)



### Normalize Prompts

Use processRecordings_FlagPromptsForTextNormalization.py (utilities\contextLabelGenerationTools\normalizePrompts) to identify normalization candidates (by punctuation, capitalization, numbers/symbols, etc)

Update the prompts to use expanded written forms, by comparing evaluating the audio

Hint: Sometimes it is possible to leverage an existing language's CAD modules.  If so, you can use that to normalize text, and then will only need to confirm the normalization, rather than manually normalize.

 

The remainder of this page references the tts_label_builder (src/i3tts/model_builder_apps) and the labelGeneration library (utilities/contextLabelGenerationTools). When it refers to the labelGen library, it's usually referring to the mlf_helpers.py file.

### 01) Create full Utterance Data from Prompts

Objective: Generate (a draft version of) full-context labels from the Normalized Prompts.  Generating full-context labels with the tts_label_builder confirms the text is sufficiently normalized, and results in the files needed for alignment generation.

#### utterancedata#Run prompts through the tts_label_builder to get utteranceData.txt

This is similar to , except we use model_builder_apps\tts_label_builder instead. See  for more details about how to run it.  Here, we're specifically leveraging output of the PhonologyModule during label building in order to get word/pos/prompt/intn info.  We don't actually care about the labels, they're just a means to get the output of the phonology module. 

Instructions:

  * If this is a new language, ensure the stub files have been added to langdev/training. You will at least need tts_lexicon_training_definition.xml and prototype_phrase_predictor_training.xml.
  * Edit the files in the training folder as appropriate (cf notes below).
  * Run prompts (a.k.a. TTS promptText) through model_builder_apps\tts_label_builder, use the option: --phonology_out utteranceData.txt
    * e.g.) ..\gen\release\w64\bin\i3tts_label_builder-w64r-%EXE_VERSION%.exe -v --basein B:\builds\media_main_team_ling\int\resources\i3tts\%langcode% --databasename "" \--input %uttfile% --output lab --phonology_out utteranceData.txt
  * When you've built successfully, you should have an utteranceData.txt file!



Notes:

  * langdev/training/tts_lexicon_training_definition.xml
    * Supplements and/or overrides default lexicon_definition. It is _required_ that this file: 1) use a phrase_predictor_training and 2) add graphemeString tag to phonology module.  NB: If your language already uses a phonology module, it needs to support {Tag=N;} data (to allow orthography to pass through).
  * langdev/training/prototype_phrase_predictor_training.xml
    * Stripped down version that does no normalization. It only does direct conversion of canonical punctuation to Intn tags, and lowercases everything.
  * langdev/training/prototype_pronunciation_dictionary.csv

    * Optional dictionary for training, if you need to supplement and/or override what is in the main dictionary




 

How is tts_label_builder different in training vs runtime?

The tts_label_builder differs from generating run-time context labels in several ways:

A) This app constricts the text processing that can be performed on the prompts

  * No change can be made in CN or TN module (lower-casing must happen in stub phrasePred), and no words can go to STP (every word must be in the dictionary).  It throws an error if any of those things happen.
  * Why? The training texts should already be normalized.  We want training labels generated directly from text, not via automatically generated normalization and pronunciations, etc. So if you get errors, add prons to the dict or finish normalizing your text. :)



B) A second additional lexicon_definition file is used (langdev\training\tts_lexicon_training_definition.xml)

  * This file specifies which files should be used _in addition to_ or _in place of_ the default files specified in tts_lexicon_definition.xml
  * To override a file, you must use the same name as the default in order to:
    * e.g. use the training version of the phrase_predictor instead of the default version [required]
    * e.g. use _only_ the training dict and not default dict
    * e.g. force the inclusion of graphemeString tag in the phonology module. [required]
  * To use a file in addition to the default, you must use an incremented name from the default in order to:  

    * e.g. use the default dict, but add the training dict entries to it. (See the stub version of tts_lexicon_training_definition.xml for an example.)



 

#### #Create utt.mlf from utteranceData.txt (@mlf_helpers.py)

We're transforming our utteranceData into an mlf file.

Instructions:

  * Follow code notes for option #1.
  * When you've built successfully, you should have an utt.mlf file!



 

### 2) Generate alignments information

We use our ASR models to provide these directed phone alignments.  This step also detects where pauses are inserted by the speaker.

#### #Create asr-friendly data from utt.mlf (@mlf_helpers.py)

Instructions:

  * Using the current utt.mlf file, create an asr-friendly version of prompts and dictionary. Follow code notes for option #2.
  * When you've built successfully, you should have an asr-prompts.txt file and an asr-dictionary.txt file!



Notes: The current version allows directed asr-alignments only.  To use asr-alignments to select among variant prons, the library will need adapted. 

#### #Get asr-align.mlf

Instructions:

  * Provide asr-prompts.txt & asr-dictionary.txt to the voice-building team (along with audio & the .hed file)
  * They will return an .mlf file with alignments info.
  * Rename to it asr-align.mlf.



 

### 3) Create master.mlf from merging prompts' utterance data (utt.mlf) and from asr alignments (asr-align.mlf)

This merging step also incorporates pause-augmentation.

#### #Merge utt.mlf and asr-align.mlf (@mlf_helpers.py)

Instructions:

  * Follow code notes for Option #3; you must specify langID and phoneMap
  * When you've built successfully, you should have an master.mlf file!
  * Manually resolve any merge conflicts (generally you'll use options 4-5 for this)



Notes:

  * We use a 'safe merge'-style operation.  Where auto-alignments hypothesized a pause but the TTS promptText did not, a non-breaking pause is inserted into the text. Where TTS promptText states a pause but the auto-alignments did not hypothesize one, the alignments are adjusted to 'make room' for this unexpected pause.
  * Key for pauses
    * "pau .", "pau ,", "pau ?": tts-prompt & asr-alignment agree; do nothing.
    * "pau ;": asr-alignment predicts non-prosodic pause; do nothing, unless you want to review that these are non-breaking pauses.
    * "pau ,?", "pau .?": tts-prompt predicts pause, asr-alignment did not.  40ms were forcefully allocated in the alignments; _You need to confirm this._
      * If this causes other phones to become too short, they will be marked with '?' (e.g. [eh?]).  _You will need to adjust alignments here as well._
  * The merging function called in option 3 uses defaults that are appropriate for most projects, but not all.  It contains settable parameters that can be adjusted if warranted by the specific project.



**     NB: You MUST manually resolve the ",?" and [phone?] instances. Do not generate labels (step 6) until this is complete.**

 

What is MASTER.MLF?

  * Master.mlf is the official 'file of record' that contains all necessary information for preparing the training data files.
  * It is created by merging the alignments file with a version of the prompts that contains part-of-speech, pronunciation, and intonation information.  The pauses hypothesized by the ASR alignments are incorporated into these master prompts.
  * The prompts & alignments are re-extracted from the master.mlf file, and the prompts are used to generate the final full-context alignments.



 

### 4-5) Manually Adjust master.mlf

These steps are only needed when making manual adjustments to the data.

#### #Convert master.mlf to textgrids (@mlf_helpers.py)

Instructions:

  * Follow code notes for Option #4.
  * When you've built successfully, you should have an master.textgrids collection file, and a folder with individual textgrids!



#### #Make adjustments

You can open individual audio/grids for specific editing, or use various praat scripts to search and display only audio/grids with specific features.

  * Common tasks:

    * This is the time to review , vs ; vs ,?

    * Manual alignment adjustments (e.g. verify/correct 'pau' instances, fix word boundaries)

    * Review & fix prons (make sure to update dict correspondingly)

  * Some scripts:
    * openWavAndGrid.praat
    * gridSearch.praat
    * validateGrids.praat



Notes:

  * Some praat scripts for handling textgrids derived from the new master.mlf format are not yet available. These should be updated as they are needed.
  * Not all the scripts listed above are checked-in yet. Ask Emma for help until they are. :)



#### #Convert textgrids to master.mlf (@mlf_helpers.py)

Instructions:

  * Follow code notes for Option #5
  * When you've built successfully, you should have an master_edited.mlf!  (master_edited.textgrids will also be created from your textgrid folder)



Note: The default is to read in a textgrid collection file, not individual grids. Uncomment & edit the appropriate section to enable that behavior.

MLF and TextGrids

Just as the master.mlf is information-complete (i.e. has everything we need to be able to generate labels), so are these Praat TextGrids.  Annotations completed in praat can be converted back to a master.mlf and then new alignments/full-context labels can be generated.

Why Praat?

  * An mlf is hard for a human to read. :)
  * Praat allows visual display of the annotation information alongside the audio. Editing can be done directly, or more complex & targeted annotations can be done by leveraging praat scripts.



 

### 6) Re-extract prompts and alignments from masterMLF. Create full-context labels from prompts.

The master.mlf file can easily be transformed to extract a new align.mlf and prompts for generating full-context labels.

#### #Transform master.mlf (@mlf_helpers.py)

Instructions:

  * Follow code notes for option #6, using your new master_edited.mlf
  * When you've built successfully, you should have an align_fromMaster.mlf file and an promptsForLabels_fromMaster.txt file!



Note: If you skipped steps 4-5 because no manual review was necessary, you must rename a copy of master.mlf to master_edited.mlf in order to complete this step.

#### #Generate full-context labels

We're generating full-context labels for real this time.

Instructions:

  * You will follow the same process as from the first time generating labels (cf instructions for running tts_label_builder, under step 01, above). This time, use the flag option "\--phonology_out utteranceData_checking.txt". (different output name)
  * When you've built successfully, you should have a 'lab' folder containing labels, and an utteranceData_checking.txt file!
  * Zip the 'lab' folder into lab.zip



### 7) Check that new prompts/labels sync with master_edited.mlf (@mlf_helpers.py)

This last step validates that the full-context labels match-up with the alignments.

Instructions:

  * Follow code notes for option #7.
  * When you've built successfully, you will get a message that 'files match'!



Notes:

  * If the files don't match, check:
    * file names, sort order
    * did manual annotations change a pronunciation & the dictionary not get updated correspondingly?
    * line-ending characters: does one version use \n and the other \r\n, for example? (This can be an issue if you use Python on Windows vs. Cygwin.)



### 8) Hand-off and Check-in of training data

#### #Handoff to Voice-Building team

  * lab.zip (Rename it to something like "es-ES_full-context-labels.zip")
  * align_fromMaster.mlf (Rename it to something like "es-ES_align.mlf")
  * Make sure they also have access to the questions file (.hed) and the location for audio recordings



#### #Check-in training data materials

  * Rename your latest & greatest to "master.mlf" and check-in to langdev/prompts
  * Also a good idea to check-in the equivalent prompts.txt for your new 'prompts_for_labels.txt' file
  * Ensure all other training data is up to date and checked into p4. (questions file, all the files in langdev/training, etc)



#### #Check-in labelGen library changes

  * Submit code changes if you added support for a new language.
  * If you ran into hassles, consider why. Is documentation misleading or error messages uninformative?  If so, make it better!



 

### ADDITIONAL SCENARIOS:

  * Do you need ASR to predict pronunciation variants?

  * Are there differences between the ASR & TTS phoneset?

  * Do you need to manually improve the alignments?




 
