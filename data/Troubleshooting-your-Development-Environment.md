## Description

* * *

At times you may run into the situation as I often have where in performing some task you have 'hosed' your development environment. Most recently it was the installation of a ruby gem to my local environment. Once that gem was added to the build system I wasn't able to 'cb' into my workspaces because the //tools/main_systest area had been updated with the new gem. When 'cb' attempted to download / install it during the 'update/check' that occurs on the tools workspace when 'cb'ing' into a codebase it failed. This page outlines tasks that can be performed to help fix your workspace.

## Issues and Possible Solutions

* * *

### When I 'cb' into a codebase the tools update fails!

Solution:

  1. Force a tools update by running the following within a command window.
  2. buildupdate tools-main --force



### When I call my CIC Server I get a fast busy or it disconnects immediately.

Things to Check:

  * #### Ensure the Interaction Center Service is running

    * The Interaction Center Service takes longer to start than the allowed time by Windows. So starting it from the Services Control Panel will always yield the warning message stating that the service is taking longer to start than Windows allows. Merely, acknowledge the message and go get a coffee. It will be up and going when you get back.
    * If starting it manually like this doesn't work feel free to open the TSServer.ininlog, as that is often the source of failed starts, and search on errors and warnings. Then contact the team if you still need help.
  * #### Ensure the ININ Media Server Service is running

    * If starting it manually like this doesn't work feel free to open the ininmediaserver.ininlog and search on errors and warnings. Then contact the team if you still need help.
  * #### Media Server License has expired

    * To determine if this is the problem open a web browser and go to <https://localhost> logging in with the password of admin / 1234.
    * If the license has expired a message in a bold red font will tell you such.
    * To update the license follow this guide:  
_Note: There may be a link on the main page that takes you here... I just didn't have a Media Server in an expired state for a screenshot._  

    * Obtain a new development license from here 
      * Select the biggest license as it will only use whatever cores are available. This allows the addition of cores without having to change the license.



### My call connects but I don't hear anything.

  * #### Ensure the ININ VoiceXML Interpreter Service is running

    * If it is already running
      * Open a web browser and navigate to <http://localhost:8090> and login to the configuration page using the default credentials admin / 1234.  

    * Refresh the page after the service restarts
      * If it still will not start email the team for further assistance.
    * When / Why does this happen?
      * The configuration that our development servers have is such that the ININ VoiceXML Server is running on the same server as the Interaction Center service. This is not recommended for production but is okay in a small development environment. With this configuration comes the issue described above regarding the Windows Service timeout. Since the two services both reside on the server and do not have a dependency on one another the ININ VoiceXML Server service will start prior to the Interaction Center Service. When it starts and the IC Server isn't ready it marks the connection as down and doesn't retry. SCR [IC-127922](http://devjira.i3domain.inin.com/browse/IC-127922) exists for this behavior as the ININ VoiceXML Server should at some point try and reconnect.
  * #### Text to Speech Engine is failing

    * Are you using Nuance Vocalizer 6 and MRCP for your TTS needs?
      * Is the 'Use MRCP for TTS' option checked?
        * Open Interaction Administrator and navigate to the System -> MRCP Servers Node  

        * Double-click on Configuration and ensure the checkbox is enabled  

      * Is the MRCP Server defined online?
        * Select the Servers node below the MRCP Servers Parent node and a list of configured MRCP servers will be shown.  

        * Make sure that server is online and can be pinged from the IC Server
      * Is the Nuance License expired?
        * Log on to the server hosting Nuance and open the Nuance License Tools application  

        * Click the Config Services Tab and take note of the value in the 'Path to the license file' field  

        * Open that file and look for the expiration date as shown in the example below  
  

          * If it is expired you can acquire a new development license here
            * Nuance Vocalizer 6 : 
            * Nuance Vocalizer 5.7 : 
          * If the machine is also running Nuance Recognizer that license will likely need to be updated as well.
            * Nuance Recognizer 10 : 
          * If both are running on the machine you'll need to merge those two licenses. Use the following KB article to guide you through the process, <https://my.inin.com/Products/Pages/KB-Details.aspx?EntryID=Q135050014100993>.
        * Once you've updated the license use the following Knowledge Base article to guide you through adding it 



 

 
