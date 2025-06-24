* * *  
  
The following steps should be followed when a new ININ / Customer project is needed.

  1. #### Create a new Speech Projects Issue for the project

     1. [Create Issue](http://devjira.inin.com/secure/CreateIssue!default.jspa)   

     2. The component should be the customer name, internal group, or internal SSDG Project name.
        1. If the component you need isn't listed select _unknown_.
        2. Add the component to the Speech Projects Components using the following instructions
           1. Go to the Speech Projects JIRA Project page - [Speech Projects](http://devjira.inin.com/browse/SP)
           2. Select Components from the left sidebar options
           3. In the upper right hand corner click, "Manage Components."
              1. Only SSDG Team members have the ability to do this.
           4. Add the new component based on the project or customer name, i.e. Delta Dental.  
  

  2. #### Create a new Perforce Stream for the new Speech Project.

     1.   3. #### Accessing the Perforce Stream for the Project

     1. Open a command prompt and type, 'cb _< customer/project name>_.latest' then press Enter.

        1. This sets up the workspace for you and takes care of some other nitty gritty details regarding what is needed for the streams references, i.e. //speechsolutions/main_systest.

     2. At this point you can type 'p4v' and press Enter to access the GUI or you may use the command line. For a list of ININ 'p' commands type 'p help commands'. This will output the ININ wrapped 'p4' commands.

        1. Typing 'p help <command name>' and pressing Enter will bring that particular commands instructions.




 
