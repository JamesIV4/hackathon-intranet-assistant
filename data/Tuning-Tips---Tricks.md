## Playing Audio Files in Excel

  1. Go to the "View" menu and Select "Macros"
  2. Create a new macro called "PlayAudio"
  3. Enter the code, below, into the macro editor and save
  4. Select close and return to Microsoft Excel from File menu
  5. Select Macros:View
  6. Select "Options" for your new macro in the list.  Place "p" in the shortcut.  Next, select "Run"
  7. Move to any cell with an audio path and press "ctrl p" to play



Public Declare Function sndPlaySound Lib "winmm.dll" _

Alias "sndPlaySoundA" (ByVal lpszSoundName As String, _

ByVal uFlags As Long) As Long

Sub PlayAudio()

   Application.ScreenUpdating = False

   On Error Resume Next

   sndPlaySound ActiveCell.Text, 0

End Sub

 
