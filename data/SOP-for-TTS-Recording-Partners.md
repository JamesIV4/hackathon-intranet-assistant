This document is designed to clearly articulate Interactive Intelligence's needs for TTS recording projects, and specifically note places where these differ from typical GM Voices procedures. All stakeholders should sign off on an up-to-date version of this document at the beginning of each new TTS language project. Doing so should help ensure consistency from project to project, and the document can be a single point-of-reference for the linguists and engineers during the course of each project.

### Stakeholders:

GM Voices Account Manager for Interactive Intelligence: _Rachel Hembree ([rhembree@gmvoices.com](mailto:rhembree@gmvoices.com))  
_

GM Voices Lead Sound Engineer: _Michael Hayhurst ([mhayhurst@gmvoices.com](mailto:mhayhurst@gmvoices.com))  
_

Interactive Intelligence liaison to GM Voices: _Jon McCain ([jon.mccain@inin.com](mailto:jon.mccain@inin.com))  
_

Interactive Intelligence lead linguist: _Scott Randal ([scott.randal@inin.com](mailto:scott.randal@inin.com) Skype: scottranda1)  
_

Interactive Intelligence project linguist:_Emma Ehrhardt ([emma.ehrhardt@inin.com](mailto:emma.ehrhardt@inin.com) Skype: emma.ehrhardt), Rich Campbell ([rich.campbell@inin.com](mailto:rich.campbell@inin.com) Skype: rich.campbell1234), or Linda Lanz ([linda.lanz@inin.com](mailto:linda.lanz@inin.com) Skype: lindalanz1),_ depending on project

## Project Workflow for a TTS Voice

Voice Talent Recording Samples

  * ININ requests voice talent samples for a new language.
  * GMV provides samples of available voice talent (checking availability for TTS), and project quote.
  * ININ provides GMV with a Purchase Order number for the recording project, which will be referenced on the billing invoice.
  * ININ narrows down the voice talents to 2 candidates to audition.



Studio Samples

  * GMV provides 'studio samples' of both audition candidates for ININ to evaluate  

    * A 30-second sample recording is made (some generic IVR prompts are sufficient), using the same recording conditions that will be used for the full recordings.
    * Rationale: Since ININ records at a higher fidelity than the original samples, it is necessary to confirm the talent's studio can meet the technical quality requirements.
  * If the initial quality is not sufficient, GMV adjusts studio setup as necessary until ININ approves new samples.



Voice Talent 'Audition', for Top 2 Candidates

  * ININ provides prompt script to GMV, approximately 150 sentences.
  * GMV schedules recording sessions for both audition candidates.
  * Recording sessions
    * Note: The same procedures apply here as for the full recordings.
    * Also note: Make sure to document setup details (mic placement, etc), since these recordings will be merged with the full recordings, and those may not take place for some time.
  * GMV does post-processing & delivery of prompts.
  * ININ builds prototype TTS voices with each audition talent, and selects one voice talent to record the full project.



Full Recording Project

  * ININ notifies GMV which voice talent was selected for full project recordings.
  * ININ provides prompt recording script to GMV.
  * GMV schedules recording sessions.
  * Recording sessions
  * GMV does post-processing & delivery of prompts.
  * ININ identifies any prompts that need to be rerecorded.
  * GMV sends the project invoice to accountspayable@inin.com, referencing the Purchase Order number, and with "ININ Accounts Payable" in the "Bill to" box.



## Scheduling Recording Sessions

  * ININ will direct each session, via Skype.
  * The SAME engineer will be assigned to every session (within a language).
  * If a recording session must be scheduled on short notice (less than 24 hrs), the availability of the ININ linguists who will be involved in the session MUST be confirmed.



## Recording Sessions

#### Setup Details

  * ININ Direction via Skype
  * The SAME engineer will be assigned to every session (within a language).
  * Voice talents will use the same microphone and equipment setup as Jill (en-US) or Jayde (es-US). e.g. Neumann U87 microphone, etc.
  * All technical specs will be set up exactly the same each session, i.e, microphone placement etc.
  * Full Spectrum recording (originally recorded at 48k).



#### Procedure

  * ININ Guidelines for Voice Talent
    * If Voice Talent misspeaks, she needs to restart the prompt from the beginning (not pick up in the middle).
    * If the Voice Talent is fighting a cold, reschedule the recording session.  Nasality cannot reliability be detected over Skype, though it shows up in recordings.  Better to reschedule than rerecord later.
  * At the beginning of each recording session, playback 5-10 prompts from an earlier session for Voice Talent, to ensure voice talent consistency (especially regarding rate of speech).
  * The Engineer will carefully make note of any wording that is changed during the sessions, and GMV will provide this information as processed recordings are delivered.
  * After recording begins for each session, GMV to send ININ a segment (5-10 prompts) of audio for quick evaluation.  The session will then continue once ININ has verified everything is acceptable.
  * After the first day of recordings for the full corpus, GMV to send ININ the full raw audio buffer overnight, to be verified by ININ before next recording session.



## Post-processing & Delivery of Audio

#### Timeline

  * ININ should communicate to GMV as soon as feasible if there are any priority concerns with delivery timeline for recordings.
  * GMV provides ININ expected delivery timeline once recording sessions begin.



#### Audio Editing

  * Do not remove prompt-internal pauses (ININ wants to keep the original length), otherwise (I believe) standard GMV procedures are used.



#### Deliverables

  * Audio Formats for all prompts
    * 48-k Client
    * 16-k
    * mu-law
  * Any changes to prompt wording from the sessions



#### Prompt Naming

  * **Project**
    * <Vendor>_<locale code>_<voice talent name>
      * **Example:  **GMV_fr-CA_Hilorie


  * **Deliverable**
    * **ZIP**
      * <Vendor>_<locale code>_<voice talent name>_<domain>_<prompt ID range>.zip
        * **Example:  **GMV_fr-CA_Hilorie_ivr_001-500.zip
    * **Prompt Naming**
      * <domain>_<prompt ID>.wav
        * **Example:** ivr_0001.wav
      * **Prompt Naming of Alternates**
        * When an alternate is introduced, it needs to be named consistently with the original prompt naming.
          * <prompt name>_ALT.wav



 
