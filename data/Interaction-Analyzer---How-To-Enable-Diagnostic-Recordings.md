For developers and support engineers to troubleshoot the audio processing engine of Interaction Analyzer, it is critical to reproduce the audio in internal testing. Recordings obtained through applications such as "Recorder" are less useful, because these recordings are typically post-processed after they are captured, including encryption, and compression.

The best approach is to enable "diagnostic recordings" that capture the audio exactly as it was processed by the Media Server.

### Configuration for Media Server

  1. Open the web config, and examine the Parameters tab.
  2. Ensure that "Http Trace Log Access" is set to "AnyConnection". It is not enabled by default.
  3. This parameter is required to enable HTTP fetching of the diagnostic recordings from the IC server.



### Configuration for Telephony Server

  1. Open Interaction Administrator, and go to the configuration for the server.



  1. Open the tab for "Telephony Parameters" and ensure that "Keyword Spotting Diagnostic Recording" and "Fetch Diagnostic Recordings From Media Server" are both checked.



### Diagnostic Recording Location

If the preceding steps are followed, all diagnostic recordings of keyword spotting sessions will be fetched from the Media Server, and stored in the folder:

﻿<IC>/logs/diagnostics

Where <IC> is the IC server installation folder.
