# Introduction  
  
To get more insights into the conversation between the call center agent and the customer we need the ability to measure some metrics based on who talks and how long.  Some of the metrics to capture:

  1. Histogram/distribution of speech spurt duration of agent and customer (this shows who dominates the conversation)
  2. Histogram/distribution of customer being silent after agent stops speaking ("awkward silence", fluidity of conversation)
  3. Histogram/distribution of agent being silent after customer stops speaking ("awkward silence", fluidity of conversation, agent professionalism).
  4. Number of times agent speaks over/interrupts customer. 
  5. Number of times customer speaks over/interrupts agent.



Note that for #4 and #5 above assuming the other party speaking is likely not goo enough.  It instead will require some research to determine a good heuristics as during long talk spurts/explanations the other party may show that they're still listening by saying something like "yes", "uh-huh", and similar.  Treating that as interruption would be bad.  One option would be to simply ignore very short utterances while the other party is speaking and doesn't stop speaking within a few seconds of the utterance (i.e. being actually interrupted). There also needs to be a lockout period due to VAD hangover.

 

 
