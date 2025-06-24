This is an attempt to categorize ASR test errors. Please modify and improve the page.

S.No.| Error Category| Details| Symptom| Action  
---|---|---|---|---  
1| VAD issues| 

  *     1. VAD unable to pick-up speech of low volume
    2. VAD treating long pauses as speech

| 

    1. Bulk deletions
    2. Bulk insertions

| 

    1. Try increasing/decreasing VAD sensitivity for the language

  
2| Grammar issues| 

    1. Out-of-grammar utterances

| 

    1. Hypothesis words are acoustically similar to reference, but are incorrect
    2. Completely wrong hypothesis
    3. Words hypothesized due to other misrecognized words, because hypothesis has to the follow grammar

| 

    1. Check if the reference is in grammar. If not,  change the grammar or remove the test utterance

  
3| Lexical issues|  | 

    1. Specific words consistently substituted
    2. Audio prepared by concatenating a single word from the database has different pronunciation than its lexical entry/entries

| 

    1. Change the lexical entry/entries
    2. Provide alternate pronunciation(s)
    3. Model frequent word-pairs as a single word

  
4| Transcription errors|  | 

    1. High confidence score for misrecognized word
    2. No specific reason for misrecognition

| 

    1. Make note and give feedback

  
5| Errors due to mispronunciation| 

    1. Fast speaking
    2. Wrongly uttered words
    3. Speaking with a tone / song-like
    4. Words ended with reduced volume, as whispers, accompanying breath signal

| 

    1. No specific reason for misrecognition

| 

    1. Remove the files from training and possibly testing

  
6| Audible short-lived noises| 

    1. Breath events
    2. Sudden sounds

| 

    1. Insertions acoustically dissimilar to the neighbouring words in reference

| 

    1. Remove the files from training and testing
    2. Check if the original transcription has a noise tag, if not, give feedback. Make sure such files are removed from the database.
    3. Try increasing VAD's sensitivity

  
7| Background noise| 

    1. Environmental noise
    2. Background music / TV / babble

| 

    1. No specific reason for misrecognition

| 

    1. If too noisy, remove the utterance from training and testing

  
8| Text normalization issue|  | 

    1. Reference doesn't match hypothesis due to spelling mistake / upper ASCII characters

| 

    1. Correct the reference / grammar

  
9| Partial signal missing / signal clipping| 

    1. Initial part of signal missing as the person started speaking ahead of the prompt
    2. Final signal portion missing
    3. Signal clipped

| 

    1. Initial words misrecognized

| 

    1. Remove the files from training and testing

  
10| Reverberation issue|  | 

    1. Bulk deletions
    2. Completely wrong hypothesis

| 

    1. If too reverberated, remove the files from training and testing

  
11| Uncategorized errors|  | 

    1. No specific reason for misrecognition

| 

    1. Try increasing the decoding beamwidth


