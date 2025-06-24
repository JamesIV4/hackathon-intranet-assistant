# Installing and Getting Started With MRCP  
  
## Introduction

These instructions describe how to install an MRCP server and configure it for use with an Interaction Center Platform (xIC). It describes how to install each supported vendor's MRCP server and how to configure IC to communicate with that server. 

## Before You Begin

A typical MRCP installation consists of a dedicated server to run a third party MRCP server. Since MRCP servers are media intensive (speech synthesis, speech recognition, recording etc.) it is recommended that the MRCP server have ample processing speed and physical memory. Also, since audio is streamed to and from the server to xIC using RTP, it is recommended that the MRCP server be in the same subnet and have a high bandwidth connection to the xIC server. The following are other prerequisites to installing:

  * Check the updated list of third party MRCP vendors that are supported. You can do this by going to <http://testlab.inin.com/>.
  * Secure copies of third party MRCP server media. This typically includes the MRCP server installer and installers for the MRCP resources being used. For example, if you are using the MRCP server for speech synthesis a copy of the vendors text to speech engines are needed.
  * Appropriate licenses for the MRCP resources being used. NOTE: Typically the MRCP server itself does not need licenses. The licenses are usually for the actual resource being used (i.e. TTS licenses).



## Step One: Install the 3rd Party MRCP Server.

  * Installing Loquendo Speech Suite
  * Installing Nuance Speech Server



## Step Two: Configure xIC to use the MRCP Server.

  * On the IC server bring up Interaction Administrator.
  * Go to MRCP Servers container under System Configurations.
  * Select Servers and right click on the right pane and select "New..." on the context menu.



  * Enter in the name of the server.
  * In the server configuration enter in the vendor and the SIP address of the MRCP server. **NOTE:** The sip address of the MRCP server typically begins with sip:mresources and it is recommend that MRCP servers for xIC installations use the port 6060 as to not conflict with default ports used by other SIP endpoints.  



  * In the Supported Resources tab make sure Speech Synthesizer resource is selected.  



  * In the Voices tab add all the voices installed for the MRCP server being configured. To add a voice click "Add...".  



  * Once added configure the gender and supported languages of the voice. Click OK to complete the MRCP server configuration.  




## Step Three: Test the Installation.

In the configurations dialog under the MRCP Servers container, you can configure an IC server to use MRCP solely for TTS. To do this you simply check the "Use MRCP for TTS" option in the Configuration tab. Before doing this however, it is advisable to test the MRCP installation to make sure everything is working correctly. To do this you can use a custom handler that has a "Play String Extended" toolstep in it. To have the toolstep use MRCP for playing simply add "MRCP" as the first optional parameters under the input tab in the tool.  

