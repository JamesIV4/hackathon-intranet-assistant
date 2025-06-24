## How to add/remove processes.

Adding or removing active interpreter processes requires working through the ProcessLauncher object.  Inside the vxml_manager, the ProcessLauncher object is a singleton, so it can be accessed like this:

    process_launcher::ProcessLauncher_t::instance()

### ProcessLauncher::add_process()  


To add a process, the ProcessLauncher::add_process() method needs to be called.  Here is its documentation:

  


Here is an example of its use (stolen from the commented out Service:TestAddProcess() method in vxml_manager\service.cpp):

### ProcessLauncher::remove_process()  


To remove a process, the ProcessLauncher::remove_process() method needs to be called.  Here is its documentation:

  


Here is an example of its use (stolen from the commented out Service:TestRemoveProcess() method in vxml_manager\service.cpp):

  


## How to communicate with VoiceXML interpreters.

Communicating with the VoiceXML interpreters requires working the VxmlIpcServer object, which is inside the Service object.  (My thought is that the HTTP host will be started up inside the Service object).  In the Service object, it can be accessed through the m_vxml_IpcServerPtr member variable.

### VxmlIpcServer::request_info()

To get general information from a VoiceXML interpreter, the VxmlIpcServer::request_info() method must be called.  Here is its documentation:

 

Here is an example of its use (stolen from the commented out Service:TestGetInfo() method in vxml_manager\service.cpp):

 

### VxmlIpcServer::request_status()

To get the current status from a VoiceXML interpreter, the VxmlIpcServer::request_info() method must be called.  Here is its documentation:

 

Here is an example of its use (stolen from the commented out Service:TestGetStatus() method in vxml_manager\service.cpp):

 

 

### VxmlIpcServer::set_accept_sessions()

To tell a VoiceXML interpreter whether or not to accept new sessions, VxmlIpcServer::set_accept_sessions() method must be called.  Here is its documentation:

 

Here is an example of its use (stolen from the commented out Service:TestGetInfo() method in vxml_manager\service.cpp):

 

### VxmlIpcServer::set_configuration()

To set the configuration for a VoiceXML interpreter, VxmlIpcServer::set_configuration() method must be called.  Here is its documentation:

 

Here is an example of its use (stolen from the commented out Service:TestSetConfig() method in vxml_manager\service.cpp):

 

 

## Accessing vxml_manager configuration.

Accessing the vxml_manager configuration parameters requires working through the ConfigManager object.  Inside the vxml_manager, the ConfigManager object is a singleton, so it can be accessed like this:

    vxml_manager::ConfigManager_t::instance()

  


This object will allow the configuration parameters in the registry to be read and written.  Here is a list of the available methods:

# To-Dos

  * Authentication
    * add UI login page
    * Add response generator to HTTP server to check for token before passing the request to the API
    * Generate access tokens from /api/v1/token
    * Add SecurityContext to HTTP server for HTTPS support
  * Validate parameter values (check for correct type)
  * Ensure that API error responses print a message for the new vxmlmanager.restapiresources error codes  




 
