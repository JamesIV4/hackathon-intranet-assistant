## Overview

[Aumtech](http://www.aumtech.com/) provides an [MRCP Connector](http://www.aumtech.com/WhitePapers/MRCP_Connector_Overview.pdf) for Microsoft Office Server 2007 Speech Server (OCS) to be able to utilize its Speech Recognition and TTS functionality. The following page will document our findings when using the MRCP Connector with our MRCP ASR Server.

Aumtech uses [Microsoft's Unified Communications Managed API 2.0 Core SDK ](http://msdn.microsoft.com/en-us/library/dd253340\(v=office.13\).aspx) to support ASR.

## Installation

Aumtech connector install is unconventional and is run using a windows bat file instead of a windows installer. The install and documentation can be found here: \\\i3files\I3CDImages_Aumtech\connectorPkg.20120224\

### Notes/Issues

  * The Aumtech MRCP connector shows up as a generic "MRCPService" in the services control panel. There is no way to configure service log on during installation so it always uses the LocalSystem account.
  * The installer will not let you configure which drive nor folder location the connector is installed in.



## Configuration

Configuration of the connector is done using a config file in the C:\Program Files\Aumtech\ArcMrcpConnector\conf folder called **_.TEL.cfg_**.

### Notes/Issues

  * The configuration file has configurations that are artifacts of previous incarnations and are not used (SIP_MS2007IP=172.19.23.49, SIP_MS2007Port=5060).
  * No configuration for HTTP caching which leads us to believe it does not cache.



## Functionality

### Notes/Issues

  * No documentation in general. The only documentation provided is the one for the install.



### Initial BFT Findings

  * Returned 409 error code to SET-PARAMS request. Additional investigation will be needed to determine why the request fails and what workaround is most appropriate
  * Appears that the STOP request is not supported, which cause us to fail if there is DTMF input or a noinput timeout.



## Performance

### Initial BFT Findings

  * Binary caching does not seem to be effectively implemented. Using a large names grammar, there is a delay of several seconds before the grammar can be used for each session.


