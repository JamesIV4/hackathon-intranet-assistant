## Want to try out our homegrown Text-To-Speech voices? 

There is a demo webapp running at <http://adampaughpc.us.int.genesyslab.com:3000/#/texttts> with several examples to get you started.  This is great if you just want to play around, or if you need to test audio output or text processing (e.g. Say-As support).

## What if I come across a word that is mispronounced, or something that is read out incorrectly?

Please report errors at: 

## Is Don Brown's voice really available as TTS?

Yep!  A 2015 hackathon team built a TTS voice from Don's quarterly update videos, so we've included it here for one and all to enjoy. 

That was before we switched from GMM to DNN voices, though, so Don's voice is only available on the page that uses GMM-based models (see below).

## What version of code is this running?

This webapp runs code from staging.speech, not systest.  So some features here may not be available in systest yet.

## (Speech Technology Developers Only:) How do I easily debug the source of a voice or textProcessing error?

A second version of the webapp is available with increased tracing at <http://adampaughpc.us.int.genesyslab.com:3001/#/texttts>

Please contact Adam Paugh for more info.

Only use the debug one if you need to look at the traces as its level is All and can grow fast.  If you want to just play around or test audio output, use the normal one at port 3000.

## (Speech Technology Developers Only:) What if I want to generate audio from our old GMM-based TTS models?

As of January 2018, our DNN voices are at the main port (3000) and our old GMM voices are at port 3002:<http://adampaughpc.us.int.genesyslab.com:3002/#/texttts>

  


  

