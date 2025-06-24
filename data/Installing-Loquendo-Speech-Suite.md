# Installing Loquendo Speech Suite MRCP

## Introduction

Loquendo Speech Suite is Loquendo's MRCP server offering used with Loquendo TTS (LTTS) and Loquendo ASR (LASR). Currently Loquendo Speech Suite can only be used for Speech Synthesis (LTTS) when used with xIC. Using MRCP with Loquendo TTS is an ideal solution for offloading LTTS onto another server since Loquendo's SAPI integration for TTS does not support an off server configuration.

## Details

To install Loquendo Speech Suite for use with LTTS it is recommend that the following steps be taken in the order specified:

1\. Install Loquendo Text To Speech Engine (for 7.x and above): The media for the installation can usually be found internally on i3files (file://i3files/I3CDImages/_Loquendo\\) or for customers on Loquendo's customer area at their website (http://www.loquendo.com/customerarea/index.asp\\).

  * Install the LTTS Engine (Full Version).
  * Install LTTS languages.
  * Install LTTS Voices (Telephony Versions).
  * Install the LTTS licenses: 
    * Run the Loquendo License Manager. Generate a license request.
    * Go to Loquendo's customer area on their website (http://www.loquendo.com/customerarea/index.asp\\).
    * Log in and locate the customer's list of Product Identification Keys (PIKs). Select the PIK for the LTTS product being installed.
    * Click on licensing. Cut and paste the license request in license request text box.
    * Click Get License and download the license executable.
    * Run the executable on the LTTS machine.
  * Test the installation by running the control panel speech applet, selecting a loquendo voice for TTS, and previewing the voice.



2\. Install Loquendo Speech Suite (LSS):

**NOTE:** Loquendo Speech Suite uses SNMP for configuration. Please make sure SNMP services have been installed on the server before hand. Also make sure that after the LSS installation that the appropriate LoquendoAdmin community and respective traps have been automatically configured with SNMP. Look at the installation document attachment below for more information. 

3\. Configure Loquendo Speech Suite:

  * To confiure LSS first make sure the Loquendo Management Context service is running.
  * Go to Start->Program Files->Loquendo->Loquendo Speech Server->Management Console.
  * If the local server has not been added then add it.



Server Name: Local  
IP Address: 127.0.0.1  
Community: LoquendoAdmin  
Port: 161

Under the advanced MRCP configurations the following configurations are recommended for use with xIC:

Configuration | Setting | Description  
---|---|---  
createNewResource  |  Enabled  |    
apConfiguration - apParametersTable  |   |    
Provider RTPProvider: type  |  realtime  |    
Provider RTPProvider: enableSilenceSupression  |  true  |    
Provider RTPProvider: g711InPacketSize  |  160  |    
Provider RTPProvider: g711OutPacketSize  |  160  |    
Provider RTPProvider: g711PacketDuration  |  20  |    
Ports  |   |    
sipPort  |  6060  |  
