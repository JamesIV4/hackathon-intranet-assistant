none3

# Overview

This is the proposed design for a REST API for the Media Server. It will provide similar functionality to the web config in a script-friendly manner, which will be useful for both CaaS and Testing. It will be bundled in with the recording retrieval server in order to make use of i3core's i3inet and will authenticate using mutual TLS and/or digest authentication, configurable through the web config.

These requirements are branched from the API detailed in .

# SCRs

Feature| SCR| Description  
---|---|---  
Project| falseInteractive Intelligencea6f784b9-ef5d-3d60-bca5-6d0a3771dd27DP-1525|    
Umbrella SCR| falseInteractive Intelligencea6f784b9-ef5d-3d60-bca5-6d0a3771dd27IC-128499|    
Initial API version| falseInteractive Intelligencea6f784b9-ef5d-3d60-bca5-6d0a3771dd27IC-126064|    
Turn API on and off through the web config| falseInteractive Intelligencea6f784b9-ef5d-3d60-bca5-6d0a3771dd27IC-129385|    
Digest authentication| falsekey,summary,type,created,updated,due,assignee,reporter,priority,status,resolutionInteractive Intelligencea6f784b9-ef5d-3d60-bca5-6d0a3771dd27IC-129660|    
  
# Requirements

BLOCKNumber| Description| Detail| Priority  
---|---|---|---  
R1| The user shall be able to activate and deactivate the media server.|  | Must Have  
R2| The user shall be able to query the deactivation status, including a view of the command servers that still have active resources.|  | Must Have  
R3| The user shall be able to add, remove, and set media server properties.|  | Must Have  
R4| The user shall be able to add and remove command servers.|  | Must Have  
R5| The user shall be able to query properties.|  | Should Have  
R6| The user shall be able to query statistics about the audio engines.|  | Should Have  
R7| The user shall be able to add, remove, set, and query properties about the command servers.|  | Could Have  
R8| All resources shall support HEAD requests where GET is supported.|  | Could Have  
  
# Configuration

By default, the REST API is disabled. It can be enabled using the Administration page in the web config. Before enabling the REST API, you must set a username and password. This configuration is stored in the registry under the keys RestApiEnabled, RestApiLoginName, and RestApiLoginPassword. If the registry keys for the credentials are empty or deleted, the REST API will disable itself.

Currently, the REST API is a part of the Recording Retrieval Server, which runs on port 8102 by default.  The Media Server parameters RecordingHttpsRequired and RecordingHttpsMutualAuth therefore affect the REST API by requiring HTTPS and mutual authentication respectively.  It is strongly recommended that if the REST API is enabled, RecordingHttpsRequired should be set to true.

# Methods

## Activation and Deactivation

### /api/v1/server/deactivate (PUT)

honeydewPUT /api/v1/server/deactivategraydarkgreen

Begins the deactivation process. If already deactivated or in the process of deactivating, no change occurs.

#### Request

* * *

##### Request body

None

#### Response

* * *

##### 200 OK

Field Name| Type| Description| Notes  
---|---|---|---  
deactivationStatus| string| "deactivating" or "deactivated"| The new status of the server. Should not be "activated" because that would indicate the deactivation didn't work.  
Example: PUT /api/v1/server/deactivatejstrue

### /api/v1/server/activate (PUT)

honeydewPUT /api/v1/server/activatedarkgreen

If the server is in the process of deactivating, cancels deactivation; if completely deactivated, re-activates. If already activated, no change occurs.

#### Request

* * *

##### Request body

None

#### Response

##### 200 OK

Field Name| Type| Description| Notes  
---|---|---|---  
deactivationStatus| string| "activated"| The new status of the server. Should not be "deactivated" or "deactivating" because that would indicate the activation didn't work.  
Example: PUT /api/v1/server/deactivatejstrue

### /api/v1/server/deactivationstatus (GET)

##### Parameters

None

azureGET /api/v1/server/deactivationstatussteelblue

Returns the deactivation status, which is either "deactivating", "deactivated", or "activated". If the status is "deactivating", also returns a list of command servers with the number of resources they each have left.

#### Request

* * *

##### Request body

None

#### Response

* * *

##### 200 OK

Returned on success.

Response Payload:

Field Name| Type| Description| Notes  
---|---|---|---  
deactivationStatus| string| "deactivating", "deactivated", or "activated"|    
commandServers[]| array of | nonempty only if the status is "deactivating"|    
Example: GET /api/v1/server/deactivationstatusjstrue

## Command Servers

### /api/v1/commandservers (GET, POST)

##### Parameters

None

azureGET /api/v1/commandserverssteelblue

Get a list of all the command servers.

#### Request

* * *

##### Request body

None

#### Response

* * *

##### 200 OK

Response payload:

Field Name| Type| Description  
---|---|---  
commandServers[]| array of |    
Example: GET https://<mediaserveruri>/api/v1/commandserversjstruehoneydewPOST /api/v1/commandserversdarkgreen

Add a command server to the media server. The media server will have to be approved on the IC server before it is allowed to establish a regular connection to the IC server.

#### Request

* * *

##### Request body

Field Name| Type| Description| Notes  
---|---|---|---  
notifierHost| string| Notifier's hostname| Optional; Omit or leave empty for connection to localhost  
icUserId| string| Username to log into the IC server|    
icPassword| string| Password to log into the IC server|    
acceptSessions| bool| If true, the media server will accept sessions from this command server| Optional; Default is true  
copyPropertiesFromId| int| Numerical ID of the command server to copy properties from| Optional  
  
 

#### Response

* * *

##### 201 Created

Includes the location in the header.

Response Payload:

A single  representing the newly created Command Server, with additional  information.

Example: POST https://<mediaserveruri>/api/v1/commandserversjstrue

Response body:

None

##### 400 Bad Request

Returned when there is something wrong with the request body.

### /api/v1/commandservers/{id} (GET, PATCH, DELETE)

##### Parameters

Field Name| Type| Description| Notes  
---|---|---|---  
id| int| Numerical ID of the command server|    
**Optional Query Parameters**  
force| bool| If true, delete the command server even if there are sessions still active. Default is false. Accepts "true" or "1" for a true bool value.| For DELETE only  
azureGET /api/v1/commandservers/{id}steelblue

Get a command server given an ID.

#### Request

* * *

##### Request body

None

#### Response

* * *

##### 200 OK

Response Payload:

A single 

Example: GET https://<mediaserveruri>/api/v1/commandservers/1jstrue

##### 404 Not Found

Returned when there is no command server with the specified ID.

honeydewPATCH /api/v1/commandservers/{id}darkgreen

Modify a command server. Currently can only be used to set accept-sessions.

#### Request

* * *

##### Request body

Field Name| Type| Description| Notes  
---|---|---|---  
acceptSessions| bool| If true, the media server will accept sessions from this command server|    
  
#### Response

* * *

##### 200 OK

The new state of the command server as a 

##### 400 Bad Request

Returned when there is something wrong with the request body.

##### 404 Not Found

Returned when there is no command server with the specified ID.

mistyroseDELETE /api/v1/commandservers/{id}maroon

Remove a command server from the media server.

#### Request

* * *

##### Request body

None

#### Response

* * *

##### 204 No Content

Response body

None

##### 404 Not Found

Returned when there is no command server with the specified ID.

##### 409 Conflict

Returned if the "force" query parameter is false or missing, and there are still active sessions on this command server.

### /api/v1/commandservers/{id}/certificate (GET)

##### Parameters

Field Name| Type| Description| Notes  
---|---|---|---  
id| int| Numerical ID of the command server|    
azureGET /api/v1/commandservers/{id}/certificatesteelblue

Get command server certificate information given an ID.

#### Request

* * *

##### Request body

None

#### Response

* * *

##### 200 OK

Response Payload:

Certificate information from the command server with the specified ID:

**Field Name**| **Type**| **Description**  
---|---|---  
id| int| Media Server's numerical ID for this command server  
notifierHost| string| URI to access this command server's notifier  
certificate| |    
  
##### 404 Not Found

Returned when there is no command server with the specified ID or no certificate information could be found.

GET https://<mediaserveruri>/api/v1/server/commandservers/10/certificatejstrue

### /api/v1/commandservers/{id}/properties (GET, PATCH, PUT)

##### Parameters

Field Name| Type| Description| Notes  
---|---|---|---  
id| int| Numerical ID of the command server|    
  
Refer to the similar .

### /api/v1/commandservers/{id}/properties/{property-name} (GET, PUT, DELETE)

##### Parameters

Field Name| Type| Description| Notes  
---|---|---|---  
id| int| Numerical ID of the command server|    
  
Refer to the similar .

## Media Server Configuration and Statistics

### /api/v1/server/parameters (GET, PATCH, PUT)

##### Parameters

None

azureGET /api/v1/server/parameterssteelblueGet the current parameters of the media server.  


#### Request

* * *

##### Request body

None

#### Response

* * *

##### 200 OK

Response Payload:

Returns the current state of all the parameters on the server as a list of .

Example: GET /api/v1/server/parametersjstruehoneydewPATCH /api/v1/server/parametersdarkgreen

Set configuration parameters for the media server.

#### Request

* * *

##### Request body

A list of . Request contains all of the parameters to set. Any omitted parameters will not be changed.

Example: PATCH /api/v1/server/parametersjstrue

#### Response

* * *

##### 200 OK

Returns the current state of all the parameters on the server as a list of .

Example: PATCH /api/v1/server/parametersjstrue

##### 400 Bad Request

Returned when there is something wrong with the request body due to invalid syntax, an invalid parameter name, or an invalid value.

lightyellowPUT /api/v1/server/parametersdarkgoldenrod

Overwrite the parameters for the media server.

#### Request

* * *

Request body

A list of . Request contains all of the parameters to set. Any omitted properties will be given a default value.

#### Response

* * *

##### 200 OK

Returns the current state of all the parameters on the server as a list of .

##### 400 Bad Request

Returned when there is something wrong with the request body due to invalid syntax, an invalid parameter name, or an invalid value.

### /api/v1/server/parameters/{parameter-name} (GET, PUT)

##### Parameters

Field Name| Type| Description| Notes  
---|---|---|---  
parameter-name| string| name of a valid parameter|    
azureGET /api/v1/server/parameters/{parameter-name}steelblue

Get the parameter value.

#### Request

* * *

##### Request body

None

#### Response

* * *

##### 200 OK

Response Payload:

Field Name| Type| Description| Notes  
---|---|---|---  
value| string or string[]| The current value of the parameter|    
  
##### 404 Not Found

Returned when the parameter name is invalid.

lightyellowPUT /api/v1/server/parameters/{parameter-name}darkgoldenrod

Overwrite the parameter value.

#### Request

* * *

##### Request body

Field Name| Type| Description| Notes  
---|---|---|---  
value| string or string[]| The value to be set|    
Example: PUT /api/v1/server/parameters/AsrWorkerMaxWorkRatiojstrue

#### Response

* * *

##### 200 OK

Response Payload:

Field Name| Type| Description| Notes  
---|---|---|---  
value| string or string[]| The current value of the parameter|    
  
##### 400 Bad Request

Returned when there is something wrong with the request body or the parameter name is invalid.

### /api/v1/server/properties (GET, PATCH, PUT)

##### Parameters

None

azureGET /api/v1/server/propertiessteelblue

Get properties for the media server.

#### Request

* * *

##### Request body

None

#### Response

* * *

##### 200 OK

Response Payload:

A list of . Response contains the current property values.

Example: GET /api/v1/server/propertiesjstruehoneydewPATCH /api/v1/server/propertiesdarkgreen

Set properties for the media server.

#### Request

* * *

Request body

A list of . Request contains all of the properties to set. If a property does not yet exist, it will be created. Any omitted properties will not be changed or deleted. To delete a property, give it a null value.

Example: PATCH /api/v1/server/propertiesjstrue

#### Response

* * *

##### 200 OK

Response Payload:

Field Name| Type| Description| Notes  
---|---|---|---  
value| string or string[]| The current value of the parameter|    
Example: PATCH /api/v1/server/propertiesjstrue

##### 400 Bad Request

Returned when there is something wrong with the request body due to invalid syntax, an invalid property name, or an invalid value.

lightyellowPUT /api/v1/server/propertiesdarkgoldenrod

Overwrite the properties for the media server.

#### Request

* * *

##### Request body

A list of . Request contains all of the properties to set. Any omitted properties will be deleted.

#### Response

* * *

##### 200 OK

Response Payload:

Response contains the current property values.

##### 400 Bad Request

Returned when there is something wrong with the request body due to invalid syntax, an invalid property name, or an invalid value.

### /api/v1/server/properties/{property-name} (GET, PUT, DELETE)

##### Parameters

Field Name| Type| Description| Notes  
---|---|---|---  
property-name| string| name of a valid property|    
azureGET /api/v1/server/properties/{property-name}steelblue

Get the property value if it exists.

#### Request

* * *

##### Request body

None

#### Response

* * *

##### 200 OK

Response Payload:

Field Name| Type| Description| Notes  
---|---|---|---  
value| string or string[]| The current value of the property|    
  
##### 404 Not Found

Returned if the property name does not exist.

lightyellowPUT /api/v1/server/properties/{property-name}darkgoldenrod

Overwrite the property value or create the property.

#### Request

* * *

##### Request body

Field Name| Type| Description| Notes  
---|---|---|---  
value| string or string[]| The value to be set|    
Example: PUT /api/v1/server/parameters/Test3jstrue

#### Response

* * *

##### 200 OK, 201 Created

Response Payload:

Field Name| Type| Description| Notes  
---|---|---|---  
value| string or string[]| The value after being set|    
Example: PUT /api/v1/server/parameters/Test3jstrue

##### 400 Bad Request

Returned when there is something wrong with the request body or the property name is invalid (i.e. contains unacceptable characters).

mistyroseDELETE /api/v1/server/properties/property-namemaroon

Delete the property.

#### Request

* * *

##### Request body

None

#### Response

* * *

##### 204 No Content

Response Payload:

None

##### 404 Not Found

Returned when the property name does not exist.

 

### /api/v1/server/enginestatus (GET)

##### Parameters

Field Name| Type| Description| Notes  
---|---|---|---  
includeasr| bool| include the "asrStatistics" field| true, false, 1, 0 accepted. Default is false if not included.  
azureGET /api/v1/server/enginestatussteelblue

Get statistics about the media engines and ASR.

#### Request

* * *

##### Request body

None

#### Response

* * *

##### 200 OK

Response Payload:

Field Name| Type| Description| Notes  
---|---|---|---  
audioengines[]| Array of audioengine statistics| Field Name| Type| Description| Notes  
---|---|---|---  
index| int|  |    
threadId| string (hex number)|  |    
cpuId| int|  |    
location| string|  |    
currentLoad| double| Percentage (0.0 to 100.0) or "n/a"|    
averageLoad| double| Percentage (0.0 to 100.0), 30s moving average or "n/a"|    
graphs| int| Number of active graphs or "n/a"|    
elements| int| Number of active elements or "n/a"|    
 |    
avgCurrentLoad| Percentage (0.0 to 100.0) or "n/a"|  |    
avgAverageLoad| Percentage (0.0 to 100.0), 30s moving average or "n/a"|  |    
totalGraphs| Total number of active graphs or "n/a"|  |    
totalElements| Total number of active elements or "n/a"|  |    
asrStatistics| Object containing ASR statistics ("n/a" for each if the value cannot be retrieved):| Field Name| Type| Description| Notes  
---|---|---|---  
currentASRWorkerThreads| int|  |    
maxASRWorkerThreads| int|  |    
activeRecoTasks| int|  |    
activeASRSearchJobs| int|  |    
avgASRSearchJobs| double|  |    
avgWorkRatio| double|  |    
maxCompletionDelay| int|  |    
avgCompletionDelay| int|  |    
minSearchSpeed| double|  |    
maxSearchSpeed| double|  |    
avgSearchSpeed| double|  |    
Included if and only if the includeasr parameter is true|    
Example: GET /api/v1/server/enginestatus?includeasr=1jstrue

 

### /api/v1/server/about (GET)

azureGET /api/v1/server/aboutsteelblue

Get general information about the media server.

#### Request

* * *

##### Request body

None

#### Response

* * *

##### 200 OK

Response Payload:

Field Name| Type| Description| Notes  
---|---|---|---  
machineName| string| Name of the machine that the mediaserver is running on|    
machineUptime| string| Duration that media server has been running|    
ipAddressLocal| string| Single IP address or comma-separated IP addresses|    
licenseType| string| Unlicensed, Development, or Production|    
productVersion| string| e.g. CIC 2015 R1|    
fileVersion| string| The internal build version for the Interaction Media Server files| Optional  
specialBuild| string| The internal build process identifier that generated the files forInteraction Media Server| Optional  
privateBuild| string|  | Optional  
hotfix| string| The latest Service Update that has been applied to this InteractionMedia Server| Optional  
hotfixVersion| string|  | Optional  
Example: GET /api/v1/server/aboutjstrue

 

# Types

## CommandServerInfo

Field Name| Type| Description  
---|---|---  
id| int| Media Server's numerical ID for this command server  
notifierHost| string| Host name for this command server's notifier  
icServerName| string| Name of IC server to which command server is connected (empty if not connected)  
activeResources| int| Number of active resources on this command server; -1 if unknown  
status| string| Status of the command server  
details| string| Details about the command server's status  
clientId| string (GUID)| Unique identifier of the client API instance (empty if not connected)  
recordingRescueId| string (GUID)| IC server rescue ID  
acceptSessionsStatus| bool| True if the media server can currently accept sessions from this command server  
acceptSessions| bool| True if the media server is configured to accept sessions from this command server  
cpuCapacity| string| Logical capacity of server (frequency of CPUs multiplied by number of CPUs)  
  
## Parameters and Properties

Parameters on the Media Server must always be set. If they are not specified in a PUT request, they will be set to a default value. Custom parameters are not allowed.

Properties may or may not be set. If a property is not set, it is considered deleted. Custom properties are allowed.

In terms of REST API requests and responses, parameters and properties are name-value pairs, where the value is a string or an array of strings. The value may have restrictions on range and format, depending on the parameter or property. For a full list of parameters and properties and their types, consult the Media Server Technical Reference.

Only the following characters are allowed in property names: :.$-_0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ

Parameter and Property names are case-sensitive. Be careful that, for example, if you're trying to edit the property "NotifierDscpValue", specifying "notifierdscpvalue" will create a property called "notifierdscpvalue" instead.

 

### Special Formats

Type| Accept| Output (if different)| Notes  
---|---|---|---  
String| valid JSON strings, numbers, true, false, or null| valid JSON strings|    
Boolean| true, false, "true", "false", 0, 1| "true", "false"|    
Integer| 123, "123", etc| "123"| Range restrictions may apply.  
Number| 1.5, "1.5", etc| "1.5"| Range restrictions may apply  
OneOf| A string that matches one of the multiple choice values|  |    
Directory| A string containing a directory path or the friendly name of a network interface on the server|  |    
Network Interface| A string containing "Any" or|  |    
Port Range| "16384-32767", "16384,32767", or array of similar| "16384-32767"|    
DSCP Value| an Integer from 0 to 63 inclusive| "46", etc|    
IP Address| "127.0.0.1", "2001:db8:85a3:0:0:8a2e:370:7334", etc.|  |    
IP Address Type| One of: "all", "IP4", "IP6", "IP4IP6"|  |    
CPU Mask| array of Boolean, where the first position represents CPU 0, etc.|  |    
  
 

## Certificate info

Field Name| Type| Description  
---|---|---  
certSerialNumber| string|    
issuer| Distinguished Name object:| Field Name| Type| Description  
---|---|---  
organization| string|    
organizationalUnit| string|    
commonName| string|    
   
subject| Distinguished Name object|    
  
 

# Using the API

Requests that contain a body MUST specify the Content-Type header as "application/json". The API will return a 400 error if this header doesn't match or is omitted. The Content-Type header can be excluded if the request body is empty.

URIs are case-sensitive.

## Sample Powershell Script

powershell

 

# HTTP Status Codes

  * 200 OK - Response to a successful request that returns a body.
  * 201 Created - Response to a POST that results in a creation. May include a Location header.
  * 204 No Content - Response to a successful request that does not return a body (POST, PUT, DELETE)
  * 400 Bad Request - Something went wrong in the body of the request, such as an invalid parameter value
  * 401 Unauthorized - Authentication failed
  * 404 Not Found - When a non-existent resource is requested, such as an invalid command server ID
  * 405 Method Not Allowed - When an HTTP method is being requested that is not supported for the specified resource.
  * 409 Conflict - When a command server DELETE cannot be completed.



# Error Messages

Returned in the body of 400 and 404 responses.

## Format

Field Name| Type| Description| Notes  
---|---|---|---  
status| int| Status code; matches the HTTP status code of the response|    
message| string| user-friendly message|    
messageWithParams| string| (Optional) Message with placeholders for parameters|    
messageParams| string| (Optional) Object containing a list of parameters for the user message|    
code| string| Error code (see below)|    
  
## Codes

Name| Description  
---|---  
error.restresourcelib| Generic error code.  
error.restresourcelib.resource.invalid| Something is wrong with the request URI.  
error.restresourcelib.request.invalid| Something is wrong with the request body.  
error.restresourcelib.request.field.missing| A required field is missing from the request body.  
error.restresourcelib.request.field.notRecognized| A field in the request body is unrecognized.  
error.restresourcelib.request.field.invalidValue| A field in the request body has a value that is of the wrong type, out of range, or could not be parsed.  
  
## Example

js

 

 

# Troubleshooting FAQ

### Why am I getting connection errors (closed connection, handshake failure, SSL auth failed) when sending a request with the correct credentials?

You probably have mutual authentication enabled and don't have certificates set up correctly.

In Powershell:

Powershell symptomspowershellChrome symptomsFirefox symptomsFirefox symptomsBLOCK

 

Running the REST API under mutual authentication is untested and therefore not officially supported because of the difficulty of using mutual authentication with a self-signed certificate chain.

 
