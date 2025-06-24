Although MRCP ASR support isn't available until 4.0 SU3, some customers may need to start testing the MRCP ASR integration before SU3 is released and before a site's CIC server is upgraded to SU3. In particular, Nuance Recognizer 10 (NR10) requires MRCP, and some customers may need to start testing NR10 as soon as possible.

Since the ININ MRCP ASR component is an off server installation, a customer can start testing the MRCP integration from an SU2 CIC server. The CIC installer for SU2 does not add the MRCP EIM, so additional configuration is required compared to SU3.

## IC server set up

Starting in SU3, the MRCP EIM is installed on the IC server, and these steps are already taken care of.

  1. Obtain the SU2 MRCP EIM. (For now, \\\userfiles\users\Steven.Stark\public\RecoEIMMrcp_SU2) Copy RecoEIMMrcpU.dll and RecoEIMMrcpU.pdb to the IC Server. The installer will place them in I3\IC\Server\, but they can be used from any location. The path is configured in step 3.
  2. Start dseditu (ex. from the command line). Note that the following strings are case sensitive and must be copied exactly as they appear below, omitting the surrounding quotation marks. 
     * Go to Production/$Server/Recognition/ASR Engines/
     * Add a new entry (Entry->Add Entry) and name it "Mrcp" with an object class "RecoASREngine". (No attributes need to be entered; IA should be used to configure any settings after finishing these steps.)
     * With Mrcp highlighted on the left, add three more entries (with no attributes): 
       * Name="Preloaded Grammars", Class="RecoPreloadedGrammars"
       * Name="Properties", Class="RecoProperties"
       * Name="Servers", Class="RecoASRServers"
  3. Mrcp should show up in Interaction Administrator (IA) under the Recognition container in System Configuration. If IA was already running, it may need to be closed and restarted for the EIM to show up. Note: The IC server must be licensed for MRCP ASR in order to use the EIM. 
     * With Recognition/Mrcp selected in IA, double click Configuration. Check Enabled, and set the path to the EIM. (The path used in step 1.)



## MRCP server set up

On the MRCP Server run MrcpASRServer_SU3.msi.

## Configuration

The basic configuration for MRCP ASR works the same way as the other ININ ASR servers. Once the ININ MRCP ASR Server is installed and running, open the server's web configuration page (by default, on port 8120). Connect the ASR server to the IC server using the same process as the other ININ ASR server web configuration pages. (Config->Servers->Add Server) If the third party MRCP server is listening for SIP on port 5060 and uses TCP, no additional configuration should be needed. Otherwise, the Config->Mrcp Server page allows the SIP Address, SIP Protocol, and other settings to be configured.
