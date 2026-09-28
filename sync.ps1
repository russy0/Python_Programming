$ErrorActionPreference = "Stop"

$RepoUrl = "https://github.com/JavaTeacher/Python_Programming.git"
$TargetPath = (Get-Location).Path

$TempPath = Join-Path $env:TEMP "Python_Programming_sync"

if (Test-Path $TempPath) {
    Remove-Item $TempPath -Recurse -Force
}

try {
    Write-Host ""
    Write-Host "========================"
    Write-Host " Python Programming Sync"
    Write-Host "========================"
    Write-Host ""

    Write-Host "[1/3] GitHub 저장소를 가져오는 중..."
    Write-Host $RepoUrl
    Write-Host ""

    git clone --depth 1 --single-branch --branch main $RepoUrl $TempPath

    if ($LASTEXITCODE -ne 0) {
        throw "Git clone에 실패했습니다."
    }

    Write-Host ""
    Write-Host "[2/3] 로컬에 없는 파일을 확인하는 중..."
    Write-Host ""

    $sourceFiles = Get-ChildItem `
        -Path $TempPath `
        -Recurse `
        -File `
        -Force

    $added = 0
    $skipped = 0

    foreach ($sourceFile in $sourceFiles) {
        $relativePath = $sourceFile.FullName.Substring(
            $TempPath.Length
        ).TrimStart('\')

        if (
            $relativePath -eq ".git" -or
            $relativePath.StartsWith(".git\")
        ) {
            continue
        }

        $targetFile = Join-Path $TargetPath $relativePath
        $targetDir = Split-Path $targetFile -Parent

        if (Test-Path -LiteralPath $targetFile) {
            Write-Host "[SKIP] $relativePath"
            $skipped++
            continue
        }

        if (-not (Test-Path -LiteralPath $targetDir)) {
            New-Item `
                -ItemType Directory `
                -Path $targetDir `
                -Force | Out-Null
        }

        Copy-Item `
            -LiteralPath $sourceFile.FullName `
            -Destination $targetFile

        Write-Host "[ADD ] $relativePath"
        $added++
    }

    Write-Host ""
    Write-Host "[3/3] 동기화 완료"
    Write-Host ""
    Write-Host "추가된 파일 : $added"
    Write-Host "기존 파일   : $skipped"
    Write-Host ""
}
catch {
    Write-Host ""
    Write-Host "[ERROR] $($_.Exception.Message)" -ForegroundColor Red
    exit 1
}
finally {
    if (Test-Path $TempPath) {
        Remove-Item $TempPath -Recurse -Force
    }
}
