@echo off
REM Script para rodar o ApiClient Tester Pro com ambiente virtual

echo Ativando ambiente virtual...
call .\venv\Scripts\activate.bat

echo Executando ApiClient Tester Pro...
python app.py

echo.
echo Pressione qualquer tecla para sair...
pause > nul
