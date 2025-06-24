# About the Data

This was a small group of es-US data and the customer's grammar files were in SWI-semantics format.

# Issues

  * Need to revise the SWI format grammar files to SRGS format so that i3asr system can interpret them correctly
  * There were lots of OOG instances (mainly due to grammar):
    * There was "_" in grammar files but no "_" in transcription
    * date_swi.xml file: after revision, it didn't trigger error in i3asr system but all the instances had OOG output (will check the grammar contents)



# Performance (excluding date data)

  * OOG performance was good
  * IG performance need to be improved: many instances were detected but with low confidence. Recommend to review the confidence model.

dialog-state|  utterances|  IG|  IG-CA|  %|  IG-FA|  %|  IG-FR|  %|  OOG|  OOG-CR|  %|  OOG-FA|  %|  NI|  NI-CR|  %  
---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---  
Overall| 1263| 966| 220| 22.8| 6| 0.6| 740| 76.6| 176| 164| 93.2| 12| 6.8| 121| 44| 36.4  


