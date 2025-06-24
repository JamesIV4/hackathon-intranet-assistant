42  
  
## Description

* * *

The goal of this page is to provide the reader with an understanding of how the Speech Enablement Group stores, maintains, versions, and deploys its applications.

## Speech Enablement Architecture Implementation Views

* * *

Implementation Views ImplementationViews

ImplementationViews

speech_solutions_main_folder_architecture11

The above view will allow common items such as grammars or global root vxml documents to be housed. It will also contain our document templates, processes, and other methodologies as they pertain to the overall work performed within the team. 

This will use an As-Is reference model meaning that the Customer streams will reference the Speech Solutions main line for the commonly used code. They will use the latest and greatest of that which resides there. An item of importance to note with this is when a customer project is delivered it will have a specific version of the main_systest stream released with it. If the customer decides to come back for further work any items within the customer stream that rely upon those common items MAY have to be updated based on improved or additional functionality.

[Request a new Perforce Stream, Pulse Build, and new Speech Project.](https://confluence.inin.com/display/MediaGroup/Starting+a+New+SSDG+Project#StartingaNewSSDGProject-RequestanewPerforceStream,PulseBuild,andnewSpeechProject.)

## Build / Deployment Process

* * *

This section will be used to outline the build process as well as what occurs with respect to the packages defined within the main stream as well as individual customer streams.

### Versioning

A build process will be developed that will update an VXML, GRXML, and any other text based file we need. It will NOT however include Office type documents. Those will be versioned with respect to the source control revision mechanism. A version table should be used as it is today for updates and those same comments should be used in the submission to perforce.

#### Meta Data within VXML and GRXML 

The items in ALL CAPS will / should be updated via the build process. This will only occur if the VoiceXML File is checked into Perforce, i.e. generated code will not have these updated automatically and frankly cannot have such done due to the current VoiceXML File code generation.

Example: VXML Metadata

VXML Metadata

### Deployment Package Creation

#### //SpeechSolutions Streams - Speech:: project

speech_project.rb

Perforce Location: //speechsolutions/main_systest/pub/resources/ininbuild

**Speech::project [  do ... end ]**

Packages up all files in subdirectories of the application directory into {root}/pub/gen/distrib/<current_date: MMDDYYYY>/[QA|UAT|PROD]_project_.zip.

The UAT version will actually package will actually contain UAT in the name to allow for simultaneous deployment within a production environment if necessary, i.e. UAT = TheNumberDome-UAT.war, PROD = TheNumberDome.war.

All of the options below are truly optional but require the following to be true:

  1.      1. Directory Structure
        1. /pub/resources/APPLICATION_NAME/
        2. 2-design
        3. 3-development/application/bin
     2. 3D file name must match APPLICATION_NAME within directory name, i.e. /pub/resources/TheNumberDome/2-design/TheNumberDome.docm



**Options:**

  *     * **********[ project '_name' ]_  _  
_**********
      * Defaults to name of application directory, i.e. /pub/resources/ <application_name>, /pub/resources/TheNumberDome.
      * Specify a project name if the application directory structure doesn't match what the project name should be, i.e. /pub/resources/ivr_replacement/3-development/Ameren/bin rather than /pub/resources/TheNumberDome/3-development/application/bin.
    * ****[ design_doc_name '_name' ]_****
      * Defaults to ININ if under an InternalProjects or src directory.
      * Specify a design_doc_name using a relative path to the 2-design folder if the path / name differs from the application name
        * For Example:
          * /pub/resources/ivr_replacement/2-design/Residential/IL/Ameren_3D-IL-Residential.docm rather than /pub/resources/TheNumberDome/2-design/TheNumberDome.docm
          * /pub/resources/VoiceBiometricsDemo/2-design/Voice_Bio_Demo_TradeHarbor.vsdm rather than /pub/resources/VoiceBiometricsDemo/2-design/VoiceBiometricsDemo.vsdm
    * **[  include '_paths'_ , 'target_directory in deployment file (war|zip)' ]**  
**  
****NOTE:**  dialog_state.jsp, it's corresponding WEB-INF files (web-qa.xml, web-uat.xml, and web-prod.xml versions are required), and all JavaScript from //speechsolutions/main_systest are copied into the project by default  
  

      * Default include is **/* which means all files within the target directory, i.e. /pub/resources/<application_name>/3-development/application.
      * This option is used to explicitly specify _additional_  files to include (excludes do not work against things explicitly included).
      * Include additional directories from any TIER and add those to the deployment package without having them physically checked in to that location within your stream.
      * There can be one to many of these defined.
    * ****[  exclude '_paths' ]_****
      * Default Exclusions: rakefile* gen gen/**/* bin bin/**/* overrides overrides/**/*
      * If you want to exclude a subdirectory, you'll have to use something like: exclude 'dir', 'dir/**/*'
      * This is due to the Ruby glob rules.
      * See <http://www.ruby-doc.org/core-2.1.1/Dir.html> (the Glob function in particular which lists the matching expressions) and <http://rake.rubyforge.org/Rake/FileList.html> which is what's used to construct the initial file list minus the excluded paths.
    * **[  build_type 'type' **]
      * Allowable values: 'war' | 'zip'
      * Defaults to WAR deployment type
    * **[ enabled']**  
**The purpose of this flag is to allow the usage of the Speech :: project module to create the WAR or ZIP files for the applications where DialogStudio was used to create the application. It is also required if VXML Code generation is desired.  
**
      * Allowable values 'true' | 'false'
      * Defaults to false value if not defined.



Example Usage:

ruby

### SEG Perforce Branches

 

Development/SpeechEnablementGroup/SEG Perforce Streams Webinar.mp4BLOCK
