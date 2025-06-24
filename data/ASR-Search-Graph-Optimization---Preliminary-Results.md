## 1\. Introduction

The goal of this project is to improve the speed for searching and matching phrases in automatic speech recognition by reducing the number of objects (nodes or edges) in the search space, which is a grammar (at the word level) or a pronunciation graph (at the phone level). This can be achieved by first enhancing the data structure used to represent the search space, described in Section 2, and then performing graph reduction on the search space, described in Section 3. Some examples are presented in Section 4, and Section 5 conclude with ongoing work.

## 2\. The WordGraph Data Structure (for grammars)

In the data structure used to represent a grammar (class Grammar), each rule is represented by a Sequence element, which consists of elements such as Tokens, Tags, RuleRefs, and Alternatives; within an Alternatives element, there are multiple items (branches) which wrap around Sequences containing more elements (see srgs_parse_tree.h). This is a faithful representation of the grammar file, and it may be sufficient for storing a grammar and translating it into a recognition graph. However, the wrap-around approach makes it difficult to modify the data structure so as to reduce redundancy by merging common elements in different branches.

This consideration has led us to create another data structure (class WordGraph) that represents a grammar with nodes and edges. Each node, called a WordNode, has the following attributes (data members):

  * Type: Token, Tag, RuleRefLocal, RuleRefExternal, RuleRefSpecial
  * Value: additional information based on its type. For example, if it is a Token, its value would be the actual word the token represent.
  * A list of WordNode(s) pointing to it (i.e. words, tags or rule references preceding it in the sentences specified in the grammar file)
  * A list of WordNode(s) it points to (i.e. words, tags or rule references that follow after it in the grammar file)



In other words, instead of wrapping elements with additional elements like Sequence and Alternatives in the original data structure, WordGraph simply represents the grammar with a graph, with each word, tag or rule reference being a WordNode, and expressing the sentence relationships with edges between WordNodes.

The following graphs illustrate the different approaches of class Grammar and class WordGraph in representing the same rule, **_$rule = a ( b c | d ) e;_**

|   
---|---  
class Grammar  |  class WordGraph   
  
  
While the WordGraph is for representing grammars at the word level, we could construct a similar data structure to represent pronunciations at the phone level (by simply expanding the WordGraph). Moreover, similar reduction techniques (described below) also apply.

## 3\. WordGraph Reduction

A WordGraph can be made more concise if common tokens, tags, or rule-refs in different branches could be factored out. To perform such factorization, the program first factorizes each path, then searches for the first node in the path with the targeted type (token, rule-ref or tag), and finally merges paths with common first-nodes.

In addition to factoring out nodes in common, it is desirable for the tags to appear as late as possible (i.e. pushed as far back from the root as possible), due to the additional overhead created by tags. Some examples are described [here](https://confluence.inin.com/display/MediaGroup/i3asr-+Graph+Optimization).

To achieve these goals, we perform the following reduction in order:

  1. Factor out tokens/rulerefs from the front (i.e. from the root node of each rule)
  2. Factor out tags from the back (i.e. from the end nodes)
  3. Factor out tags from the front
  4. Factor tokens/rulerefs from the back



The order of items 1-2 could be swapped, and so could 3-4; however, each of 1-2 must be performed before each of 3-4, due to the preference for tokens/rule-refs at the front and tags at the back.

## 4\. Experimental Results

#### Example 1: Menu

WordGraph reduction results are shown for the following grammar, menu:

[ WordGraph before reduction ]  |  [ WordGraph after reduction ]   
---|---  
|   
  
Note that in the rule $test, there are 4 paths from the root to the end, though some of them are the same due to redundancy in the grammar specification. The reduction result preserves all 4 paths; in other words, it keeps every possible combination given by the grammar, and does not remove redundant combinations. Depending on how accurate we wish the reduced graph to reflect the original grammar, the may be enhanced to handle redundancy.

#### Example 2: Swedish Yes/No

Similar principles could also be used at the pronunciation or even phone level. Note the reduction in the rules $yes_emphasis and $no_emphasis in the following grammar, SwedishYesNo:

[ WordGraph before reduction ]  


[ WordGraph after reduction ]  


## 5\. Ongoing Work

  * Preprocessing (before reduction) to group tokens/rule-refs to the front, and tags to the back.
  * Repetition of phrases (specified in the original grammar with < . >) are currently unaccounted for.
  * Implementation and experiments at the phone level.
  * Code clean-up and optimization for speed and space.


