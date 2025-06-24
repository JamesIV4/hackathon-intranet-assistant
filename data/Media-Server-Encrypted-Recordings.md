# Encrypted Recording support in Media Server

## Overview

Since its inception, the Media Server has always been able to record calls. This feature is arguable one of the Media Server's strengths. In the next iteration the following features will be added that should help streamline call recordings in xIC:

  * **Audio Format Support per Recording** : The Media Server can record a call and transcode it directly into a specific wave format. Currently this is controlled on a per media server basis and is configured using the web config. Part of this change would allow Interaction Recorder/Tools to specify the audio format to use for individual call recordings.
  * **Encryption Support** : Currently, the Media Server does not support writing to an SASF wave data format. Part of this is because there have been no way to communicate encryption parameters to the Media Server from IR. Part of this change is to allow IR to specify encryption parameters for a call recording and have the Media Server write directly into a SASF wave format.
  * **Automatic Level Support** : While recording the call the Media Server can apply an automatic level control on the audio so that the audio has consistent energy throughout the call.



IR server is the primary client for these new features. Currently, IR will do both transcoding and encryption after the call recording has been created using the Compression Manager . With these new features transcoding/encryption will be done as the call is being recorded on the Media Server so there will be no need for any post processing.

## Major Features and Requirements

  * Use Media Server for encrypted recordings.
  * Use Media Server for client (adHoc) and workgroup recordings.
  * Support on-demand fetching of recordings from the Media Server using HTTP/HTTPS.
  * Support different audio formats for the recording (Will allow bypassing compression on the IC server).
  * Remove IR server's dependence on Compression Manager for encryption/compression.



## Design

Several components/subsystems in IC may have to change to accommodate the new Record Call functionality using the media server. This section will document which components are being researched and any changes that may have to be as a result.

### TS API Changes

A new TSAPI call has been added for Encrypted Call Recordings. The new API is a port from the current  API. It has been improved with the following features:

  * and  have been encapsulated in its own class. This will allow extensibility for future changes to the API.
  * The ION serializer is used for sending the request to . This will allow for forward and backward compatibility for new versions of this API call.
  * New Recording parameters have been added for MIME type, Automatic Level Control, and Crypto suite and key.
  * For Media Server recordings an HTTP URI will be returned with the results that can be used to access that recording on the Media Server.



The new API call is as follows:

### IP and Tool Changes

#### Record Call

The Record Call tool will now use the new TSAPI:: API. This change includes being able to download the recording from the Media Server if an HTTP URI is being returned for the recording URI.

##### Migration to the New Version

The Record Call tool will be migrated to a 3.0 version with the following new fields:

  * **Mime Type** (Media Server only): The audio format to record the audio to. Default is empty which defaults to the format specified on the media server.
  * **Automatic Level Control** (Media Server only): Whether ALC should be applied to the audio. Default is false.


