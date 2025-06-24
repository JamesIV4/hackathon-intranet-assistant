# Parameter List  
  
Recognition parameters shall be set within the standard 3D (Dialog Design Document) under the "Developer Notes" section for a given DM.  Below is a list of all settable parameters:

 

**Name**| **(VXML equivalent property)**| **Default Value**| **Description**  
---|---|---|---  
collection_confidencelevel| confidence| 0.45| Rejection threshold for initial DM recognition  
collection_highconfidencelevel| n/a| 0.65| Confirmation threshold for initial DM recognition  
collection_incompletetimeout| incompletetimeout| 0.75s| Incomplete timeout in seconds  
collection_completetimeout| completetimeout| 0.0s| Complete timeout in seconds  
collection_sensitivity| sensitivity| 0.50| Endpointer sensitivity  
collection_maxspeechtimeout| maxspeechtimeout| 60s| Max speech timeout in seconds  
collection_timeout| timeout| 7s| No speech timeout in seconds  
collection_bargein| Set at field level| true| Allows turning barge-in on/off for recognition  
collection_interdigittimeout| interdigittimeout| 3s| DTMF interdigit timeout in seconds  
collection_termtimeout| termtimeout| 7s| DTMF term timeout in seconds  
collection_secureData| com.inin.securedata on CIC, secureData in Logging.js| "none"| Secure data masking (or encryption?).  Can have values 'none', 'mask', or 'encrypt'.  If set to 'mask', com.inin.securedata = true.  If set to encrypt, we currently do not support, but may in the future.  
confirmation_confidencelevel| confidence| 0.55| Rejection threshold for DM confirmation  
confirmation_incompletetimeout| incompletetimeout| 0.75s| Incomplete timeout in seconds  
confirmation_completetimeout| completetimeout| 0.0s| Complete timeout in seconds  
confirmation_sensitivity| sensitivity| 0.50| Endpointer sensitivity  
confirmation_maxspeechtimeout| maxspeechtimeout| 60s| Max speech timeout in seconds  
confirmation_timeout| timeout| 7s| No speech timeout in seconds  
confirmation_bargein| Set at field level| true| Allows turning barge-in on/off for recognition  
confirmation_interdigittimeout| interdigittimeout| 3s| DTMF interdigit timeout in seconds  
confirmation_termtimeout| termtimeout| 7s| DTMF term timeout in seconds  
confirmation_secureData| com.inin.securedata on CIC, secureData in Logging.js| none| Secure data masking (or encryption?).  Can have values 'none', 'mask', or 'encrypt'.  If set to 'mask', com.inin.securedata = true.  If set to encrypt, we currently do not support, but may in the future.  
nuance_swi_meaning| n/a| false| To differentiate the handling of SWI meaning grammar for ameren. this variable needs to set to true for ameren otherwise default value is false.  
yesNoSpeechFile| n/a| yesno.jsp| This variable meant to have the file name and extension used for specific clients depending on their needs.  
yesNoDtmfFile| m/a| yesno_dtmf.jsp| This variable meant to have the file name and extension used for specific clients depending on their needs.  
dtmfPath| n/a| (dtmf/) / (en-US/)| This variable is to set the path for dtmf grammars for their specific clients.  
yesNoGrammarModeVoice| n/a| none| The default value is none, this variable is used to set the mode to voice/dtmf depending the conditional check(if voice grammars are null then use dtmf grammar) in vxml.  
 |  |  |    
  
 

 

 

# Implementation Notes

Here is a guide for  getting  it working.

 

**Configure logging and classes**

Dialog_state.jsp has its own logging and library files.  Insert the files attached web-inf.zip to the WEB-INF folder of the Tomcat application that is being run. In the file classes>log4j2.xml change the log file location to the desired location.

 

**Properties file**

Create a file called dialog_state_config.xml. This will be the property file that holds all the configurable properties. This file has a section containing the default value for each configurable property. All the defaults must be provided.   Properties can be overridden at the language level, the application level and the dmName level.  A sample file is attached.

 

Dialog_state will search for a property in the following order:

  * Language > appName > dmName
  * Language > appName
  * Language
  * Default



 

**Place files  in VXML directory**

Add the both dialog_state.jsp and dialog_state_config.xml files to the vxml directory

 

**Calling the jsp     **

Here is a sample call to the jsp:

<subdialog name="dialog_state" srcexpr="dialogStateURL" namelist = "appName dmName Language">     

               Language , appName and dialogStateURL can be defined in root.vxml.  For example:                          

                              <var name="dialogStateURL" expr="'[http://localhost:8080/DSrita/vxml/dialog_state.jsp'"/](http://localhost:8080/DSrita/vxml/dialog_state.jsp)>

                               <var name="appName" expr="'Rita'"/>

<var name="Language" expr="'en-US'"/>

               The dmName will be defined in the dm node.  

<var name="dmName" expr="'RT1000_Greeting_DM'"/>

 

**Language**

               If no Language parameter is passed in the default 'en-US' is used

 

**Outstanding issues**

  * Need to resolve how to set the secureData global variable as discussed in the task force meeting
  * Dialog_state can be cleaned up a bit. This effort only converted it to a jsp
  * Some more logging might be desired. We can see as we use it.



# dialog_state_config.xml

 
    
    
    <?xml version="1.0" encoding="UTF-8"?>
    
    
    <properties>
    
    
     
    
    
        <default>
    
    
            <param name="collection_confidencelevel" value="0.45"/>
    
    
            <param name="collection_incompletetimeout" value="0.75s"/>
    
    
            <param name="collection_completetimeout" value="0.0s"/>
    
    
            <param name="collection_sensitivity" value="0.5"/>
    
    
            <param name="collection_maxspeechtimeout" value="60s"/>
    
    
            <param name="collection_timeout" value="7s"/>
    
    
            <param name="collection_bargein" value="true"/>
    
    
            <param name="collection_interdigittimeout" value="3s"/>
    
    
            <param name="collection_termtimeout" value="7s"/>
    
    
            <param name="collection_secureData" value="none"/>
    
    
           
    
    
            <param name="confirmation_confidencelevel" value="0.55"/>
    
    
            <param name="confirmation_incompletetimeout" value="0.75s"/>
    
    
            <param name="confirmation_completetimeout" value="0.0s"/>
    
    
            <param name="confirmation_sensitivity" value="0.5"/>
    
    
            <param name="confirmation_maxspeechtimeout" value="60s"/>
    
    
            <param name="confirmation_timeout" value="7s"/>
    
    
            <param name="confirmation_bargein" value="true"/>
    
    
            <param name="confirmation_interdigittimeout" value="3s"/>
    
    
            <param name="confirmation_termtimeout" value="7s"/>
    
    
            <param name="confirmation_secureData" value="none"/>
    
    
           
    
    
            <param name="collection_highconfidencelevel" value="0.7"/>

               

              <param name="nuance_swi_meaning" value="false"/>            

             <param name="yesNoGrammarModeVoice" value="none"/>

            <!-- For ameren the below values are set-->

             <param name="yesNoSpeechFile" value="yesno.jsp"/>    

             <param name="yesNoDtmfFile" value="yesno_dtmf.jsp"/>

             <param name="dtmfPath" value="en-US/"/>

 

            <!-- For Wellcare the below values are set-->

             <param name="yesNoSpeechFile" value="yesno.aspx"/>    

             <param name="yesNoDtmfFile" value="yesno_dtmf.xml"/>

             <param name="dtmfPath" value="dtmf/"/>

            

            
    
    
           
    
    
        </default>
    
    
       
    
    
        <language name="en-US">
    
    
            <application name="AILRES">
    
    
                <param name="collection_termtimeout" value="5s"/>   
    
    
                <dm name="AU01000_PhoneOrAcctNum_DM">
    
    
                    <param name="collection_termtimeout" value="4s"/>
    
    
                </dm>
    
    
            </application> 
    
    
        </language> 
    
    
     
    
    
        <language name="es-MX">
    
    
        <param name="collection_termtimeout" value="0.65"/>
    
    
        </language> 
    
    
       
    
    
    </properties>

 

 
