Decisions on issues we may need to handle - or explicitly decide _not_ to handle - for Japanese TTS support.

  * **input:**
    * **orthography:** we support typical Japanese input (mixed kanji, kana, and roman script)
    * **encoding:** most common encodings for Japanese are EUC-JP and Shift-JIS, and then Unicode. Do we need to restrict input so that we only get Unicode, or convert any non-Unicode input to Unicode?
      * Per , we can assume the input will be UTF-8 by the time it reaches TTS.
    * **character width:** Japanese uses [half-width and full-width characters](http://en.wikipedia.org/wiki/Halfwidth_and_fullwidth_forms). (Half-width is only an option for katakana and romaji, apparently.) We would probably want to convert all input to one type. Update: character normalizer & dictionary resolve this issue.
  * **dictionary:  **Because we're using tokenizer with its own dictionary (ca. 750,000 entries), we may not need a typical TTS dictionary.
  * **part of speech dictionary:**
    * Unlike other languages, dictionary will include some POS values, such as "prefix", that are for bound morphemes. This is a result of how tokenizers output Japanese text.
    * Early version of POS dict included cl (numeral classifiers), dt (determiner), and in (preposition/subordinating conjunction). Removed from current version, as they're never in tokenized output.
  * **phoneset:** differs slightly from ASR
    * Geminates phones for voiceless obstruents only, mainly to help avoid double releases.
    * There are no voiced geminate obstruents in Japanese phonology; if a loan word should have them, such as "baggu", speakers generally devoice /gg/. We've chosen to represent voiced geminates with a sequence of phones rather than with a geminate voiced phone (e.g. /g g/ in "baggu" rather than /gg/).
    * Originally we chose to represent long vowels as a sequence of two short vowels; however, this may lead to undesirable coarticulations. Test voices were produced using both ASR and TTS phonesets; ASR phoneset using long vowel phones appeared to give better results. Therefore, we changed the TTS phoneset back to having separate long and short vowel phones.
    * The moraic nasal is represented with one phone in ASR but three in TTS. The three allophones are 100% predictable based on phonological environment.


