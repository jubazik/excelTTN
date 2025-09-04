#!/bin/bash
echo "Установка TTN Generator для macOS..."
echo ""

# Проверяем Python
if ! command -v python3 &> /dev/null; then
    echo "Python3 не установлен!"
    echo "Установите Python3: brew install python"
    exit 1
fi

# Устанавливаем зависимости
pip3 install openpyxl

# Создаем папки
mkdir -p "$HOME/TTN_Generator"
cp -R src/* "$HOME/TTN_Generator/"
cp run_ttn.py "$HOME/TTN_Generator/"

# Создаем .command файл для запуска
cat > "$HOME/Desktop/TTN Generator.command" << 'EOF'
#!/bin/bash
cd "$HOME/TTN_Generator"
python3 run_ttn.py
EOF

chmod +x "$HOME/Desktop/TTN Generator.command"

echo ""
echo "Установка завершена!"
echo "Для запуска дважды кликните на 'TTN Generator.command' на рабочем столе"
echo "Выберите файл ТТН через интерфейс приложения"