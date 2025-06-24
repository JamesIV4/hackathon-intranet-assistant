After you have built a voice, it is convenient to record samples so the other people can hear how this voice sounds. I wrote a little script (which I called saverecordings.sh) that uses text2wave to record a set of prompts. This script is at the bottom of this page.  
  
In order to set up the script, you will need to type in what prompts you want, and put them as members of the PROMPTS list. This list is a newline separated list of strings (of course, the "..." is not actually meant to be there). Then, change the variable called VOICE to be the voice you want to record.

After that, you can run the script like:

NOTE: this creates a directory with the same name as the voice. If such a directory already exists (as is often the case if you have already recorded some prompts from that voice) then it will overwrite the wav files contained therein. It is a good practice to rename a directory with voice specific information as soon as it is done recording all prompts. This will not only keep that directory from being overwritten, but it will also remind you what distinguished those wavs from the rest of them. There is also a README file automatically generated in each folder. It is also a good idea to use that file to store remarks about the voice used in the making.

SECOND NOTE:It is possible (likely) that this will throw the following error and fail to create the wav files:

This happened to me the first time I tried it. Look [here](http://developer.berlios.de/bugs/?func=detailbug&bug_id=3542&group_id=3272) for a fix to the problem. I found that I did not have to change text2wave at all (the last patch is unnecessary). Of course, you will need to recompile festival. You will not need to rebuild your voice.

  


* * *

  
saverecordings.sh
