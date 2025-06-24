Key differences from Nuance Recognizer 9 

Installing Nuance Recognizer 10 (NR10) is quite a bit different than installing Nuance Recognizer 9 (NR9), so special attention to the installation instructions is necessary.  There are two main changes that make the installation procedure different:

  1. NR10 no longer supports a "native" integration .  For NR9, the ININ ASR Nuance Recognizer service actually hosted the NR9 ASR engine in process, but that is no longer supported by Nuance.  Instead, MRCP must be used. (IC support for MRCP ASR was added to 4.0 SU3, and is not available in 3.0.)
  2. The NR10 architecture is more complex than NR9 and requires separate processes for the MRCP server (Nuance Speech Server, NSS), and the ASR engine (NR10).  The NR10 engine is now a 64 bit process, which allows it to utilize more memory, but NSS is still a 32 bit process.



# Version Compatibility

Planning is required to ensure that the correct versions are being used.  Nuance imposes constraints on which versions of its software can be installed on the same machine.  The versioning constraints apply to the ASR engine, the TTS engine, the MRCP engine, as well as the ASR language packs and TTS voices.    (Note that multiple versions of the same product cannot be installed on the same server; NR9 and NR10 cannot be installed on the same server, just like NSS5 and NSS6 cannot be installed on the same server.)

MRCP Engine (NSS) | ASR Engine (NR) | TTS Engine (Vocalizer) | ASR Language |  TTS Voice  
---|---|---|---|---  
 NSS 6.2 |  NR 10.2 | Vocalizer 5.7 | 10*| 5.2 or 5.7**  
Vocalizer 6.0| 6.0  
 NSS 5.2|  NR 9.0| Vocalizer 5.2 | 9 | 5.2   
  
Notes:

*The language packs for NR9 are not compatible with NR10.  However, Nuance offers language packs with NR10 that use the same models as NR9.  New applications should use the new NR10 models to get the accuracy improvements available in NR10, but the NR9 models can be used to avoid retuning applications.

** Vocalizer 5.7 supports the exact same voices that were used with Vocalizer 5.2, and those are the voices that customers should use.  Vocalizer 5.7 also introduces support for new and improved voices, but the memory and CPU requirements make them inappropriate for most telephony applications.

# Installing Nuance Recognizer 10 

These instructions assume a clean server with respect to Nuance software.  Multiple versions of the same Nuance product cannot be installed on the same server, so older versions of any products must be uninstalled before installing newer versions (i.e. uninstall NR9 before installing NR10 and uninstall NSS 5 before installing NSS 6).  Note the version compatibility described above and in Nuance's Release Notes.  Early service packs of NR 10.2 are not compatible with later service packs of NSS 6.2 and vice versa.  The Nuance Release Notes for each product list which service packs of other products are supported.

The media for the installation can usually be found internally on i3files (<file://i3files/I3CDImages/_Nuance/>) or for customers on from the inin speech site (<http://www.inin.com/products/ININspeech>). **NOTE:** Make sure to restart the server every time the install prompts for one.

You can ignore the troubleshooting tips as you go along, but if the NR10 installation isn't working after you complete the steps, it's best to start at the troubleshooting steps for #1 and work your way down again.  This procedure helps isolate what issues exist and usually provide more helpful error messages.

1\. Install [Nuance License Manager](file://i3files/I3CDImages/_Nuance/Core%20Services/License%20Manager)

  * Run and complete the Nuance License Manager Setup.  (\\\i3files\I3CDImages\\_Nuance\Core Services\License Manager, Version 11.7 was used while writing these instructions.)
  * Apply the license file. (A temp license can be found at  [file://i3files/I3CDImages/_Nuance/Recognition and Verification/Nuance Recognizer/Recognizer 10/License](file://i3files/I3CDImages/_Nuance/Recognition and Verification/Nuance Recognizer/Recognizer 10/License), but it should be copied to the local machine.  Nuance License Manager does not appear to support UNC file paths for the license file.) 
    * Run LMTools (Start->Programs->Nuance->License Manager->Licensing Tools.)
    * On "Config Services" tab, Browse for the "Path to the license file"
    * Save Service.
    * Restart Nuance Licensing Service in the services control panel.
  * Troubleshooting tip: Verify that license manager is listening to correct port (i.e. netstat -a and look for port 27000).



2\. Install [Nuance Recognizer 10](file://I3FILES/I3CDImages/_Nuance/Recognition and Verification/Nuance Recognizer/Recognizer 10)

  * \\\i3files\I3CDImages\\_Nuance\Recognition and Verification\Nuance Recognizer\Recognizer 10
  * Run and complete the Nuance Recognizer 10.2 x86_64 Setup. Restart if prompted. _This installs Nuance Recognizer Server (NRS), which is the process that hosts the NR10 ASR engine.  Other utilities are also installed._
  * Install at least one NR10 [language pack](file://I3FILES/I3CDImages/_Nuance/Recognition and Verification/Nuance Recognizer/Recognizer 10/Languages).  Choose at least one language, then run and complete the Setup wizard.



3\. Configure Nuance Recognizer licensing **(New step  compared to NR9)**

  * _Note: With NR9, this step was often unnecessary  because NR9 had a high default value, and setting the value too high would not prevent the service from starting because Nuance would check out fewer licenses if needed.  However, NR10 will fail to start up if it can't check out the configured number of licenses.  With a clean installation, NRS will try to check out 8 licenses and fail to start if there are only 4 available.  Similarly, if you paid for 20 licenses but leave the default setting, you won't be able to use all the licenses you've paid for._
  * Open Baseline.xml from the Nuance Recognizer config folder (ex. \Program Files\Nuance\Recognizer\config).
  * Find "swirec_license_ports" and "swiep_license_ports", and make sure the that <value> is set correctly based on the license being used.  For example, the temp license only has 4 ports, so the value node should become <value>4</value> for both "swirec_license_ports" and "swiep_license_ports".
  * Troubleshooting tip: Verify that the NR10 engine, language pack, and licensing have been properly installed and configured.  With NSS and NRS not running (description for running them is in later steps), open a command prompt, navigate to Program Files\Nuance\Recognizer\samples\swirec_sample (depending on installation directory chosen), and run the command "SWIrecSample.exe".  After a delay, many screens of text should be written by the sample app.  (Some warnings are normal, but critical errors must be corrected.)  Towards the end, you should find a successful recognition result.  The line starts with "XML result is = <?xml version='1.0'?><result>" followed by recognition result that contains "<input mode="dtmf">6 1 7 4 2 8 4 4 4 4</input>".  If the command exits early and doesn't print a recognition result, there is a configuration problem.  The sample app should print a helpful message if it encounters an error.  (Ex. no languages installed, could not check out licenses, etc.)  Note:  SWIrecSample requires the Microsoft Visual C++ 2005 SP1 Redistributable Package. You may get an error like "The application has failed to start because its side-by-side configuration is incorrect" if not installed.  Either skip this troubleshooting step, or install the Redistributable Package and security update from <http://www.microsoft.com/en-us/download/details.aspx?id=5638> and <http://www.microsoft.com/en-us/download/details.aspx?id=26347>.



4. Start Nuance Recognition Server **(New step  compared to NR9)**

  * _Note: This step wasn't necessary with NR9 because the ASR engine was hosted either in NSS, or more commonly inside the ININ Nuance Recognizer Server  process.  Neither of these options are possible with NR10 - it must be a separate process, and additional configuration is required to run that process._
  * There are a couple different ways to run the Nuance Recognition Server (NRS) process, and you must pick one. 
    * The Nuance Recognition Server (NRS) process, can be run from the command line.  (The Nuance installer updates the PATH so you can run these commands from anywhere.) 
      * To run with the default number of threads (currently 4): `nuance-server -servlet nrs -port 8200` (works fine for a small, development test server, but not recommended for anything larger than about three simultaneous calls)

      * Or, to run with a custom number of threads: `nuance-server -servlet nrs -port 8200 -nthreads <val>`; See Nuance documentation for details, but 1.2 times the number of simultaneous ASR channels is generally recommended for <val>.  Ex. 96 is a good number for 80 channels of ASR.

      * Some warnings are normal, but the program should not exit or return to the command prompt unless a critical error occurred (which must be fixed).
    * While future versions may install NRS as a Windows service, currently the service must be installed manually if the command line interface isn't adequate.  Note that the service and command line version of NRS cannot be run simultaneously.

      * From the command line, cd to C:\Program Files\Nuance\Recognizer\Recognizer Service\amd64\bin (or wherever nrs-win-service-init.exe was installed), and run: 
        * ``nrs-win-service-init.exe -i nrs-win-service.exe -servlet nrs -port 8200 -nthreads <val>``

        * See Nuance documentation for details, but 1.2 times the number of simultaneous ASR channels is generally recommended for <val>.  Ex. 96 is a good number for 80 channels of ASR.
        * Installing the service is a little hit or miss, and the command doesn't display helpful messages or even write a message to indicate success or failure.  Sometimes restarting the server is necessary before the command will work.
      * nrs-win-service-init.exe installs a new Windows service:  Nuance Recognition Service.  This service can be removed with the command: `nrs-win-service-init -uf`



5\. Install [Nuance Speech Server 6](file://I3FILES/I3CDImages/_Nuance/MRCP/Nuance Speech Server 6) **(New step  compared to NR9)**

  * _Note: This step wasn't necessary with NR9 because the ASR engine was hosted inside the ININ Nuance Recognizer Server process, which is no longer possible for NR10._
  * These instructions assume you're not installing Vocalizer on this server.  If you are installing Vocalizer on this server, complete that installation now to avoid the hassle of changing NSS configuration files after Vocalizer is installed. 
  * If you need to install Vocalizer after installing Nuance Speech Server 6.2, see instructions below.
  * Run and complete the Nuance Speech Server 6.2 Setup. Restart if prompted.
  * If this MRCP server has a total of more than 96 recognizer and vocalizer licenses, you must adjust the configuration.
    * Open NSSserver.cfg (by default located in ProgramFiles\Nuance\Speech Server\Server\config\\).
    * Change "server.mrcp2.sip.maxCountOfSession" to a value at least as high as the total Vocalizer and Recognizer ports.  For example, set to 100 or higher if you have 80 Recognizer ports and 20 Vocalizer ports.
    * Restart Nuance Speech Server service for change to take effect if not making additional changes to NSSserver.cfg right now.
  * **Optional** : Change the SIP port that NSS uses.  If this is a dedicated ASR/TTS server, the default port of 5060 is fine.  If this is running on the IC server (not recommended for anything but a small Dev environment), 5060 will need to be used by other software.  In the past, we've recommended that the TTS MRCP port be changed to 6060.  Although this can be done for ASR, it usually isn't necessary and needlessly makes the installation process more complicated. 
    * Open NSSserver.cfg (by default located in Program Files\Nuance\Speech Server\Server\config\\)
    * Change "server.mrcp2.sip.transport.tcp.port", "server.mrcp2.sip.transport.udp.port", and "server.mrcp2.sip.transport.tls.port" if desired.
    * Restart Nuance Speech Server service for settings to take effect.



6\. Install ININ MRCP ASR server

  * MrcpASRServer_SU3.MSI was released with [4.0 SU3](file://i3devfiles/Releases/Interaction Center/4.0/SU03/2013-02-05-CL773612-1598/products/install_images/release).
  * Run and complete the ININ MRCP ASR Setup.
    * If you changed the SIP port of NSS, you should enter the port number during installation.  The default is 5060.
  * Run the MSP for the current SU of MrcpASRServer.
  * Use the Web config page ([http://localhost:8120](http://localhost:8120,) by default) to add the IC server(s).



7\. Startup order

  * This is the order of dependencies. The software listed on top must be running before the software below it can work properly.
    * Nuance License Manager service
    * Nuance Recognition Server (either from a command line or as a service, but not both)
    * Nuance Speech Server service
    * ININ MRCP ASR Server service



## Logs

The default logging location for NR 10, NSS 6 and licensing is C:\ProgramData\Nuance\Enterprise\system\diagnosticLogs.  (It used to be that each program would write a log to separate folders.)  The command for NRS (either from the command line or when registering the service) can specify a different directory by adding a -DDiagFileName argument.  Not specifying this parameter is like specifying -DDiagFileName=**%NUANCE_DATA_DIR%/system/diagnosticLogs/nrs.log**

## KB article

Support created a KB article at <https://extranet.inin.com/Support/Pages/KB-Details.aspx?EntryID=Q138042670904846> for installing NR10.  Those details may vary slightly from these instructions.  The KB article removes extraneous details and may be kept more up to date based on the results of installations in the field and feedback from Nuance.

## Installing Vocalizer After Nuance Speech Server

Some configuration changes are required when installing Vocalizer after Nuance Speech Server has already been installed. For some reason, installing Vocalizer after the causes Nuance Recognizer to stop working properly. In order to restore functionality to Nuance Recognizer 10, do the following:

  1. In NSSserver.cfg un-comment the following lines
     * #server.mrcp2.resource.0.dll VXIString nrsspeechrecog
     * #server.mrcp2.resource.0.name VXIString Nuance Open Speech Recognizer
     * #server.mrcp2.resource.0.type VXIString speechrecog dtmfrecog
     * #server.mrcp2.resource.0.cfgprefix VXIString server.mrcp2.osrspeechrecog.  
 
  2. Restart the Nuance Speech Server service.  
  
 



 
