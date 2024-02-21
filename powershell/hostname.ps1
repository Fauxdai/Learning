#UNTESTED - USE AT YOUR OWN PERIL

# Get current hostname
$currentHostname = hostname

# Get serial number
$serial = Get-WmiObject Win32_BIOS | Select-Object -ExpandProperty SerialNumber

# Leave blank unless using a static prefix for multiple machines
$prefix = ''

# Comment read line and fill in prefix if using static prefix for multiple machines
$prefix = Read-Host "Company 3 Letter Prefix"

# Convert prefix to uppercase
$prefix = $prefix.ToUpper()

# Concatenate prefix and serial for new hostname
$newHostname = "$prefix-$serial"

# Print Information
Write-Host ""
Write-Host ""
Write-Host "My current hostname is: $currentHostname"
Write-Host "My serial number is: $serial"
Write-Host "My prefix tag is: $prefix"
Write-Host "Changing hostname to: $newHostname"
Write-Host ""
Write-Host ""

# Set new hostname
$sysInfo = New-Object -ComObject Winmgmts:\\.\root\cimv2:Win32_ComputerSystem
$sysInfo.Rename($newHostname)

# Display Hostname
Write-Host "Hostname has been changed to: $newHostname"
Write-Host ""
Write-Host ""