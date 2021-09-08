function getIP{(Get-NetIPAddress).IPv4Address | Select-String "192*"};
$IP = getIP
$USER = $env:USERNAME
$HOSTNAME = hostname
$PSVERSION = $HOST.Version.Major
$DAYOFWEEK = (Get-Date).DayOfWeek
$MONTH = (Get-Date).Month
$DAY = (Get-Date).Day
$YEAR = (Get-Date).Year

$BODY = "This machines IP address is $IP. User is $USER. Hostname is $HOSTNAME. PowerShell Version $PSVERSION. Today's date is $DAYOFWEEK, $MONTH/$DAY/$YEAR."

Write-Host($BODY)

$BODY | Out-File C:\lab3.txt


Send-MailMessage -To "anthony.bothe@uc.edu" -From "emadbadawiziad@gmail.com" -Subject "IT3038C Windows sysinfo" -Body $BODY -SmtpServer smtp.gmail.com -port 587 -UseSsl -Credential (Get-Credential)