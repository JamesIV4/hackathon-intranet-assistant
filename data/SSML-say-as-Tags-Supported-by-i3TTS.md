## Tag Support - By Language  
  
Status of languages in media_main_systest as of 2016, which are at readiness level 5+

 | en-US| es-US| fr-CA| en-AU| en-GB| de-DE| pt-BR| nl-NL| ja-JP| zh-CN  
---|---|---|---|---|---|---|---|---|---|---  
****|  |   |  |  |  |  |  |  |  |    
****| | | | | | | |  | |     
**boolean**| | | | | | | |   | |    
**currency** | | | | | | | |  | |    
**date** | | | | | | | |  | |    
**digits**| | | | | | |   |  | |    
**number**| | | | | | | |   | |    
**ordinal**| | | | | | | |   | |    
**spell**| | | | | | | |   | |    
**telephone**| | | | | | | |   | |    
**time**| | | | | | | |   | |    
  
= good support

 = basic support

= feature is available in team-branch, but not yet in systest (should be pushed within a quarter).

 

Note

The above chart displays coverage from a external perspective - whether a user can type the SSML Say-As tag of this type and receive the expected interpretation.

(Developers: Here we aren't distinguishing between whether a data type is handled in Say-As or TN CAD modules.  e.g. as with 'currency'.  Nor does it record whether we're planning improvements for the existing coverage.  Internal status should be tracked through JIRA instead.)

 

 

## Implementation Details

The behavior of each Say-As tag is described below, along with any relevant notes.

### Interpret-as="address"

Available only for en-US at this time. Processes US addresses, including military addresses, PO boxes, and rural routes. Expands abbreviations based on context.

Input| Output  
---|---  
<say-as interpret-as="address">1742 Main St., Salem, OR 96607</say-as>| one seven four two main street, salem, oregon, nine six six zero seven  
<say-as interpret-as="address">PO Box 382, Salem, MS 25384</say-as>| post office box three eight two, salem, massachusetts, two five three eight four  
<say-as interpret-as="address">4642 E St Clair St NW, Salem, KY 44557</say-as>| four six four two east saint clair street northwest, salem, kentucky, four four five five seven  
<say-as interpret-as="address">65 N St Apt 2, Salem, OH 44323</say-as>| six five n street apartment two, salem, ohio, four four three two three  
<say-as interpret-as="address">PSC 802 BOX 74, APO AE 09499</say-as>| p-s-c eight zero two box seven four, a-p-o a-e, zero nine four nine nine  
<say-as interpret-as="address">RR 2 BOX 152, Bridgeport, CT 55555</say-as>| rural route 2 box 1 5 2 , bridgeport, connecticut, five five five five five  
<say-as interpret-as="address">3057 Coconut St  
Honolulu, HI 98063</say-as>| three zero five seven coconut street, honolulu, hawaii, nine eight zero six three  
  
**Notes:**

  * We recommend that you do not include the addressee name inside the say-as address tag for best results. Regular text processing is recommended for names.
  * We recommend using official USPS abbreviations for states, territories, and thoroughfare types. However, the say-as address processing will support common abbreviations for thoroughfare types (e.g. 'St' and 'Str' for 'street'). State/territory name abbreviations such as "Wash." are not supported at this time - instead, use either the official 2-letter USPS abbreviation (WA) or the full name (Washington).
  * The say-as processing decides whether "St" is "Street" or "Saint" depending on context. If you get unexpected results (e.g. you wanted 'Saint' but it's outputting 'Street' instead), you can use the full unabbreviated word to force the reading you want.
  * Addresses may contain newline characters (see final example in table above).



 

### Interpret-as="alphanumeric"

A space is added between any alphanumeric characters, and alphabetic characters are capitalized. All non-alphanumeric characters are retained. The "format" option isn't supported.

Input| Output  
---|---  
<say-as interpret-as="alphanumeric">banana</say-as>| B A N A N A  
<say-as interpret-as="alphanumeric">a1'2je</say-as>| A 1 ' 2 J E  
<say-as interpret-as="alphanumeric">test?no12.</say-as>| T E S T ? N O 1 2 .  
  
 

### Interpret-as="boolean"

"True" (and its variants such as "T") return "yes". "False" and variants return "no". Other input is unchanged. The "format" option isn't supported. Input is case-insensitive.

Input| Output  
---|---  
<say-as interpret-as="boolean">true</say-as>| yes  
<say-as interpret-as="boolean">T</say-as>| yes  
<say-as interpret-as="boolean">False</say-as>| no  
<say-as interpret-as="boolean">f</say-as>| no  
  
 

### Interpret-as="currency"

This allows currency input to be properly read out. Note that the input must contain either a supported currency symbol or 3-letter currency code (see below). The "format" option isn't supported.

Input| Output (en-US)| Output (fr-CA)  
---|---|---  
<say-as interpret-as="currency">$45.30</say-as>| forty five dollars and thirty cents| quarante-cinq dollars trente sous  
 <say-as interpret-as="currency">USD45.30</say-as>| forty five u-s dollars and thirty cents| quarante-cinq dollars americains trente sous  
<say-as interpret-as="currency">45.30USD</say-as>| forty five u-s dollars and thirty cents| quarante-cinq dollars americains trente sous  
<say-as interpret-as="currency">$7.666666667</say-as>| seven dollars and sixty-six point six six cents| sept dollars soixante-six point six-six sous  
<say-as interpret-as="currency">how about GBP9.23 more</say-as>| how about nine british pounds sterling and twenty-three pence more| \--  
<say-as interpret-as="currency">Voulez-vous me donner plus de GBP9,23?</say-as>| \--| Voulez-vous me donner plus de neuf livres anglaises vingt-trois sous?   
  
  


Currency symbols and codes supported:

  * $ USD (American dollars: dollars and cents)  

  * £ GBP (British pounds sterling: pounds and pence)
  * € EUR (euros: dollars and cents)
  * $ CAD (Canadian dollars: dollars and sous (in fr-CA))
  * $ AUD (Australian dollars: dollars and cents)
  * CHF (Swiss Francs: francs and centimes (in fr-XX))  




  


Notes:  


  * If more than two digits occur to the right of the decimal point, they are truncated to hundredths of a cent and normalized, as shown in row 4 above.
  * Extra characters to the left or right of the currency string are ignored, as in row 5 above.
  * Since VXML handles currency the same way as standard SSML, adding "vxml" to a tag will have no effect (e.g. "vxml:currency=" will be the same as "currency=").
  * For fr-CA, the default currency punctuation is the decimal comma ($12,99), but the system will also process the decimal period ($12.99).



 

### Interpret-as="date"

Examples:

Input| Output (en-US)| Output (fr-CA)  
---|---|---  
<say-as interpret-as="date" format="mdy">04/06/1994</say-as>| april sixth, nineteen ninety-four| six avril, mille neuf-cent quatre-vingt-quatorze  
<say-as interpret-as="date" format="md">4/6</say-as>| april sixth| six avril  
<say-as interpret-as="date" format="m">06</say-as>| june| juin  
<say-as interpret-as="date" format="md">22/1</say-as>| 22/1| 22/1  
<say-as interpret-as="date" format="mdy">12/10/1988a</say-as>| twelve slash ten slash one-thousand nine-hundred eighty-eight A| douze barre oblique dix barre oblique mille-neuf-cent-quatre-vingt-huit A  
  
 

Possible values for "format":

  * mdy, dmy, ymd
  * md, dm, ym, my
  * y, m, d



Dates with invalid format values (e.g. yd), or dates in which the text does not match the format tag, are normalized as if they were not tagged, as shown in row 4 above.

Single digit values may have a leading zero.

These are the valid delimiters for a date string: "/", "-", "."

Any extraneous non-digit characters appended to a date string will make it invalid as a date, and the whole input will be passed to the text normalizer.

Since VXML handles dates the same way as standard SSML, adding "vxml" to a tag will have no effect (e.g. "[vxml:date=](http://vxmldate=)" will be the same as "date=").

 

### Interpret-as="digits"

Input| Output (en-US)  
---|---  
<say-as interpret-as="digits">781</say-as>| seven eight one  
<say-as interpret-as="digits">5k</say-as>| five k  
  
All digits are spaced out (to be read out separately by text normalizer). Non-digit content is retained.

 

### Interpret-as="number"

Input| Output (en-US)  
---|---  
<say-as interpret-as="number">456100</say-as>| four hundred six thousand one hundred  
<say-as interpret-as="number">52X98</say-as>| fifty-two X ninety-eight  
  
Numbers are processed together rather than separately. Non-digit content is retained.

 

### Interpret-as="ordinal"

Input| Output (en-US)| Output (fr-CA)  
---|---|---  
<say-as interpret-as="ordinal">12th</say-as>| twelfth| douze t h  
<say-as interpret-as="ordinal">12</say-as>| twelfth| douzieme  
<say-as interpret-as="ordinal">12e</say-as>| twelve e| douzieme  
<say-as interpret-as="ordinal">1</say-as>| first| premier OR premiere (depends on gender; finalized in text normalizer)  
<say-as interpret-as="ordinal">1re</say-as>| one r e| premiere  
<say-as interpret-as="ordinal">1 femme</say-as>| one femme| premiere femme  
<say-as interpret-as="ordinal">1 coeur</say-as>| one coeur| premier coeur  
<say-as interpret-as="ordinal">1.5</say-as>| one point five| un virgule cinq  
  
For Spanish (es-US) and Canadian French (fr-CA), the system will hypothesize the most likely gender for ordinals that can have gendered forms (e.g. premier vs. premiere for French). For best results, we suggest inputting a valid ordinal ending with these digits, such as in row 4 above.

If the input contains a valid ordinal ending in that language, it will be retained. If it does not (that is, it's just a bare number), we will turn it into an ordinal. Decimal numbers pass through with no change (see row 7 above).

 

### Interpret-as="spell"

All alphanumeric characters are spaced out and read individually as letters. Any punctuation or whitespace is replaced by the name of that punctuation/space in the language in question.

Input| Output (en-US)| Output (en-GB)| Output (fr-CA)  
---|---|---|---  
<say-as interpret-as="spell">my example</say-as>| M Y space E X A M P L E| M Y space E X A M P L E| M Y espace E X A M P L E  
<say-as interpret-as="spell">cats & dogs</say-as>| C A T S space ampersand space D O G S| C A T S space ampersand space D O G S| C A T S espace et commercial espace D O G S  
<say-as interpret-as="spell">chats & chiens</say-as>| C H A T S space ampersand space C H I E N S| C H A T S space ampersand space C H I E N S| C H A T S espace et commercial espace C H I E N S  
<say-as interpret-as="spell">#</say-as>| pound sign| hash| carre  
  
 

### Interpret-as="telephone"

Input| Output (en-US)| Output (fr-CA)  
---|---|---  
<say-as interpret-as="telephone">(781)771-7777</say-as>| area code seven eight one, seven seven one, seven seven seven seven| indicatif regional sept huit un, sept sept un, sept sept sept sept  
<say-as interpret-as="telephone">781-771-7777, ex. 23</say-as>| area code seven eight one, seven seven one, seven seven seven seven, extension two three| indicatif regional sept huit un, sept sept un, sept sept sept sept, poste deux trois  
<say-as interpret-as="telephone">+1-781-771-7777</say-as>| plus one, seven eight one, seven seven one, seven seven seven seven| plus un, sept huit un, sept sept un, sept sept sept sept  
<say-as interpret-as="telephone">1-800-GET-HELP</say-as>| one eight-hundred g-e-t help| un huit-cents g-e-t help  
<say-as interpret-as="telephone">011-52-55-5080-2000</say-as>| zero one one, five two, five five, five zero eight zero, two zero zero zero| zero un un, cinq deux, cinq cinq, cinq zero huit zero, deux zero zero zero  
<say-as interpret-as="telephone">[sip:1234567@domain.com](http://sip:1234567@domain.com)</say-as>| sip colon one two three four five six seven at domain dot com| sip deux-points un deux trois quatre cinq six sept arobase domain point com  
<say-as interpret-as="telephone">911</say-as>| nine one one| neuf un un  
  
 

A few notes:

  * Currently, any content in the "format" section is deleted.
  * If the number starts with +, we assume it's an international number, and "country code" is inserted before those digits.
  * Adds the words "area code" before any area code that isn't a toll-free number.
  * "800" in toll-free numbers is read out as "eight hundred" instead of "eight zero zero."
  * Numbers are spaced out to be read individually by text normalizer, and commas are added for pauses between number groupings.
  * Allows for extensions after the primary phone number.
  * SIP phone numbers (which tend to look like email addresses) are passed through for the text normalizer to process.
  * The specifics will almost certainly change depending on language/region, as phone number standards differ in every country. The norms used in the es-US version of the say-as interpreter assume that the location is the US or Canada (since both share the "1" country code and the same dialing plan).
  * Allows for alphanumeric phone numbers, such as 1-800-ASK-DOUG. (Phrase predictor phone number handling does not, so if user wants alphanumeric phone number treated as a phone number, use of say-as telephone tag is recommended.) Any alpha characters will be processed using our normal processes for all-uppercase words, which differ from language to language.



 

### Interpret-as="time"

Currently supports time with hours, minutes, and seconds, and the 12-hour or 24-hour clock. No "format" options are currently in place, but most of what they do is already handled by our system. Future improvements should include support for "format" options such as hms12, hms24. Per W3 standard, "wall clock" time is supported, while durations are not.

Input| Output (en-US)| Output (fr-CA)| Output (es-US)  
---|---|---|---  
<say-as interpret-as="time">2:30 a.m.</say-as>| two thirty a-m| deux heures et demi| dos treinta de la mañana  
<say-as interpret-as="time">15:30</say-as>| fifteen thirty| quinze et demi|    
<say-as interpret-as="time">08:20:05</say-as>| eight hours, twenty minutes, and five seconds| huit heures, vingt minutes, et cinq secondes|    
<say-as interpret-as="time">3h22</say-as>| \--| trois heures vingt-deux| \--  
<say-as interpret-as="time">The train departs at 2 p.m.</say-as>| The train departs at two p-m|  |    
The train departs at <say-as interpret-as="time">2 p.m.</say-as>.| The train departs at two p-m.|  |    
  
fr-CA allows h as a separator, as shown in row 4.

Note that the processor consumes final periods, so if you have input such as "The train departs at 2 p.m." it's best to wrap only the time in a say-as tag, keeping your sentence-final punctuation outside the tag (see rows 5 & 6).

  


intermediate

 
