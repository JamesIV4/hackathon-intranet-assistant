This page describes the standard directory structure for an SSDG customer project stored on Perforce:

 

### **/pub/resources/ <customer_name>/<project_name>/.**

  * /0-preDiscovery
    * Needs Assessment
    * Request for (Product | Information | Quote)
    * Statement of Work
    * Initial Business Requirements are defined here.
  * /1-discovery  

    * Business Requirements Document
    * This is the final version prior to moving into the Design phase. This is important to note as some of the requirements will already have been outlined/discussed during the Pre-Discovery phase.
    * Caller Profiles
    * System Persona Definition
    * Voice User Interface Requirements
    * Compliance Requirements
    * High-level Data Interface Requirements
    * Reporting Requirements
  * /2-design
    * Data Interface Document
    * /<lang>
      * Detailed Dialog Design (3D)
      * Call Flow (Visio)
      * Grammar Specification
      * /woz
  * /3-development
    * System Architecture Design
    * Path Transversal Testing
    * <lang>
      * Code goes here!!
      * /grammars
  * /4-testing
    * /sit
    * /qa
    * /uat
    * /grammars
  * /5-tuning
  *     * /analysis
    * /reports


