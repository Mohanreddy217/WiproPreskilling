$timestamp = Get-Date -Format "yyyy-MM-dd_HH-mm-ss"

$reportPath = "reports\$timestamp"

robot -d $reportPath .