Both ISR and TTS use internal pronunciation dictionaries covering the pronunciation of most of the common words or phrases. The performance of both ISR and TTS however is improved if in addition to the internal pronunciation dictionaries application specific dictionaries are used. One can use such a user defined dictionary to add the specific pronunciation for uncommon names or surnames of persons or for particular pronunciations of certain business names.  
  
Although the same pronunciation dictionary format is used by both ISR and TTS, the pronunciations contained inside end up being utilized differently by the ISR respectively TTS. The syntax of the user defined lexicons supported follows the prescriptions of the Pronunciation Lexicon Specification (PLS) Version 1.0 found at <https://www.w3.org/TR/pronunciation-lexicon/>.

 

## Testing user defined lexicons in ISR

 

ISR uses a grammar based recognition process. The syntax used to specify those grammars follows the Speech Recognition Grammar Specification Version 1.0 (SRGS) (specification could be found at <https://www.w3.org/TR/speech-grammar/>). SRGS allows a grammar to optionally refer one or more external lexicons.

What is specific to the ISR is the fact that the pronunciations provided by the user defined lexicons are used as alternatives in the recognition process. This means that if the internal lexicon provides one pronunciation and 2 more pronunciations are specified in user defined lexicons, the 3 alternatives are all considered acceptable in the recognition process.

 

To test user defined lexicon in ISR we've added to the built in digits grammar 3 lexicons containing pronunciation of some of the digits in Spanish. As a results in the recognition process both the English and the Spanish pronunciation are recognized for those digits.

 

The digits grammar modified to include those user lexicons is defined as:

 

 

The base declaration specifies a base URI to be used in resolving the relative URIs for user lexicons. The grammar refers 3 user lexicons: first specified using an absolute URI, the remaining 2 by using relative URIs. To use this grammar you might need to adjust the paths depending on the location of the lexicons.

 

The content of the user defined lexicon lex_digits_en_pron_es_1.pls is:

 

 

The content of the user defined lexicon lex_digits_en_pron_es_2.pls is:

 

 

The content of the user defined lexicon lex_digits_en_pron_es_3_4.pls is:

 

 

As it can be seen the Spanish pronunciation for 1 - _" uw n ow"_, 2 - _" d ow s"_, 3 - _" t r ey s"_ and 4 - _" k w aa t r ow"_ are added as valid pronunciation in this case to their respective English pronunciations for 1, 2, 3 and 4.

 

## Testing user defined lexicons in TTS

 

TTS supports the usage of Speech Synthesis Markup Language (SSML) Version 1.1 (specification could be found at <https://www.w3.org/TR/speech-synthesis11/>). Section 3.1.5 of SSML describes how external lexicons to be used are specified and how they are used in synthesis.

What differentiates TTS case from ISR is the way it behaves when 2 or more pronunciations are available for the same token. Using "lookup" elements in SSML one can specify the order the user defined lexicons are searched to find the pronunciation. The first pronunciation found when the user defined lexicons and the built in lexicon are traversed in the order imposed by the "lookup" elements, is the one which is actually used.

 

To test user defined lexicon in TTS we've created user defined lexicons which replace the pronunciation for the word "white" with pronunciation for some other colors. The SSML test is organized as a sequence of affirmative sentences such as:

_I say white._

followed by verification, questioning sentences such as:

_Have you heard white?_

When pronunciation dictionaries are used, the pronunciation for "white" in the former affirmative sentence is however replaced based on the highest priority pronunciation dictionary at that point with a pronunciation for a different color (for example "red").  For reference the latter questioning sentence contains the color whose pronunciation we're expecting to hear. If for example the lexicon replacing the pronunciation for "white" with the pronunciation for "red" is the one with the highest priority, the 2 sentences in the test are written as:

_I say white. Have you heard red?_

The version synthesized however should actually sound as:

_I say red. Have you heard red?_

 

Here is a complete SSML example:

 

 

The content of the user defined lexicon lex_white_as_red.pls is:

 

 

The content of the user defined lexicon lex_white_as_blue.pls is:

 

 

The content of the user defined lexicon lex_white_as_purple.pls (as an alternative this lexicon uses the **ipa** alphabet instead of the internal **x-inin-arpabet**) is:

 

 

The content of the user defined lexicon lex_blanco_rojo.pls (note the language **es-US** used by this lexicon) is:

 
