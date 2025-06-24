## Supported Features

Media Server Call Analysis was introduced in 2009 Q1 as an advanced Media Server operation in CIC 3.0 SU7 (and is used in Genesys Cloud). This component analyzes audio in an RTP stream from an outbound call in real time, and reports call progress events of interest.  TsServer (Telephony process running on the CIC server) receives requests from Dialer to place an outbound call and perform call analysis, which is performed on the Media Server running call analysis.  There are some other use cases for call analysis not associated with Dialer, which include the analysis to detect a live speaker when using the client application Follow-me settings, which dials all available numbers for a user of the CIC system, and once one of those numbers answers with a live speaker (detected through call analysis), the person calling that CIC user will be connected to the phone of the user (for example, it could first ring the users business number and then their cell phone number, so that they can be mobile).  It used to be used for remote station connections as well (see [this](https://help.genesys.com/pureconnect/mergedProjects/wh_tr/mergedProjects/wh_tr_media_server/desktop/call_analysis_for_remote_stations.htm)).

#### Tone Sequence Detection

  * Ringback
  * Busy
  * Call Waiting
  * Special Information Tone (SIT)
  * Fax tones and preambles
  * These are based on tones discovered in customer datasets that align with the standard set forth in VARIOUS TONES USED IN NATIONAL NETWORKS (ACCORDING TO ITU-T RECOMMENDATION E.180)(03/1998) (<https://www.itu.int/ITU-T/inr/forms/files/tones-0203.pdf>).  Some carriers deviate outside of the range, which our tone model was updated to accommodate for (as long as it doesn't conflict with other tone classifications for that region at least).



#### Live Speaker Detection (LSD)

  * Greeting from primary speaker
  * Robust to background noise
  * Minimal response time
  * The general rule is that a live speaker is detected (speech.person) after 700ms of silence, granted that the speech before that is less than ~2.2 seconds (2.2+ seconds of speech is a machine, speech.machine).  There are various exceptions that could lead to a live speaker being detected after a longer pause of silence, such as 1-1.5 seconds (in some cases where the speech is close to 2.2 seconds and it uses more silence to disambiguate from a short machine greeting and a long live speaker greeting).



#### Answering Machine Detection

  * Message with extended speech segment
  * Common shared answering services
  * Common tones
  * The general rule for generic machine detection (speech.machine) is 2.2 seconds of continuous speech with no greater than 700ms of silence within that (700ms of silence would cause a live speaker detection to occur with less than 2.2 seconds of speech).  There are various exceptions that could lead to speech.machine detection taking a little longer or a little shorter (such as only 1.5 seconds of speech, e.g., if speech is immediately followed by a tonal signal).



#### Music Detection

  * Ringback option from some networks



#### Recording Detection

  * Network messages (not preceded by SIT)
  * Call Screeners & Privacy Managers
  * Shared Answering Services
  * Ringback composed of speech



  


**MSCA Events**

For a list of all events that call analysis can detect, please refer to .

  


CallAnalysisModelsDiagram2

  


CallAnalyzerDetectorsAndClassificationDiagram14

  


CallAnalysisClassificationExample6

  


The below version is a condensed form of the above layout (e.g., for presentation slide use)

CallAnalysisClassificationExampleCondensed7

  


CallAnalysisRecordingModelUpdateProcess6

  

