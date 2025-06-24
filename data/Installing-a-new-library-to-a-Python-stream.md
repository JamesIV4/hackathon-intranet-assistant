These instructions assume an update to the Windows library, so substitute the Linux path and idioms for that platform where necessary.

  


  * CB to the python stream
    * For example, "cb //external/python.3.5_static" or "cb //external/python.latest_static"
  * Confirm that the library is not installed
    * For example, through the command line interpreter by typing at the cb command line, 'python' and after hitting enter, at the prompt >>> type, 'import [library_name]', which should give an error.  Type 'exit()' to quit the interpreter.
  * Make sure there are no existing files in the stream that are not checked in (or at least be aware if there are any)  

    * For example, right-click on the python folder in .\pub\tools\winhost\python\ and select Reconcile Offline Work
    * This helps to avoid checking them in unintentionally with the new library.  If it finds files that are not checked in, then note those and don't add them to the change list if you don't need them.
  * Install the new library to the stream on your local machine
    * For example, 'python -m pip install [name_of_library]'
      * Note: This should install the library into the Python stream, since the python executable should be pointing to ...\pub\tools\winhost\python\python.exe.  To see this path, from the command line run, 'where python'.
  * Validate that the new library is installed
    * For example, through the interactive terminal mentioned previously and this time there should be no error during the import.
  * Fix the hard coded file path references in any EXEs to be generic, in order to apply to other dev machines
    * First, navigate to the directory: ...\pub\tools\winhost\python
    * … then run: 'python fix_script_exe.py'
      * It will print an informational message for each EXE that was processed, checking them out into the default change list in Perforce. 
      * Since it doesn't currently check if the EXE was modified (it will process previously fixed EXEs still), right-click on the change list and select Revert Unchanged Files to only keep the ones that changed.  Your new library may not contain any EXE files, in which case, none will be remain in the change list.
  * Add the new library files to a change list for check-in.
    * One way is to mark this whole directory for add: .\pub\tools\winhost\, and then right-click on the change list and select Revert Unchanged Files to only keep the new files.  Review the remaining files to make sure they match your new library.  Most, if not all of the new files will be under .\pub\tools\winhost\python\Lib\site-packages\ in a sub-directory related to your new library.  However, there may be other child directories if there are other library dependencies that were installed as well.


