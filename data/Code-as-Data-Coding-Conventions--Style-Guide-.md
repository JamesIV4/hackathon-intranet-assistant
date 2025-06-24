## Style Guides  
  
  * Use search instead of match for regex
  * Use 4-space tabs
  * Use parens around the second set of curly braces if you get the repeat range error
  * Use $1, not \1, although both work
  * To specify a list of items in a regex, clarity is more important than compactness, so just list them if they wouldn't look clear otherwise.
  * Don't add unnecessary marks to clarify (e.g. use -+ instead of [-]+)
  * When listing items in a regex, order LC before UC
  * Naming convention: Use lower-camel-case for variables
  * Alternation expressions should list items longest to shortest.  Alternation expressions default to 'eager' match (not 'greedy' match), so unless there are clear right-boundary conditions that force the appropriate match, the match will only capture what it first encounters (not the longest item in the alternation).  So the better habit is to always write longest-to-shortest. (Note: This 'eager' match behavior for alternations is a characteristic of the most common type of regex engine, which includes Boost. The other type does match the longest alternative, but it doesn't have stingy quantifiers or look-ahead. <http://www.regular-expressions.info/alternation.html>)
  * Maintain consistent style across modules as much as possible (e.g. phrase_predictor uses @digit instead of \d, because other modules include other variations, like @nonZeroDigit)



 

## Efficiency Notes

  * Have a ton of simple text expansions?  Use a _ReplacementTable_ instead of a series of _Rege_ _xSearchReplace._ A ReplacementTable will run through the input text string one time, but using Regex means cycling through the input text as many times as there are regexes.
  * Are you in the characterNormalizer or phrasePredictor?
    * These modules see the entire input text (unless there were intervening SSML marks like <say-as> or <mark>).
    * So be careful that regex are very targeted. Don't unnecessarily search the entire input string.
  * Keeping your regex from being too power-hungry (cf. <http://www.regular-expressions.info/catastrophic.html>)  

    * The left end of the regex has a huge effect on the search space.  Make it as narrow as possible.  (".*x" is way worse than "x.*" in how long it takes to search the string)
    * Do not put adjacent "match anything" or "match almost anything" expressions adjacent or nested (e.g. "(.+)+"). This creates combinatorial search space, and is almost always a sign you should refactor the regex.
  * Regex debuggers available to evaluate efficiency: <https://www.debuggex.com/>



 
