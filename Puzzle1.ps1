$data = Get-Content .\Puzzle1_input.txt
$lines = $data.Split("`r`n")

$buckets = @();
$currentBucket = 0;
$lines | ForEach-Object {
    $data = $_.TrimEnd("`r`n");
    if ([String]::IsNullOrWhiteSpace($data)) {
        $buckets += $currentBucket;
        $currentBucket = 0
    } Else {
        $currentBucket += [int]::Parse($data);
    }
}

$max = 0;
$x = 0;
For ($i = 0; $i -lt $buckets.Length; $i++) {
    if ($buckets[$i] -gt $max) {
        $max = $buckets[$i];
        $x = $i;
    }
}

Write-Host "Elf $x`: Value $max"

$sorted = $buckets | Sort-Object -Descending
$value = 0;
For ($i = 0; $i -lt 3; $i++) {
    $value += $sorted[$i];
}

Write-Host "Top 3 Total: $value";
