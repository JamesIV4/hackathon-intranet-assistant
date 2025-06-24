### 0.  Assumptions/Introduction

What is described here is the presumed initial system, before a tokenizer is added.  In this system, each character is a token (modulo normalization scheme below), and is replaced with its most frequent pronunciation during look-up.  Since this is probably a temporary solution, we will not try to do too much normalization, since much of that may be done by the tokenizer later.  We assume that text processing will be done on characters (not pinyin).

### 1\. Say-As Interpreter

End of March version:

  * date
  * number (cardinal)



End of April version:

  * currency
  * ordinal
  * time
  * telephone



Later versions:

  * alphanumeric
  * boolean
  * digits
  * spell



### 2.  Character normalizer

  * roman characters can be retained-they can be treated as characters and be listed in the dictionary;
  * treatment of Arabic digits will depend on how much treatment of longer numerals is required for the initial version:  if none, i.e. if numerals are to be read out by digits, then all Arabic digits can be converted to hanzi characters at this point.



### 3.  Tokenizer

not required at initial stage.

### 4\.  Phrase Predictor

  * deal with punctuation, inserting any prosodic symbols needed
  * preliminary research suggests use of up to five intonation types (see <https://en.wikipedia.org/wiki/Intonation_(linguistics)#Intonation_in_Mandarin_Chinese>, [https://books.google.com/books?id=gcVBAAAAQBAJ&pg=PA44&lpg=PA44&dq=tao+continuing+intonation+mandarin&source=bl&ots=2OYGu96PEY&sig=YaCJkVMGYTO8RXbYmA1m_jtfs4g&hl=en&sa=X&ved=0ahUKEwjB6Z6vp9rKAhUEnoMKHfGgAKIQ6AEIIjAC#v=onepage&q=tao%20continuing%20intonation%20mandarin&f=false](https://books.google.com/books?id=gcVBAAAAQBAJ&pg=PA44&lpg=PA44&dq=tao+continuing+intonation+mandarin&source=bl&ots=2OYGu96PEY&sig=YaCJkVMGYTO8RXbYmA1m_jtfs4g&hl=en&sa=X&ved=0ahUKEwjB6Z6vp9rKAhUEnoMKHfGgAKIQ6AEIIjAC#v=onepage&q=tao%20continuing%20intonation%20mandarin&f=false)):
    * declarative / neutral
    * A-not-A questions
    * 'ma' questions and unmarked questions 
    * continuing (comma) intonation
    * exclamations



### 5.  Text Normalizer

  * need guidance on expectations re numerals, currency, date, time, etc. for initial version.
  * it may be necessary to resolve longer Arabic numerals here (depending on whether this is required); this should be straightforward (similar to ja-JP), but needs research
  * numeral handling:
    * currently (3/2/16) we're dealing with longer Arabic numerals by recognizing them in the phrase predictor (and deleting group separators), then converting them to hanzi in the text normalizer
    * numerals with <12 digits that don't start with 0 can 
      * be grouped by western commas or Chinese commas
      * be grouped by spaces
      * be grouped in threes
      * be grouped in fours
      * be ungrouped
    * only digit strings with consistent grouping are recognized as single numerals
    * otherwise each group (if there are groups) are read out as individual numerals
      * e.g. '12,345,6789' is read out as (translating) 'twelve <comma-intonation> three hundred forty-five <comma-intonation> six thousand seven hundred eighty-nine'
      * e.g. '12,345 678' is read out as (translating) 'twelve <comma-intonation> three hundred forty-five six hundred seventy-eight'
      * this is true even though in both examples, the first two groups and the last two groups each follow the pattern for a single numeral-we have no way of choosing one over the other, however, so we default to reading each group separately.
  * assume we won't have access to characters in the phonology module, so some lexically-specific tone sandhi rules has to be done here:  character/words whose tone changes depending on context need to be marked here as containing alternate pronunciations; e.g 不 bu 'not' has tone 4, but this is changed to tone 2 if the following word has tone 4; in the text normalizer 不 will be marked as 不tone2pron or similar in this context, and then 不tone2pron will be in the dictionary with the appropriate pronunciation and tone.  (this might also be handled with judicious use of POS tags)
  * in later version, how much is included here will depend largely on what the tokenizer provides



### 6.  Stress Predictor

  * deal with output of IPA transcriber (already in code review)
  * deal with any possible STP output in later versions (see below)



###  7.  Phonology

  * tone sandhi rules that are not lexically specific; e.g. 3rd Tone Sandhi
  * erhua - determining realization of 儿 as 'r' coloring of previous syllable vs. separate syllable



### 8.  Dictionary

  * character, pos, pronunciation is the essential part
  * pinyin can be a fourth field for ease of reference
  * contains characters with their most frequent pronunciation
  * contains alternate versions (see Text Normalizer, above)
  * contains each English letter with its isolated pronunciation (as in current pinyin-based dictionary)
  * may contain some other words in roman script



### 9.  STP

  * this may ultimately be necessary to deal with roman letter sequences not in dictionary
  * but for initial version it may be sufficient to read such sequences letter by letter


