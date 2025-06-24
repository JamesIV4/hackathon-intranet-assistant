
    model builder

| 
    
    
    input files(via command line)

| 
    
    
    input files(via config files) This list can change based on language,Paths to these files are relative to command-line arg "--basein"

| 
    
    
    output file  
  
---|---|---|---  
      
    
    int/src/i3kws/model_builder_apps/lexicon_builder/

| 
    
    
    int/resources/i3ca/#{LANG}/lexicon/lexicon_builder.cfg

| 
    
    
    prototype_phoneme_dictionary.txt  
    ../../x-inin-global/lexicon/prototype_phoneme_dictionary_ipa.txt  
    prototype_pronunciation_dictionary_1.txt  
    prototype_phoneme_validator.txt  
    prototype_aligned.xml  
    prototype_text_normalizer.xml  
    fom_model_builder.cfg  
    prototype_pronunciation_transcriber_ipa.xml  
    prototype_phone_stats.csv  
    prototype_en-US_prefix.txt  
    prototype_en-US_suffix.txt  
    prototype_en-US_confusion_pairs.txt  
    prototype_fom_model_expression.txt  
    prototype_fom_error_bar.txt

| 
    
    
    pub/gen/resources/i3ca/#{LANG}/lexicon.i3serialize  
      
    
    int/src/i3ca/model_builder_apps/acoustic_model_builder/

| 

  * int/resources/i3ca/#{LANG}/acoustic_model/acoustic_model_definition.xml

  * pub/gen/resources/i3ca/#{LANG}/lexicon.i3serialize (built with lexicon_builder app)


| 
    
    
    acoustic_model_parameters.xml  
    asr/prototype_decision_tree_leaves.xml  
    asr/prototype_decision_tree_mappings.xml  
    asr/prototype_feature_transform_matrix_lda.xml  
    ../../x-inin-global/acoustic_model/prototype_feature_means.txt  
    ../../x-inin-global/acoustic_model/prototype_feature_variance.txt
    
    
     

| 
    
    
    pub/gen/resources/i3ca/#{LANG}/acoustic_model.i3serialize  
      
    
    int/src/i3ca/model_builder_apps/recording_model_builder/

| 
    
    
    int/resources/i3ca/#{LANG}/recording_model_builder.cfg

| 
    
    
    A large number of ".wav" files as specified in the config-file,   
    which can span multiple regions (e.g., en-US also uses .wav files in en-GB and en-CA),   
    stored in int/resources/i3ca/#{LANG}/recordings/

| 
    
    
    pub/gen/resources/i3ca/#{LANG}/recording_model.ininmodel  
      
    
    int/src/i3ca/model_builder_apps/sign_model/

| 
    
    
    int/resources/i3ca/en-US/sign_model.cfg 

| 
    
    
    int/resources/i3ca/templates/confidence_model.ininmodel  
    int/resources/i3ca/templates/speech_model.ininmodel  
    int/resources/i3ca/templates/tone_model.ininmodel

| 
    
    
    pub/gen/resources/i3ca/#{LANG}/confidence_model.ininmodel  
    pub/gen/resources/i3ca/#{LANG}/speech_model.ininmodel  
    pub/gen/resources/i3ca/#{LANG}/tome_model.ininmodel  
      
    
    int/src/i3tts/model_builder_apps/tts_lexicon_builder/
    
    
     

| 

  * int/resources/i3tts/#{LANG}/tts_lexicon_definition.xml

  * int/resources/i3tts/privateKey


| 
    
    
    tts_lexicon/prototype_phoneme_dictionary.txt  
    ../x-inin-global/prototype_phoneme_dictionary_ipa.txt  
    tts_lexicon/prototype_pos_dictionary.xml  
    tts_lexicon/prototype_pronunciation_transcriber_ipa.xml  
    tts_lexicon/prototype_pronunciation_dictionary.pls  
    tts_lexicon/prototype_phoneme_validator.txt  
    ../../i3ca/en-US/lexicon/prototype_aligned.xml  
    tts_lexicon/prototype_code_as_data_sayas_interpreter.xml  
    tts_lexicon/prototype_code_as_data_phrase_predictor.xml  
    tts_lexicon/prototype_code_as_data_text_normalizer.xml  
    tts_lexicon/prototype_code_as_data_stress_predictor.xml  
    tts_lexicon/tts_lexicon_test.xml

| 
    
    
    pub/gen/resources/i3tts/#{LANG}/tts_lexicon.i3serialize  
      
    
    int/src/i3tts/model_builder_apps/tts_voice_builder/

| 

  * int/resources/i3tts/voices/#{VOICE}/tts_voice_definition.xml

  * int/resources/i3tts/privateKey

  * pub/gen/resources/i3tts/#{LANG}/tts_lexicon.i3serialize (built using tts_lexicon_builder)


| 
    
    
    prototype_hts_logF0_gv.bin  
    prototype_hts_mcep_gv.bin  
    prototype_hts_duration_model.bin  
    prototype_hts_logF0_model.bin  
    prototype_hts_mcep_model.bin  
    prototype_hts_duration.tree  
    prototype_hts_logF0.tree  
    prototype_hts_mcep.tree  
    prototype_excitation_model.xml

| 
    
    
    pub\gen\resources\i3tts\#LANG}\voices\#{VOICE}\tts_voice.i3serialize
