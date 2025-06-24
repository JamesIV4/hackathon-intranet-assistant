# Analyzer JSON Schemas

## Keyword

KeywordjsProperty Name| Description  
---|---  
`name`| Name assigned to this keyword. This is the primary identifier for this object, and not necessarily the same as the underlying words to be detected by the Keyword Spotter.There are no restrictions to this string-it is used only to identify keywords and events reported by the Keyword Spotter, and is never used for lexical lookup  
`tag`| Semantic tag associated with the keyword.This arbitrary string contains user-specified application data that gets included inline with classification events when this keyword is detected. The data is typically used for semantic interpretation of the keyword, which may affect the detection result.This value is optional and may be empty. The content and format of this tag is entirely application dependent. However, ININ speech-related applications will typically use text expressions using Semantic Interpretation for Speech Recognition (SISR) format.Example:  
`confidenceThreshold`| Confidence threshold (a.k.a. "sensitivity") for this keyword.The "confidence threshold" ranges from 0 (low threshold, high sensitivity) to 1 (high threshold, low sensitivity), and 0.5 is the value that is recommended for most cases.  A value of -1 indicates to use the system default value.Notes:

  * Increase this threshold to reduce sensitivity for this keyword and reduce false positives.
  * Reduce this threshold to increase sensitivity for this keyword and reduce false negatives.
  * This value is used for fine tuning, and scaled internally to match the dynamic range of the system. It is recommended to initially use the system default of -1, and if performance is insufficient, choose a precise value and adjust until a proper balance is achieved between false positives and false negatives.

  
`words`| Array of orthographic spelling of the word to be recognized.A "word" is an orthographic spelling of a word or phrase for the system to detect, in order to indicate that a keyword event occurred. Each word is converted at runtime into a phonetic "pronunciation" through lexical lookup.  The keyword "name" property value may be a member of this word Array but does not have to be.Each entry may mix upper and lower case, and may contain one or more natural language words separated by whitespace. Leading and trailing whitespace, and any redundant whitespace between words are deleted. Each word may contain numbers or punctuation. When performing lexical lookup, certain word strings may be replaced with alterate orthographic spellings. For example, the string "123" may be converted internally by a U.S. English lexicon into the phrase "one hundred twenty three" before obtaining the appropriate pronunciations to detect. Likewise, punctuation such as "," may be converted into the orthographic spelling "comma".Example:  
`antiwords`| Array of user-specified "antiwords", or alternate orthographic spellings for anti-pronunciations for a keyword.An "antiword" is an orthographic spelling of a word or phrase for the system to detect, in order to indicate that the keyword event _did not_ occur to suppress mispronunciations and misrecognitions. Each antiword is converted at runtime into a phonetic "antipronunciation" through lexical lookup and a spelling-to-pronunciation model.Example:  
`pronunciations`| Array of user-specified "pronunciations", represented as sequences of phoneme names separated by whitespaceA "pronunciation" is an exact phonetic spelling for the system to detect, in order to indicate that the keyword event occurred.Notes:

  * This property is generally only used for special cases and tuning to add keywords where the spelling-to-pronunciation lookup of the orthographic spelling specified in the "words" property fails. 
  * The phoneme names in each string must belong to a specific set of case-sensitive names, which is dependent on lexicon of the language of the KeywordSet.  By default, this set is the lower case version of "Arpabet" (see <http://en.wikipedia.org/wiki/Arpabet>)

Example:  
`antipronunciations`| Array of user-specified "anti-pronunciations", represented as sequences of phoneme names separated by whitespace.An "anti-pronunciation" is an exact phonetic spelling for the system to detect, in order to indicate that the keyword event _did not_ occur. This is useful for suppressing false positives where an exact mispronunciation is known.The phoneme names in each string must belong to a specific set of case-sensitive names, which is dependent on the lexicon used by the KeywordComposer. By default, this set is the lower case version of "Arpabet" (see <http://en.wikipedia.org/wiki/Arpabet>).Example:  
  
## KeywordSet

KeywordSetjsProperty Name| Description  
---|---  
`id`| Unique identifier associated with this KeywordSet  
`name`| Name of this keyword set  
`language`| Language code for all keywords in the setThe language identifier is in the standard IETF format with ISO 639language subtag in lowercase, and optional ISO 3166 region subtag in uppercase.Examples: "en-US", "es-US", "fr-CA".  
`tag`| Semantic tag assigned to this keyword set.This arbitrary string contains user-specified application data that gets included inline with classification events when a keyword within this set is detected. This data is typically used for semantic interpretation of the keyword, which may affect the detection result.This value is optional and may be empty. The content and format of this tag is entirely application dependent. However, ININ speech-related applications will typically use text expressions using Semantic Interpretation for Speech Recognition (SISR) format.Example:  
`category`| Category of the keyword.  This is an arbitrary (and optional) value that can be used by the application for grouping of keywords sets.  
`version`| Access model version for all keywords in keyword set, as a numerical string in the form "major.minor.revision.build"  
`keywords`| Array of `Keyword` objects comprising this `KeywordSet`  
  
Example:

KeywordSet examplejstrue

## KeywordClassification

KeywordClassificationjsProperty Name| Description  
---|---  
`utterance`| Utterance recognized by the keyword spotting engine as sequence of phoneme names separate by spacesExample:  
`keywordName`| Name of the keyword (copy of `Keyword.name`)  
`confidence`| Confidence score of the keyword 0...1  
`timeBegin`| Precise sample position where the recognized keyword started. This time is relative to the beginning of the audio stream fed into the keyword spotting engine.   
`timeEnd`| Precise sample position where the recognized keyword ended. This time is relative to the beginning of the audio stream fed into the keyword spotting engine.   
`keywordConfidenceThreshold`| Confidence threshold of the keyword (copy of `Keyword.confidenceThreshold`)  
`keywordSetId`| Unique identifier of the `KeywordSet` instance of which this keyword is a member of (copy of `KeywordSet.id`)  
`KeywordSetCategory`| Category of the `KeywordSet` instance of which this keyword is a member of (copy of `KeywordSet.category`)  
`keywordSetName`| Name of the `KeywordSet` instance of which this keyword is a member of (copy of `KeywordSet.category`)  
`keywordTag`| Semantic tag of the `Keyword` (copy of `Keyword.tag`)  
`keywordSetTag`| Semantic tag of the `KeywordSet` (copy of `KeywordSet.tag`)  
  
 

## KeywordClassificationSet

KeywordClassificationSetjsProperty Name| Description  
---|---  
`timeReported`| Precise sample position where the keyword classifications in this set were reported.The keyword spotting engine will batch keyword spots that occur very close together.  That means the report of the keyword will be slightly delayed.  This property thus contains the exact location where the engine reported the keywords and in conjunction with the KeywordClassification.timeBegin and KeywordClassification.timeEnd properties can be used to map the times to a different timescale as necessary.  See  for an example.  
`classifications`| Array of `KeywordClassification` objects.  
  
Example:

KeywordClassificationSet examplejstrue

 

## AnalyzerParameters

AnalyzerParametersjs

Note: All properties are optional. 

Property Name| Description  
---|---  
`keywordSets`| Array of `KeywordSetRefOrData` objects with URI reference or inlined `KeywordSet`.Note that the referenced keyword sets do not all have to use the same language. It is legal to activate keyword sets of different languages concurrently.  
`toneModel`| A `ModelRefOrData` object specifying the tone model if Analyzer is to be used for Call Progress Analysis.  
`recordingModel`| A `ModelRefOrData` object specifying the recording model (fingerprints) if Analyzer is to be used for Call Progress Analysis.  
`speechModel`| A `ModelRefOrData` object specifying the speech timing model if Analyzer is to be used for Call Progress Analysis.  
      
    
    confidenceModel

| A `ModelRefOrData` object specifying the confidence model if Analyzer is to be used for Call Progress Analysis.  
      
    
    runtimeAttributes

| A JSON serialized `i3attribute::AttributeMap` with additional runtime attributes.  
  
 

## KeywordSetRefOrData

KeywordSetRefOrDatajs

Note: The properties are mutually exclusive

Property Name| Description  
---|---  
`ref`| URI referencing a `KeywordSet` resource. The resource may be in any of the supported formats (JSON, XML, or i3serialize)  
`data`| Inlined `KeywordSet` as JSON object  
`i3serialize`| String containing i3serialize Text serialized KeywordSet object.  
  
 

## ModeltRefOrData

ModelRefOrDatajs

Note: The properties are mutually exclusive

Property Name| Description  
---|---  
`ref`| URI referencing the model resource.  
`i3serialize`| String containing i3serialize Text serialized model resource.  
  
 

 

 
