param(
    [Parameter(Mandatory = $true)]
    [string[]]$Roots,

    [string[]]$MoveScopeRoots = @(),

    [string]$OutputCsv = ""
)

$shell = New-Object -ComObject WScript.Shell
$rows = New-Object System.Collections.Generic.List[object]

function Test-IsUnderScope {
    param(
        [string]$TargetPath,
        [string[]]$Scopes
    )

    if ([string]::IsNullOrWhiteSpace($TargetPath)) {
        return $false
    }

    foreach ($scope in $Scopes) {
        if ([string]::IsNullOrWhiteSpace($scope)) {
            continue
        }
        $normalizedScope = [System.IO.Path]::GetFullPath($scope).TrimEnd('\') + '\'
        try {
            $normalizedTarget = [System.IO.Path]::GetFullPath($TargetPath)
        } catch {
            $normalizedTarget = $TargetPath
        }
        if ($normalizedTarget.StartsWith($normalizedScope, [System.StringComparison]::OrdinalIgnoreCase)) {
            return $true
        }
    }

    return $false
}

function Parse-UrlShortcut {
    param([string]$Path)

    $target = ""
    try {
        $lines = Get-Content -LiteralPath $Path -ErrorAction Stop
        foreach ($line in $lines) {
            if ($line -like 'URL=*') {
                $target = $line.Substring(4)
                break
            }
        }
    } catch {
        $target = ""
    }
    return $target
}

foreach ($root in $Roots) {
    if (-not (Test-Path -LiteralPath $root)) {
        continue
    }

    Get-ChildItem -LiteralPath $root -Recurse -File -Force -ErrorAction SilentlyContinue |
        Where-Object { $_.Extension -in '.lnk', '.url' } |
        ForEach-Object {
            $shortcutPath = $_.FullName
            $extension = $_.Extension.ToLowerInvariant()
            $targetPath = ""
            $arguments = ""
            $workingDirectory = ""
            $targetExists = $false
            $targetKind = "unknown"
            $notes = @()

            if ($extension -eq '.lnk') {
                try {
                    $shortcut = $shell.CreateShortcut($shortcutPath)
                    $targetPath = $shortcut.TargetPath
                    $arguments = $shortcut.Arguments
                    $workingDirectory = $shortcut.WorkingDirectory
                } catch {
                    $notes += "lnk_parse_failed"
                }
            } elseif ($extension -eq '.url') {
                $targetPath = Parse-UrlShortcut -Path $shortcutPath
            }

            if ($targetPath) {
                if ($targetPath -match '^[a-zA-Z]+://') {
                    $targetKind = "url"
                    $targetExists = $true
                } else {
                    $targetExists = Test-Path -LiteralPath $targetPath
                    if ($targetExists) {
                        $item = Get-Item -LiteralPath $targetPath -ErrorAction SilentlyContinue
                        if ($null -ne $item) {
                            if ($item.PSIsContainer) {
                                $targetKind = "directory"
                            } else {
                                $targetKind = "file"
                            }
                        }
                    } else {
                        $notes += "target_missing"
                    }
                }
            } else {
                $notes += "target_empty"
            }

            $rows.Add([pscustomobject]@{
                shortcut_path        = $shortcutPath
                shortcut_type        = $extension.TrimStart('.')
                target_path          = $targetPath
                target_kind          = $targetKind
                target_exists        = $targetExists
                target_in_move_scope = (Test-IsUnderScope -TargetPath $targetPath -Scopes $MoveScopeRoots)
                arguments            = $arguments
                working_directory    = $workingDirectory
                notes                = ($notes -join ';')
            })
        }
}

if ($OutputCsv) {
    $parent = Split-Path -Parent $OutputCsv
    if ($parent) {
        New-Item -ItemType Directory -Force -Path $parent | Out-Null
    }
    $rows | Export-Csv -LiteralPath $OutputCsv -NoTypeInformation -Encoding UTF8
} else {
    $rows | Format-Table -AutoSize
}
