#!/bin/bash
echo "Сборка приложения для macOS..."

# Создаем виртуальное окружение
python3 -m venv venv_mac
source venv_mac/bin/activate

# Устанавливаем зависимости
pip install -r requirements.txt
pip install py2app

# Собираем приложение
python3 setup.py py2app

# Копируем необходимые файлы
cp -R import dist/TTN_Generator.app/Contents/Resources/
mkdir -p dist/TTN_Generator.app/Contents/Resources/export

echo ""
echo "Сборка завершена!"
echo "Приложение находится в папке dist/TTN_Generator.app"
echo "Для запуска дважды кликните на TTN_Generator.app"
