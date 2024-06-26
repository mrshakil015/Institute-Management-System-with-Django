@echo off
REM Change to the root directory of your project
cd /d %~dp0

REM Find and delete all __pycache__ folders
for /f "delims=" %%i in ('dir /ad /b /s __pycache__') do (
    echo Deleting %%i
    rmdir /s /q "%%i"
)

echo All __pycache__ folders have been deleted.
pause
