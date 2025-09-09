# Script PowerShell para rodar o ApiClient Tester Pro

Write-Host "Ativando ambiente virtual..." -ForegroundColor Green
& .\venv\Scripts\Activate.ps1

Write-Host "Executando ApiClient Tester Pro..." -ForegroundColor Green
python app.py

Write-Host ""
Write-Host "Pressione qualquer tecla para sair..." -ForegroundColor Yellow
$null = $Host.UI.RawUI.ReadKey("NoEcho,IncludeKeyDown")
