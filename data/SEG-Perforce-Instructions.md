## Description

* * *

Interactive Intelligence uses [Perforce](http://www.perforce.com/) for their corporate source control solution. Some teams have begun using Git, PSO and Pure Cloud, but perforce is what the Media Team and our team will be using. The following sections are a small piece of what is available within Perforce here at ININ. Our team will be using Perforce a bit differently than the rest of development. SEG will have a main line for internal projects, common items for all projects, templates, etc. It will also use individual streams for each customer or internal project.

While the GUI interface of the Perforce Visual Client (p4v) is nice to use there are times when the command line must be used. This should only be when working in the Media or CIC Division codebase areas of Perforce. The reason for this is that the Perforce commands used by ININ are actually complex scripts that have been developed internally that wrap around and extend the functionality of the base 'p4 scripts' included with Perforce. The extended functionality is what allows a JIRA Issue to be automatically updated when a changelist is submitted. Or when a changelist needs propagated across its various versions. Because of the 'p scripts' that have been developed this is done automatically instead of having to manually run the commands each time.

If you have questions regarding Perforce or how a particular command line operation works please check out the [Online Perforce User Guide](http://www.perforce.com/perforce/doc.current/manuals/p4guide/) or from the command line type 'p help <command>'.

* * *

* * *

* * *

## Tasks

* * *

 _Notes:     The following tasks will result in the files involved being added to the default changelist unless a changelist is specified from the command line._

_If using the command line adding the -c parameter prior to the file / wildcard specification will allow a specific changelist to be specified if one already exists._

_Within the GUI a drop down list including the options of New, default, or list of existing options will be available_

Task| Command Line| GUI  
---|---|---  
Installing the Perforce Client| | N/A  
Check out one or more files for edit| p edit ... | filename | wildcards| 

  1. Select Depot Tab and Right-Click on the file(s) and / or folder(s)
  2. Select 'Check Out' or 'Check Out and Open' from the context menu

  
Add one or more files| p add ... | filename | wildcards| 

  1. Select the Workspace Tab and Right-Click on the file(s) and / or folder(s)
  2. Select 'Mark for Add' from the context menu

  
Remove / Delete files / folders| p delete... | filename | wildcards| 

  1. Select the Workspace Tab and Right-Click on the file(s) and / or folder(s)
  2. Select 'Mark for Delete' from the context menu

  
Move checked out files into another Changelist| 

  1. p change
  2. Notepad will appear. Edit the following field
  3. <Description>

| 

  1. Right-Click on the default changelist
     1. Which contains a single checked out file, or multiple files
  2. Select 'Move to another Changelist'
     1. This requires a Description to be entered.

  
Resolving and Merging checked out files| 

  1. p resolve ... | filename(s)
  2. Command line options will appear offering the following options,  
(s) skip, (ay) accept yours, (at) accept theirs, (m) merge.
     1. The recommended option will be shown after the options.

| 

  1. Right-Click on the file that needs resolved
     1. The icon will have a red question mark on it
  2. Select Resolve...

  
Attach a SCR / Issue to your Perforce Changelist| **Default Changelist**

  1. p change
  2. Go to step 2 below.

**Existing Changelist**

  1. p change -u _changelist #_
  2. _Notepad will appear and the following field needs Added after the Description  
Jobs:  
ISSUE / SCR number, SSRITA-223_

| 

  1. Right-Click on the default changelist
  2. Select Move all Files to Another Changelist
  3. Enter a description which can be a placeholder until you are ready to detail out the specifics.
  4. Right-click on the changelist and select 'View Pending Changelist'
  5. Enter the SCR / Issue number and then click Add or Click Browse to search for an SCR / Issue
  6. Click Apply then Close the change list or submit if your are ready to do so

  
Updating your local workspace to the latest build| 

  1. Open a command window.
  2. Single Command Approach
     1. Type 'buildupdate (_codebase|depot)-(latest|1.0)_ ' and press Enter.
        1. For Example: **_buildupdate speechsolutions-main_**
        2. typing **_buildupdate --help_**  prints out additional options available
     2. Once that completes type 'p sync ...' in the directory you wish to update as buildupdate only downloads that which resides in <depot>/<codebase>/pub.
        1. **CAUTION:** If you run 'p sync ...' at the root you'll get it all... in the case of /pub/resources/global_prompts that is 40k wav files...
  3. Buildupdate within a workspace
     1. Doing such removes the necessity of specifying the codebase|depot and version, etc.
        1. For Example these instructions will perform the same tasks as above:
           1. cb speechsolutions-main
           2. buildupdate -latest

| N/A  
  
* * *

* * *

* * *

## Three Way Merge via Perforce MERGE GUI tool

* * *

This utility is built-in to Perforce and available when the p4v, the Perforce GUI Interface, is installed. It is launched when merge (m) option is selected via the command line or is the result of selecting Merge via the Perforce Resolve tool. When the tool opens three columns will be shown with the source being resolved in each of them. The column layout is as follows, Left is Source, Middle is Merged, Right is Target.

* * *

* * *

* * *

## Glossary

* * *

Term| Definition  
---|---  
**Codebase:**|  The product line in Software Product Life Cycle Management or Software Product Management.  
**Depot:**| 

  *  A source control term and the ININ use of it is akin to the codebase, i.e. EIC is the codebase as well as the depot name in Perforce.
    * This contains all of the versions for that product from the team branch level up to each released version.
      * Team Branches will be discussed later.

  
**Stream:**| 

  * The location in which a particular version of a codebase resides. 
    * It contains all the files that make up the product. An example of this are the ssdg.interactionrita streams.
    * We have a main_systest, 1.0_systest, and a 1.0_su00.
      * The main_systest branch will be the 1.5 release, the 1.0_systest would be used for patching or creating engineering specials against the 1.0 release.
      * Lastly, the 1.0_su00 is the 'Generally Available' (GA) released version. No changes are allowed in a released stream.

  
**Changelist:**|  A group of files that are being added, modified, or removed from the current stream / workspace.   
**Source File |**Theirs** :**| The file/files that is/are coming FROM Perforce, i.e. the checked in version _Note: 'Theirs' is a term seen when performing resolves within the command line. It will appear in the form of a table prior to the list of files being resolved._  
**Target File | Yours:**|  The local file/files that exist in the local workspace._Note: 'Theirs' is a term seen when performing resolves within the command line. It will appear in the form of a table prior to the list of files being resolved._  
  
* * *

* * *

* * *

## File Icons and what they mean

* * *

Icon| Description  
---|---  
| Checked out for Edit  
| Checked out for Edit - Exclusive  
| Local Workspace Version Up to Date  
| Local Workspace Version Out of Date  
| Marked for Add  
| Marked for Delete  
| Marked for Add - File Move  
| Marked for Delete - File Move  
| Local Workspace Version Up to Date  
Checked out by other user   
| Multiple Concurrent Checkouts  
(You and someone else)   
| File needs 'Resolved' prior to integration  
  
* * *

* * *

* * *

 
