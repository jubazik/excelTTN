@echo off
echo Сборка приложения для Windows...
echo.

REM Создаем виртуальное окружение
python -m venv venv_windows
call venv_windows\Scripts\activate.bat

REM Устанавливаем зависимости
pip install -r requirements.txt
pip install py2exe

REM Собираем приложение
python setup.py py2exe

REM Копируем необходимые файлы
xcopy import dist\import /E /I /Y
mkdir dist\export

echo.
echo Сборка завершена!
echo Приложение находится в папке dist\
echo.
pause