This page exists to help us plan MSCA support case automation key,summary,type,created,updated,due,assignee,reporter,priority,status,resolutionInteractive Intelligencea6f784b9-ef5d-3d60-bca5-6d0a3771dd27IONMEDIA-3649. Additions welcome!

 

#| Item| Assigned| Completed| SCR| Notes  
---|---|---|---|---|---  
1.| continue documentation of support case process| ,|  |  | 

  * how to name new fingerprints (conventions)
  * PureConnect vs. PureCloud
  * old .wav style vs. new .sasf style
  * common problems that can arise in support cases
    * prompt isn't in expected language
    * prompt is truncated (either at beginning or end)
    * etc.

  
2.| progress checklist| |  |  | Add automated checklist of some type that helps you know when you're finished (make sure you do step A, step B, step B, etc.).  
3.| automate searching for likely candidates for new fingerprints| |  |  | Particularly useful for cases where there are tens of thousands of audio files. Rivarol has a working version in Matlab. Long-term, we'd prefer a non-Matlab version for licensing reasons.

  * Look into porting it to Python.
  * Have someone with a license kick it off and output the results to a shared folder. Send email notification when it's done.

  
4.| update rake to incorporate new fingerprints into the model automatically| ,|  |  | IDEA: instead of copying stuff to a local Case### directory, add new fingerprints to build directory and rake model builder to update. (If so, some of the items below would not be necessary anymore.) Should be flexible enough to allow working from local machine or network location.

  * If NOT using rake, a batch script that could do the following would simplify matters:
    * Ensure necessary directories exist on local machine.
      * parent folder for the support case
      * diagnostics subfolder
      * new fingerprint subfolder
      * existing fingerprint subfolder
      * combined fingerprint subfolder
      * i3ca subfolder with langid subfolder
    * Copy/generate config file and update its settings (langID, base file, etc.).
    * Copy files from support server to local machine (and i3devfiles?).
    * Copy existing fingerprints to local machine.
    * Copy recording model file.

  
5.| automate model building steps| , |  |  | IDEA: instead of copying stuff to a local Case### directory, add new fingerprints to build directory and rake to update. (If so, some of the items below would not be necessary anymore.)

  * ~~script to build model~~
  * ~~copy updated recording model file from diagnostics folder to i3ca/langID folder~~
  * ~~delete anything that already exists in unvalidated folder (if it's already been generated)~~
  * ~~script to run i3ca_sim~~

  
6.| make it easier to name new fingerprints in fewer steps|  |  |  | For example, if you're creating recording.ring.es.WelcomeToAcme.3.wav, you need to know 1) if there are existing fingerprints with the same - or similar - name, and if no, what number to start with for the new one. This isn't difficult, it just requires looking in the right place. We may be able to simplify this process.  
7.| Include analyzer reset information (timing) in SASF diagnostics| |  |  | Allows us to reproduce the same behavior as production since pre-connect speech.machine and speech.person events cause the analzyer to be reset as well as line connect events (when the person picks up the phone).  This is important if behavior could be different right after line connect in prod versus i3ca_sim as well as being able to avoid reviewing false positive speech.machine and speech.person events during pre-connect (e.g., during music ringback), allowing us to focus on the real machine or person that comes post connect.  I found that there is code for this already, and I've found some diagnostics that contain the information but very few (need to see why).
