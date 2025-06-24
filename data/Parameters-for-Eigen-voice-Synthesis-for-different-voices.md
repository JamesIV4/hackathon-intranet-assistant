Eigen templates and filter coefficients:

 |  | 

## Single-band

| 

## Two-band  
  
---|---|---|---  
Voice| Language| Voiced Phonemes| Template| .m file used to create excitation model.(contains all filter parameters)| Template| Remarks| .m files  
 |  | Deterministic (Eigen) Filter|  |  |  |  |    
Jill| en-US| B = templateA = See attached m file|  | | Jill_06| s,sh created separate grouping. Noise for numerator: 0.1250.6 is used for second band weight in excitation_model.cpp|    
Kendra| en-US|  |  | |   
---  
 |  |    
Ellene| en-GB| B = templateA = See attached m file|  | |   
---  
 |  |    
Kandyce| en-AU| B = templateA = See attached m file| | |   
---  
 |  |    
Jayde| es-US| B = templateA = See attached m file|  | |   
---  
 |  |    
Hilorie| fr-CA| B = templateA = See attached m file| | |   
---  
 |  |    
 Arabella|  de-DE| B = templateA = See attached m file|  | |   
---  
 |  |    
  
Notes:

  * The excitation model for each voice has phones classified into 3 or 4 types (voiced,unvoiced,plosives,semi-unvoiced) depending on the voice and use different filter parameters including Eigen template and different types of colored noise. The details and be easily found in the attached matlab scripts which create the excitation model, found in the last column.



 
