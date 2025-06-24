## Notes

  1. Inline rules: If scope information is not needed (typically if rules have no tags), the graph optimizer could simply inline rules to reduce overhead of creating ScopeInfo objects. For example -  can be written as:  Inline can be done even if the rules are public, however, the public rule should still be accessible from other grammars. For example:  Would have to be compiled to:  Note: Inlining of rule references may require some level of tag inspection to see whether any of the subsequent tags might reference the 'meta' object.  Otherwise, if the 'f' tag in our case contained "meta.foo.text" or "meta.latest().text", it would fail.  The 'meta' object is not used particularly frequently, so disabling certain optimizations for rules that reference it should be OK.
  2. Move tokens as far left as possible and tags as far right as possible. This minimizes unnecessary tag word lattice item emission for paths that get pruned out. Example:  can be re-written as:  Careful with rule references, though:  Tags cannot cross rule references unless we do deep inspection as the tag could reference rules.latest(). Thus, this can only be optimized to: 
  3. Factor out tokens (and tags)  can be re-written as:  Note how the 'a' token is factored to the left and the 'd' tag factored to the right.


