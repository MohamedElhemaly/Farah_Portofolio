Add-Type -AssemblyName System.IO.Compression.FileSystem
$docx = [System.IO.Compression.ZipFile]::OpenRead("d:\FarahProtofolio\Farah_Maher_CV.docx")
$entry = $docx.Entries | Where-Object { $_.FullName -eq 'word/document.xml' }
$stream = $entry.Open()
$reader = New-Object System.IO.StreamReader($stream)
$xml = $reader.ReadToEnd()
$reader.Close()
$docx.Dispose()
$xmlDoc = [xml]$xml
$nodes = $xmlDoc.SelectNodes('//*[local-name()="t"]')
foreach ($node in $nodes) {
    if ($node.InnerText -ne $null) {
        Write-Output $node.InnerText
    }
}
