### Overview

During our TextProcessing of TTS input text, we have a need for:

  1. Normalizing characters to a smaller standard set, allowing us to intelligently handle small variations in text (e.g. different styles of apostrophes).  All TTS languages need this functionality.
  2. Transliterating characters from one script to another.  This is necessary for certain languages (Japanese, etc), but may also be useful elsewhere.



##### Page Contents

3Overview|Transliterate

## ICU transliteration transform

General transforms provide a general-purpose package for processing Unicode text. They are a powerful and flexible mechanism for handling a variety of different tasks, including:

  1. Uppercase, Lowercase, Titlecase, Full/Halfwidth conversions
  2. Normalization
  3. Hex and Character Name conversions
  4. Script to Script conversion



#### How we intend to use ICU library

Our team is most comfortable with regex and the syntax of our current Code-As-Data language. The bread-and-butter application of ICU for us will be large-scale conversions of characters.  Where we would otherwise have to a) include a huge replacement table or b) just delete things to avoid having a huge replacement table, that's where we want to use ICU.

For an in-depth description of ICU's syntax and several examples, read through the  page.

 

* * *

## Default Character Normalization in TTS Text Processing

Update:  
The Character Normalizer will be a separate CAD module, which will occur immediately after say-as and before the tokenizer (if there is one).

Earlier plan:  
Working assumption is this normalization will occur at the beginning of the phrasePredictor Code-As-Data module.  That is, the very first thing in text-processing, with the exception that Say-As will operate first on the exact text string provided by the user.

### Character Normalization to Each Language's Local Alphabet

xml

### Character Normalization for Punctuation

All punctuation can be distilled to ASCII punc (`**_ - , ; : ! ? . ' " ( ) [ ] { } @ * / \ & # % ` ^ + < > | ~ $** `), and further reduced by language-specific mapping (e.g. map backtick ( ` ) to apostrophe ( ' ), remove tilde ( ~ ), etc.)

xml

### Character Normalization for Whitespace

xml

 _Questions to Consider when adopting this for a language:_

  * Is there information in other whitespace characters we could use, which would cause us to deviate from normal usage?  

    * e.g. ja-JP special spacing characters?



## Sample Transliteration between Scripts

xml

## Style Guidelines

  1. Include only one operation per line of code.  Do not chain statements.
     1. Why?  Debugging is easier if we can see what's happening at each step, rather than just cumulatively.
  2. Comment at macro and micro level.  (Macro level to state overall what we're trying to normalize, micro level to show what each line does)
     1. Why? Our team is new to ICU & needs time to get comfortable with the syntax.  Comments will also help prevent changing stuff later that shouldn't be.



 
