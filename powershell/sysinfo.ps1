function getIP{(Get-NetIPAddress).IPv4Address | Select-String "192*"};
$IP = getIP
Write-Host("This machine's IP address is {0}" -f $IP)