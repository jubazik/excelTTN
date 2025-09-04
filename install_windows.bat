@echo off
echo Установка TTN Generator...
echo.

REM Проверяем Python
python --version >nul 2>&1
if errorlevel 1 (
    echo Python не установлен!
    echo Пожалуйста, установите Python 3.6+ с https://python.org
    pause
    exit /b 1
)

REM Устанавливаем зависимости
pip install openpyxl

REM Создаем папки
mkdir "%USERPROFILE%\TTN_Generator"
xcopy src "%USERPROFILE%\TTN_Generator\" /E /I /Y

REM Создаем ярлык на рабочем столе
echo [InternetShortcut] > "%USERPROFILE%\Desktop\TTN Generator.url"
echo URL=file:///%USERPROFILE%/TTN_Generator/run_ttn.py >> "%USERPROFILE%\Desktop\TTN Generator.url"
echo IconIndex=0 >> "%USERPROFILE%\Desktop\TTN Generator.url"
echo IconFile=python.exe >> "%USERPROFILE%\Desktop\TTN Generator.url"

echo.
echo Установка завершена!
echo Ярлык создан на рабочем столе.
echo Для использования выберите файл ТТН через интерфейс.
echo.
pause