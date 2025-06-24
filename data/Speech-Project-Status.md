This page lists the status of various enhancements to Speech components (ASR/TTS/MRCP/VXML).   
  
# Requested Enhancements

Enhancement| Impact| Notes  
---|---|---  
IC-122646IC-122644key,summary,type,created,updated,due,assignee,reporter,priority,status,resolutionInteractive Intelligencea6f784b9-ef5d-3d60-bca5-6d0a3771dd27IONMEDIA-1592key,summary,type,created,updated,due,assignee,reporter,priority,status,resolutionInteractive Intelligencea6f784b9-ef5d-3d60-bca5-6d0a3771dd27IONMEDIA-1260| Allows tuner to display more information about the application and generate KPI (Key Performance Indicator) statistics| Needs design work  
IONMEDIA-2045| Helps allow tuning ISR applications| Needs design work  
ISR should support something like SWI_disallow so that n-best list contains valid results Details from Eric Tober:Disabling through application logic (out.disallowed, and then let VXML filter out disallowed recognitions) wouldn't work as well for the following reasons:

  1. For every recognition with an out.disallowed, you would be requiring the application to perform an n-best post-processing step to filter the results, adding overhead.  This can waste quite a bit of design and development time/effort.  Plus, it may result in diluted confidence scoring.
  2. SWI_disallow works prior to the completion of the N-Best list by the recognizer.  Hence, the application needs only process already allowed return values.  I'm not 100% sure if the conf score gets refactored in these cases.  Anyway, let's look at an example of where this would be advantageous: credit card recognition using checksum validation.  

ccnum.grmlxmlWith this type of recognition, you usually want an N-Best list on the order of 10 items.  Using an out.disallow formalism, you may end up stripping out most if not all of your hypotheses, leaving you an effective N-Best list that is much smaller or empty (negatively impacting overall accuracy by missing valid returns).  You can increase the list size, but this starts to cost you in terms of performance (latency).  By having the disallow work prior to the N-Best list formulation, you will have a much higher likelihood of obtaining a valid list with which the application can work.| Simplifies application development| Needs design work. SISR tags aren't evaluated by the media server, so most of the benefits Eric mentioned wouldn't be possible without significant architectural changes to ISR.  
IC-130659| Simplifies application development | Needs design work  
IC-132249IC-132248| Allows better reporting on NoMatch events. (Number of DTMF NoMatches vs Speech)| Biggest unknown is the VXML interpreter side (exposing the mode in lastresult$ for NoMatch). May "just work" by changing NLSML, or may require additional Bladeware changes.  
  
# Completed Enhancements 

Enhancement| Impact| Notes  
---|---|---  
IC-130183| Helps with resolving external rule references in grammars and makes ISR applications easier to tune| Built in 2015r4 and later. Available in 2015r2 and 2015r3 patches.  
IC-128821| Helps with PCI compliance by not tracing DTMF or Speech results| Built in 2015r4 and later.  
IC-128573 | Fixes SRGS parser bug for DTMF grammars| Built in 2015r4 and later.  
IONMEDIA-1877| Fixes SRGS parser bug for ISR grammars| Built in 2015r3 and later.  
IC-123916| Use same ASR port in VXML and handlers and across VXML sessions for the same call| Built in 2015r4 and later. Available in 2015r1, 2015r2, and 2015r3 patches.  
IC-123405 | Allows VXML session to use a single ASR port| Built in 2015r1 and later. Available as ES for 4.0 SU5 and SU6.  
IC-123555| Helps with PCI compliance or dealing with sensitive data| Built in 2015r1 and later. Available as ES for 4.0 SU5 and SU6.
