## 

## Intro

* * *

Welcome to the page that provides the answers to those questions you've been pondering.

YOU: What questions you ask?

ME:   Well how about this one, "How do I know that the VXML I wrote will work CIC VXML Interpreter?"

YOU: Just place a call man.

ME:   What's that you say, you just place a call to test. Can you say time waster? The following instructions will help you get a clearer understanding of what you can do to ensure that the VXML you are writing will work. Let me show you how its done.

## Tools Needed

* * *

The following are just suggestions and ways to help decrease the time it takes to create VXML based speech applications for CIC and Pure Cloud.

### Text Editor / IDE

Pick your poison: Notepad++, VI, EMACS, Visual Studio, SlickEdit, Notepad, etc. The key is whatever you're comfortable with is what will make you the most successful. I happen to use Notepad++ with a couple of plugins, [XML Tools](http://sourceforge.net/projects/npp-plugins/files/XML%20Tools/) and [JSTools](http://www.sunjw.us/jstoolnpp/).

### Web Browser

The web browser provides a medium to run yet another plugin such as [Firebug ](https://getfirebug.com/downloads)or [Chrome DevTools](https://developer.chrome.com/devtools/index). These two browser plugins provide the ability live Javascript debugging which can be crucial to the Javascript side of development of VXML.

To use these plugins you have to be able to load up and replicate the same type of environment as the interpreter. The only difference I've found at this point between the browser based compilation of javascript and bladeware is that bladeware has its own XML DOM library.

Example:

  1. Create a basic web page as follows:

  2. Open this page within your web browser and initiate the plugin, Pressing F12 launches Chrome Dev Tools.
     1. From here you can set breakpoints, watchers, etc. just as you would if you were using another debugger.



### validateVXML Script

 _NOTE: Requires VPN access and have a development environment setup with command line access to codebases, i.e. ability to run 'cb', etc._

This script is a wrapper for a tool that exists in the edge codebase, validate_vxml-w32r-1-0.exe. This tool is great for syntax validation and a build task already exists to add it to the build system such that it can be easily run without my wrapper.

Using validateVXML requires that you are within a branch within the SpeechSolutions depot but I've provided a perforce link to the Batch script below.

//speechsolutions/main_systest/pub/tools/common-bin/validateVXML.bat

Once you have access to it you can use it by typing the following command, 'validateVXML _< path to VXML file>_' and pressing Enter. If the document is syntactically correct the following message will appear, "Document Successfully Validated." Otherwise a long textual description including the line number, error message, and potentially the offending trace will appear.

### Javascript Syntax Validation

 _NOTE: Requires VPN access and have a development environment setup with command line access to codebases, i.e. ability to run 'cb', etc._

In this section I'll provide an option for javascript syntax validation. 

  1. Open a command line, type 'cb core-main' and press Enter
  2. First-time users continue while others my move to step 3
     1. type 'buildupdate --latest' and press Enter
  3. type 'cd ..\\..\pub\gen\bin\w32' and press Enter
  4. type 'i3javascript_shell-w32d-5-0.exe -i -f _< Enter __js file path here >' _and press Enter
     1. If the Javascript is syntactically correct it will load the i3javascript shell if not it will break and tell you where it is wrong.



The caveat to using this is that this shell is what is used within the Interaction Edge which uses a new version of SpiderMonkey for the backend when compared to CIC's VXML interpreter. But, this is a good test.

### Unit Testing

This is an area that is still under development / design as it relates to writing custom speech applications for CIC and Pure Cloud. There are frameworks out there that support javascript dependencies between files such that you don't have to reference every js file within every vxml file that needs it, etc. Right now the processes above are one way to test the syntax of your javascript and vxml. The following is a method that can and has been used with some success.

  1. Create a UnitTest.vxml like found here:
     1. //speechsolutions/ssdg.interactionrita.latest/int/src/interactionrita/vxml/UnitTest.vxml
  2. Create a UnitTest.js like found here:
     1. //speechsolutions/ssdg.interactionrita.latest/int/src/interactionrita/javascript/UnitTest.js
  3. Deploy this handler to your CIC test system
     1. //speechsolutions/main_systest/latest/int/src/common/handlers/SSDG_VoiceXML_Base.ihd
  4. Open Interaction Designer
     1. Open the CustomSubroutineInitiatorRouter.ihd from the Custom folder
        1. If it doesn't exist then open it from the \i3\ic\40Handlers folder and save it to the Custom folder.
     2. Add a new item to the Selection step with the value of StrEqlNoCase('p_SubroutineName', '_< HandlerName>_')
     3. From the Tools -> Custom Tab drag the SSDG_VoiceXML_Base.ihd onto the screen and connect the new selection entry to the input of the handler.
     4. Publish the newly modified CustomSubroutineInitiatorRouter.ihd.
  5. Add a new Profile within Interaction Attendant that has the following configuration  
 _Note: All settings listed below are only those that have been modified from the defaults._  

     1. Profile
        1. Name: _Enter a Unique Name, i.e. UNIT TEST - JS - Interaction RITA_
        2. Incoming Call Selection -> DNIS:
           1. Check the box
           2. Enter a DNIS with which to access this profile.
     2. Schedule
        1. Repetition
           1. Num. of times to repeat: 0
           2. Num. of seconds to wait: 1
     3. Custom Subroutine
        1. Name: _Enter the name of the Custom Handler or some variation of it, "Interaction RITA"._
        2. Subroutine: Enter the exact name of the custom handler being called, "InteractionRITA"
        3. Action When Finished: Disconnect
     4. Set Attribute
        1. Default Action: Enabled
        2. Attribute: VXML_Document_URI
           1. attribute must be EXACTLY as seen above as the handler looks for that specific call attribute
        3. Value: _HTTP:// or FILE:/// based path to the unit test vxml document_
           1.  _For example:  <http://mccmediaspeech:8098/InteractionRITA/VXML/UnitTest.vxml>_
        4. Action When Finished: Select Custom Subroutine Node defined in the previous step, i.e. Interaction RITA.
     5. Save / Publish the new profile.



You are now ready to place test calls to your Unit Test Attendant profile. When you place you're call it will fire off the javascript and you can see whether the code was successful by reviewing the vxmlserver.ininlog. The key is to design your methods in a way to log out Success or Failure along with the method name.

 

 

 
