#Use this powershell script if you need to append a domain name to a list of names. 
$inputFile = names.txt # Replace with the name of your input file
$outputFile = email.txt # Replace with the name you want for the modified file

Get-Content $inputFile  ForEach-Object { $_ + @example.com }  Set-Content $outputFile
