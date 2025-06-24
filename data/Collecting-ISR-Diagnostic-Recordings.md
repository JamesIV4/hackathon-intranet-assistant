# Overview

The following instructions goes over how to collect diagnostic recordings from customer sites and uploading it for the speech team to analyze. Diagnostic recordings are extremely helpful in not only tuning a customer's speech application but also to help us improve Interaction Speech Recognizer (ISR).

## 1\. Enable ISR Diagnostic Recordings for ISR

To enable ISR diagnostic recordings go to _**Media Servers - > Configuration**_ container in Interaction Administrator and add a property called **" recognizerDiagnosticLog"**. Set the property value to **" 1"**. The property should look as follows:  
 

Enabling diagnostic recordings will record all utterances when using ISR. Make **absolutely** sure that this ok with the customer and we have written consent to do so. If the customer is PCI compliant customer this will probably not be allowed.

 

## 2\. Verify ISR Diagnostic Recordings are Being Created

After setting the property, call into the main system IVR of the CIC server. If ISR is configured correctly for that CIC server you should hear the prompt "Please say the name of the party you would like to call". When the prompt plays go ahead and speak a name and then hang up.  An ISR diagnostic log should have been created at this point along with the utterance recording and played in the CIC server logs folder. Specifically a subfolder called "**_asr_diagnostic_** " will be created that stores diagnostic recordings for each interaction:

Each interaction folder will contain the diagnostic log and recordings:

 

## 3\. Copy the Customer Logs to \\\i3filesarchives

Once permission has been granted to use these recordings from the customer, copy the diagnostic logs to the specific customer subfolder located in [\\\i3filesarchive\SpeechAnalyticsData\ISRCallLogs](file://i3filesarchive/SpeechAnalyticsData/ISRCallLogs)

The naming convention of the sub-directories should be exactly like the logs folder where the **_< date>/asr_diagnostics/<interaction_id>_** should be maintained. For instance:

ISRCallLogs Folder Structure1

 
