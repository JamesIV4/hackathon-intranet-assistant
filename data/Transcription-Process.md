See also:   
  
# Overview

Transcription process consists of the following steps.

  1. Data collection. From collected logs and audio we have to collect audio files. The minimum information that we need is the list of files for transcription. It is advantageous to have initial guess of spoken text. We usually get this information from logs. Alternatively, we can run offline recognition and get text prediction.
  2. Then from that information we have to generate XML file, that can be used by transcription tool. This XML file is called "manifest". It is good to split data in chunks of size 200-500. Then it is possible to share transcription jobs between several transcribers.
  3. Transcription tool allows to listen files, write/edit transcription, make additional tags (gender, accent), put noise markers.
  4. Transcription is followed by reviewing: listening of transcriptions and double-checking the results. Ideally, each utterance should be verified (reviewed), but exists practice of reviewing each 3rd utterance.
  5. Transcribed data is stoped in XML files (manifests), these files should be converted to CSV file for further use for tuning and training.



# Transcription Tool

Related pages from user manual are shown here: 

## Installation Process

### Installation on STE

You don't have to install anything. Just run few commands

**On machines:**  

  * Transcription Server IND059GRE084.cscp.inin.local 217.218.59.84
  * File Server IND063GFS145.cscp.inin.local 217.218.63.145  

  * Speech Rec/NAR Server   IND059GRE083.cscp.inin.local    217.218.59.83



do this:

  1. In file explorer, go to fol;der "C:\NAR" and run file "TranscriptionTool_FirstRun.bat" (double-click on it).  
The file will do installation. It will copy shortcut for Tramscription Tool on your desktop. It will also run the transcription tool and you will see main transcription window. Now you can close it, installation is done.
  2. **Next time you want to run Transcription Tool, you should click on "Transcription Tool" icon on your Desktop.**
  3. If transcription tool is installed for one user, and **another user on the same machine**  will need to run transcription tool, the new user should do the "Step 1" - see above.
  4. If on some reason, desktop icon has disappeared, you can always repeat "Step 1" - see above.



### Installation on your laptop

Normal process is to get NAR (Nuance Application Reporting) from Nuance download site and install "Transcription Tool".

**But we have prepared an alternativ e process. Follow those steps:**

  1. In file explore open folder: \\\i3files\SEG\Transcription Tool
  2. Download to your computer this file: transcription tool.zip
  3. Extract it to "**C:\** " **(important! follow this step exactly!)** You will have then new folder "NAR" on drive C:\, and you will have full file path "C:\NAR\TranscriptionTool_FirstRun.bat"
  4. In file explorer, go to fol;der "C:\NAR" and run file "TranscriptionTool_FirstRun.bat" (double-click on it).  
The file will do installation. It will copy shortcut for Tramscription Tool on your desktop. It will also run the transcription tool and you will see main transcription window. Now you can close it, installation is done.
  5. **Next time you want to run Transcription Tool, you should click on "Transcription Tool" icon on your Desktop.**
  6. If transcription tool is installed for one user, and **another user on the same machine** will need to run transcription tool, the new user should do the "Step 4" - see above.
  7. If on some reason, desktop icon has disappeared, you can always repeat "Step 4" - see above.



### Training Data

You can also run training on sample data, it is not PCI-sensitive, but still company confidential. Don't share this data to outside ININ.

Here is how to get the data:

  1. In file explorer go to: \\\i3files\SEG\Transcription Tool
  2. Download transcription_samples.zip to your machine
  3. Unzip to C;\
  4. You will get the data on directory: C:\transcription
  5. Manifests are here: C:\transcription\1_new



# How to transcribe

## Transcription Conventions

Copy from  page

The following  section lists the common conventions used when marking up transcriptions:

  * **F1   [n]  General background noise - the recorded utterance consisted of non-speech noise (for example, an click, fire alarm or buzz)**
  * F2  [x]  Significant static, buzzing, line noise
  * F3  [b]  Beep of unknown origin - not DTMF
  * F4  [e]  Echo of our recorded prompt
  * **F5   [c]  the caller made an unintelligible noise such as a cough**
  * F6  [g]  Caller chatter - do transcribe relevant remarks
  * **F7   [q]  Questionable speech (can't understand the caller)**
  * F8  [h]  Caller hang up (must be the last utterance in a call)
  * **F9   [r]  Respiration noises, nose sounds, burps, laughs**
  * **F10   [p]  "side-speech" occurred in the audio (for example, the caller spoke to another person in the room or a TV is playing)**
  * **F11   [z]  signal drop out (for example, a dropout click on a cellular call: "i want check- [z]").  Mark this only if the engine fails to recognize the phrase correctly**
  * **F12   [d]  DTMF sound; dial tone, busy signal**
  * **[u]  the caller made a hesitation in the speech (e.g., "uh checking please")**
  * **[]  speech in foreign language (Spanish speech in English application)**
  * **dash "-": this indicates a clearly heard speech fragment (for example, "-ecking" instead of "checking").  Only mark this when the system fails to recognize the speech fragment correctly.**
  * **\\\   Missing or corrupt audio**
  * **   (empty transcription)  \- speaker doesn't say anything**



## Key shortcuts

**F1 ... F12**   insert noise marker

**Ctrl-H**   (or click Help->Shortcuts for Transcribers)  \- memo for noise marks

**Ctrl-Q**    translate the digits 0 to 9 to words: "a b 123 c d" -> "a b one two three c d")

**Ctrl-Enter  ** Take the whole transcription from combo box. Click on combo box to see more suggestions. This works well for typical phrases, e. g. "i don't know"

**Enter** (in transcription field)    submit transcription. Then tool will go to the next utterance and will start playing.

**Ctrl-S**   save the result

## General rules

  * Use lowercases, even on proper names "john lives in new york"
  * No punctuation marks. Only allowed:
    *  apostrophes: can't don't
    * hyphens: a-ha   (very seldom, e.g. Norvegian group "a-ha")
    * underscores: u_s_a  (if you are not sure, it is better to write spaces rather than underscores. But if suggested utterance has underscores, then keep them, don't replace with spaces)
  * Write "gonna", "wanna" \- if caller says like this. But write "five" even if caller has spoken something like "fav" or "fay".
  * For non-US utterances, use accents: español français portugues
  * Acronyms: separate letters by spaces (or keep underscores if this is what has been recognized): s e g, u s a
  * Write number with words: sixteen, twenty nine
  * Transcribe swear words, if caller says them. Don't mask it, write as is.
  * "o" and "0" (zero spoken as "oh") usually transcribed as "oh".  




## FAQ

  1. **When there is a break in a word (example: "in voice"), what is the best way to transcribe a pause in speech like that?**  
If you can understand that it is "invoice", and especially if it was recognized as "invoice", then transcribe as "invoice".  
If the pause was too long (about 1 second or more), transcribe as "in- -voice". I expect you will do this very very seldom.

  2. **When a person says "dash", should we transcribe that by typing "dash" or "-"?**  
Transcribe "dash". We will make a grammar and add word "dash" into dictionary, so then we can recognize phrases like "one two dash three four". "dash" is a valid spoken word, so transcribe it. And you will use "-" symbol as a mark of cut-off/incomplete word "i want check- [z]" or in combined words like "cut-off" (but this will be very very seldom).

  3. **What would you consider an "irrelevant" call? Should we type what a transcription says if it is obviously irrelevant then complete the transcription with a [g] or should we just type [g] as the transcription only?**  
if it is irrelevant, then transcribe the whole irrelevant part as "[g]".  
If caller says something about the voice system, like "stupid machine" or "it can't understand me" \- then transcribe those phrases.  
If caller says intentionally something irrelevant: "banana", "hello", "hakuna matata", "blah blah blah" \- then transcribe it, that will give us indicator that caller have difficulties with IVR, is annoyed or is saying rubbish to be connected to adviser.  
If caller says something to another person "Paul, stop it", then this is side-speech, transcribe as "[p]".  
If you can't understand what has been said, use "[q]" \- questionable speech. 
  4. **If a word is inaudible but it was recognized as something, what to do? Should we keep transcription or put a noise marker?**  
Don't trust to offered transcription 100%, it is an initial help for you, but imagine, that you don't have it, as if you transcribe from empty string.  
 If caller made some noise, and it was recognized as something, then you have to transcribe it as [q] or maybe [c]. Then we will know, that the noise has been recognized as "agent", and we can take actions.
  5. **If she hears "i don't have it i don't have it", and the system recognized "i don't have it", what to do?**  
Transcribe as "i don't have it i don't have it", then we will have a chance to add this utterance (repeating twice) to the grammar.

  6. **For "Questionable speech (can't understand the caller)", what if part of the audio is understandable and other not understandable? Do we put [q] as the full result, or do we type in the part that is understandable and put [q] just for the non-understandable part?**  
Put [q] for non-understandable part.

  7. **If caller hesitates with "uhm one two three four five", and recognizer got "**one two three four five** " correctly, do we fix the transcription to "[u] **one two three four five** ", or just leave it as is?**  
Transcribe as "[u] one two three four five" if "uhm" is clearly heard. This will be useful for our ISR team, so that they can work on voice activity detector.

  8. **< < dash "-": this indicates a clearly heard speech fragment (for example, "-ecking" instead of "checking"). Only mark this when the system fails to recognize the speech fragment correctly. >>**  
**It says don 't change the transcription unless it was misrecognized.**  
**But the case we just mentioned, you said we should put [u] even if it got it right.**  
**So I 'm a little confused on the rules of when you correct things that were recognized properly.**  
**How about if you hear "place an order <noise>" and system got "place an order", do you leave it alone or modify to "place an order [n]"?**

Well, this is indeed fuzzy.  
I would say, it is not a big issue if you transcribe with extra noise markers or not. We will consider them in only difficult cases.

So, if the recognition was affected by noise markers, definitely transcribe them.  
If the recognition is not affected, then transcribe them if you think they are significant/loud/you heard them clearly.  
If they are quiet/soft - skip them.

The rule "don't put noise markers if that was recognized correctly" is good for our purposes, and that makes transcription process fast.  
But if we want to give data to production team, they may need more noise markers, especially [u] and markers at the start of the utterance. 

  9. **I would think if the transcriber hits submit without any modifications then you can automatically determine that the recognition was correct.**  
**But if we make any edit like putting a noise marker, are you still able to automatically determine that the recognition is correct, or do you need to manually review these?**

Our tuning comparison tool will ignore all noise markers for comparison, no manual work for us.  
Again, for major analysis noise markers will be ignored for comparison recognized vs. transcribed strings.  
Even cut-offs like "-two" will be not considered.

But we will see, for example, that common misrecognition is:  
[n] -> repeat  
[b] -> three  
And so on.

So then we could consider changing sensitivity or changing thresholds.

  10. **And how about caller says "place my order" and recognizer got "place order", and transcriber corrects it as "place my order".   Will you need to manually determine that is a correct recognition?**  


If "place my order" and "place order" are both in grammars, we will see the parsed meaning (out/SWI_meaning), they will be identical, and this will be a match. And we can also correct that with our remapping tool.  
But if "place my order" was not in the grammar, and you transcribe it correctly, we will see that and add that phrase to the grammar.  
So please transcribe all words.  
If it was recognized "place order" but caller has spoken "place orders" (plural)  transcribe as plural "place orders".

 



 

 

# Transcription of PCI data in STE

## Start Transcription Tool

Use thise instruictions to start transcription in STE:

  1. Connect to STE.
  2. We have installed transcription tool on those machines:
     1. Transcription Server     IND059GRE084.cscp.inin.local     217.218.59.84
  3. In directory C:\NAR\bin you will find "Transcription Tool". Create shortcut (don't MOVE!) to it on your Desktop.  
Or you find "Transcription Tool" in installed programs in Metro interface. Press "Win" key for Metro screen. 
  4. Start it.



## Self-management

We want less management in organizing transcriptions, Usually nobody will tell you that you must do this and this. Just follow this process.

 
    
    
    E:.  
    └───transcription  
        └───wellcare  
            ├───1_new  
            ├───2_work  
            │   ├───sergey  
            │   └───eric  
            ├───3_for_review  
            ├───4_reviewed  
            └───backup

 

  1. In STE on drive E: you will see folder "E;\transcription". Go there and find your project, e.g. "wellcare"
  2. In folder "1-new" you will files available for transcription. Take 1-2 files and **move** (not just copy) them to your working folder, e.g. "2_work\sergey".  
You will work with those files, And no one else will take your files and no one will do double work.
  3. Rename those files: add your name to the filename. wellcare_pci_201608_010.trmxml --> wellcare_pci_201608_010**_sergey**.trmxml   . It is necessary for the following steps.
  4. Open transcription tool and do transcriptions.
  5. WHen finished, move your saved manifests to "3_for_review" folder. You can return to step 2 and pick up new files. Or you can do the review.
  6. In "3_for_review" folder, select 1-2 files and move to your working directory. **Don't rename this time.**
  7. Do review: listen to every (in some cases to every 3rd utterance) and verify transcription. Make corrections, if needed.
  8. WHen finished, save changed and move saved files to 4_reviewed folder. Finished with this file. Go to step 2.



 

Moving files ensures, that two people will not do the same work. Be careful, but we have all untranscribed files, so you can't do a lot of harm by accident. Lead SPeech Scientist will take care of data backup and do some minor transcription management.

If you have questions, talk to other transcriber, ask your SpSci and read this fine manual.

# Create transcription manifests

**... EDITING ...**
    
    
    In the following, step-by-step instructions are given for Speech Scientists.  
    # Sample (random selection, files are shuffled before sampling)
    
    
    python i3csvsample.py --in wavs.utd --out ../transcribe/wellcare_pci_201608.utd --field guris --config toTranscribe.csv
    
    
      
    # --in wavs.utd UTD file from logs  
    # --out ../transcribe/wellcare_pci_201608.utd output UTD file  
    # --field guris what filed to use for sampling, can be "dm_name"  
    # --config toTranscribe.csv CSV/UTD file for transcription, must have header.
    
    
     
    
    
     
    
    
    # now generate manifests, they will be generated in the same directrory as UTD file and will use its name as basis
    
    
    python i3csv2trm.py --in ../transcribe/wellcare_pci_201608.utd --split 200 --utt utt_no --call call_no --transcription rawt -- audio e:/data/wellcare/en-us/201608_tuning/rec
    
    
    # --in ../transcribe/wellcare_pci_201608.utd input utd  
    # --split 200 split size  
    # --utt utt_no if you have utt_no field, use it like this, otherwise don't use the parameter  
    # --call call_no if you have call_no field, use it like this, otherwise don't use the parameter  
    # --transcription rawt field that has transriptions  
    # -- audio e:/data/wellcare/en-us/201608_tuning/rec this path (if specified) will be added to all audio file paths. If not specified - then nothing will be changed.
    
    
      
    toTranscribe.csv example:  
    ==============================================   
    maxnum,regex  
    4000,au00000_identifyidmember  
    4000,au00010_identifyidother_d  
    2000,au02000_identifyprovideri  
    800,au02010_identifyidnpi_dm  
    800,au02020_identifyidtin_dm  
    800,au04000_provgetmemberid_d

 

 

 

 

 

 

 

 

# See also

Transcription Tool webinar recording: open folder: \\\i3files\SEG\SEG Internal Team Files\Transcription Training 

 

 
