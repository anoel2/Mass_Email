$inputFile = names.txt # Replace with the name of your input file
$outputFile = email.txt # Replace with the name you want for the modified file

Get-Content $inputFile  ForEach-Object { $_ + @colorado.edu }  Set-Content $outputFile
