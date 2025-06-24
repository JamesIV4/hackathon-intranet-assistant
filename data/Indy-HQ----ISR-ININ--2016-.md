# Data

This data set was collected in 2016 starting July 22nd. 2-week data was used in the following analysis.

# Results and Analysis

The data set was run through different models to compare the performance:

  * 2016r3 systest
  * 2016r4 systest
  * 2016 Q3 staging @beginning
  * 2016 Q3 staging @9/20



## Overall Results

The performance was based on the following parameter setting: confidence level=0.5, vad sensitivity=0.5.

 | dialog-state|  utterances|  IG|  IG-CA|  %|  IG-FA|  %|  IG-FR|  %|  OOG|  OOG-CR|  %|  OOG-FA|  %|  NI|  NI-CR|  %  
---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---  
systest 2016r3| Overall| 9589| 6073| 4951| 81.5| 254| 4.2| 868| 14.3| 2847| 2456| 86.3| 391| 13.7| 669| 291| 43.5  
systest 2016r4| Overall| 9589| 6073| 5125| 84.4| 153| 2.5| 795| 13.1| 2847| 2406| 84.5| 441| 15.5| 669| 291| 43.5  
2016 Q3 Beginning| Overall| 9589| 6073| 5130| 84.5| 131| 2.2| 812| 13.4| 2847| 2447| 86| 400| 14| 669| 291| 43.5  
2016 Q3 Mid| Overall| 9589| 6073| 4786| 78.8| 86| 1.4| 1201| 19.8| 2847| 2703| 94.9| 144| 5.1| 669| 291| 43.5  
2016 Q3 Mid + Tuned Grammar| Overall| 9589| 6049| 4793| 79.2| 83| 1.4| 1173| 19.4| 2871| 2723| 94.8| 148| 5.2| 669| 291| 43.5  
  
  * The performance got better from 2016r3 to 2016 Q3 Beginning, however it was deteriorate by 2016 Q3 Mid. The analysis had shown this was due to the new confidence model which was later on under reconstruction.
  * To improve the performance, the customer's grammar was tuned. It increased in grammar performance slightly but not significant.



## Categorized Results

Further analysis was performed to the categorized sub data set: digits and names (company directory). systest 2016r4 model was used in this analysis and same parameter setting as the overall data testing.

 |  utterances|  IG|  IG-CA|  %|  IG-FA|  %|  IG-FR|  %|  OOG|  OOG-CR|  %|  OOG-FA|  %|  NI|  NI-CR|  %  
---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---  
Overall| 9589| 6073| 5125| 84.4| 153| 2.5| 795| 13.1| 2847| 2406| 84.5| 441| 15.5| 669| 291| 43.5  
Digits| 555| 512| 429| 83.8| 47| 9.2| 36| 7| 43| 35| 81.4| 8| 18.6| 0| 0| 0  
Name| 961| 954| 791| 82.9| 33| 3.5| 130| 13.6| 7| 4| 57.1| 3| 42.9| 0| 0| 0  
  
### Digits

The digits' performance was slightly worse than the overall. There were three type errors in the hypotheses:

  * Single digit error: one digit was replaced by another. This was the typical error we expected.

Trans:| eight two seven six six zero  
---|---  
Hyp:| six      two seven six six zero  
  
  *  Nomatch: don't know how to get this output

Trans:| one zero five two one eight four three five  
---|---  
Hyp:| #nomatch#  
  
  * Names:  don't know why we got this output although the confidence of the hypothesis was very low

Trans:| one one two eight four zero two one five  
---|---  
Hyp:| Gwenlynn Ortman  
Hyp:| Lynn McCready  
  
### Names

The names' performance was also slightly worse than the overall in grammar. There were not many instances in out of grammar. For in grammar errors, there were nine different causes:

  * Poor recording qualities: such as background noise, music mixed in

trans| Eric Cohen  
---|---  
hyp| Christian Klein (noise before "Eric")  
hyp| LeonRavenna Conf ( background music)  
  
  * The same speaker got denied twice. This increased the error instances.

trans| Darren Gill  
---|---  
hyp| Aaron Bickell   
hyp| Aaron Bickell  
  
  * Some speakers had heavy accents

trans| Eric Cohen  
---|---  
hyp| Andy Kauffman  
trans| Donald Anderson  
---|---  
hyp| Fahad Shaikh  
  
 

  * Low voice

trans| Steve Holt  
---|---  
hyp| help  
  
  * Saturated voice

trans| Steve Holt  
---|---  
hyp| Stephen Tatton  
  
  * Some names have similar pronunciations

trans| Ken Moore  
---|---  
hyp| Ben Four  
  
  * Some speakers pronounced the transcript wrong

trans| Paul McGuire  
---|---  
hyp| Paul Pryor ( he didn't say McGuire)  
  
  * Don't know the reason, but got no match or no input

trans| Justin Helmig  
---|---  
hyp| #noinput#  
  
  * Wrong STP: for some foreign names, the correct pronunciations are different from English's phoneme rules. In the following example, the correct pronunciation of "Nguyen" is "When".

trans| Mimi Nguyen  
---|---  
hyp| Mimi When  
  
  * same person but has differently spelled names

trans| Adriana Ramadanis  
---|---  
hyp| Adriana Viola-Ramadanis
