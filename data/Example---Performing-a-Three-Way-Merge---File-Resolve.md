  1. Open a command prompts and type 'cb speechsolutions-main -t 4q15' and press Enter  
  2. Change to the appropriate directory
     1. Hernan - /pub/resources/javascript
     2. Ralph - /pub/resources/com.inin.ssdg.kpilogging/
  3. Type 'p pull …' and press Enter
     1. The command line output will look something like this: (This shows both files as I did a pull from /pub/resources but you get the idea)  

  4. Type p4v to open the Perforce UI which should place you directly into this stream.
  5. Within the Pending Changelist Tab you'll have these files listed under the default changelist. They will have a red question mark in the file status icon, . This will occur when it cannot automatically resolve the changes between the parent and the
  6. Now, right click on the file and select 'Resolve'
     1. This will pop up a menu structure that will let you select to either Accept the Target (The local stream version), Accept the Source (That which resides in the parent), or Run the 3 - Way Merge tool (which is often the right choice to resolve conflicts)  

     2. After clicking Run Merge Tool you'll see the following dialog  

     3. At this point you can click the buttons on the right hand side to select which option you want OR you can manually edit the text within the Merge file used for resolve section like so:
        1. Here I manually edited the version numbers entered here.  

        2. Here is one where a method signatures has changed as well as the replacement of a line of code in favor of conditional syntax  
  

           1. Here I'll click the Green Option on the right to keep those lines  

     4. Once you've completed the resolution of all conflicts or any other edits click the Save icon or close the window, if you choose to close the window it will prompt you to save it.
        1. If you have not resolved all conflicts it will prompt you...  

        2. After you click Save / Close and Save you'll see this Dialog  

        3. Click Yes and that completes the Merging process. At this time it would be wise to review the code in the areas where merges happened or to initiate any unit tests you have on the code prior to submission


