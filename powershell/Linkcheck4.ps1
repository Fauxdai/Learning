# Define the list of links
$links = @(

)
ipconfig /flushdns
# Function to get SSL certificate expiration date
function Get-SSLCertificateExpiration {
    param (
        [string]$url
    )
    try {
        # Ignore SSL warnings
        [Net.ServicePointManager]::ServerCertificateValidationCallback = { $true }
        
        # Create TCP connection
        $hostname = $url -replace "https?://", ""
        $tcpClient = New-Object System.Net.Sockets.TcpClient($hostname, 443)
        $sslStream = New-Object System.Net.Security.SslStream($tcpClient.GetStream(), $false, ({$true}))
        $sslStream.AuthenticateAsClient($hostname)
        
        # Get SSL certificate
        $cert = $sslStream.RemoteCertificate
        $expirationDate = [datetime]::Parse($cert.GetExpirationDateString())
        
        $tcpClient.Close()
        return $expirationDate
    } catch {
        return "Error retrieving certificate: $_"
    }
}

# Function to get IP address
function Get-IP {
    param (
        [string]$url
    )
    try {
        $hostname = $url -replace "https?://", ""
        $ipAddress = (Resolve-DnsName -Name $hostname).IPAddress
        return $ipAddress
    } catch {
        return "Error retrieving IP address: $_"
    }
}

# Function to get the status code
function Get-StatusCode {
    param ($url)
    try {
        $request = [System.Net.WebRequest]::Create($url)
        $request.Method = "HEAD"
        $response = $request.GetResponse()
        $statusCode = $response.StatusCode
        $response.Close()
    } catch [System.Net.WebException] {
        $statusCode = $_.Exception.Response.StatusCode
    }
    return $statusCode
}

# Function to get nameservers
function Get-Nameservers {
    param (
        [string]$url
    )
    try {
        $hostname = $url -replace "https?://", ""
        $domainParts = $hostname.Split('.')
        $domain = "$($domainParts[-2]).$($domainParts[-1])"
        $nameservers = (Resolve-DnsName -Name $domain -Type NS).NameHost -join ", "
        return $nameservers
    } catch {
        return "Error retrieving nameservers: $_"
    }
}

# Function to get domain registrar information
function Get-DomainRegistrarInfo {
    param (
        [string]$url
    )
    try {
        $hostname = $url -replace "https?://", ""
        $whoisResult = whois $hostname
        $registrar = ($whoisResult | Select-String -Pattern "Registrar:").Line -replace "Registrar: ", ""
        $creationDate = ($whoisResult | Select-String -Pattern "Creation Date:").Line -replace "Creation Date: ", ""
        $expirationDate = ($whoisResult | Select-String -Pattern "Registry Expiry Date:").Line -replace "Registry Expiry Date: ", ""
        $nameServers = ($whoisResult | Select-String -Pattern "Name Server:").Line -replace "Name Server: ", ""

        return [PSCustomObject]@{
            Domain         = $hostname
            Registrar      = $registrar
            CreationDate   = $creationDate
            ExpirationDate = $expirationDate
            NameServers    = $nameServers
        }
    } catch {
        return [PSCustomObject]@{
            Domain  = $hostname
            Error   = $_.Exception.Message
        }
    }
}

# Initialize an array to store the results
$results = @()

# Iterate over each link and collect the required information
foreach ($link in $links) {
    try {
        $statusCode = Get-StatusCode -url $link
        $expirationDate = Get-SSLCertificateExpiration -url $link
        $ipAddress = Get-IP -url $link
        $nameservers = Get-Nameservers -url $link
        $registrarInfo = Get-DomainRegistrarInfo -url $link
        
        $result = [PSCustomObject]@{
            URL                     = $link
            StatusCode              = $statusCode
            SSLCertificateExpiration = $expirationDate
            IPAddress               = $ipAddress
            Nameservers             = $nameservers
            Registrar               = $registrarInfo.Registrar.Trim()
            DomainCreationDate      = $registrarInfo.CreationDate.Trim()
            DomainExpirationDate    = $registrarInfo.ExpirationDate.Trim()
        }
        
        $results += $result
        Write-Output $result
    } catch {
        $errorResult = [PSCustomObject]@{
            URL                     = $link
            StatusCode              = "Error"
            SSLCertificateExpiration = "Error"
            IPAddress               = "Error"
            Nameservers             = "Error"
            Registrar               = "Error"
            DomainCreationDate      = "Error"
            DomainExpirationDate    = "Error"
        }
        $results += $errorResult
        Write-Output $errorResult
    }
}

# Get the path to the desktop
$desktopPath = [Environment]::GetFolderPath("Desktop")

# Export the results to a CSV file on the desktop
$results | Export-Csv -Path "$desktopPath\\domain_info.csv" -NoTypeInformation

Write-Output "Results have been exported to $desktopPath\\domain_info.csv"
