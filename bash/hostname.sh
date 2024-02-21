#/!/bin/bash

#Variables and Input read
currentHostname=`hostname -s`
serial=`ioreg -l | awk '/IOPlatformSerialNumber/ { split($0, line, "\""); printf("%s\n", line[4]); }'`

#Leave blank unless using a static prefix for multiple machines
prefix=''

#comment read line and fill in prefix if using static prefix for multiple machines
read -p "Company 3 Letter Prefix: " -n 3 -r prefix

prefix=$(echo "$prefix" | tr '[:lower:]' '[:upper:]')
#newHostname must be after read line to store input.
newHostname="$prefix-$serial"


#Print Information
echo ''
echo ''
echo "My current hostname is: $currentHostname"
echo "My serial number is: $serial"
echo "My prefix tag is: $prefix"
echo "Changing hostname to: $newHostname"
echo ''
echo ''

#These lines set the new HostName
#sudo scutil --set HostName "$newHostname"
#sudo scutil --set ComputerName "$newHostname"
#sudo scutil --set LocalHostName "$newHostname"

# Display Hostname
echo "Hostname has been changed to: $newHostname"
echo
echo