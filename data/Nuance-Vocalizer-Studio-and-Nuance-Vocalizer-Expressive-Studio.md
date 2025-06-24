## Description

There have been a number of questions recently surrounding the ordering, licensing, and installation of Vocalizer Studio / Vocalizer Expressive Studio. The following is what I've been able to gather from Robert Hazinski our Technical Account Manager from Nuance. 

**What does a customer need to order / obtain Nuance Vocalizer Studio or Nuance Vocalizer Expressive Studio?**  

Cheryl could you enlighten us? Or maybe Mark. 

**What is the difference between Nuance Vocalizer Studio (VS) and Nuance Vocalizer Expressive Studio 1.1 - 1.3(VES)?** 

VS only works with Nuance Vocalizer 5.x

VES only works with Nuance Vocalizer 6.x and up 

**What type of Licensing do I need to use either VS or VES?**  

Neither of these are actual licensed products meaning that they come with the purchase of Vocalizer ports. 

However, 

  * For Playback ONLY you need an instance of Nuance License Manager, local or remote, with available Vocalizer licenses.
  * To SAVE the TTS as a wave file for use as a prompt if a customer is using a specific TTS voice in their IVR and they wanted to use it as "brand voice" for static recordings in their Music On Hold, Announcements and other areas outside their IVR.
    * Vocalizer Offline license is required
      * Download a new license with the feature "vestudio_wavegen" in the license
      * Merge with other licenses
  * $10,000 per language / per year
    * EACH language requires a license, i.e. 3 languages (en-US, fr-CA, es-MX) equates to $30,000 per year.



**What Features can I use in Vocalizer Studio if I don 't want to save a wave file?**

  

ALL of the above. J

**How do I install VS or VES?**

  1. Install Nuance License Manager
     1. Optional if the sites production instance will be used.
     2. Install Nuance Vocalizer 5.x / 6.x as applicable
     3. Install Nuance Voices as applicable
     4. If Nuance Vocalizer 5.x was installed proceed to step 5 else skip ahead to step 6.
     5. VS
        1. Download the VStudio_1.3.0_Common.zip and the VStudio_1_CLC_Package_1.3.0.zip from the ININSpeech Product page from within the appropriate TTS subfolders.
        2. Extract the contents of those zip files to their own folders on your desktop.
        3. Run the Vocalizer Studio install first followed by the Common Language Components.
        4. VES
           1. Download the Nuance_VEStudio_1-3-0.zip from ININSpeech Product page or this link if you're internal.
           2. Extract the contents into %SystemDrive%/Program Files (x86)/Nuance
           3. Create a shortcut to the desktop for VocalizerExpressiveStudio.exe



**Is Prompt Sculptor a better solution than recording Professional Prompts?**

NO. But, what it does get you is the ability to create prompts at ANY time and use them anywhere. Professional Prompts are normally licensed for use only in telephony applications.

Also, the quality of the saved TTS output is directly proportional to the skills of the user creating it. Prompt Sculptor requires training and just because you get the application doesn't mean you know how to create amazing prompts with it.
