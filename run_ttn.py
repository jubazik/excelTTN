#!/usr/bin/env python3
"""
Простой скрипт для запуска TTN Generator
"""

import sys
import os
from pathlib import Path

# Добавляем путь к src в sys.path
src_path = Path(__file__).parent / "src"
sys.path.insert(0, str(src_path))

try:
    from gui import main
    print("Запуск графического интерфейса...")
    main()
except ImportError as e:
    print(f"Ошибка импорта: {e}")
    print("Убедитесь, что все зависимости установлены:")
    print("pip install openpyxl")
except Exception as e:
    print(f"Произошла ошибка: {e}")