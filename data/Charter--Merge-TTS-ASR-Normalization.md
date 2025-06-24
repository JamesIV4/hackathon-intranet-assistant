## Vision

Document Status|  _Red DRAFT_  
---|---  
Name| Merge TTS/ASR Normalization  
Epic|    
Timeframe| Start 17Q2  
Project Value Statement| MVP - Improve text normalization available in ASR by leveraging the same normalization as in TTS.

  * ASR is currently impoverished in its normalization compared to TTS.  Want to re-use TTS so don't have to repeat that work.
  * Using the same file for both systems allows future improvements to directly be utilized by both.
  * Will simplify architecture maintenance down the road and is a preparatory step towards fully merging the Lexicon Models (text norm, phoneset, dictionary, etc) between ASR & TTS.

  
Chartering Team|  ,   
Chartering Date|  04/20/2017  
Next Steps|    
  
 

 

_  RedMUST YellowSHOULD GreenCOULD _Grey WONT__

MVP - Goals| Success Measures| Potential Risks | MoSCoW  
---|---|---|---  
**Architecture (engine)**|   |  |    
Move "normalization" modules/code into the "KWS codebase" (currently done at utteranceComposer codebase level|  |  |    
Need unit tests for various scenarios discussed (so creates a record of why decisions were made)|  |  |    
Strip Intn tags from PP output if in ASR|  |  | _Red MUST_  
PP split into 2 files (ppPrep and ppSplit), so ASR reference only the first, while TTS can reference both|  |  |    
tts_lexicon_test harness adapt to use for both ASR and TTS simultaneously|  |  |    
  
  * behind the scenes, ignore any line that's not applicable for the engine being tested (e.g. stressPred line ignored in ASR)

|  |  |    
  
  * for lines w prons that are different in ASR vs TTS: make use of regex functionality to allow for both

|  |  |    
  
  * for lines w prons that are different in ASR vs TTS: add attribute engine="asr" or engine="tts" to pick out which to use. (Don't add attribute to line if not needed)

|  |  |    
  
  * PronunciationDictionaryOutput needs to handle the fact that ASR can return multiple prons for a single word

|  |  |    
  
  *     * default: will assert lexicon_test matches one of the outputs

|  |  |    
  
  *     * add special tag to show all output prons (will only work on single-word lookups, e.g. in lexicon_test_prons.xml)

|  |  |    
Languages can be enabled to use this approach 1 at a time.|  |  | _Red MUST_  
  
  * add files to i3ca, mark for delete in i3tts, update config files for asr and tts

|  |  |    
Update asr config file to use xml format?|  |  | _Green COULD_  
**Architecture (Lg-specific files)**|   |  |    
Verify no dependencies between CAD and Dictionary in each language|  |  |    
  
  * Abbreviation expansion where ambiguous (e.g. "st." and "dr.") should exit CAD with an ID tag and not a word expansion

|  |  |    
  
  * en-US 's (plural/possessive) becomes a separate word
    * problem for ASR: dict lookup won't work right (unless add phonMod to asr for variant prons)
    * problem for UDD: fix by using "-{pos=in}s" instead of " 's".  Though requires passing all pos for compounds (another project for Adam)

|  |  |    
  
  * CN can collapse words w foreign char spellings, preventing TTS UDD from distinguishing names like "Alta" and "Alta". Would also fail for emoji text sequences, etc.

|  | Outside what we feel is reasonable expected use cases|  __Grey WONT__  
  
  * Tts UDD if our normalization isn't what they want: they can implement a "altpron"-style fix.  I.e. change the word somehow so it doesn't get normalized, and add THAT to the UDD

|  |  |    
Interaction between Intn tags in TTS vs lack of in ASR|  |  |    
  
  * Can PP be split into ppPrep and ppAssign? Any dependencies preventing this?

|  |  |    
Any additional effects on ASR pron lookup?|  |  |    
Any additional effects on User-Defined Dictionaries?|  |  |    
  
  * Initial release will be as soft 'beta' (not announced, hopefully Eric will give us feedback).

|  |  |    
  
  * Focus is on MVP...Once we see problems people get themselves into, we can tweak how it works.

|  |  |    
  
  * Current code looks up strings AFTER normalization, causing some (known) problems when our normalization takes multi-word context into consideration.  E.g. if a word becomes multi-word, it won't get looked up as that multi-word string anymore.  So Word+punc/space normalizations are where UDD will run off rails.  Role of underscores?

|  |  |    
  
  * Idea for improvement: lookup dict first before text normalizing, and if find an exact match, turn it into a pron tag.  Otherwise go through TN & normal (priority) lookup.

|  |  |    
  
  * Where pron tags are integrated into the string:  TTS adds pron tag in utteranceComposer (after phonMod). ASR doesn't do composing, so needs it at LexiconOutput or afterwards.  So add utteranceComposer level to ASR (which is where pronTag is integrated).  Rename this level?

|  |  |    
  
  * While at renaming, should LexiconModel be renamed to something more linguistically correct?  (e.g. LanguageModel)

|  |  |    
  
## Outstanding Questions

What's the ultimate vision for the Lexicon Model?  If we want to use the same file for both ASR/TTS, then would need to have engine-processing changes, rather than CAD-enable/disable for 2 separate asr vs tts lexicon models

##   
Open Items

Issue ID| Date| Description| Priority| JIRA| Owner| Notes  
---|---|---|---|---|---|---  
 |  |  |  |  |  |    
  
 

 

## Closed Items

Issue ID| Date| Description| Priority| JIRA| Owner| Notes|    
---|---|---|---|---|---|---|---  
 |  |  |  |  |  |  |    
  
 

 
